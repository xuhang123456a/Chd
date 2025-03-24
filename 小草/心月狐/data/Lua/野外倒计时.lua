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
	if(mob_hp(mob_obj("沙雅之王")) > 0)
	then
		_sleep(1000)
		if(mob_y(mob_obj("沙雅之王")) <= 383)
		then
			if(mob_x(mob_obj("沙雅之王")) >= 1259 and mob_x(mob_obj("沙雅之王"))<=1820)
			then
				system_msg("/p 沙雅之王在公主坟")
			end
		elseif(mob_y(mob_obj("沙雅之王")) <= 735)
		then
			if(mob_x(mob_obj("沙雅之王")) >= 2005 and mob_x(mob_obj("沙雅之王"))<=2255)
			then
				system_msg("/p 沙雅之王在海鲜街")
			end
		elseif(mob_y(mob_obj("沙雅之王")) <= 751)
		then
			if(mob_x(mob_obj("沙雅之王")) >= 2659 and mob_x(mob_obj("沙雅之王"))<=3041)
			then
				system_msg("/p 沙雅之王在新发地")
			end
		elseif(mob_y(mob_obj("沙雅之王")) == 1503)
		then
			if(mob_x(mob_obj("沙雅之王")) < 1600)
			then
				system_msg("/p 沙雅之王在下面左边")
			else
				system_msg("/p 沙雅之王在下面右边")
			end
		else
			system_msg("/p 沙雅之王在X："..mob_x(mob_obj("沙雅之王")).."…………Y："..mob_y(mob_obj("沙雅之王")))
		end
	end
	if(mob_obj("迷失黄龙") > 0)
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
    		time = "王野倒计时："..math.floor(minutes)..":"..math.floor(seconds)
	end
	if(mob_obj("沙雅之王") > 0 or mob_obj("佐尼之王") > 0 or mob_obj("雪莉丝之王") > 0 or mob_obj("阿修罗之王") > 0)
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
    		time1 = "低野倒计时："..math.floor(minutes1)..":"..math.floor(seconds1)
	end
		_sleep(1000)
	  	system_msg("/p "..time.."…………"..time1)
	  	system_print(time.."…………"..time1,1000)
	if(mob_obj("迷失黄龙") == 0 and mob_obj("佐尼之王") == 0 and mob_obj("沙雅之王") == 0 and mob_obj("雪莉丝之王") == 0 and mob_obj("阿修罗之王") == 0 and tp == 1)
	then
	  	system_print("BOSS死亡，2秒钟内回城")
		_sleep(5000)
		if(mob_hp(mob_obj("迷失黄龙")) > 0 or mob_hp(mob_obj("沙雅之王")) > 0 or mob_hp(mob_obj("佐尼之王")) > 0 or mob_hp(mob_obj("雪莉丝之王")) > 0 or mob_hp(mob_obj("阿修罗之王")) > 0)
		then
			tp=0
	  		system_print("重新发现BOSS，取消回城")
		end
		if(tp == 1)
		then
			instance_plane(123)
			tp=0
		end
	end	
	if(mob_hp(mob_obj("迷失黄龙")) > 0 or mob_hp(mob_obj("沙雅之王")) > 0 or mob_hp(mob_obj("佐尼之王")) > 0 or mob_hp(mob_obj("雪莉丝之王")) > 0 or mob_hp(mob_obj("阿修罗之王")) > 0)
	then
		tp = 1
	end
	return 1000
end



