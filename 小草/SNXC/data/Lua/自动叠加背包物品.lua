--[[
自动叠加消耗,其他,任务背包物品,类似游戏整理功能,但不会移动物品排序
提示:执行后需要开关一次背包
--]]
function RUN()
	if(item_merge(1) == 0 and item_merge(2) == 0 and item_merge(3) == 0)
	then
		return 0
	else
		--这里需要关闭背包窗口,才能正确刷新显示
		dlg_game_close("30007000")
	end
	return 150
end