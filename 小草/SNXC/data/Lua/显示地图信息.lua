--[[
��ʾ��ǰ��ͼ��Ϣ
--]]
lastMapid = 0
function RUN()
	if (lastMapid ~= map_id())
	then
		lastMapid = map_id()
		local sMsg = "��ǰ��ͼ��["..map_name().."]     ��ͼID��["..map_id().."]"
		system_msg(sMsg)
		system_print(sMsg)
	end
	return 1000
end