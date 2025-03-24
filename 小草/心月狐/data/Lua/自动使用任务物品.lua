--[[
自动持续使用物品,直到物品使用完为止
--]]
--物品1=[%ITEM4]
--物品2=[%ITEM4]
--物品3=[%ITEM4]
--物品4=[%ITEM4]
--物品5=[%ITEM4]
--物品6=[%ITEM4]
--物品7=[%ITEM4]
--物品8=[%ITEM4]
--物品9=[%ITEM4]
sItemList = {}
sItemList[1] = 物品1
sItemList[2] = 物品2
sItemList[3] = 物品3
sItemList[4] = 物品4
sItemList[5] = 物品5
sItemList[6] = 物品6
sItemList[7] = 物品7
sItemList[8] = 物品8
sItemList[9] = 物品9
system_print("开始运行:自动持续使用任务物品")
system_print("3秒开始使用,如误点可停止加载!")
_sleep(3000)
function RUN()
	if (system_online() == 0)
	then
		return 1000
	end
	local bItemNum = 0
	for key, value in pairs(sItemList) do
		if(item_num(value) ~= 0)
		then
			bItemNum = 1
		end
	end
	if (bItemNum == 0)
	then
		system_print("背包里已没有相应物品,使用物品完毕")
		system_end()
	end
	for key, value in pairs(sItemList) do
		if(item_use(value) ~= 0)
		then
			system_print("使用物品:"..value)
			break
		end
	end
	return 500	--返回0表示结束循环
end