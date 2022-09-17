import tkinter as tk
from playsound import playsound
from os.path import abspath


class RemindWindow():
    def __init__(self, remind_text):
        remind_text = self.wrap(remind_text)
        self.win = tk.Tk()
        self.w, self.h = 300, 250
        self.win.title('Notify')
        self.win.geometry(f'{self.w}x{self.h}')
        self.win['bg'] = '#000'
        self.stop = False

        font_size = round((self.w/len(remind_text[:25])*1.4)-(remind_text.count('\n')*0.5))  # formula to get optimal size
        font_size = font_size if font_size < 50 else 50  # making max size 50
        reminder_label = tk.Label(self.win, text=remind_text, bg='#000', fg='#fff', font=('Regular', font_size, 'bold'))
        stop_btn = tk.Button(self.win, text='Stop', bg='#fff', font=('Regular', 35, 'bold'), width=self.w, command=self.stop_ringing)

        reminder_label.pack(side=tk.TOP, pady=5)
        stop_btn.pack(side=tk.BOTTOM)

        self.ring()

    def stop_ringing(self):
        self.stop = True

    def ring(self):
        playsound(abspath('music/bell_sound.mp3'))
        if self.stop: self.win.destroy()
        else: self.win.after(ms=500, func=self.ring)

    def wrap(self, text: str) -> str:
        wrap_count = len(text) // 25 if len(text) / 25 == len(text) // 25 else len(text) // 25 + 1  # checking how much wrap we need
        result = ''
        for i in range(wrap_count):
            result += text[i*25:(i+1) * 25]+'\n'

        return result

    def run(self):
        self.win.mainloop()