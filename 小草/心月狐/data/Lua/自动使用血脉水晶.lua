--[[
�Զ�Ѫ��ˮ��
--]]
sItemList = {}
sItemList = {
'ԭʼʱ��Ѫ��ˮ��',
'��ͼ�ʱ��Ѫ��ˮ��',
'�ͼ�ʱ��Ѫ��ˮ��',
'�м�ʱ��Ѫ��ˮ��',
'�߼�ʱ��Ѫ��ˮ��',
'��߼�ʱ��Ѫ��ˮ��',
'�ͼ�Ѫ��ˮ��(��)',
'�м�Ѫ��ˮ��(��)',
'�߼�Ѫ��ˮ��(��)',
'�ؼ�Ѫ��ˮ��(��)'
}
system_print("��ʼ����:�Զ������Զ�Ѫ��ˮ��")
system_print("3�뿪ʼʹ��,������ֹͣ����!")
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
			system_print("ʹ����Ʒ:"..value)
			bItemUse = 2
			break
		elseif (item_num(value) ~= 0)
		then
			bItemUse = 1
		end
	end
	if (bItemUse == 0)
	then
		system_print("��������û����Ӧ��Ʒ,ʹ����Ʒ���")
		system_end()
	end
	return 500
end