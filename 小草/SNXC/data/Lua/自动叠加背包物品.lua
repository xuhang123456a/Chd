--[[
�Զ���������,����,���񱳰���Ʒ,������Ϸ������,�������ƶ���Ʒ����
��ʾ:ִ�к���Ҫ����һ�α���
--]]
function RUN()
	if(item_merge(1) == 0 and item_merge(2) == 0 and item_merge(3) == 0)
	then
		return 0
	else
		--������Ҫ�رձ�������,������ȷˢ����ʾ
		dlg_game_close("30007000")
	end
	return 150
end