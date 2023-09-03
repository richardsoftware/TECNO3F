from tkinter import Tk, Entry, Button

ventana = Tk()

ventana.configure(background="light blue")
ventana.title("Calculadora Basica")
ventana.geometry("350x350")
ventana.resizable(False, False)

datos = Entry(ventana,bg="black", fg="white")
datos.grid(columnspan=10, ipadx=113, ipady=10)

boton1 = Button(ventana, text="1", fg="black", bg="white", height=2, width=6)
boton1.grid(columnspan=2, row=2, column=0)

boton2 = Button(ventana, text="2", fg="black", bg="white", height=2, width=6)
boton2.grid(columnspan=2, row=2, column=2)

boton3 = Button(ventana, text="3", fg="black", bg="white", height=2, width=6)
boton3.grid(columnspan=2, row=2, column=4)

boton4 = Button(ventana, text="+", fg="black", bg="white", height=2, width=6)
boton4.grid(columnspan=2, row=2, column=6)



boton5 = Button(ventana, text="4", fg="black", bg="white", height=2, width=6)
boton5.grid(columnspan=2, row=4, column=0)

boton6 = Button(ventana, text="5", fg="black", bg="white", height=2, width=6)
boton6.grid(columnspan=2, row=4, column=2)

boton7 = Button(ventana, text="6", fg="black", bg="white", height=2, width=6)
boton7.grid(columnspan=2, row=4, column=4)

boton8 = Button(ventana, text="-", fg="black", bg="white", height=2, width=6)
boton8.grid(columnspan=2, row=4, column=6)


boton9 = Button(ventana, text="7", fg="black", bg="white", height=2, width=6)
boton9.grid(columnspan=2, row=6, column=0)

boton10 = Button(ventana, text="8", fg="black", bg="white", height=2, width=6)
boton10.grid(columnspan=2, row=6, column=2)

boton11 = Button(ventana, text="9", fg="black", bg="white", height=2, width=6)
boton11.grid(columnspan=2, row=6, column=4)

boton12 = Button(ventana, text="*", fg="black", bg="white", height=2, width=6)
boton12.grid(columnspan=2, row=6, column=6)


boton13 = Button(ventana, text="0", fg="black", bg="white", height=2, width=6)
boton13.grid(columnspan=2, row=8, column=0)

boton14 = Button(ventana, text=".", fg="black", bg="white", height=2, width=6)
boton14.grid(columnspan=2, row=8, column=2)

boton15 = Button(ventana, text="Borrar", fg="red", bg="white", height=2, width=6)
boton15.grid(columnspan=2, row=8, column=4)

boton16 = Button(ventana, text="/", fg="black", bg="white", height=2, width=6)
boton16.grid(columnspan=2, row=8, column=6)


boton17 = Button(ventana, text="(", fg="black", bg="white", height=2, width=6)
boton17.grid(columnspan=2, row=10, column=0)

boton18 = Button(ventana, text=")", fg="black", bg="white", height=2, width=6)
boton18.grid(columnspan=2, row=10, column=2)

boton19 = Button(ventana, text="=", fg="white", bg="red", height=2, width=6)
boton19.grid(columnspan=2, row=10, column=4)

#boton20 = Button(ventana, text="=", fg="black", bg="white", height=2, width=6)
#boton20.grid(columnspan=2, row=10, column=6)


ventana.mainloop()
