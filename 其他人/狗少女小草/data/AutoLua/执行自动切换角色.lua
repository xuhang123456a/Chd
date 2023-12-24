local sName = system_changeplayer()
if (sName == '')
then
	system_print('未找到已设置可切换角色')
else
	system_print('准备切换角色:'..sName)
end