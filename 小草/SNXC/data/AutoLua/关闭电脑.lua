sleepCount = 60
while (sleepCount > 0)
do
	system_print(sleepCount.."秒后即将关闭电脑,如想取消请到自动副本列表停止LUA执行",1500)
	sleepCount = sleepCount - 1
	_sleep(1000)
end
system_log("开始执行关闭电脑")
_sleep(1000)
system_close(1)