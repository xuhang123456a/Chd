--[[
自动使用通天塔箱子
--]]
sItemList = {}
sItemList = {
'石之塔宝箱',
'石之塔高级宝箱',
'石之塔特级宝箱',
'铁之塔宝箱',
'铁之塔高级宝箱',
'铁之塔特级宝箱',
'银之塔宝箱',
'银之塔高级宝箱',
'银之塔特级宝箱',
'金之塔宝箱',
'金之塔高级宝箱',
'金之塔特级宝箱',
'暗之塔宝箱',
'暗之塔高级宝箱',
'暗之塔特级宝箱',
'魔之塔宝箱'
}
system_print("开始运行:自动持续使用通天塔箱子")
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