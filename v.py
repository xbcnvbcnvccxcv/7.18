# def 함수이름():
#     return

class Dog :
    def __init__(self, name, breed): #그릇 만들기
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "여"
    def bark(self) :
        print("개가 짖습니다.")

Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()

#
class Dog :
    def __init__(self, name, breed): #그릇 만들기
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "여"
    def bark(self) :
        print(self.dog_name + "가 짖습니다.") #self.dog_breed를 하면 말티즈가 짖습니다.

Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()
Dog("뽀삐", "말티즈").bark()

#
class Dog :
    def __init__(self, name, breed): #그릇 만들기
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "여"
    def bark(self) :
        print(self.dog_name + "가 짖습니다.") #self.dog_breed를 하면 말티즈가 짖습니다.

my_dog = Dog("뽀삐", "말티즈")
my_dog.bark()
my_dog.bark()
my_dog.bark()
my_dog.bark()
