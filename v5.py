class Man:
    def __init__(self, name, age, phone):
        self.name = name
        self. age = age
        self. phon = phone

    def print_info(self):
        print(
            "이름 :", self.name,
            "\n나이 :", self.age,
            "\n연락처 :", self.phone)


my_list= Man("정유진", "23", "010-8455-3116")

my_list.print_info() # .append 를 쓰는 부분입니다. 정말 중요

#교수님
class Person :
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    def print_info(self):
        print(self.name, self.age, self.phone)

my_person = Person("정유진","23","010-8455-3116")
my_person.print_info()

이승연 왔다감ㅋ