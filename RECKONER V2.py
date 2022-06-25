from tkinter import *

root = Tk()

isItThere = bool()

root.minsize(height = 500, width = 900)

noticeLabel = Label(root, text = """[NOTICE] THIS IS A RECKONER PROGRAM ANYTHING ELSE DOES NOT SUIT IT

DO NOT RESIZE THE WINDOW""")
noticeLabel.pack()

print("IF YOU CAN SEE THIS YOU HAVE FOUND THE CONSOLE. NOW CONTINUE WITH THE INSTRUCTIONS")


def Menu():
    confirmationLabel.destroy()
    confirmationButton.destroy()

    #.place(relx = 0.5, rely = 0.5, anchor = "center")

    global choosingLabel

    choosingLabel = Label(root, text = "Options:", font = ("Times_New_Roman", 25))
    choosingLabel.pack()

    global DTB

    DTB = Button(root, text = "Decimal To Binary", font = ("Times_New_Roman", 25), command = DecimalToBinary)
    DTB.place(relx = 0.5, rely = 0.3, anchor = "center")

    global BTD

    BTD = Button(root, text = "Binary To Decimal", font = ("Times_New_Roman", 25), command = BinaryToDecimal)
    BTD.place(relx = 0.5, rely = 0.5, anchor = "center")

    global HTB

    HTB = Button(root, text = "Hexadecimal To Binary", font = ("Times_New_Roman", 25), command = HexadecimalToBinary)
    HTB.place(relx = 0.5, rely = 0.7, anchor = "center")


    global BTH

    BTH = Button(root, text = "Binary To Hexadecimal", font = ("Times_New_Roman", 25), command = BinaryToHexadecimal)
    BTH.place(relx = 0.5, rely = 0.9, anchor = "center")


    backButton.destroy()
    decimalEntry.destroy()
    convert1.destroy()
    doSpaces.destroy()
    convert3.destroy()
    BinaryToDecimalEntry.destroy()
    HexadecimalToBinaryEntry.destroy()
    donNotDoSpaces.destroy()
    convert4.destroy()
    BinaryToHexadecimalEntry.destroy()
    doSpaces.destroy()
    convert5.destroy()





def DecimalToBinary():

    choosingLabel.destroy()
    DTB.destroy()
    BTD.destroy()
    HTB.destroy()
    BTH.destroy()



    global decimalEntry

    decimalEntry = Entry(root, width = 20)
    decimalEntry.pack()


    global backButton

    backButton = Button(root, text = "Back", font = ("Times_New_Roman", 25), command = Menu)
    backButton.pack(side = BOTTOM)

    global convert1

    convert1 = Button(root, text = "CONVERT!!!", command = DecimalToBinary2)
    convert1.pack()

def DecimalToBinary2():

    binNums = [128, 64, 32, 16, 8, 4, 2, 1]

    binNum2 = [8, 4, 2, 1]

    finBin = []

    i = 0

    count = 0


    convert = int(decimalEntry.get())

    for i in range(8):

        if convert >= binNums[i]:

            convert = convert - binNums[i]
            finBin.append(1)

        else:

            finBin.append(0)
            pass

        i = i + 1

    print(finBin)


def BinaryToDecimal():

    choosingLabel.destroy()
    DTB.destroy()
    BTD.destroy()
    HTB.destroy()
    BTH.destroy()

    global BinaryToDecimalEntry

    BinaryToDecimalEntry = Entry(root, width = 20)
    BinaryToDecimalEntry.pack()
    \

    global doSpaces

    doSpaces = Label(root, text = "Make sure you do a space between each number,  for example : (1 0 1 0 1 0 1 0) instead of: (10101010)")
    doSpaces.pack()

    global backButton

    backButton = Button(root, text = "Back", font = ("Times_New_Roman", 25), command = Menu)
    backButton.pack(side = BOTTOM)

    global convert3

    convert3 = Button(root, text = "CONVERT!!!", command = BinaryToDecimal2)
    convert3.pack()

def BinaryToDecimal2():

    i = 0

    binaryOutput = []

    decimalNumber = BinaryToDecimalEntry.get()

    binaryNumbers = [128,  64, 32, 16, 8, 4, 2, 1]

    binaryHolder = decimalNumber.split()

    binaryHolder = list(map(int, binaryHolder))

    finalDecimalNumber = 0

    for i in range(8):

        if binaryHolder[i] == 1:
            finalDecimalNumber = finalDecimalNumber + binaryNumbers[i]

        if binaryHolder[i] == 0:
            pass

        i = i + 1

    print(finalDecimalNumber)


def HexadecimalToBinary():

    choosingLabel.destroy()
    DTB.destroy()
    BTD.destroy()
    HTB.destroy()
    BTH.destroy()

    global HexadecimalToBinaryEntry

    HexadecimalToBinaryEntry = Entry(root, width = 20)
    HexadecimalToBinaryEntry.pack()

    global donNotDoSpaces

    donNotDoSpaces = Label(root, text = "Enter your Hexadecmial numbers. (No spaces)")
    donNotDoSpaces.pack()

    global convert4

    convert4 = Button(root, text = "CONVERT!!!", command = HexadecimalToBinary2)
    convert4.pack()

    global backButton

    backButton = Button(root, text = "Back", font = ("Times_New_Roman", 25), command = Menu)
    backButton.pack(side = BOTTOM)

def HexadecimalToBinary2():

    binNums = [8, 4, 2, 1]

    finNums = []

    convert4 = HexadecimalToBinaryEntry.get()

    loop = 0

    if convert4 != "":

        for i in range(0, len(convert4), 1):


            hexNumber1 = convert4[i]

            if hexNumber1 == "1":
                newNumber = 1
            if hexNumber1 == "2":
                newNumber = 2
            if hexNumber1 == "3":
                newNumber = 3
            if hexNumber1 == "4":
                newNumber = 4
            if hexNumber1 == "5":
                newNumber = 5
            if hexNumber1 == "6":
                newNumber = 6
            if hexNumber1 == "7":
                newNumber = 7
            if hexNumber1 == "8":
                newNumber = 8
            if hexNumber1 == "9":
                newNumber = 9
            if hexNumber1 == "A":
                newNumber = 10
            if hexNumber1 == "B":
                newNumber = 11
            if hexNumber1 == "C":
                newNumber = 12
            if hexNumber1 == "D":
                newNumber = 13
            if hexNumber1 == "E":
                newNumber = 14
            if hexNumber1 == "F":
                newNumber = 15


            for loop in range(4):

                if newNumber >= binNums[loop]:

                    newNumber = newNumber - binNums[loop]
                    finNums.append(1)

                else:

                    finNums.append(0)
                    pass
                    loop = loop + 1

        print(finNums)


def BinaryToHexadecimal():

    choosingLabel.destroy()
    DTB.destroy()
    BTD.destroy()
    HTB.destroy()
    BTH.destroy()

    global BinaryToHexadecimalEntry

    BinaryToHexadecimalEntry = Entry(root, width = 20)
    BinaryToHexadecimalEntry.pack()

    global doSpaces

    doSpaces = Label(root, text = "Input your binary numbers (only 4 numbers and make sure to put spaces in between to find your hexadecimal)")
    doSpaces.pack()

    global backButton

    backButton = Button(root, text = "Back", font = ("Times_New_Roman", 25), command = Menu)
    backButton.pack(side = BOTTOM)

    global convert5

    convert5 = Button(root, text = "CONVERT!!!", command = BinaryToHexadecimal2)
    convert5.pack()

def BinaryToHexadecimal2():

    hex0 = [0, 0, 0, 0]
    hex0 = list(map(int, hex0))

    hex1 = [0, 0, 0, 1]
    hex1 = list(map(int, hex1))

    hex2 = [0, 0, 1, 0]
    hex2 = list(map(int, hex2))

    hex3 = [0, 0, 1, 1]
    hex3 = list(map(int, hex3))

    hex4 = [0, 1, 0, 0]
    hex4 = list(map(int, hex4))

    hex5 = [0, 1, 0, 1]
    hex5 = list(map(int, hex5))

    hex6 = [0, 1, 1, 0]
    hex6 = list(map(int, hex6))

    hex7 = [0, 1, 1, 1]
    hex7 = list(map(int, hex7))

    hex8 = [1, 0, 0, 0]
    hex8 = list(map(int, hex8))

    hex9 = [1, 0, 0, 1]
    hex9 = list(map(int, hex9))

    hexA = [1, 0, 1, 0]
    hexA = list(map(int, hexA))

    hexB = [1, 0, 1, 1]
    hexB = list(map(int, hexB))

    hexC = [1, 1, 0, 0]
    hexC = list(map(int, hexC))

    hexD = [1, 1, 0, 1]
    hexD = list(map(int, hexD))

    hexE = [1, 1, 1, 0]
    hexE = list(map(int, hexE))

    hexF = [1, 1, 1, 1]
    hexF = list(map(int, hexF))


    binChoosing = BinaryToHexadecimalEntry.get()

    binaryHolder = binChoosing.split()

    binaryHolder = list(map(int, binaryHolder))

    finNums = []

    for i in range(1):
        if binaryHolder == hex0:
            finNums.append(0)
        elif binaryHolder == hex1:
            finNums.append(1)
        elif binaryHolder == hex2:
            finNums.append(2)
        elif binaryHolder == hex3:
            finNums.append(3)
        elif binaryHolder == hex4:
            finNums.append(4)
        elif binaryHolder == hex5:
            finNums.append(5)
        elif binaryHolder == hex6:
            finNums.append(6)
        elif binaryHolder == hex7:
            finNums.append(7)
        elif binaryHolder == hex8:
            finNums.append(8)
        elif binaryHolder == hex9:
            finNums.append(9)
        elif binaryHolder == hexA:
            finNums.append("A")
        elif binaryHolder == hexB:
            finNums.append("B")
        elif binaryHolder == hexC:
            finNums.append("C")
        elif binaryHolder == hexD:
            finNums.append("D")
        elif binaryHolder == hexE:
            finNums.append("E")
        elif binaryHolder == hexF:
            finNums.append("F")

    print(finNums)


def confirmation():

    global confirmationLabel

    confirmationLabel = Label(root, text = "Hello. Welcome to RECKONER V2! Click \"OK\" to start your conversions!", font = ("Helvetica", 20))
    confirmationLabel.place(relx = 0.5, rely = 0.4, anchor = "center")

    global confirmationButton

    confirmationButton = Button(root, text = "OK", font = ("Times_New_Roman", 30), command = Menu)
    confirmationButton.pack(side = BOTTOM)



confirmation()


root.mainloop()