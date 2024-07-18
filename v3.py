#
class Game :
    def __init__(self, name, sex, job):
        self.game_name = name
        self.game_sex = sex
        self.game_job = job

    def bark(self) :
        print("공격")


my_cha = Game("유진", "여", "학생")

my_cha.bark()
print(my_cha.game_name)

#교수님
class Game :
    def __init__(self,name,sex,cr):
        self.game_name = name
        self.game_sex = sex
        self.game_cr = cr

    def bark(self):
        print(self.game_name, "(이)가 공격했다!")

my_Game = Game("유진","여","학생")

my_Game.bark()
print(my_Game.game_name)

#"~를 공격했다!" 로 만들기
class Game :
    def __init__(self,name,sex,cr):
        self.game_name = name
        self.game_sex = sex
        self.game_cr = cr


    def bark(self , b):
        print(self.game_name, "(이)가", b ,"를 공격했다!")
        return b


my_Game = Game("유진","여","학생")

my_Game.bark("괴물")
print(my_Game.game_name)