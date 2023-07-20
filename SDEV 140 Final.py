from tkinter import *
import random


#===============main=====================
class Sleeves_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("670x570+0+0")
        self.root.title("Knee Sleeves")
        title = Label(self.root, text = "Knee Sleeves", font = ('times new roman', 30, 'bold'), pady = 2, bd = 12, bg = "#07B4FF", fg = "Black", relief = GROOVE)
        title.pack(fill = X)
        
    # ================SBD Sleeve=======================
        self.phan = IntVar()
      
    # ============Inzer Sleeve==============================
        self.ergo = IntVar()
       
    
    # ==============Customer==========================
        self.name = StringVar()

        

        
    # =============Customer Info======================
        F1 = LabelFrame(self.root, text = "Customer Information", font = ('times new roman', 15, 'bold'), bd = 10, fg = "Black", bg = "#07B4FF")
        F1.place(x = 0, y = 80, relwidth = 1)

    # =============Text Box================

        name_lbl = Label(F1, text = "Name:", bg = "#07B4FF", font = ('times new roman', 15, 'bold'))
        name_lbl.grid(row = 0, column = 0, padx = 20, pady = 5)
        
        name_txt = Entry(F1, width = 15, textvariable = self.name, font = 'arial 15', bd = 7, relief = GROOVE)
        name_txt.grid(row = 0, column = 1, pady = 5, padx = 10)
        
    # ===================SBD====================================
        F2 = LabelFrame(self.root, text = "SBD", font = ('times new roman', 15, 'bold'), bd = 10, fg = "Black", bg = "#07B4FF")
        F2.place(x = 5, y = 180, width = 325, height = 380)

    # ==================SBD Button====================
        phan_lbl = Label(F2, text = "SBD Phantom", font = ('times new roman', 16, 'bold'), bg = "#07B4FF", fg = "black")
        phan_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        phan_btn = Button(F2, width = 10, command = self.phan, text = ("SBD Sleeve"))
        phan_btn.grid(row = 0, column = 1, padx=10, pady=10)

    # ========Photo=============
        


    # ==========Inzer=========================
        F3 = LabelFrame(self.root, text = "Inzer", font = ('times new roman', 15, 'bold'), bd = 10, fg = "Black", bg = "#07B4FF")
        F3.place(x = 340, y = 180, width = 325, height = 380)
        
    # ===============Inzer Button============
        ergo_lbl = Label(F3, text = "Inzer Ergo Pro", font = ('times new roman', 16, 'bold'), bg = "#07B4FF", fg = "black")
        ergo_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        ergo_btn = Button(F3, width=10, command = self.ergo, text = ('Ergo Sleeve'))
        ergo_btn.grid(row = 0, column = 1, padx = 10, pady = 10)



        
       

root = Tk()
obj = Sleeves_App(root)
root.mainloop()

