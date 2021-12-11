# if True:    #如果 表达式为真，则执行print('111')
#     print('111')

# if 1==1:   #1==1为真，所以执行print('111')
#     print('111')

# if 1==2:  #1==2为假，所以不执行print('111')
#     print('111')

# if 1==1 and 2==2: #and 代表并且, 为真，所以执行print('111')
#     print('111')

# if 1==1 and 2==3: #and 代表并且, 为假，所以不执行print('111')
#     print('111')

# if 1==1 or 1==2: #or 代表或者,为真，所以执行print('111')
#     print('111')

# if 1!=2: #!= ,不等于，为真，所以执行print('111')
#     print('111')

# if 'a' in 'aaaa':  # in 表示包含，aaaa包含a,为真，所以执行print('111')
#     print('111')

# if 'a' not in 'aaaa':  #not in 不包含，为假，所以不执行print('111')
#     print('111')

# list=['aaaa','bbbb','ccc']
# if 'a' in list:   #不包含，为假，所以不执行print('包含')
#     print('包含')

# dict={"name":"xiaowang","age":25}
# if 'xiaowang' in dict:   #比较的是键并不是值，为假，所以不执行print('包含')
#     print('包含')


# for i in range(1,101):    #循环输出1到100，初始值为1，当 i等于101时循环终止
#     print(i)

# sum=0
# for i in range(1,51): #1到50的和
#     sum=sum+i
# print(sum)

# list=[1,3,4,3,3,5,6,7]
# for i in list:    #count统计元素出现次数，如果次数大于1，则说明有重复的数
#     if list.count(i)>1:
#         print(list.index(i))

# try:
#     print(2+"2")
# except TypeError:   #如果发生TypeError异常，则执行下面的语句
#     print("数字与字符串不能相加")


# try:
#     print(2+2)
# except Exception as e:   #Exception所有异常的父类，
#     print("数字与字符串不能相加",e)
