while(true)
do
mapid_now = getmapid()
sleep(10)
	if (mapid_now ~= mapid_last) then--��ֹ���ص�ͼ����--
		mapid_last = mapid_now
		print("��ǰ��ͼid��"..getmapid().."     ��ǰ��ͼ����["..getmapname().."]")
		sleep(10)
	end
end