--[[
�Զ�����ʹ����Ʒ,ֱ����Ʒʹ����Ϊֹ
--]]
--��Ʒ1=[%ITEM2]
--��Ʒ2=[%ITEM2]
--��Ʒ3=[%ITEM2]
--��Ʒ4=[%ITEM2]
--��Ʒ5=[%ITEM2]
--��Ʒ6=[%ITEM2]
--��Ʒ7=[%ITEM2]
--��Ʒ8=[%ITEM2]
--��Ʒ9=[%ITEM2]
sItemList = {}
sItemList[1] = ��Ʒ1
sItemList[2] = ��Ʒ2
sItemList[3] = ��Ʒ3
sItemList[4] = ��Ʒ4
sItemList[5] = ��Ʒ5
sItemList[6] = ��Ʒ6
sItemList[7] = ��Ʒ7
sItemList[8] = ��Ʒ8
sItemList[9] = ��Ʒ9
system_print("��ʼ����:�Զ�����ʹ��������Ʒ")
system_print("3�뿪ʼʹ��,������ֹͣ����!")
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
		system_print("��������û����Ӧ��Ʒ,ʹ����Ʒ���")
		system_end()
	end
	for key, value in pairs(sItemList) do
		if(item_use(value) ~= 0)
		then
			system_print("ʹ����Ʒ:"..value)
			break
		end
	end
	return 500	--����0��ʾ����ѭ��
end
