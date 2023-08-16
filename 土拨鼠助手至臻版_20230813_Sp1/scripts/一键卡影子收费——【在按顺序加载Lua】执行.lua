check=1
printgame(0,255,0,"友情提示：土拨鼠289卡超越收费Lua脚本")
while(true)
do
	if(getmapname()=="艾丽娅斯城市") then
	open_npc(110088)
	npc_plane(110088,431241,0,43124101,0)
	close_npc(110088)
	sleep(1500)
	end
end