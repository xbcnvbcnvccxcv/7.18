class 사칙연산:
    def 더하기 (self, a, b):
        result= a+b
        return result

    def 곱하기 (self, a, b):
        result = a*b
        return result

    def 나누기 (self, a, b):
        result = a/b
        return result

    def 빼기 (self, a, b):
        result = a-b
        return result

app = 사칙연산()
print(app.나누기(3,4))

#
# def add(a,b):
#     result= a+b + b**b + a**a
#     return result
# ap= add()
# print(ap