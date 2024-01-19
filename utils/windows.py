from tkinter import *

class window:

    def window_center(self):
        size_form = Tk()
        size_form.withdraw()
        width = round(size_form.winfo_screenwidth()/1.5)
        height = round(size_form.winfo_screenheight()/1.2)
        left = round((size_form.winfo_screenwidth() - width)/2)
        top = round((size_form.winfo_screenheight() - height)/2)
        window_size = str(width) + 'x' + str(height) + '+' + str(left) + '+' + str(top)
        size_form.destroy()
        return window_size