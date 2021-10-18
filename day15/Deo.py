'''
    r:读取
    w：写入
    +:  r+ ,w+
    a:附加

    b:byte字节模式（操作多媒体文件）

'''


try:
    file = open(file="白冰.jpg", mode="rb")
    # file1 = open(file="D:\\白冰1.jpg",mode="wb")
    data = file.read()
    # file1.write(data)

    print(data)

except Exception :
    print("改文件不存在！别瞎弄！")
