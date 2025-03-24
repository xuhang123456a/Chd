--[[
显示当前地图信息
--]]
lastMapid = 0
function RUN()
	if (lastMapid ~= map_id())
	then
		lastMapid = map_id()
		local sMsg = "当前地图：["..map_name().."]     地图ID：["..map_id().."]"
		system_msg(sMsg)
		system_print(sMsg)
	end
	return 1000
end