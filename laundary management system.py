from tkinter import *
from tkinter import messagebox
import random
import time;
import datetime

root= Tk()
root.geometry("1350x750+0+0")
root.title("Laundary Management System")
root.configure(background='black')

Tops = Frame(root, width= 1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1= Frame(root, width= 900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width= 440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a= Frame(f1, width= 900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width= 900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width= 440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width= 440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa= Frame(f1a, width= 400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab= Frame(f1a, width= 400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

lblInfo = Label(Tops, font=('arial', 70,'bold'), text= "  Laundary Management System  " ,bd =10)
lblInfo.grid(row=0,column=0)

#===============================METHODS================================
def qExit():
    qExit= messagebox.askyesno("QUIT SYSTEM","Do you want to quit?")
    if qExit > 0:
        root.destroy()


def Reset():
    global E_Shirt,E_Trouser,E_TShirt,E_Kurtas,E_Lower,E_Pullower,E_Bedsheet,E_Pillow_cover,E_Towel,E_Jeans,E_Curtains,E_Jackets,E_Suits,E_Coats,E_Blankets, E_Dress
    TotalCost.set("")
    CostofLaundary.set("")
    Costofdrycleaning.set("")
    txtReceipt.delete("1.0",END)
    E_Shirt.set("0")
    E_Trouser.set("0")
    E_TShirt.set("0")
    E_Kurtas.set("0")
    E_Lower.set("0")
    E_Pullower.set("0")
    E_Bedsheet.set("0")
    E_Pillow_cover.set("0")
    E_Towel.set("0")
    E_Jeans.set("0")

    E_Curtains.set("0")
    E_Jackets.set("0")
    E_Suits.set("0")
    E_Coats.set("0")
    E_Blankets.set("0")
    E_Dress.set("0")


def CostofItems():
    Item1=float(E_Shirt.get())
    Item2=float(E_TShirt.get())
    Item3=float(E_Kurtas.get())
    Item4=float(E_Lower.get())
    Item5=float(E_Bedsheet.get())
    Item6=float(E_Pillow_cover.get())
    Item7=float(E_Curtains.get())
    Item8=float(E_Jackets.get())
    Item9=float(E_Shirt.get())
    Item10=float(E_Coats.get())
    Item11=float(E_Dress.get())
    Item12=float(E_Pullower.get())
    Item13=float(E_Trouser.get())
    Item14=float(E_Jeans.get())
    Item15=float(E_Suits.get())
    Item16=float(E_Towel.get())
    PriceofLaundary=(Item1 * 2)+(Item2 * 2)+(Item3 * 2)\
                     +(Item4 * 2)+(Item5 * 2)+(Item6 * 2)+(Item7 * 2)+(Item8 * 2)
    PriceofDrycleaning=(Item9 * 2)+(Item10 * 2)+(Item11 * 2)\
                        +(Item12 * 2)+(Item13 * 2)+(Item14 * 2)+(Item15 * 2)+(Item16 * 2)

    LaundaryPrice="Rs.",str('%.2f'%(PriceofLaundary))
    DrycleaningPrice="Rs.",str('%.2f'%(PriceofDrycleaning))
    CostofLaundary.set(LaundaryPrice)
    Costofdrycleaning.set(DrycleaningPrice)
    TC="Rs.",str('%.2f'%(PriceofLaundary + PriceofDrycleaning))
    TotalCost.set(TC)
    

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("BILL"+randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get()+'\t\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,'CLOTHES\t\t\t\t'+"Cost of Total clothes \n\n")
    txtReceipt.insert(END,'Shirt:\t\t\t\t'+E_Shirt.get()+"\n")
    txtReceipt.insert(END,'TShirt:\t\t\t\t'+E_TShirt.get()+"\n")
    txtReceipt.insert(END,'Kurtas:\t\t\t\t'+E_Kurtas.get()+"\n")
    txtReceipt.insert(END,'Trouser:\t\t\t\t'+E_Trouser.get()+"\n")
    txtReceipt.insert(END,'Lower:\t\t\t\t'+E_Lower.get()+"\n")
    txtReceipt.insert(END,'Pullower:\t\t\t\t'+E_Pullower.get()+"\n")
    txtReceipt.insert(END,'Bedsheet:\t\t\t\t'+E_Bedsheet.get()+"\n")
    txtReceipt.insert(END,'Pillow_cover:\t\t\t\t'+E_Pillow_cover.get()+"\n")
    txtReceipt.insert(END,'Towel:\t\t\t\t'+E_Towel.get()+"\n")
    txtReceipt.insert(END,'Jeans:\t\t\t\t'+E_Jeans.get()+"\n")
    txtReceipt.insert(END,'Curtains:\t\t\t\t'+E_Curtains.get()+"\n")
    txtReceipt.insert(END,'Jacket:\t\t\t\t'+E_Jackets.get()+"\n")
    txtReceipt.insert(END,'Suits:\t\t\t\t'+E_Suits.get()+"\n")
    txtReceipt.insert(END,'Coat:\t\t\t\t'+E_Coats.get()+"\n")
    txtReceipt.insert(END,'Blanket:\t\t\t\t'+E_Blankets.get()+"\n")
    txtReceipt.insert(END,'Dress:\t\t\t\t'+E_Dress.get()+"\n")
    txtReceipt.insert(END,'Cost of Laundary:\t\t\t\t'+' '.join(eval(CostofLaundary.get()))+"\n")
    txtReceipt.insert(END,'Cost of Dry Cleaning:\t\t\t\t'+' '.join(eval(Costofdrycleaning.get()))+"\n")
    txtReceipt.insert(END,'Total Cost:\t\t\t\t'+' '.join(eval(TotalCost.get()))+"\n")
    

#===========================================CHECKBUTTONS======================================
def chkbutton_value():
    if (var1.get() == 1):
        txtShirt.configure(state= NORMAL)
    elif var1.get() == 0:
        txtShirt.configure(state= DISABLE)
        E_Shirt.set("0")
    if (var2.get() == 1):
        txtTShirt.configure(state= NORMAL)
    elif var2.get()== 0:
        txtTShirt.configure(state= DISABLE)
        E_TShirt.set("0")
    if (var3.get() == 1):
        txtTrouser.configure(state= NORMAL)
    elif var3.get()== 0:
        txtTrouser.configure(state= DISABLE)
        E_Trouser.set("0")
    if (var4.get() == 1):
        txtKurtas.configure(state= NORMAL)
    elif var4.get()== 0:
        txtKurtas.configure(state= DISABLE)
        E_Kurtas.set("0")
    if (var5.get() == 1):
        txtLower.configure(state= NORMAL)
    elif var5.get()== 0:
        txtLower.configure(state= DISABLE)
        E_Lower.set("0")
    if (var6.get() == 1):
        txtPullower.configure(state= NORMAL)
    elif var6.get()== 0:
        txtPullower.configure(state= DISABLE)
        E_Pullower.set("0")
    if (var7.get() == 1):
        txtBedsheet.configure(state= NORMAL)
    elif var7.get()== 0:
        txtBedsheet.configure(state= DISABLE)
        E_Bedsheet.set("0")
    if (var8.get() == 1):
        txtPillow_cover.configure(state= NORMAL)
    elif var8.get()== 0:
        txtPillow_cover.configure(state= DISABLE)
        E_Pillow_cover.set("0")
    if (var9.get() == 1):
        txtTowel.configure(state= NORMAL)
    elif var9.get()== 0:
        txtTowel.configure(state= DISABLE)
        E_Towel.set("0")
    if (var10.get() == 1):
        txtJeans.configure(state= NORMAL)
    elif var10.get()== 0:
        txtJeans.configure(state= DISABLE)
        E_Jeans.set("0")
    if (var11.get() == 1):
        txtCurtains.configure(state= NORMAL)
    elif var11.get()== 0:
        txtCurtains.configure(state= DISABLE)
        E_Curtains.set("0")
    if (var12.get() == 1):
        txtSuits.configure(state= NORMAL)
    elif var12.get()== 0:
        txtSuits.configure(state= DISABLE)
        E_Suits.set("0")
    if (var13.get() == 1):
        txtCoats.configure(state= NORMAL)
    elif var13.get()== 0:
        txtTrouser.configure(state= DISABLE)
        E_Coats.set("0")
    if (var14.get() == 1):
        txtBlankets.configure(state= NORMAL)
    elif var14.get()== 0:
        E_Blankets.set("0")
    if (var15.get() == 1):
        txtDress.configure(state= NORMAL)
    elif var15.get()== 0:
        E_Dress.set("0")
    if (var16.get() == 1):
        txtJackets.configure(state= NORMAL)
    elif var16.get()== 0:
        E_Jackets.set("0")    

#================================================================================================    

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtShirt.configure(state= DISABLED)
    txtTShirt.configure(state= DISABLED)
    txtKurtas.configure(state= DISABLED)
    txtLower.configure(state= DISABLED)
    txtBedsheet.configure(state= DISABLED)
    txtPillow_cover.configure(state= DISABLED)
    txtTowel.configure(state= DISABLED)
    txtCurtains.configure(state= DISABLED)
    txtJackets.configure(state= DISABLED)
    txtBlankets.configure(state= DISABLED)
    txtCoats.configure(state= DISABLED)
    txtDress.configure(state= DISABLED)
    txtPullower.configure(state= DISABLED)
    txtTrousers.configure(state= DISABLED)
    txtJeans.configure(state= DISABLED)
    txtSuits.configure(state= DISABLED)



    
#==================================VARIABLES====================    



DateofOrder=StringVar()
Receipt_Ref=StringVar()
TotalCost=StringVar()
CostofLaundary=StringVar()
Costofdrycleaning=StringVar()
DateofDelivery=StringVar()

var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()




DateofOrder.set(time.strftime("%d/%m/%y"))
DateofDelivery.set(time.strftime("%d/%m/%y"))

E_Shirt=StringVar()
E_Trouser=StringVar()
E_TShirt=StringVar()
E_Kurtas=StringVar()
E_Lower=StringVar()
E_Pullower=StringVar()
E_Bedsheet=StringVar()
E_Pillow_cover=StringVar()
E_Towel=StringVar()
E_Jeans=StringVar()

E_Curtains=StringVar()
E_Jackets=StringVar()
E_Suits=StringVar()
E_Coats=StringVar()
E_Blankets=StringVar()
E_Dress=StringVar()

E_Shirt.set("0")
E_Trouser.set("0")
E_TShirt.set("0")
E_Kurtas.set("0")
E_Lower.set("0")
E_Pullower.set("0")
E_Bedsheet.set("0")
E_Pillow_cover.set("0")
E_Towel.set("0")
E_Jeans.set("0")

E_Curtains.set("0")
E_Jackets.set("0")
E_Suits.set("0")
E_Coats.set("0")
E_Blankets.set("0")
E_Dress.set("0")




#=========================================LAUNDARY================================================
Shirt = Checkbutton(f1aa, text="Shirt \t", variable = var1, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 0, sticky=W)
TShirt = Checkbutton(f1aa, text="T-Shirt\t", variable = var2, onvalue = 1, offvalue=0,
                      font=('arial', 18,'bold')).grid(row= 1, sticky=W)
                           
Kurtas = Checkbutton(f1aa, text="Kurtas\t", variable = var3, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 2, sticky=W)
Lower = Checkbutton(f1aa, text="Lower\t", variable = var4, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 3, sticky=W)
Bedsheet = Checkbutton(f1aa, text="Bedsheet\t", variable = var5, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 4, sticky=W)
Pillow_cover = Checkbutton(f1aa, text="Pillow cover\t", variable = var6, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 5, sticky=W)
Towel= Checkbutton(f1aa, text="Towel\t", variable = var7, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 6, sticky=W)

Curtains = Checkbutton(f1aa, text="Curtains\t", variable = var8, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 7, sticky=W)

#================================DRY CLEANING================================================

Jackets = Checkbutton(f1ab, text="Jackets\t", variable = var9, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 1, sticky=W)
Suits = Checkbutton(f1ab, text="Suits\t", variable = var10, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 2, sticky=W)
Blankets = Checkbutton(f1ab, text="Blankets\t", variable = var11, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 3, sticky=W)
Coats = Checkbutton(f1ab, text="Coats\t", variable = var12, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 4, sticky=W)
Dress = Checkbutton(f1ab, text="Dress\t", variable = var13, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 5, sticky=W)
Jeans = Checkbutton(f1ab, text="Jeans\t", variable = var14, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 6, sticky=W)
Trousers = Checkbutton(f1ab, text="Trousers\t", variable = var15, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 7, sticky=W)
Pullower = Checkbutton(f1ab, text="Pullower\t", variable = var16, onvalue = 1, offvalue=0,
                     font=('arial', 18,'bold')).grid(row= 8, sticky=W)

#=========================================ENTER WIDGET FOR LAUNDARY================================================
txtShirt = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Shirt, state= NORMAL)
txtShirt.grid(row= 0, column =1)

txtTShirt= Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_TShirt, state= NORMAL)
txtTShirt.grid(row= 1, column =1)
txtKurtas = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Kurtas, state=NORMAL)
txtKurtas.grid(row= 2, column =1)
txtLower = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Lower, state= NORMAL)
txtLower.grid(row= 3, column =1)

txtBedsheet = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Bedsheet, state= NORMAL)
txtBedsheet.grid(row= 4, column =1)
txtPillow_cover = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Pillow_cover, state= NORMAL)
txtPillow_cover.grid(row= 5, column =1)
txtTowel = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Towel, state= NORMAL)
txtTowel.grid(row= 6, column =1)


txtCurtains = Entry(f1aa,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Curtains, state= NORMAL)
txtCurtains.grid(row= 7, column =1)




#=========================================ENTER WIDGET FOR DRY CLEANING================================================
txtJackets = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Jackets,state= NORMAL)
txtJackets.grid(row= 1, column =1)
txtSuits = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Suits, state= NORMAL)
txtSuits.grid(row= 2, column =1)
txtBlankets = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Blankets, state= NORMAL)
txtBlankets.grid(row= 3, column =1)
txtCoats = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Coats, state= NORMAL)
txtCoats.grid(row= 4, column =1)
txtDress = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Dress , state= NORMAL)
txtDress.grid(row=5, column =1)
txtTrousers = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Trouser, state= NORMAL)
txtTrousers.grid(row= 6, column =1)
txtJeans = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable=E_Jeans, state= NORMAL)
txtJeans.grid(row= 7, column =1)
txtPullower = Entry(f1ab,font=('arial', 18,'bold'), bd=8, width = 6, justify='left',textvariable= E_Pullower,state= NORMAL)
txtPullower.grid(row= 8, column =1)

#============================================INFORMATION==============================================================
lblReceipt = Label(ft2,font=('arial',12,'bold'),text="Receipt",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt= Text(ft2, width = 59, height= 22,bd=8,bg="white",font=('arial', 11,'bold'))
txtReceipt.grid(row=1, column =0)

#===============================COST ITEM INFORMATIOM=============================================
lblCostofLaundary = Label(f2aa,font=('arial',16,'bold'),text="Cost of Laundary", bd=8, )
lblCostofLaundary.grid(row=0,column=0,sticky=W)
txtCostofLaundary=Entry(f2aa,font=('arial',16,'bold'),bd=8, insertwidth=2, justify='left',textvariable=CostofLaundary)
txtCostofLaundary.grid(row=0,column=1,sticky=W)

lblcostofdrycleaning=Label(f2aa,font=('arial',16,'bold'),text="Cost of Dry Cleaning", bd=8,anchor='w')
lblcostofdrycleaning.grid(row=3,column=0,sticky=W)
txtcostofdrycleaning=Entry(f2aa,font=('arial',16,'bold'),bd=8, insertwidth=2, justify='left',textvariable=Costofdrycleaning)
txtcostofdrycleaning.grid(row=3,column=1,sticky=W)


#============================PAYMENT INFORMATION==========================================
lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text="Total Cost", bd=8)
lblTotalCost.grid(row=0,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),bd=8,
                   insertwidth=2,justify='left' , textvariable=TotalCost)
txtTotalCost.grid(row=0,column=1,sticky=W)


    
#=========================BUTTON=============================================================
btnTotal=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial',16,'bold'),width=5,
                text="Total ",command=CostofItems).grid(row=0, column=0)
btnReceipt=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial',16,'bold'),width=5,
                text="Receipt ",command=Receipt).grid(row=0, column=1)
btnReset=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial',16,'bold'),width=5,
                text="Reset ", command=Reset).grid(row=0, column=2)
btnExit=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial',16,'bold'),width=5,
                text="Exit ", command=qExit).grid(row=0, column=3)

root.mainloop()
