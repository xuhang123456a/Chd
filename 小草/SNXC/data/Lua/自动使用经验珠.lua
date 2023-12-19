--[[
自动使用经验珠
--]]
sItemList = {}
sItemList = {
'败家经验珠',
'超级败家经验珠',
'宝莱坞经验珠(主职业)',
'高级经验药水',
'特级经验药水'
}
system_print("开始运行:自动持续使用经验珠")
system_print("3秒开始使用,如误点可停止加载!")
_sleep(3000)
function RUN()
	if (system_online() == 0)
	then
		return 1000
	end
	local bItemUse = 0
	for key, value in pairs(sItemList) do
		if(item_use(value) ~= 0)
		then
			system_print("使用物品:"..value)
			bItemUse = 2
			break
		elseif (item_num(value) ~= 0)
		then
			bItemUse = 1
		end
	end
	if (bItemUse == 0)
	then
		system_print("背包里已没有相应物品,使用物品完毕")
		system_end()
	end
	return 1000
end