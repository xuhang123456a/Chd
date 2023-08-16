while(true)
do
mapid_now = getmapid()
sleep(10)
	if (mapid_now ~= mapid_last) then--防止加载地图崩溃--
		mapid_last = mapid_now
		print("当前地图id："..getmapid().."     当前地图名：["..getmapname().."]")
		sleep(10)
	end
end