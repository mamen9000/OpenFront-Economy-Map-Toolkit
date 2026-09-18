-- Build: 302af6745b1d5bf583c3031a80d216fc
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
