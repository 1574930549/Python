import uiautomator2 as u2
from time import sleep

d = u2.connect('127.0.0.1:7555')
print(d)
# # 启动App
d.app_start("com.tencent.mm")
#
# # 搜索
# d(resourceId="com.meizu.mzbbs:id/j0").click()
#
# # 输入关键字
# d(resourceId="com.meizu.mzbbs:id/p9").set_text("flyme")
#
# # 搜索按钮
# d(resourceId="com.meizu.mzbbs:id/tp").click()
#
# sleep(2)
#
# # 停止app
# d.app_stop("com.meizu.mzbbs")