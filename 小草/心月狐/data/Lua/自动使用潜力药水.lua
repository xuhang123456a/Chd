--[[
�Զ�����ʹ��Ǳ��,�Զ���Ǳ������
--]]
--�Զ���Ǳ����=�ر�,����
sItemBagList = {}
sItemList = {}
sItemBagList = {'����Ǳ������','�м�Ǳ������','�߼�Ǳ������'}
sItemList = {'����HPǱ��ҩˮ','����SPǱ��ҩˮ','��������Ǳ��ҩˮ','��������Ǳ��ҩˮ','����ħ����Ǳ��ҩˮ','��������ֵǱ��ҩˮ','����������Ǳ��ҩˮ','����ħ���ֿ���Ǳ��ҩˮ','�м�HPǱ��ҩˮ','�м�SPǱ��ҩˮ','�м�����Ǳ��ҩˮ','�м�����Ǳ��ҩˮ','�м�ħ����Ǳ��ҩˮ','�м�����ֵǱ��ҩˮ','�м�������Ǳ��ҩˮ','�м�ħ���ֿ���Ǳ��ҩˮ','�߼�HPǱ��ҩˮ','�߼�SPǱ��ҩˮ','�߼�����Ǳ��ҩˮ','�߼�����Ǳ��ҩˮ','�߼�ħ����Ǳ��ҩˮ','�߼�����ֵǱ��ҩˮ','�߼�������Ǳ��ҩˮ','�߼�ħ���ֿ���Ǳ��ҩˮ'}
system_print("��ʼ����:�Զ�����ʹ��Ǳ����Ʒ")
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
	if (�Զ���Ǳ���� == '����' and bItemUse ~= 2)
	then
		for key, value in pairs(sItemBagList) do
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
	end
	if (bItemUse == 0)
	then
		system_print("��������û����Ӧ��Ʒ,ʹ����Ʒ���")
		system_end()
	end
	return 1000
end