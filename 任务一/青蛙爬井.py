i = 0
day = 1
while True:
    if i < 20:
        i += 3

        print("第", day, "天向上爬了", i, "米")
        if i >= 20:
            print("第", day, "天爬到")
            break
        i -= 2
        print("第", day, "天夜晚下滑到了", i, "米")
        day += 1