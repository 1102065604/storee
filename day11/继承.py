'''
    面向对象：
    继承：
        子类与父类



'''
class Person:
    username = ""
    age = 0
    sex = ""
    address = None


class Address:
    country = ""
    province = ""
    street = ""
    door = ""

p  =  Person()
p.username = "尉超会"
p.sex = "female"
p.age = 56

add = Address()
add.country = "CN"
add.province = "安徽省"
add.street = "桃园路"
add.door = "SS001"

p.address = add






























