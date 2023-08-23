from tkinter import *

def change_image(event, new_image):
    current_label.config(image=new_image)
    current_label.image = new_image

if __name__ == '__main__':
    window = Tk()
    window.title("Калькулятор стоимости окон")
    window.geometry("1000x1000")
    window.configure(bg="#c0e0e0")

    title_label = Label(window, text="Параметры Вашего окна", font=("Helvetica", 16, "bold"), bg="#c0e0e0")
    title_label.pack(pady=20)

    icon_frame = Frame(window, bg="#c0e0e0")

    icon1 = PhotoImage(file="1.png")
    icon2 = PhotoImage(file="2.png")
    icon3 = PhotoImage(file="3.png")

    icon_label1 = Label(icon_frame, image=icon1, bg="#c0e0e0")
    icon_label2 = Label(icon_frame, image=icon2, bg="#c0e0e0")
    icon_label3 = Label(icon_frame, image=icon3, bg="#c0e0e0")

    icon_label1.grid(row=0, column=0, padx=10)
    icon_label2.grid(row=0, column=1, padx=10)
    icon_label3.grid(row=0, column=2, padx=10)
    icon_frame.pack()

    current_label = Label(window, bg="#c0e0e0")
    current_label.pack(pady=20)

    icon_label1.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="4.png")))
    icon_label2.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="5.png")))
    icon_label3.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="6.png")))

    window.mainloop()
