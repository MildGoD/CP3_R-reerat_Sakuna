from tkinter import *
import math

def leftClickButton(event):
    bmi = format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f')
    bmiShow = ""

    if float(bmi) <= 18.5:
        bmiShow = "ผอมเกินไป"

    elif float(bmi) >= 18.6 and float(bmi) <= 22.9:
        bmiShow = "น้ำหนักปกติ เหมาะสม"

    elif float(bmi) >= 23 and float(bmi) <= 24.9:
        bmiShow = "น้ำหนักเกิน"

    elif float(bmi) >= 25 and float(bmi) <= 29.9:
        bmiShow = "อ้วน"

    elif float(bmi) >= 30:
        bmiShow = "อ้วนมาก"

    labelBmi.configure(text=bmiShow)
    labelResult.configure(text=bmi)

MainWindow = Tk()

labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

labelBmi = Label(MainWindow, text="BMI")
labelBmi.grid(row=3, column=1)

MainWindow.mainloop()