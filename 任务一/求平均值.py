def max(*a):
    m = a[0]
    for x in a:
        if x > m:
            m = x
    return m
k,b,c,d,e,f,g,h,i,j=map(int,input().split(","))
print("最大值为：", max(k,b,c,d,e,f,g,h,i,j))
print("平均数为：", (k+b+c+d+e+f+g+h+i+j)/10)
print("和为：", k+b+c+d+e+f+g+h+i+j)







# sum = 0
# or i in list:
#    int(i)
#    s = s + i
# print("和为", s)
#
# print("平均数为", s/len(list))  # lenth

