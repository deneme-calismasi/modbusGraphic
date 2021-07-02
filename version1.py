import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(width=1400, height=900, bg="white")
canvas.create_rectangle(10, 10, 120, 120, fill='red')
# canvas.create_rectangle(110, 100, 120, 110, fill='blue')


# canvas['bg'] = 'white'
canvas.pack(fill='both', expand=True)

root.mainloop()
