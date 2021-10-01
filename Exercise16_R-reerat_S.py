menuList = []
def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print("Menu :", menuList[number][0])
        print("Price :", menuList[number][1])

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()

