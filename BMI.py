import datetime
class Pesson:
    pre_name = ''
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age  #共有属性
        self.__weight = weight  # 私有属性
        self.__height = height

    def old(self,age):
        p= age - self.age
        print('出生时间',p)
        #return p

    def __getBMI(self):
        bmi = self.__weight/self.__height**2
        return bmi
    def getgrad(self):

        dd = datetime.datetime.now()
        now_age = self.old(dd.year)
        if now_age >= 18:

            bmi = self.__getBMI()
            print('身体的质量指数BMI=','%.2f' %bmi,end='')

            if bmi < 18.5:
                print('过轻')
            elif bmi < 25.0:
                print('正常')
            elif bmi < 28.0:
                print('过重')
            elif bmi < 32:
                print('肥胖')
            else:
                print('非常肥胖')

        else:
            print('未满18不计算BMI')


pd = Pesson('lhj',20,52.5,1.70)
print('姓名',pd.name)
print('年龄',pd.age)
print(pd.old(20))
print('体重',pd._Pesson__weight,'kg')
#pd.getgrad()


