menuList = []
priceList = []

def showBill():     # ต้องอยู่ข้างบนก่อนเรียกใช้
    total = 0       # ประกาศตัวแปรเปล่าๆก่อนค่อยเอาไปใช้
    print("-------My Food-------")
    for number in range(len(menuList)): # วนซ้ำโดยใช้ len เช็คตามจำนวนรอบที่ใส่ไป
        print("Menu :", menuList[number])
        print("Price :", priceList[number])
        total += int(priceList[number])
        print("Total :",total)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() =="exit"):  # .lower เปลื่ยนตัวข้างหน้าเป็นพิมพ์ใหญ่
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)   # .append ฟีลเหมือนเอาลง list มั้ง
        priceList.append(menuPrice)

print(menuList,priceList)
showBill()

