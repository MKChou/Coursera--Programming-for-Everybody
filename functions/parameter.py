#定義函式
def greet(number):
    if number=="1":
        print("number=1")
    elif number=="2":
        print("number=2")
    else:
        print("number!=1,2")

#1.輸入輸字
number=input("Enter a number:")
greet(number)

#2.直接呼叫函式
greet("1")

#3.宣告
number="2"
greet(number)

