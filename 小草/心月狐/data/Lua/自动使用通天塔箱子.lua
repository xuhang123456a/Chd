--[[
�Զ�ʹ��ͨ��������
--]]
sItemList = {}
sItemList = {
'ʯ֮������',
'ʯ֮���߼�����',
'ʯ֮���ؼ�����',
'��֮������',
'��֮���߼�����',
'��֮���ؼ�����',
'��֮������',
'��֮���߼�����',
'��֮���ؼ�����',
'��֮������',
'��֮���߼�����',
'��֮���ؼ�����',
'��֮������',
'��֮���߼�����',
'��֮���ؼ�����',
'ħ֮������'
}
system_print("��ʼ����:�Զ�����ʹ��ͨ��������")
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
	return 1000
end