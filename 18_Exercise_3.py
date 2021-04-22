# n = 10
# print("Game Start")
# print("You Have 5 Chances to find correct num")
# print("Rols - You enter num 1 - 20 only")
# print("1 Chance try it")
# x = int(input("Enter num"))
# print("2 chance")
# x = int(input("Enter num"))
# print("3 chance")
# x = int(input("Enter num"))
# print("4 chance")
# x = int(input("Enter num"))
# print("5 chance")
# x = int(input("Enter num"))
# print("Game Over")

# if(x>15):
#     print("You are Enter less",x,"number")
# elif(x>11):
#     print("You are Enter less",x,"number")
# elif(x<10):
#     print("You enter small grater",x,"number")
# elif(x<5):
#     print("You enter grater",x,"number")
# elif(x==10):
#     print("Winner!!!!!!!!")
# else:
#     print("You are out of range")

print("You have only 5 chances")
x = 0
y = 5
s = 1
e = 5
for i in range(x,y):
    for j in range(s,e):
        print("Enter num chance",j)
        a = int(input())
        if(a>15):
            print("You are Enter less",a,"number")
        # elif(a>=11):
        #     print("You are Enter less",a,"number")
        elif(a<10):
            print("You enter small grater",a,"number")
        # elif(a<1):
        #     print("You enter grater",a,"number")
        elif(a==10):
            print("Winner!!!!!!!!")
        else:
            print("You are out of range")
        continue
print("Game over")