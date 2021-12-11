# i=10
# if i==8:
#     print("这是8")
# elif i>9:
#     print("大于9")
# else:
#     print("不是8，也不是9")
#
# list=[1,2,3,4,5]
#
# try:
#       print(list[5])
#
# except Exception as e:
#       print("下标太长",e)
#
# dir(sys.modules['__builtin__'])

# b=True
#
# if b:
#     print("b为真")

# if 'a' in 'abd':
#     print("包含")
#
# for i in range(1,101):
#   print(i)

# list=[1,2,3,4,5,3]
# for i in list:
#   if list.count(i)>1:
#     print(list.index(i))
#
# try:
#   print("2"+2)
# except Exception as e:
#   print("类型错误",e)

# def test():
#   print("111")

class Father:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(f"{self.name}正在跑")


class Child:
    @staticmethod
    def go():
        print("我是孩子")


class Greatchild(Father, Child):
    @staticmethod
    def demo():
        print("我是孙子")


f = Father("张三", 5, 180)


if __name__ == '__main__':

    # f = Father("张三", 5, 180)
    # f.run()
    # c = Child("张三", 5, 180)
    # c.go()
    g = Greatchild("张三", 5, 180)
    g.demo()
