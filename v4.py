class Home :
    def __init__(self, A , B , C , D , E ):
        self.Home_A = A
        self.Home_B = B
        self.Home_C = C
        self.Home_D = D
        self.Home_E = E

    def bark(self):
        print(self.Home_A, self.Home_B, self.Home_C, self.Home_D, self.Home_E)

my_ar = Home("유진하우스", "대구 복현동", "1억", "2018년", "42평")

my_ar.bark()

#
class Building:
    def __init__(self, loc, y , p , a):
        self.__init__()

        def print_info(self):
            print(
                "건물위치 :", self
            )