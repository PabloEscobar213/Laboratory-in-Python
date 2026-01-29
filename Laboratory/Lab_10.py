from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext


def create_app():
    window = Tk()
    window.title("Хвостиков Павел Павлович — ЗИТ 252")
    window.geometry("600x400")

    tabs = ttk.Notebook(window)
    tab1 = Frame(tabs)
    tab2 = Frame(tabs)
    tab3 = Frame(tabs)

    tabs.add(tab1, text="Калькулятор")
    tabs.add(tab2, text="Чекбоксы")
    tabs.add(tab3, text="Работа с текстом")
    tabs.pack(expand=1, fill="both")

    # Вкладка Калькулятор 
    Label(tab1, text="Число 1:").grid(column=0, row=0, padx=10, pady=10)
    num1 = Entry(tab1, width=10)
    num1.grid(column=1, row=0)

    Label(tab1, text="Операция:").grid(column=0, row=1, padx=10, pady=10)
    operation = ttk.Combobox(tab1, width=5)
    operation["values"] = ("+", "-", "*", "/")
    operation.current(0)
    operation.grid(column=1, row=1)

    Label(tab1, text="Число 2:").grid(column=0, row=2, padx=10, pady=10)
    num2 = Entry(tab1, width=10)
    num2.grid(column=1, row=2)

    result_label = Label(tab1, text="Результат: ")
    result_label.grid(column=0, row=4, columnspan=2, pady=10)

    def calculate():
        try:
            a = float(num1.get())
            b = float(num2.get())
            op = operation.get()

            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "*":
                res = a * b
            elif op == "/":
                if b == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                res = a / b
            else:
                res = "Неизвестная операция"

            result_label.configure(text=f"Результат: {res}")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")

    Button(tab1, text="Вычислить", command=calculate).grid(column=0, row=3, columnspan=2, pady=10)

    # Вкладка Чекбоксы + всплывающее окно 
    Label(tab2, text="Выберите вариант:").grid(column=0, row=0, pady=10)

    chk1_state = BooleanVar()
    chk2_state = BooleanVar()
    chk3_state = BooleanVar()

    chk1 = ttk.Checkbutton(tab2, text="Первый", variable=chk1_state)
    chk2 = ttk.Checkbutton(tab2, text="Второй", variable=chk2_state)
    chk3 = ttk.Checkbutton(tab2, text="Третий", variable=chk3_state)

    chk1.grid(column=0, row=1, sticky=W, padx=20)
    chk2.grid(column=0, row=2, sticky=W, padx=20)
    chk3.grid(column=0, row=3, sticky=W, padx=20)

    def show_choice():
        if chk1_state.get():
            messagebox.showinfo("Выбор", "Вы выбрали первый вариант")
        elif chk2_state.get():
            messagebox.showinfo("Выбор", "Вы выбрали второй вариант")
        elif chk3_state.get():
            messagebox.showinfo("Выбор", "Вы выбрали третий вариант")
        else:
            messagebox.showwarning("Выбор", "Ничего не выбрано")

    Button(tab2, text="Показать выбор", command=show_choice).grid(column=0, row=4, pady=20)

    # Вкладка Работа с текстом + загрузка файла 
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    text_area = scrolledtext.ScrolledText(tab3, width=70, height=20)
    text_area.pack(padx=10, pady=10)

    def load_text():
        file_path = filedialog.askopenfilename(
            filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text_area.delete(1.0, END)
                    text_area.insert(INSERT, f.read())
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Загрузить текст", command=load_text)
    menu_bar.add_cascade(label="Файл", menu=file_menu)

    return window


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
