systemMenu = {"หมู": 50, "เห็ด": 60, "เป็ด": 70, "ไก่": 80}
menuList = []

def showbill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += int(menuList[number][1])
        print("Total :", total)


while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showbill()