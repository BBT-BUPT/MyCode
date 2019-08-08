#BatchInstall.py
import os

#数据读入与处理
datals = []
to_install = open("第三方库安装目录.txt", "r", encoding="utf-8")
for line in to_install:
    line = line.replace("\n","")
    datals.append((line.split(" ")))
to_install.close()

#脚本安装
try:
    for datal in datals:
        for pyname in datal:
            os.system("pip3 install "+pyname)
            print("Start install "+pyname)
except:
    print("Failed Somehow")
else:
    print("Successful Install!!!")
