check=1

name="��֮��2��"
state=0
getbox=1
--1Ҫ���� 0��Ҫ����--

while(true)
do   
	if(getmapname()==name) then --�Ѿ������--
		box_if=indun_box_if()--�������״̬--
		if(box_if==0) then
			bot_start()--�����һ�--
		end
		if(box_if==1) then --���ӳ���--
			if(getbox==1) then
				indun_box_get()--������--
			end
			break
		end
	else
		state=indun_into(name)
		if(state==2) then
			break
		elseif(state==1) then
			bot_start()--�����һ�--
		elseif(state==-1) then
			bot_start()--�����һ�--
		elseif(state==0) then
		elseif(state==3) then
			if(useitem("�߼�����������")==0) then
				if(useitem("�м�����������")==0) then
					if(useitem("�ͼ�����������")==0) then
						break
					end
				end
			end
		end

	end
end
bot_stop()

if(state==2) then
	printgame(0,255,0,"��������ʾͨ������"..name.."�Ѿ�ˢ����û��ͨ����ɨ��ָ����~��")
elseif(state==3) then
	printgame(0,255,0,"��������ʾ��ȱ������")
else
	printgame(0,255,0,"     ��������ʾͨ������"..name.."����ɣ�     ��дby:ţ��")
end
sleep(1000)