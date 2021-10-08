'''
    老手机：
        打电话：手机号，彩铃
    新手机：
        打电话：手机号，彩铃，归属地，大头贴，录音
'''
import time
class OldPhone:
    phoneNumber = ""
    voice = ""

    def call(self,number):
        print(self.phoneNumber,"正在打电话，打给：",number,"正在响铃：",self.voice)
        for i  in range(8):
            print(".",end="")
            time.sleep(1)
        print("对方已接通！！")

class NewPhone(OldPhone):
    # 归属地，大头贴，录音
    address = ""
    picture = ""
    mic = False

    def call(self,number):
        # 2个属性由老手机代码显示
        super().call(number)

        # 3个新属性由新手机自己显示
        self.mic = True
        print("本机归属地：",self.address,"，对方大头贴为：",self.picture,",已经开启了录音功能！")
        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print("本次通话完成[5:36]！")


phone = NewPhone()
phone.phoneNumber = "13552648187"
phone.voice = "江南style"
phone.picture = "野猪佩奇"
phone.address = "北京移动"

phone.call("13379854676")






















