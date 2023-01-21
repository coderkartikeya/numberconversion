from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numbersystem
import mysql.connector

numb=Tk()

numb.geometry('1500x700+10+10')
numb.title('NUMBER CONVERTER')
numb.configure(bg='black')
p=PhotoImage(file='login.png')
numb.iconphoto(False,p)






#################################image####
ph2=PhotoImage(file='g.png')
ph=ph2.subsample(3,3)
pho=Label(numb,image=ph)
pho.pack()

############variables#############
entry1=StringVar()
entry2=StringVar()
en=StringVar()
l=StringVar()

################convertera#################################################################################
def con():

	mydb=mysql.connector.connect(
			host='localhost',
			user='root',
			password='sunilvats',
			database='payroll'
			)
	mycursor=mydb.cursor()
	#mycursor.execute("CREATE TABLE  numberconv (NO INTEGER AUTO_INCREMENT PRIMARY KEY ,NAME VARCHAR(255),PASSWORD VARCHAR(255))")
	lea="SELECT  * FROM numberconv where NO='%s' and PASSWORD='%s'"%(entry1.get(),entry2.get())
	mycursor.execute(lea)
	e=mycursor.fetchone()



	d=entry1.get()
	f=entry2.get()
	if e is None:
		messagebox.showinfo('MESSAGE','USER NOT FOUND')


	elif e is not None:

		num=Toplevel()
		num.geometry('1500x700+0+0')
		p2=PhotoImage(file='cd.png')
		num.iconphoto(False,p2)


		###############image##################################################################
		po=PhotoImage(file='cd.png')
		pol=po.subsample(4,4)

		po1=Label(num,image=pol)
		po1.pack()
		###################################textbox#######################################
		tc=Text(po1,fg='black',bg='lightblue',font='comicsans 15 bold',bd=10)
		tc.place(x=135,y=470)


		##################################################################################

		#################frames###############################################################
		fc1=Frame(po1,bd=10,bg='black',padx=520,relief='raise')
		fc1.place(x=0,y=0)

		#fc2=Frame(po1,bd=5,bg='orange',relief='raise')
		#fc2.place(x=100,y=100)

		#####################functions#####################################################

		def clear():
			tc.delete('1.0','end')
			ec1.delete(0,END)
			cc1.delete(0,END)


		def binary():
			inp=en.get()



			if inp=='OCTAL':
				n=l.get()
				out=numbersystem.octalToBinary(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='BINARY':
				messagebox.showinfo('MESSAGE','NUMBER ALREADY IN BINARY')
			elif inp=='DECIMAL':
				n=int(l.get())
				out1=numbersystem.decimalToBinary(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='HEXADECIMAL':
				n1=l.get()
				out1=numbersystem.hexaToBinary(n1)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')
			else:
				print('lol')

		def octal():
			inp=en.get()
			n=l.get()


			if inp=='BINARY':
				#n=int(l.get())
				out=numbersystem.binaryToOctal(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='OCTAL':
				messagebox.showinfo('MESSAGE','NUMBER ALREADY IN OCTAL')
			elif inp=='DECIMAL':
				#n=int(l.get())
				out1=numbersystem.decimalToOctal(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='HEXADECIMAL':
				n1=l.get()
				out1=numbersystem.hexaToOctal(n1)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')
			else:
				print('jai shree ram')

		def decimal():
			inp=en.get()
			n=l.get()


			if inp=='BINARY':
				#n=int(l.get())
				out=numbersystem.binaryToDecimal(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='DECIMAL':
				messagebox.showinfo('MESSAGE','NUMBER ALREADY IN DECIMAL')
			elif inp=='OCTAL':
				#n=int(l.get())
				out1=numbersystem.octalToDecimal(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='HEXADECIMAL':
				n1=l.get()
				out1=numbersystem.hexaToDecimal(n1)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')
			else:
				print('jai shree ram')
		def hexadecimal():
			inp=en.get()


			if inp=='BINARY':
				n=l.get()
				out=numbersystem.binaryToHexa(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='HEXADECIMAL':
				messagebox.showinfo('MESSAGE','NUMBER ALREADY IN HEXADECIMAL')
			elif inp=='OCTAL':
				n=l.get()
				out1=numbersystem.octalToHexa(n)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')

			elif inp=='DECIMAL':
				n1=l.get()
				out1=numbersystem.decimalToHexa(n1)
				tc.insert(END,'                     ANSWER                      ')
				tc.insert(END,'\n -----------------------------------------------------------------------------------------------\n ')
				tc.insert(END,out1)
				tc.insert(END,'\n-------------------------------------------------------------------------------------------------')
				tc.insert(END,'\n THANKS FOR USING OUR CONVERTER')
			else:
				print('jai shree ram')
		def cancel():
			num.destroy()
			em1.delete(0,END)
			em2.delete(0,END)





		#############labels###################################################################
		lc1=Label(fc1,bg='black',text='WELCOME TO OUR CONVERTER',font='comisans 20 bold ',fg='white')
		lc1.pack()

		lc2=Label(po1,bg='black',text='ENTER NUMBER',font='comisans 20 bold ',fg='white',bd=5,relief='raise')
		lc2.place(x=100,y=100)

		lc3=Label(po1,bg='black',text='TYPE OF NUMBER \n YOU ENTERED',font='comisans 17 bold ',fg='white',bd=5,relief='raise')
		lc3.place(x=100,y=150)

		lc4=Label(po1,bg='#03b5fc',text='CLICK ON THE BUTTON TO CHOOSE IN WHICH TYPE YOU WANT TO CONVERT',font='comisans 20 bold ',fg='black',bd=5,relief='raise')
		lc4.place(x=100,y=260)

		######################entries#############################################
		ec1=Entry(po1,bg='white',fg='black',font='comisans 20 bold ',bd=5,relief='raise',textvariable=l)
		ec1.place(x=330,y=100)

		cc1=ttk.Combobox(po1,values=['BINARY','HEXADECIMAL','OCTAL','DECIMAL'],font='comicsans 20 bold',textvariable=en)
		cc1.place(x=330,y=160)
		cc1.current()


		######################################buttons#############################################
		bc1=Button(po1,bg='black',fg='white',text='BINARY',font='comisans 20 bold',bd=5,relief='raise',command=binary)
		bc1.place(x=100,y=340)

		bc2=Button(po1,bg='black',fg='white',text='HEXADECIMAL',font='comisans 20 bold',bd=5,relief='raise',command=hexadecimal)
		bc2.place(x=290,y=340)

		bc3=Button(po1,bg='black',fg='white',text='OCTAL',font='comisans 20 bold',bd=5,relief='raise',command=octal)
		bc3.place(x=560,y=340)

		bc4=Button(po1,bg='black',fg='white',text='DECIMAL',font='comisans 20 bold',bd=5,relief='raise',command=decimal)
		bc4.place(x=760,y=340)

		bc5=Button(po1,bg='black',fg='white',text='CLEAR',font='comisans 20 bold',bd=5,relief='raise',command=clear)
		bc5.place(x=990,y=340)

		bc5=Button(po1,bg='black',fg='white',text='LOG OUT',font='comisans 20 bold',bd=5,relief='raise',command=cancel)
		bc5.place(x=1200,y=540)



		num.mainloop()
	#else:
		#messagebox.showerror('ERROR','user not found')
		#print('jai ho')

#######################converter end################################################################

########################create ######################################################################
def create():
	new=Toplevel()
	new.geometry('1500x700+0+0')
	p2=PhotoImage(file='pp.png')
	new.iconphoto(False,p2)


	p=PhotoImage(file='pp.png')
	p1=p.subsample(4,4)
	im1=Label(new,image=p1)
	im1.pack()
	####################################variables################################################

	enr1=StringVar()
	e2=StringVar()

	##############################functions#######################################################

	def can():
		new.destroy()
		em1.delete(0,END)
		em2.delete(0,END)
	def c():
		er1.delete(0,END)
		er2.delete(0,END)
		er4.delete(0,END)


	def save():
		mydb=mysql.connector.connect(
			host='localhost',
			user='root',
			password='sunilvats',
			database='payroll'
			)
		mycursor=mydb.cursor()
		l=enr1.get()
		o=e2.get()

		#mycursor.execute("CREATE TABLE  numberconv (NO INTEGER AUTO_INCREMENT PRIMARY KEY ,NAME VARCHAR(300),PASSWORD VARCHAR(300))")


		mycursor.execute("INSERT INTO numberconv(NAME,PASSWORD) VALUES (%s,%s)",(enr1.get(),e2.get()))
		up="SELECT * FROM numberconv where NAME='%s'and PASSWORD='%s'"%(enr1.get(),e2.get())
		mycursor.execute(up)
		s=mycursor.fetchone()

		id2=s[0]
		print(id2)
		#er3.insert(enr1.get(),id1)
		if l=='' and o=='':
			messagebox.showinfo('MESSAGE','ALL FIELDS MUST BE FIILED')
		else:

			er4.insert(e2.get(),id2)

		mydb.commit()




	##################frames#######################################################################
	fr1=Frame(im1,bd=10,bg='black',padx=605,relief='raise')
	fr1.place(x=0,y=0)

	###################labels######################################################################
	lr1=Label(fr1,bg='black',text='CREATE NEW LOGIN',font='comisans 20 bold ',fg='white')
	lr1.pack()

	lr2=Label(im1,bg='black',text='NAME',font='comisans 25 bold ',fg='white',relief='raise',bd=10)
	lr2.place(x=350,y=150)

	lr3=Label(im1,bg='black',text='PASSWORD',font='comisans 25 bold ',fg='white',relief='raise',bd=10)
	lr3.place(x=300,y=230)

	lr4=Label(im1,bg='black',text='PLZ NOTE YOUR ID',font='comisans 25 bold ',fg='white',relief='raise',bd=10)
	lr4.place(x=230,y=330)

	#######################entries#################################################################
	er1=Entry(im1,bg='white',fg='black',font='comisans 25 bold',bd=10,relief='raise',textvariable=enr1)
	er1.place(x=550,y=150)

	er2=Entry(im1,bg='white',fg='black',font='comisans 25 bold',bd=10,relief='raise',textvariable=e2)
	er2.place(x=550,y=230)

	er4=Entry(im1,bg='white',fg='black',font='comisans 25 bold',bd=10,relief='raise')
	er4.place(x=570,y=330)


	############################buttons############################################################

	br1=Button(im1,bg='black',fg='white',font='comisans 20 bold',bd=7,relief='raise',text='SAVE',command=save)
	br1.place(x=700,y=440)

	br2=Button(im1,bg='black',fg='white',font='comisans 20 bold',bd=7,relief='raise',text='CANCEL',command=can)
	br2.place(x=900,y=440)

	br3=Button(im1,bg='black',fg='white',font='comisans 20 bold',bd=7,relief='raise',text='CLEAR',command=c)
	br3.place(x=1120,y=440)









	new.mainloop()


############################create end################################################################



######################frames in main tk ####################
fm1=Frame(pho,bd=10,bg='black',padx=620,relief='raise')
fm1.place(x=0,y=0)

fm2=Frame(pho,bd=10,bg='pink',relief='raise')
fm2.place(x=450,y=100)

ph3=PhotoImage(file='login.png')
phl=ph3.subsample(2,2)
phol=Label(pho,image=phl,relief='raise',bd=5)
phol.place(x=700,y=100)


########################labels #################################
lm1=Label(fm1,bg='black',text='NUMBER CONVERTER',font='comisans 20 bold ',fg='white')
lm1.pack()

lm2=Label(pho,bg='black',fg='white',text='LOGIN',font='comisans 40 bold ',relief='raise',bd=5)
lm2.place(x=450,y=200)

lm3=Label(pho,bg='black',fg='white',text='YOUR ID',font='comisans 20 bold ',relief='raise',bd=5)
lm3.place(x=450,y=300)

lm4=Label(pho,bg='black',fg='white',text='PASSWORD',font='comisans 20 bold ',relief='raise',bd=5)
lm4.place(x=450,y=350)

lm4=Label(pho,bg='black',fg='white',text='कार्तिकेय वत्स',font='comisans 25 bold',bd=10,relief='raise')
lm4.place(x=1000,y=625)

#############entries####################################################

em1=Entry(pho,bg='white',fg='black',font='comisans 20 bold ',bd=5,textvariable=entry1)
em1.place(x=650,y=300)

em2=Entry(pho,bg='white',fg='black',font='comisans 20 bold ',bd=5,textvariable=entry2)
em2.place(x=650,y=350)

###############button####################################################

bm1=Button(pho,bg='black',fg='white',text='SUBMIT',font='comisans 20 bold',bd=5,relief='raise',command=con)
bm1.place(x=500,y=400)

bm2=Button(pho,bg='black',fg='white',text='CREATE',font='comisans 20 bold',bd=5,relief='raise',command=create)
bm2.place(x=740,y=400)


numb.mainloop()
