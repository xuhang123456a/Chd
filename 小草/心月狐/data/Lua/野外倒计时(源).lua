starttime1 = system_time(0)
starttime3 = system_time(0)
time = ","
time1 = ","
tp = 0
tp1 = 0
function RUN()
	if(map_id() == 63404)
	then
		dlg_game_click("33006000",225,55)
		tp = 0
		tp1 = 0
	end
	if(map_id() == 1900)
	then
		dlg_game_click("33006000",225,55)
		tp = 0
		tp1 = 0
	end
	if(mob_hp(mob_obj("ɳ��֮��")) > 0)
	then
		_sleep(1000)
		if(mob_y(mob_obj("ɳ��֮��")) <= 383)
		then
			if(mob_x(mob_obj("ɳ��֮��")) >= 1259 and mob_x(mob_obj("ɳ��֮��"))<=1820)
			then
				system_msg("/p ɳ��֮���ڹ�����")
			end
		elseif(mob_y(mob_obj("ɳ��֮��")) <= 735)
		then
			if(mob_x(mob_obj("ɳ��֮��")) >= 2005 and mob_x(mob_obj("ɳ��֮��"))<=2255)
			then
				system_msg("/p ɳ��֮���ں��ʽ�")
			end
		elseif(mob_y(mob_obj("ɳ��֮��")) <= 751)
		then
			if(mob_x(mob_obj("ɳ��֮��")) >= 2659 and mob_x(mob_obj("ɳ��֮��"))<=3041)
			then
				system_msg("/p ɳ��֮�����·���")
			end
		elseif(mob_y(mob_obj("ɳ��֮��")) == 1503)
		then
			if(mob_x(mob_obj("ɳ��֮��")) < 1600)
			then
				system_msg("/p ɳ��֮�����������")
			else
				system_msg("/p ɳ��֮���������ұ�")
			end
		else
			system_msg("/p ɳ��֮����X��"..mob_x(mob_obj("ɳ��֮��")).."��������Y��"..mob_y(mob_obj("ɳ��֮��")))
		end
	end
	if(mob_obj("��ʧ����") > 0)
	then
		starttime1 = system_time(0)
	else
		starttime2 = system_time(0)
		local elapsed = starttime2 - starttime1
    		local minutes = (((545000-elapsed)/1000) % 3600) / 60
    		local seconds = ((545000-elapsed)/1000) % 60
    		if(minutes < 10)
		then
			minutes = "0"..minutes
		end
    		if(seconds < 10)
		then
			seconds = "0"..seconds
		end 
    		time = "��Ұ����ʱ��"..math.floor(minutes)..":"..math.floor(seconds)
	end
	if(mob_obj("ɳ��֮��") > 0 or mob_obj("����֮��") > 0 or mob_obj("ѩ��˿֮��") > 0 or mob_obj("������֮��") > 0)
	then
		starttime3 = system_time(0)
	else
		starttime4 = system_time(0)
		local elapsed1 = starttime4 - starttime3
    		local minutes1 = (((545000-elapsed1)/1000) % 3600) / 60
    		local seconds1 = ((545000-elapsed1)/1000) % 60
    		if(minutes1 < 10)
		then
			minutes1 = "0"..minutes1
		end
    		if(seconds1 < 10)
		then
			seconds1 = "0"..seconds1
		end 
    		time1 = "��Ұ����ʱ��"..math.floor(minutes1)..":"..math.floor(seconds1)
	end
		_sleep(1000)
	  	system_msg("/p "..time.."��������"..time1)
	  	system_print(time.."��������"..time1,1000)
	if(mob_obj("��ʧ����") == 0 and mob_obj("����֮��") == 0 and mob_obj("ɳ��֮��") == 0 and mob_obj("ѩ��˿֮��") == 0 and mob_obj("������֮��") == 0 and tp == 1)
	then
	  	system_print("BOSS������2�����ڻس�")
		_sleep(5000)
		if(mob_hp(mob_obj("��ʧ����")) > 0 or mob_hp(mob_obj("ɳ��֮��")) > 0 or mob_hp(mob_obj("����֮��")) > 0 or mob_hp(mob_obj("ѩ��˿֮��")) > 0 or mob_hp(mob_obj("������֮��")) > 0)
		then
			tp=0
	  		system_print("���·���BOSS��ȡ���س�")
		end
		if(tp == 1)
		then
			instance_plane(123)
			tp=0
		end
	end	
	if(mob_hp(mob_obj("��ʧ����")) > 0 or mob_hp(mob_obj("ɳ��֮��")) > 0 or mob_hp(mob_obj("����֮��")) > 0 or mob_hp(mob_obj("ѩ��˿֮��")) > 0 or mob_hp(mob_obj("������֮��")) > 0)
	then
		tp = 1
	end
	return 1000
end



