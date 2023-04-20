from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Style

raiz = Tk()
raiz.title("Ejercicio1")
raiz.geometry("600x450")

mainFrame = ttk.Frame(raiz)
mainFrame.grid(column= 0, row=0)
secondFrame = ttk.Frame(mainFrame, padding = "190 35 191 35", relief="raised")
secondFrame.grid(column=1, row = 1)
thridFrame = ttk.Frame(mainFrame, padding = "299 5 299 5", relief="raised")
thridFrame.grid(column=1, row=2)
fourthFrame = ttk.Frame(mainFrame, padding= "53 5 54 5", relief="raised")
fourthFrame.grid(column=1, row=3)
fifthFrame = ttk.Frame(mainFrame, padding = "142 20 143 20", relief="raised")
fifthFrame.grid(column=1, row=4)
sixthFrame = ttk.Frame(mainFrame, padding = "143 20 143 20", relief="raised")
sixthFrame.grid(column=1, row=5)
seventhFrame = ttk.Frame(mainFrame, padding = "267 31 268 30", relief="raised")
seventhFrame.grid(column=1, row=6)

#secondFrame
notebook = ttk.Notebook(secondFrame)
notebook.grid(column=1, row=1)

style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="blue")
style.map("TNotebook", background= [("selected", "red")])

frame1 = Frame(notebook)
frame1.grid(column=1, row=1)
frame2 = Frame(notebook)
frame2.grid(column=2, row=1)
frame3 = Frame(notebook)
frame3.grid(column=3, row=1)
frame4 = Frame(notebook)
frame4.grid(column=4, row=1)
frame5 = Frame(notebook)
frame5.grid(column=5, row=1)

notebook.add(frame1, text="Add")
notebook.add(frame2, text="Delete")
notebook.add(frame3, text="Search")
notebook.add(frame4, text="Services")
notebook.add(frame5, text="Help")

#thirdFrame
ttk.Label(thridFrame, text= "").grid(column=1, row=1)

#fourthFrame
ttk.Label(fourthFrame, text= "First name: ").grid(column=1, row=1, sticky=(E))
ttk.Label(fourthFrame, text= "Last name: ").grid(column=5, row=1, sticky=(E))
ttk.Label(fourthFrame, text= "").grid(column=1, row=2)
ttk.Label(fourthFrame, text= "Birth date: ").grid(column=1, row=3, sticky=(E))
ttk.Label(fourthFrame, text= "Country: ").grid(column=5, row=3, sticky=(E))

fnameEntry = ttk.Entry(fourthFrame, width = 30)
fnameEntry.grid(column=2, row=1, columnspan=3)
lnameEntry = ttk.Entry(fourthFrame, width = 30)
lnameEntry.grid(column=6, row=1)
diaEntry = Entry(fourthFrame, width=5)
diaEntry.grid(column=3, row=3)
mesEntry = Entry(fourthFrame, width=5)
mesEntry.grid(column=2, row=3)
añoEntry = Entry(fourthFrame, width=5)
añoEntry.grid(column=4, row=3)
countryEntry = Entry(fourthFrame, width=30)
countryEntry.grid(column=6, row=3)

#fifthFrame
ttk.Label(fifthFrame, text= "Credit card (if any): ").grid(column=1, row=1, sticky=(W))
ttk.Label(fifthFrame, text= "Credit card Type(if any): ").grid(column=1, row=2, sticky=(W))

cardEntry = ttk.Entry(fifthFrame, width = 30)
cardEntry.grid(column=2, row=1, columnspan=3)
RadioA = StringVar()
visa = ttk.Radiobutton(fifthFrame, text="Visa", variable=RadioA, value='visa', compound='center').grid(column=2, row=2, sticky=(W))
mastercard = ttk.Radiobutton(fifthFrame, text="Mastercard", variable=RadioA, value='mastercard', compound='center').grid(column=3, row=2, sticky=(W))

#sixthFrame
ttk.Label(sixthFrame, text= "Room type: ").grid(column=1, row=1, sticky=(N))
ttk.Label(sixthFrame, text= "Total Staying Time (days): ").grid(column=4, row=1, sticky=(N))
totalEntry = ttk.Entry(sixthFrame, width= 5)
totalEntry.grid(column=5, row=1)
ttk.Label(sixthFrame, text="   ").grid(column=3, row=1)

RadioB = StringVar()
normal = ttk.Radiobutton(sixthFrame, text="Normal", variable=RadioB, value='normal', compound='center').grid(column=2, row=1, sticky=(W))
familiar = ttk.Radiobutton(sixthFrame, text="Familiar", variable=RadioB, value='familiar', compound='center').grid(column=2, row=2, sticky=(W))
special = ttk.Radiobutton(sixthFrame, text="Special", variable=RadioA, value='special', compound='center').grid(column=2, row=3, sticky=(W))

#seventhFrame
ttk.Button(seventhFrame, text="Submit").grid(column=1, row=1)

raiz.mainloop()