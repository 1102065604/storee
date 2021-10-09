'''
    所有类的共同父类：object
    object规范和管理所有的子类。
    面试题：
        python2x.3x中继承：
            2纵向查找
            3横向查找
    面向对象版的中国工商银行：
        代码
'''

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(D.__mro__)

