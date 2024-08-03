from tkinter import Tk, Label, Frame, LabelFrame, ttk, Entry, Text, Listbox, Scrollbar, END, Button,StringVar,messagebox,PhotoImage
from datetime import date,timedelta
import mysql.connector,tkinter
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        height = self.root.winfo_screenheight()
        width = self.root.winfo_screenwidth()
        self.root.geometry(f'{width}x{height}')
        img=PhotoImage(file='book.png')
        self.root.iconphoto(False,img)

        L1 = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg='#10B1FF', fg='#4600AE', bd=18, relief='ridge',
                   font=('times new roman', 30, 'bold'), padx=2, pady=6)
        L1.pack(side='top', fill='x')

        frame = Frame(self.root, bd=12, relief='ridge', padx=20, bg='powder blue')
        frame.place(x=0, y=88, width=1270, height=372)

        # ======================================Variable================================

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.program_var = StringVar()
        self.mobile_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()
 # =================================================DataFrameLeft================================

        DataFrameLeft = LabelFrame(frame, text='Library Membership Information', bg='#10B1FF', fg='black', bd=7,
                                   relief='ridge', font=('Arial', 12, 'bold'))
        DataFrameLeft.place(x=-15, y=0, width=785, height=345)

        LblMember = Label(DataFrameLeft, text='Member Type:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=2,
                          pady=6)
        LblMember.grid(row=0, column=0, sticky='W')

        ComMember = ttk.Combobox(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.member_var, width=23,
                                 state='readonly')
        ComMember['values'] = ('Admin Staf', 'Student', 'Lecturer')
        ComMember.current(0)
        ComMember.grid(row=0, column=1)

        LblPRN_NO = Label(DataFrameLeft, text='PRN No:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5, pady=6)
        LblPRN_NO.grid(row=1, column=0, sticky='W')
        TxtPRN_NO = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.prn_var, width=25)
        TxtPRN_NO.grid(row=1, column=1)

        LblTitle = Label(DataFrameLeft, text='ID No:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5, pady=6)
        LblTitle.grid(row=2, column=0, sticky='W')
        TxtTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.id_var, width=25)
        TxtTitle.grid(row=2, column=1)

        LblFirstName = Label(DataFrameLeft, text='First Name:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5,
                             pady=6)
        LblFirstName.grid(row=3, column=0, sticky='W')
        TxtFirstName = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.firstname_var, width=25)
        TxtFirstName.grid(row=3, column=1)

        LblLastName = Label(DataFrameLeft, text='Last Name:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5,
                            pady=4)
        LblLastName.grid(row=4, column=0, sticky='W')
        TxtLastName = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.lastname_var, width=25)
        TxtLastName.grid(row=4, column=1)

        LblProgram = Label(DataFrameLeft, text='Program:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5, pady=6)
        LblProgram.grid(row=5, column=0, sticky='W')
        TxtProgram = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.program_var, width=25)
        TxtProgram.grid(row=5, column=1)

        LblMobile = Label(DataFrameLeft, text='Mobile:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5, pady=6)
        LblMobile.grid(row=6, column=0, sticky='W')
        TxtMobile = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.mobile_var, width=25)
        TxtMobile.grid(row=6, column=1)

        LblAddress = Label(DataFrameLeft, text='Address:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5, pady=6)
        LblAddress.grid(row=7, column=0, sticky='W')
        TxtAddress = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.address_var, width=25)
        TxtAddress.grid(row=7, column=1)

        LblPostCode = Label(DataFrameLeft, text='Post Code:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=5,
                            pady=6)
        LblPostCode.grid(row=8, column=0, sticky='W')
        TxtPostCode = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.postcode_var, width=25)
        TxtPostCode.grid(row=8, column=1)

        LblBookId = Label(DataFrameLeft, text='Book Id:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=20, pady=6)
        LblBookId.grid(row=0, column=2, sticky='W')
        TxtBookId = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.bookid_var, width=25)
        TxtBookId.grid(row=0, column=3)

        LblBookTitle = Label(DataFrameLeft, text='Book Title:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=20,
                             pady=6)
        LblBookTitle.grid(row=1, column=2, sticky='W')
        TxtBookTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.booktitle_var, width=25)
        TxtBookTitle.grid(row=1, column=3)

        LblAuther = Label(DataFrameLeft, text='Auther:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=20, pady=6)
        LblAuther.grid(row=2, column=2, sticky='W')
        TxtAuther = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.auther_var, width=25)
        TxtAuther.grid(row=2, column=3)

        LblDataBorrowe = Label(DataFrameLeft, text='Date Borrowed:', bg='#10B1FF', font=('arial', 12, 'bold'),
                               padx=20, pady=6)
        LblDataBorrowe.grid(row=3, column=2, sticky='W')
        TxtDataBorrowe = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.dateborrowed_var, width=25)
        TxtDataBorrowe.grid(row=3, column=3)

        LblDateDue = Label(DataFrameLeft, text='Date Due:', bg='#10B1FF', font=('arial', 12, 'bold'), padx=20,
                           pady=6)
        LblDateDue.grid(row=4, column=2, sticky='W')
        TxtDateDue = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.datedue_var, width=25)
        TxtDateDue.grid(row=4, column=3)

        LblDaysOnBook = Label(DataFrameLeft, text='Days On Book:', bg='#10B1FF', font=('arial', 12, 'bold'),
                              padx=20, pady=6)
        LblDaysOnBook.grid(row=5, column=2, sticky='W')
        TxtDaysOnBook = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.daysonbook_var, width=25)
        TxtDaysOnBook.grid(row=5, column=3)

        LblLateReturnFine = Label(DataFrameLeft, text='Late Return Fine:', bg='#10B1FF', font=('arial', 12, 'bold'),
                                  padx=20, pady=6)
        LblLateReturnFine.grid(row=6, column=2, sticky='W')
        TxtLateReturnFine = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.latereturnfine_var,
                                  width=25)
        TxtLateReturnFine.grid(row=6, column=3)

        LblDateOverDue = Label(DataFrameLeft, text='Date Over Due:', bg='#10B1FF', font=('arial', 12, 'bold'),
                               padx=20, pady=6)
        LblDateOverDue.grid(row=7, column=2, sticky='W')
        TxtDateOverDue = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.dateoverdue_var, width=25)
        TxtDateOverDue.grid(row=7, column=3)

        LblActualPrice = Label(DataFrameLeft, text='Actual Price :', bg='#10B1FF', font=('arial', 12, 'bold'),
                               padx=20, pady=6)
        LblActualPrice.grid(row=8, column=2, sticky='W')
        TxtActualPrice = Entry(DataFrameLeft, font=('arial', 13, 'bold'), textvariable=self.actualprice_var, width=25)
        TxtActualPrice.grid(row=8, column=3)

# ======================================Data Frame Right================================

        DataFrameRight = LabelFrame(frame, text='Book Details', bg='#10B1FF', fg='black', bd=7, relief='ridge',
                                    font=('Arial', 12, 'bold'), padx=2, pady=6)
        DataFrameRight.place(x=770, y=0, width=450, height=345)

        self.TxtBox = Text(DataFrameRight, font=('Arial', 10, 'bold'), width=35, height=19, padx=0, pady=0)
        self.TxtBox.grid(row=0, column=2, padx=7)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky='ns')

        listBooks = ['Python Crash Course', 'Operating System Concepts', 'The Design of the UNIX Operating System',
                     'Object-Oriented Analysis and Design with Applications', 'Data Structure Using C',
                     'Computer Fundamentals','Principles of Programming and Algorithms', 'Mercantile Law',
                     'Business Accounting','Python for Data Analysis','Deep Learning', 'R for Data Science', 'Think Stats',
                     'Database System Concepts', 'Database Management Systems','Fundamentals of Database Systems',
                     'Business Organisation and Management','Don Quixote','Little Women','	Oliver Twist',
                     'Harry Potter and the Chamber of Secrets']

        def SelectBook(Event=''):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == 'Python Crash Course'):
                self.bookid_var.set('BKID01')
                self.booktitle_var.set('Python Crash Course')
                self.auther_var.set('Dr. Mark Gillenson')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.785')

            elif (x == 'Operating System Concepts'):
                self.bookid_var.set('BKID02')
                self.booktitle_var.set('Operating System Concepts')
                self.auther_var.set('Peter Bear Galvin')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.550')


            elif (x == 'The Design of the UNIX Operating System'):
                self.bookid_var.set('BKID03')
                self.booktitle_var.set('The Design of the UNIX Operating System')
                self.auther_var.set('Maurice J.Bach')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.885')


            elif (x ==  'Object-Oriented Analysis and Design with Applications'):
                self.bookid_var.set('BKID04')
                self.booktitle_var.set('Object-Oriented Analysis and Design with Applications')
                self.auther_var.set('Grady Booch')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.930')

            elif (x == 'Data Structure Using C'):
                self.bookid_var.set('BKID05')
                self.booktitle_var.set('Data Structure Using C')
                self.auther_var.set('Dr. E. Balagurusamy')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.760')


            elif (x == 'Computer Fundamentals'):
                self.bookid_var.set('BKID06')
                self.booktitle_var.set('Computer Fundamentals')
                self.auther_var.set('PK. Sinha')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.490')


            elif (x == 'Principles of Programming and Algorithms'):
                self.bookid_var.set('BKID07')
                self.booktitle_var.set('Principles of Programming and Algorithms')
                self.auther_var.set('Bhavana Chaudhari')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.340')


            elif (x == 'Mercantile Law'):
                self.bookid_var.set('BKID08')
                self.booktitle_var.set('Mercantile Law')
                self.auther_var.set('M.C. Kuchhal & Vivek Kuchhal')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.1000')


            elif (x == 'Business Accounting'):
                self.bookid_var.set('BKID09')
                self.booktitle_var.set('Business Accounting')
                self.auther_var.set('Jill Collis')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.880')


            elif (x == 'Python for Data Analysis'):
                self.bookid_var.set('BKID10')
                self.booktitle_var.set('Python for Data Analysis')
                self.auther_var.set('Wes Mckinney')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.580')



            elif (x == 'Deep Learning'):
                self.bookid_var.set('BKID11')
                self.booktitle_var.set('Deep Learning')
                self.auther_var.set('Youshua Bengio')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.290')



            elif (x == 'R for Data Science'):
                self.bookid_var.set('BKID12')
                self.booktitle_var.set('R for Data Science')
                self.auther_var.set('Hadley Wickham')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.780')



            elif (x == 'Think Stats'):
                self.bookid_var.set('BKID13')
                self.booktitle_var.set('Think Stats')
                self.auther_var.set('Allen B. Downey')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.240')



            elif (x == 'Database System Concepts'):
                self.bookid_var.set('BKID14')
                self.booktitle_var.set('Database System Concepts')
                self.auther_var.set('S. Sudarshan')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.980')


            elif (x ==  'Database Management Systems'):
                self.bookid_var.set('BKID15')
                self.booktitle_var.set( 'Database Management Systems')
                self.auther_var.set('Raghu Ramakrishnan')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.980')


            elif (x =='Fundamentals of Database Systems'):
                self.bookid_var.set('BKID16')
                self.booktitle_var.set('Fundamentals of Database Systems')
                self.auther_var.set('Shamkant Navathe')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.980')


            elif (x == 'Business Organisation and Management'):
                self.bookid_var.set('BKID17')
                self.booktitle_var.set('Business Organisation and Management')
                self.auther_var.set('C. B. Gupta')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.1050')


            elif (x =='Don Quixote'):
                self.bookid_var.set('BKID18')
                self.booktitle_var.set('Don Quixote')
                self.auther_var.set('Shamkant Navathe')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.780')

            elif (x == 'Little Women'):
                self.bookid_var.set('BKID19')
                self.booktitle_var.set('Little Women')
                self.auther_var.set('Louisa May Alcott')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.800')

            elif (x =='	Oliver Twist'):
                self.bookid_var.set('BKID20')
                self.booktitle_var.set('Oliver Twist')
                self.auther_var.set('Charles Dickens')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.510')


            elif (x =='Harry Potter and the Chamber of Secrets'):
                self.bookid_var.set('BKID21')
                self.booktitle_var.set('Harry Potter and the Chamber of Secrets')
                self.auther_var.set('J.K. Rowling')

                d1 = date.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)

                self.daysonbook_var.set(15)
                self.latereturnfine_var.set('Rs.50')
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set('Rs.480')





        listBox = Listbox(DataFrameRight, font=('Arial', 12, 'bold'), width=16, height=15)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

 # ======================================buttons frame================================

            Framebutton = Frame(root, bd=12, relief='ridge', padx=20, bg='#10B1FF')
            Framebutton.place(x=0, y=458, width=1270, height=55)

            btnAddData = Button(Framebutton,command=self.add_data,text='Add Data', font=('Arial', 12, 'bold'), width=19, bg='#FF6531',
                                fg='white')
            btnAddData.grid(row=0, column=0)

            btnshowData = Button(Framebutton,command=self.showData,text='Show Data', font=('Arial', 12, 'bold'), width=19, bg='#FF6531',
                                 fg='white')
            btnshowData.grid(row=0, column=1)

            btnupdateData = Button(Framebutton,command=self.update, text='Update', font=('Arial', 12, 'bold'), width=19, bg='#FF6531',
                                   fg='white')
            btnupdateData.grid(row=0, column=2)

            btndeleteData = Button(Framebutton,command=self.delete, text='Delete', font=('Arial', 12, 'bold'), width=19, bg='#FF6531',
                                   fg='white')
            btndeleteData.grid(row=0, column=3)

            btnresetData = Button(Framebutton,command=self.reset, text='Reset', font=('Arial', 12, 'bold'), width=19, bg='#FF6531',
                                  fg='white')
            btnresetData.grid(row=0, column=4)

            btnexitData = Button(Framebutton,command=self.iExit,text='Exit', font=('Arial', 12, 'bold'), width=19, bg='#FF6531', fg='white')
            btnexitData.grid(row=0, column=5)

# ======================================information frame================================

            FrameDetails = Frame(root, bd=12, relief='ridge', padx=20, bg='#10B1FF')
            FrameDetails.place(x=0, y=510, width=1270, height=140)

            Table_Frame = Frame(FrameDetails, bd=6, relief='ridge', bg='#10B1FF')
            Table_Frame.place(x=0, y=2, width=1200, height=115)

            xscroll = ttk.Scrollbar(Table_Frame, orient='horizontal')
            yscroll = ttk.Scrollbar(Table_Frame, orient='vertical')

            self.library_table = ttk.Treeview(Table_Frame, column=('membertype', 'prnno', 'idno', 'firstname', 'lastname',
                                                                   'program', 'mobile', 'address','postcode', 'bookid',
                                                                   'booktitle', 'auther', 'dateborrowed', 'datedue', 'daysonbook',
                                                                   'latereturnfine', 'dateoverdue', 'actualprice'),
                                              xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

            xscroll.pack(side='bottom', fill='x')
            yscroll.pack(side='right', fill='y')

            xscroll.config(command=self.library_table.xview)
            yscroll.config(command=self.library_table.yview)

            self.library_table.heading('membertype', text='Member Type')
            self.library_table.heading('prnno', text='PRN No')
            self.library_table.heading('idno', text='ID No')
            self.library_table.heading('firstname', text='First Name')
            self.library_table.heading('lastname', text='Last Name')
            self.library_table.heading('program', text='Program')
            self.library_table.heading('mobile', text='Mobile Number')
            self.library_table.heading('address', text='Address')
            self.library_table.heading('postcode', text='Post Code')
            self.library_table.heading('bookid', text='Book Id')
            self.library_table.heading('booktitle', text='Book Title')
            self.library_table.heading('auther', text='Auther')
            self.library_table.heading('dateborrowed', text='Date Of Borrowed')
            self.library_table.heading('datedue', text='Date Due')
            self.library_table.heading('daysonbook', text='Days On Book')
            self.library_table.heading('latereturnfine', text='Late Return Fine')
            self.library_table.heading('dateoverdue', text='Date Over Due')
            self.library_table.heading('actualprice', text='Actual Price')

            self.library_table['show'] = 'headings'
            self.library_table.pack(fill='both', expand=1)

            self.library_table.column('membertype', width=100)
            self.library_table.column('prnno', width=100)
            self.library_table.column('idno', width=100)
            self.library_table.column('firstname', width=100)
            self.library_table.column('lastname', width=100)
            self.library_table.column('program', width=100)
            self.library_table.column('mobile', width=100)
            self.library_table.column('address', width=100)
            self.library_table.column('postcode', width=100)
            self.library_table.column('bookid', width=100)
            self.library_table.column('booktitle', width=100)
            self.library_table.column('auther', width=100)
            self.library_table.column('dateborrowed', width=100)
            self.library_table.column('datedue', width=100)
            self.library_table.column('daysonbook', width=100)
            self.library_table.column('latereturnfine', width=100)
            self.library_table.column('dateoverdue', width=100)
            self.library_table.column('actualprice', width=100)

            self.fatch_data()
            self.library_table.bind('<ButtonRelease-1>',self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='nirajsojitra@321',database='sys')
        my_cursor = conn.cursor()
        my_cursor.execute('insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.program_var.get(),
            self.mobile_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.actualprice_var.get()
                              ))

        conn.commit()
        self.fatch_data()
        conn.close()


        messagebox.showinfo('Success', 'Member Has Been Inserted Successfully')

    def update(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='nirajsojitra@321',database='sys')
        my_cursor = conn.cursor()
        my_cursor.execute('update library set Member=%s,ID_No=%s,First_Name=%s,Last_Name=%s,Program=%s,'
                                'Mobile_No=%s,Address=%s,Post_Code=%s,Book_ID=%s,Book_Title=%s,Auther=%s,Date_Of_Borrowed=%s,'
                                'Date_Due=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_due=%s,Actual_Price=%s where PRN_No=%s',(

            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.program_var.get(),
            self.mobile_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.actualprice_var.get(),
            self.prn_var.get()
                          ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo('Success','Member has been updated')


    def fatch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='nirajsojitra@321', database='sys')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from library')
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=' '):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.program_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.address_var.set(row[7]),
        self.postcode_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.actualprice_var.set(row[17])

    def showData(self):
        self.TxtBox.insert(END, 'Member Type:\t\t' + self.member_var.get() + '\n')
        self.TxtBox.insert(END, 'PRN No:\t\t' + self.prn_var.get() + '\n')
        self.TxtBox.insert(END, 'ID No:\t\t' + self.id_var.get() + '\n')
        self.TxtBox.insert(END, 'First Name:\t\t' + self.firstname_var.get() + '\n')
        self.TxtBox.insert(END, 'Last Name:\t\t' + self.lastname_var.get() + '\n')
        self.TxtBox.insert(END, 'Program:\t\t' + self.program_var.get() + '\n')
        self.TxtBox.insert(END, 'Mobile No:\t\t' + self.mobile_var.get() + '\n')
        self.TxtBox.insert(END, 'Address:\t\t' + self.address_var.get() + '\n')
        self.TxtBox.insert(END, 'Post Code:\t\t' + self.postcode_var.get() + '\n')
        self.TxtBox.insert(END, 'Book ID:\t\t' + self.bookid_var.get() + '\n')
        self.TxtBox.insert(END, 'Book Title:\t\t' + self.booktitle_var.get() + '\n')
        self.TxtBox.insert(END, 'Auther:\t\t' + self.auther_var.get() + '\n')
        self.TxtBox.insert(END, 'DateBorrowed:\t\t' + self.dateborrowed_var.get() + '\n')
        self.TxtBox.insert(END, 'Datedue:\t\t' + self.datedue_var.get() + '\n')
        self.TxtBox.insert(END, 'DaysOnBook:\t\t' + self.daysonbook_var.get() + '\n')
        self.TxtBox.insert(END, 'LateReturnFine:\t\t' + self.latereturnfine_var.get() + '\n')
        self.TxtBox.insert(END, 'DateOverDue:\t\t' + self.dateoverdue_var.get() + '\n')
        self.TxtBox.insert(END, 'Actual Price:\t\t' + self.actualprice_var.get() + '\n')

    def reset(self):
        self.member_var.set(''),
        self.prn_var.set(''),
        self.id_var.set(''),
        self.firstname_var.set(''),
        self.lastname_var.set(''),
        self.program_var.set(''),
        self.mobile_var.set(''),
        self.address_var.set(''),
        self.postcode_var.set(''),
        self.bookid_var.set(''),
        self.booktitle_var.set(''),
        self.auther_var.set(''),
        self.dateborrowed_var.set(''),
        self.datedue_var.set(''),
        self.daysonbook_var.set(''),
        self.latereturnfine_var.set(''),
        self.dateoverdue_var.set(''),
        self.actualprice_var.set('')
        self.TxtBox.delete('1.0',END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno('Library Management System','Are you sure you want to exit?')
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=='' or self.id_var.get()=='':
            messagebox.showerror('Error','Data is not compelete')
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='nirajsojitra@321',database='sys')
            my_cursor = conn.cursor()
            query = 'Delete from library where PRN_No=%s'
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo('Success','Member has been deleted!')






if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()

