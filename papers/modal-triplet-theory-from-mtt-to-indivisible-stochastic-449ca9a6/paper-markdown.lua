-- Preserve locally built citations and revision notes in the generated Markdown.
local function read_file(name)
  local f = io.open(name, "r")
  if not f then return nil end
  local text = f:read("*a")
  f:close()
  return text
end
local source = assert(read_file("main.tex"))
local bibliography = source:match("\\begin{thebibliography}{%d+}(.-)\\end{thebibliography}")
if not bibliography then
  bibliography = assert(read_file("main.bbl"), "Build the PDF before Markdown")
end
local entries, numbers, descriptions, refs = {}, {}, {}, {}
local offset = 1
while true do
  local first, last, key = bibliography:find("\\bibitem{([^}]+)}", offset)
  if not first then break end
  local following = bibliography:find("\\bibitem{", last + 1, true)
  local body = bibliography:sub(last + 1, following and following - 1 or -1)
  body = body:gsub("\\end{thebibliography}", "")
  body = body:gsub("\\newblock", " ")
  entries[#entries + 1] = {key = key, body = body}
  numbers[key] = #entries
  offset = last + 1
end
for body in source:gmatch("\\begin{description}(.-)\\end{description}") do
  descriptions[#descriptions + 1] = body:gsub("^%b[]", "")
end
for key, value in (read_file("main.aux") or ""):gmatch("\\newlabel{([^}]+)}{{([^}]*)}") do
  refs[key] = value
end
local function cite(node)
  local result = pandoc.Inlines({pandoc.Str("[")})
  for i, item in ipairs(node.citations) do
    local number = assert(numbers[item.id], "Unknown citation: " .. item.id)
    if i > 1 then result:insert(pandoc.Str(",")) end
    result:insert(pandoc.Link(tostring(number), "#ref-" .. item.id))
  end
  result:insert(pandoc.Str("]"))
  return result
end
local function bibliography_blocks()
  local blocks = pandoc.Blocks({pandoc.Header(1, "References")})
  for i, item in ipairs(entries) do
    blocks:insert(pandoc.RawBlock("html", '<a id="ref-' .. item.key .. '"></a>'))
    local parsed = pandoc.read(item.body, "latex"):walk({Cite=cite}).blocks
    if parsed[1] and parsed[1].content then
      parsed[1].content:insert(1, pandoc.Str("[" .. tostring(i) .. "] "))
    end
    blocks:extend(parsed)
  end
  return blocks
end
function Pandoc(doc)
  local description_index, has_bibliography = 0, false
  doc = doc:walk({
    Cite = cite,
    Para = function(node)
      -- Pandoc treats \path as a graphics command and drops this filename.
      if pandoc.utils.stringify(node):find("The frozen manifest is ;", 1, true) then
        local filename = assert(source:match("The frozen manifest is \\path{([^}]+)}"))
        for i, inline in ipairs(node.content) do
          if inline.t == "Str" and inline.text == ";" then
            node.content:insert(i, pandoc.Code(filename))
            break
          end
        end
        return node
      end
    end,
    Div = function(node)
      if node.classes:includes("thebibliography") then
        has_bibliography = true
        return bibliography_blocks()
      end
      if not node.classes:includes("description") then
        local number = refs[node.identifier]
        local first = node.content[1]
        if number and first and first.t == "Para" and first.content[1]
          and first.content[1].t == "Strong" then
          local name = pandoc.utils.stringify(first.content[1]):match("^(%a+)")
          if name then first.content[1] = pandoc.Strong(name .. " " .. number) end
        end
        return node
      end
      description_index = description_index + 1
      local body = assert(descriptions[description_index])
      local blocks, pos = pandoc.Blocks({}), 1
      while true do
        local first, last, label = body:find("\\item%[([^%]]+)%]", pos)
        if not first then break end
        local following = body:find("\\item[", last + 1, true)
        local text = body:sub(last + 1, following and following - 1 or -1)
        local parsed = pandoc.read(text, "latex"):walk({Cite=cite}).blocks
        if parsed[1] and parsed[1].content then
          parsed[1].content:insert(1, pandoc.Space())
          parsed[1].content:insert(1, pandoc.Strong(label))
        end
        blocks:extend(parsed)
        pos = last + 1
      end
      return blocks
    end,
    Header = function(node)
      if node.identifier:find(":", 1, true) then
        return {pandoc.RawBlock("html", '<a id="' .. node.identifier .. '"></a>'), node}
      end
    end,
    Link = function(node)
      local key = node.attributes["reference"]
      if key then
        local result = pandoc.Inlines({})
        for part in key:gmatch("[^,]+") do
          local number = refs[part]
          if not number then return node end
          if #result > 0 then result:insert(pandoc.Str(", ")) end
          local value = part:match("^eq:") and "(" .. number .. ")" or number
          result:insert(pandoc.Link(value, "#" .. part))
        end
        return result
      end
      return node
    end,
    RawInline = function(node)
      if node.format == "tex" or node.format == "latex" then
        local value = node.text:match("\\path{(.*)}")
        if value then return pandoc.Code(value) end
      end
    end,
    Math = function(node)
      if node.mathtype ~= "DisplayMath" then return nil end
      local result = pandoc.Inlines({})
      for key in node.text:gmatch("\\label{([^}]+)}") do
        result:insert(pandoc.RawInline("html", '<a id="' .. key .. '"></a>'))
      end
      node.text = node.text:gsub("\\label{[^}]+}", "")
      result:insert(node)
      return result
    end
  })
  if source:find("% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE", 1, true) then
    local blocks = pandoc.Blocks({})
    local managed = false
    for _, block in ipairs(doc.blocks) do
      if block.t == "Header" and pandoc.utils.stringify(block.content) == "Computational Evidence and Reproducibility" then
        managed = true
        blocks:insert(pandoc.RawBlock("html", "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"))
      end
      blocks:insert(block)
    end
    if managed then blocks:insert(pandoc.RawBlock("html", "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->")) end
    doc.blocks = blocks
  end
  if not has_bibliography then doc.blocks:extend(bibliography_blocks()) end
  local opening = pandoc.Blocks({pandoc.Header(1, pandoc.utils.stringify(doc.meta.title))})
  opening:insert(pandoc.Para(pandoc.utils.stringify(doc.meta.author)
    .. ". " .. pandoc.utils.stringify(doc.meta.date)))
  opening:insert(pandoc.Header(2, "Abstract"))
  opening:extend(doc.meta.abstract)
  opening:extend(doc.blocks)
  doc.blocks = opening
  return doc
end
