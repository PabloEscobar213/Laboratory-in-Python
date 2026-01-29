from tkinter import *
from tkinter import messagebox
import requests
import json


def fetch_github_data():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Введите имя пользователя GitHub")
        return

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code == 404:
            messagebox.showerror("Ошибка", "Пользователь не найден")
            return

        if response.status_code != 200:
            messagebox.showerror("Ошибка", f"Ошибка запроса: {response.status_code}")
            return

        data = response.json()

        filtered = {
            "login": data.get("login"),
            "name": data.get("name"),
            "company": data.get("company"),
            "email": data.get("email"),
            "created_at": data.get("created_at"),
            "id": data.get("id"),
            "url": data.get("html_url")
        }

        filename = f"{username}_info.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=2, ensure_ascii=False)

        messagebox.showinfo("Успех", f"Данные сохранены в файл: {filename}")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# GUI
window = Tk()
window.title("Хвостиков Павел Павлович — ЗИТ 252")
window.geometry("400x150")

Label(window, text="Введите имя пользователя GitHub:").pack(pady=10)
entry = Entry(window, width=30)
entry.pack()

Button(window, text="Получить данные", command=fetch_github_data).pack(pady=10)

window.mainloop()
