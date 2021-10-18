


def getValue():
    try:
        print("嘻嘻！")
        raise SystemError("蓝瓶的！")
        return 1
    except Exception:
        print("哈哈！")
        return 2
    finally:
        print("你超勇啊！")

print(getValue())




















