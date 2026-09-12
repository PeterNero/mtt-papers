-- This manuscript uses an embedded bibliography rather than a .bib database.
-- Preserve citation identities using Pandoc's AST; leave the PDF source intact.
local handle = assert(io.open("main.tex", "r"))
local source = handle:read("*a")
handle:close()
local descriptions, description_index = {}, 0
for body in source:gmatch("\\begin{description}%b[](.-)\\end{description}") do
  descriptions[#descriptions + 1] = body
end
local bibliography = assert(source:match(
  "\\begin{thebibliography}{%d+}(.-)\\end{thebibliography}"))
local entries, numbers = {}, {}
local position = 1
while true do
  local first, last, key = bibliography:find("\\bibitem{([^}]+)}", position)
  if not first then break end
  local following = bibliography:find("\\bibitem{", last + 1, true)
  local body = bibliography:sub(last + 1, following and following - 1 or -1)
  entries[#entries + 1] = {key = key, body = body}
  numbers[key] = #entries
  position = last + 1
end

local function citation(node)
  local result = pandoc.Inlines({pandoc.Str("[")})
  for i, item in ipairs(node.citations) do
    local number = assert(numbers[item.id], "Unknown bibliography key: " .. item.id)
    if i > 1 then result:insert(pandoc.Str(",")) end
    result:insert(pandoc.Link(tostring(number), "#ref-" .. item.id))
  end
  result:insert(pandoc.Str("]"))
  return result
end

local function replace_bibliography(node)
  if node.classes:includes("description") then
    description_index = description_index + 1
    local description = assert(descriptions[description_index])
    local blocks, offset = pandoc.Blocks({}), 1
    while true do
      local first, last, label = description:find("\\item%[([^%]]+)%]", offset)
      if not first then break end
      local following = description:find("\\item[", last + 1, true)
      local body = description:sub(last + 1, following and following - 1 or -1)
      local parsed = pandoc.read(body, "latex").blocks
      parsed[1].content:insert(1, pandoc.Space())
      parsed[1].content:insert(1, pandoc.Strong(label))
      blocks:extend(parsed)
      offset = last + 1
    end
    return blocks
  end
  if not node.classes:includes("thebibliography") then return nil end
  local blocks = pandoc.Blocks({pandoc.Header(1, "References")})
  for i, item in ipairs(entries) do
    blocks:insert(pandoc.RawBlock("html", '<a id="ref-' .. item.key .. '"></a>'))
    local body = pandoc.read(item.body, "latex"):walk({Cite = citation}).blocks
    if body[1] and body[1].content then
      body[1].content:insert(1, pandoc.Str("[" .. tostring(i) .. "] "))
    end
    blocks:extend(body)
  end
  return blocks
end

local function clean_table(node)
  -- Pandoc retains the repeated longtable print header as its first body row.
  if node.head.rows[1] and node.bodies[1] and node.bodies[1].body[1] then
    local function row_text(row)
      local parts = {}
      for _, cell in ipairs(row.cells) do
        parts[#parts + 1] = pandoc.utils.stringify(cell.contents)
      end
      return table.concat(parts, "|")
    end
    local head = row_text(node.head.rows[1])
    local first = row_text(node.bodies[1].body[1])
    if head == first then node.bodies[1].body:remove(1) end
  end
  return node
end

function Pandoc(doc)
  local equation_number, section_number = 0, 0
  local reference_numbers = {}
  local displays = {}
  for _, environment in ipairs({"equation", "align"}) do
    local pattern = "()\\begin{" .. environment .. "}(.-)\\end{" .. environment .. "}"
    for offset, body in source:gmatch(pattern) do
      displays[#displays + 1] = {offset = offset, body = body, environment = environment}
    end
  end
  table.sort(displays, function(a, b) return a.offset < b.offset end)
  for _, display in ipairs(displays) do
    local rows = {display.body}
    if display.environment == "align" then
      rows = {}
      for row in (display.body .. "\\\\"):gmatch("(.-)\\\\") do rows[#rows + 1] = row end
    end
    for _, row in ipairs(rows) do
      if not row:find("\\nonumber", 1, true) and not row:find("\\notag", 1, true) then
        equation_number = equation_number + 1
      end
      for key in row:gmatch("\\label{([^}]+)}") do
        reference_numbers[key] = "(" .. equation_number .. ")"
      end
    end
  end
  doc:walk({
    Header = function(node)
      if node.level == 1 and not node.classes:includes("unnumbered") then
        section_number = section_number + 1
        reference_numbers[node.identifier] = tostring(section_number)
      end
    end
  })
  doc = doc:walk({Cite = citation, Div = replace_bibliography, Table = clean_table})
  doc = doc:walk({
    BlockQuote = function(node)
      if #node.content == 1 and node.content[1].t == "CodeBlock" then
        return pandoc.CodeBlock(node.content[1].text, pandoc.Attr("", {"text"}))
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
    end,
    Header = function(node)
      if node.identifier:match("^sec:") then
        return {pandoc.RawBlock("html", '<a id="' .. node.identifier .. '"></a>'), node}
      end
    end,
    Link = function(node)
      local key = node.attributes["reference"]
      if key and reference_numbers[key] then
        return pandoc.Link(reference_numbers[key], node.target)
      end
      return node
    end
  })
  local opening = pandoc.Blocks({pandoc.Header(1, pandoc.utils.stringify(doc.meta.title))})
  opening:insert(pandoc.Para(pandoc.utils.stringify(doc.meta.author)
    .. ". " .. pandoc.utils.stringify(doc.meta.date)))
  opening:insert(pandoc.Header(2, "Abstract"))
  opening:extend(doc.meta.abstract)
  opening:extend(doc.blocks)
  doc.blocks = opening
  return doc
end
