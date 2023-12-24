--[[
自动血脉水晶
--]]
sItemList = {}
sItemList = {
'原始时空血脉水晶',
'最低级时空血脉水晶',
'低级时空血脉水晶',
'中级时空血脉水晶',
'高级时空血脉水晶',
'最高级时空血脉水晶',
'低级血脉水晶(绑定)',
'中级血脉水晶(绑定)',
'高级血脉水晶(绑定)',
'特级血脉水晶(绑定)'
}
system_print("开始运行:自动持续自动血脉水晶")
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
	return 500
end