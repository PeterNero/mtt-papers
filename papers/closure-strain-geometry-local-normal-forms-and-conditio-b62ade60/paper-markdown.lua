-- Keep local citations, revision descriptions and built cross-references readable.
local function read_file(name)
  local f = io.open(name, "r")
  if not f then return nil end
  local value = f:read("*a")
  f:close()
  return value
end
local source = assert(read_file("main.tex"))
local bibliography = assert(source:match("\\begin{thebibliography}{%d+}(.-)\\end{thebibliography}"))
local entries, numbers, descriptions, refs = {}, {}, {}, {}
local offset = 1
while true do
  local first, last, key = bibliography:find("\\bibitem{([^}]+)}", offset)
  if not first then break end
  local following = bibliography:find("\\bibitem{", last + 1, true)
  local body = bibliography:sub(last + 1, following and following - 1 or -1)
  body = body:gsub("\\newblock", " ")
  body = body:gsub("\\frozenresult{([^}]+)}{([^}]+)}", function(id, title)
    return "\\href{https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/"
      .. id .. "/artifact.json}{" .. title .. "}"
  end)
  entries[#entries + 1] = {key = key, body = body}
  numbers[key] = #entries
  offset = last + 1
end
for body in source:gmatch("\\begin{description}(.-)\\end{description}") do
  descriptions[#descriptions + 1] = body
end
for key, value in (read_file("main.aux") or ""):gmatch("\\newlabel{([^}]+)}{{([^}]*)}") do
  refs[key] = value
end
local function cite(node)
  local result = pandoc.Inlines({pandoc.Str("[")})
  for i, item in ipairs(node.citations) do
    if i > 1 then result:insert(pandoc.Str(",")) end
    result:insert(pandoc.Link(tostring(assert(numbers[item.id], item.id)), "#ref-" .. item.id))
  end
  result:insert(pandoc.Str("]"))
  return result
end
local function reference_blocks()
  local blocks = pandoc.Blocks({pandoc.Header(1, "References")})
  for i, item in ipairs(entries) do
    blocks:insert(pandoc.RawBlock("html", '<a id="ref-' .. item.key .. '"></a>'))
    local parsed = pandoc.read(item.body, "latex"):walk({Cite = cite}).blocks
    if parsed[1] and parsed[1].content then
      parsed[1].content:insert(1, pandoc.Str("[" .. tostring(i) .. "] "))
    end
    blocks:extend(parsed)
  end
  return blocks
end
function Pandoc(doc)
  local description_index, references_seen = 0, false
  doc = doc:walk({
    Cite = cite,
    Div = function(node)
      if node.classes:includes("thebibliography") then
        references_seen = true
        return reference_blocks()
      end
      if not node.classes:includes("description") then return nil end
      description_index = description_index + 1
      local body = assert(descriptions[description_index])
      local blocks, pos = pandoc.Blocks({}), 1
      while true do
        local first, last, label = body:find("\\item%[([^%]]+)%]", pos)
        if not first then break end
        local following = body:find("\\item[", last + 1, true)
        local parsed = pandoc.read(body:sub(last + 1, following and following - 1 or -1), "latex")
          :walk({Cite = cite}).blocks
        if parsed[1] and parsed[1].content then
          parsed[1].content:insert(1, pandoc.Space())
          parsed[1].content:insert(1, pandoc.Strong(label))
        end
        blocks:extend(parsed)
        pos = last + 1
      end
      return blocks
    end,
    Link = function(node)
      local key = node.attributes["reference"]
      if key and refs[key] then return pandoc.Link(refs[key], node.target) end
    end
  })
  if not references_seen then doc.blocks:extend(reference_blocks()) end
  local opening = pandoc.Blocks({pandoc.Header(1, pandoc.utils.stringify(doc.meta.title))})
  opening:insert(pandoc.Para(pandoc.utils.stringify(doc.meta.author)
    .. ". " .. pandoc.utils.stringify(doc.meta.date)))
  opening:insert(pandoc.Header(2, "Abstract"))
  opening:extend(doc.meta.abstract)
  opening:extend(doc.blocks)
  doc.blocks = opening
  return doc
end
