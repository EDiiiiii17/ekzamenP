from tkinter import *
from tkinter import ttk


def change_image(event, new_image):
    current_label.config(image=new_image)
    current_label.image = new_image


if __name__ == '__main__':
    window = Tk()
    window.title("Калькулятор стоимости окон")
    window.geometry("1700x1000")
    window.configure(bg="#c0e0e0")

    title_frame = Frame(window, bg="#c0e0e0")
    title_label = Label(title_frame, text="Параметры Вашего окна", font=("Helvetica", 16, "bold"), bg="#c0e0e0")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    icon1 = PhotoImage(file="1.png")
    icon2 = PhotoImage(file="2.png")
    icon3 = PhotoImage(file="3.png")

    icon_label1 = Label(title_frame, image=icon1, bg="#c0e0e0")
    icon_label2 = Label(title_frame, image=icon2, bg="#c0e0e0")
    icon_label3 = Label(title_frame, image=icon3, bg="#c0e0e0")

    icon_label1.grid(row=0, column=2, padx=10)
    icon_label2.grid(row=0, column=3, padx=10)
    icon_label3.grid(row=0, column=4, padx=10)

    title_frame.pack(side=TOP, anchor="w", padx=20)

    icon_label1.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="4.png")))
    icon_label2.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="5.png")))
    icon_label3.bind("<Button-1>", lambda event: change_image(event, PhotoImage(file="6.png")))

    current_label = Label(window, bg="#c0e0e0")
    current_label.pack(fill="both", expand=True, side=LEFT, padx=20)

    # Создание Combobox
    combo_frame = Frame(window, bg="#c0e0e0")

    combo_label1 = Label(combo_frame, bg="#c0e0e0")
    combo1 = ttk.Combobox(combo_frame, values=["Пластик", "Дерево", "Алюминий"], state="readonly")
    combo1.set("Профиль")

    combo_label2 = Label(combo_frame, bg="#c0e0e0")
    combo2 = ttk.Combobox(combo_frame, values=["Лимонный Орех", "Черный", "Орех"], state="readonly")
    combo2.set("Цвет")

    combo_label3 = Label(combo_frame, bg="#c0e0e0")
    combo3 = ttk.Combobox(combo_frame, values=["VORNE(Турция)", "SIEGENIYA(Германия)"], state="readonly")
    combo3.set("Фурнитура")

    combo_label4 = Label(combo_frame, bg="#c0e0e0")
    combo4 = ttk.Combobox(combo_frame, values=["Двухкамерный", "Энергосберегающий"], state="readonly")
    combo4.set("Стеклопакет")

    combo_label1.grid(row=0, column=0, padx=10, pady=5)
    combo1.grid(row=0, column=1, padx=10, pady=5)

    combo_label2.grid(row=1, column=0, padx=10, pady=5)
    combo2.grid(row=1, column=1, padx=10, pady=5)

    combo_label3.grid(row=2, column=0, padx=10, pady=5)
    combo3.grid(row=2, column=1, padx=10, pady=5)

    combo_label4.grid(row=3, column=0, padx=10, pady=5)
    combo4.grid(row=3, column=1, padx=10, pady=5)

    width_label = Label(combo_frame, text="Ширина (см)", bg="#c0e0e0")
    width_entry = Entry(combo_frame)
    width_label.grid(row=0, column=2, padx=10, pady=5)
    width_entry.grid(row=0, column=3, padx=10, pady=5)

    height_label = Label(combo_frame, text="Высота (см)", bg="#c0e0e0")
    height_entry = Entry(combo_frame)
    height_label.grid(row=1, column=2, padx=10, pady=5)
    height_entry.grid(row=1, column=3, padx=10, pady=5)

    combo_frame.pack(side=RIGHT, anchor="e", padx=20)

    # Словари для хранения цен на параметры
    material_prices = {
        "Пластик": 1000,
        "Дерево": 1500,
        "Алюминий": 2000,
    }

    color_prices = {
        "Лимонный Орех": 900,
        "Черный": 800,
        "Орех": 850,
    }

    hardware_prices = {
        "VORNE(Турция)": 2000,
        "SIEGENIYA(Германия)": 2200,
    }

    glazing_prices = {
        "Двухкамерный": 1500,
        "Энергосберегающий": 1800,
    }

    icon_prices = {
        "icon1": 1000,
        "icon2": 2000,
        "icon3": 3000
    }

    selected_icon = StringVar()


    def change_image(event, new_image):
        current_label.config(image=new_image)
        current_label.image = new_image

        # Обновляем выбранную иконку
        selected_icon.set(new_image)

        # Учитываем стоимость иконки
        selected_icon_value = selected_icon.get()
        total_price = int(price_label.cget("text").split(":")[1].strip().split(" ")[0])
        total_price += icon_prices.get(selected_icon_value, 0)
        price_label.config(text=f"Стоимость окна: {total_price} грн.")


    def calculate_price():
        material = combo1.get()
        color = combo2.get()
        hardware = combo3.get()
        glazing = combo4.get()
        width = float(width_entry.get())
        height = float(height_entry.get())

        total_price = (
                              material_prices.get(material, 0) +
                              color_prices.get(color, 0) +
                              hardware_prices.get(hardware, 0) +
                              glazing_prices.get(glazing, 0)
                      ) + (width + height)+ (width + height)

        selected_icon_value = selected_icon.get()
        if selected_icon_value:
            total_price += icon_prices.get(selected_icon_value, 0)

        price_label.config(text=f"Стоимость окна: {total_price} грн.")


    calculate_button = Button(window, text="Рассчитать стоимость", command=calculate_price)
    calculate_button.pack(pady=250)

    price_label = Label(window, text="Стоимость окна: ???", font=("Helvetica", 16, "bold"), bg="#c0e0e0")
    price_label.pack(pady=100)

    window.mainloop()