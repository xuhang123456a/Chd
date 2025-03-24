--[[
自动使用梦灵碎片
--]]
--自动开梦灵碎片包=开启,关闭
sItemList = {}
sItemList = {
'[梦灵]石碑碎片',
'[梦灵]丑八怪大王碎片',
'[梦灵]幼年独角兽碎片',
'[梦灵]上京城碎片',
'[梦灵]菲轮塔碎片',
'[梦灵]虎狼寺碎片',
'[梦灵]粉色电气石碎片',
'[梦灵]小山羊碎片',
'[梦灵]火箭龙猫碎片',
'[梦灵]木偶碎片',
'[梦灵]爱丽丝碎片',
'[梦灵]龙猫妹妹碎片',
'[梦灵]传送门碎片',
'[梦灵]混沌碎片',
'[梦灵]上忍碎片',
'[梦灵]坎贝尔碎片',
'[梦灵]棕熊碎片',
'[梦灵]粉团子碎片',
'[梦灵]红龙碎片',
'[梦灵]回音雪地碎片',
'[梦灵]狐狸队长碎片',
'[梦灵]玄武碎片',
'[梦灵]绿企鹅碎片',
'[梦灵]滑板龙猫碎片',
'[梦灵]雷比碎片',
'[梦灵]初月祭坛碎片',
'[梦灵]影像石碑碎片',
'[梦灵]传送门碎片',
'[梦灵]上京城碎片',
'[梦灵]浑沌碎片',
}
system_print("开始运行:自动持续使用梦灵碎片")
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
	if (自动开梦灵碎片包 == '开启' and bItemUse ~= 2)
	then
		if(item_use('梦灵碎片包') ~= 0)
		then
			system_print("使用物品:梦灵碎片包")
			bItemUse = 2
		elseif (item_num('梦灵碎片包') ~= 0)
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