import os

os.popen("chcp 65501")
ret = input("已配置希沃白板为原启，是否还原？若不还原则不输入，否则输入1：")
if ret == "1":
    print(os.popen("./xwbb/return/restore.bat"))
    print("删除成功")
elif ret == "":
    print(os.popen("./xwbb/change/set.bat"))
    print("设置成功")
else:
    raise SyntaxError

os.popen("pause")
