from tkinter import *
import requests
from PIL import Image, ImageTk

root = Tk()
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
w = w - 200  # смещение от середины
h = h - 200
root.geometry('500x350+{}+{}'.format(w, h))


# key = 772b28435ed2d6363ec9d4716f104ef6

def get_weather():
    city = cityField.get()
    key = '772b28435ed2d6363ec9d4716f104ef6'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


back = Canvas(root, width=600, height=350)
img = ImageTk.PhotoImage(Image.open("back.jpg"))
back.create_image(0, 0, image=img, anchor="center")
back.pack()

root.title('Погода')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#191970', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=20)
cityField.pack(padx=5, pady=5)

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather, font=20)
btn.pack(padx=5, pady=5)

info = Label(frame_bottom, text='Погода', font=40)
info.pack()

root.mainloop()
