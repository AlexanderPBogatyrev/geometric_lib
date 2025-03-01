import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "78aabc988ebc797eaaec183b7fe6af6c"
CITY = "Санкт-Петербург"

def get_weahter():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        message = f'Погода в Санкт-Петербурге: {weather_description}, температура: {temperature}°C'
        messagebox.showinfo("Состояние погоды", message)
    else:
        messagebox.showerror("Ошибка", "Не удалось получить данные о погоде")

def shortcut(event):
    get_weahter()

root = tk.Tk()
root.title("WeatherPlagin")
root.bind('<Control-w>', shortcut)
root.mainloop()
