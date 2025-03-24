--[[
自动持续使用潜力,自动开潜力灵龛
--]]
--自动开潜力灵=关闭,开启
sItemBagList = {}
sItemList = {}
sItemBagList = {'初级潜力灵龛','中级潜力灵龛','高级潜力灵龛'}
sItemList = {'初级HP潜力药水','初级SP潜力药水','初级力量潜力药水','初级体力潜力药水','初级魔法力潜力药水','初级幸运值潜力药水','初级防御力潜力药水','初级魔法抵抗力潜力药水','中级HP潜力药水','中级SP潜力药水','中级力量潜力药水','中级体力潜力药水','中级魔法力潜力药水','中级幸运值潜力药水','中级防御力潜力药水','中级魔法抵抗力潜力药水','高级HP潜力药水','高级SP潜力药水','高级力量潜力药水','高级体力潜力药水','高级魔法力潜力药水','高级幸运值潜力药水','高级防御力潜力药水','高级魔法抵抗力潜力药水'}
system_print("开始运行:自动持续使用潜力物品")
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
	if (自动开潜力灵 == '开启' and bItemUse ~= 2)
	then
		for key, value in pairs(sItemBagList) do
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
	end
	if (bItemUse == 0)
	then
		system_print("背包里已没有相应物品,使用物品完毕")
		system_end()
	end
	return 1000
end