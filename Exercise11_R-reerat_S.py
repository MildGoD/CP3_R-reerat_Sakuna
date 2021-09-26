x = int(input())
y = x-1
z = 1

for i in range(x):
    print(" "*y,end="")
    print("*"*z)
    z+=2
    y-=1