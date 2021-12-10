from tkinter import *
from tkinter import ttk

main = Tk()
main.title("Gold Karat Convert Program version 0.1")
main.configure(bg = "black")

def click():
    customerchoice = radiovar1.get()
    convertto = radiovar2.get()
    user_amount = float(textentry.get())
    print_result = normal_formular(customerchoice, convertto, user_amount)
    #output.insert("You need to add more alloy: {0} \n And your total amount of your gold will be : {1} \n".format(alloy_to_add,total_amount))
    output.delete(0.0, END)
    output.insert(END, print_result)

#create question for type of user's gold
label1 = Label(main, text="กรุณาเลือกชนิดทองของคุณ", fg="yellow", bg="black").grid(row=1, column=1, sticky=W)


#make choice of karat user have
radiovar1 = DoubleVar()
radio1_0 = ttk.Radiobutton(main, text="96.5 %", value=9.65, variable=radiovar1)
radio1_1 = ttk.Radiobutton(main, text="90 %", value=9.00, variable=radiovar1)
radio1_2 = ttk.Radiobutton(main, text="18K", value=7.50, variable=radiovar1)
radio1_3 = ttk.Radiobutton(main, text="14K", value=5.83, variable=radiovar1)

#grid radio button on same row

radio1_0.grid(row=1, column=2, stick=W)
radio1_1.grid(row=2, column=2, stick=W)
radio1_2.grid(row=3, column=2, stick=W)
radio1_3.grid(row=4, column=2, stick=W)

#ask amount of user's gold
label2 = Label(main, text="กรุณาใส่จำนวนทองของคุณ หน่วยเป็น กรัม (g)", fg="yellow", bg="black")
label2.grid(row=6, column=1, sticky=W)

textentry = Entry(main, width=5, bg="white")

textentry.grid(row=6, column=2, sticky=W)

#label3 = Label(main, text="g.", fg="yellow", bg="black").grid(row=6, column=2, sticky=E)

#ask Karat user want
label4 = Label(main, text="กรุณาเลือก Karat (K) ที่ต้องการ", bg="black", fg="yellow")
label4.grid(row=7, column=1, sticky=W)

#second radio button
radiovar2 = DoubleVar()
radio2_0 = ttk.Radiobutton(main, text="18K", value=7.50, variable=radiovar2)
radio2_1 = ttk.Radiobutton(main, text="14K", value=5.83, variable=radiovar2)
radio2_2 = ttk.Radiobutton(main, text="10K", value=4.16, variable=radiovar2)

radio2_0.grid(row=7, column=2, stick=W)
radio2_1.grid(row=8, column=2, stick=W)
radio2_2.grid(row=9, column=2, stick=W)

#result
label5 = Label(main, text="ผลลัพธ์ที่ต้องการ", bg="black", fg="yellow")
label5.grid(row=10, column=1, stick=W)

output = Text(main, width=40, wrap=WORD, bg="white", height=5)
output.grid(row=11, column=1, columnspan=2, sticky=W)

#submit button
button1 = Button(main, text="คำนวณ", width=6, command=click).grid(row=12, column=1, sticky=E)

#customerchoice = radiovar1.get()
#convertto = radiovar2.get()
#user_amount = float(text1.get())



def normal_formular(customerchoice, convertto, user_amount):

    alloy_factor = (customerchoice / convertto) - 1.00
    #user_amount = input("Amount of your 96.5% gold : (gram)") #ask user amount of their gold
    alloy_to_add = alloy_factor * float(user_amount)
    #print("You need to add more alloy: \n", alloy_to_add)
    total_amount = float(user_amount) + float(alloy_to_add)
    #print("\n And your total amount of your gold will be : \n", total_amount)
    return "You need to add more alloy: {0} \n And your total amount of your gold will be : {1} \n".format(alloy_to_add,
                                                                                                        total_amount)


main.mainloop()
