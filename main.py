from tkinter import *
from utils.windows import window
from utils.styles import *
from core.files import *
from core.ftp import *

#window####################################################
main_form = Tk()
main_form.title('FTP InfoVetWeb')
main_form.iconbitmap("static/images/ftp.ico")

main_form.resizable(True,True)
#main_form.state("zoomed")

obj_window = window()
window_size =  obj_window.window_center()
main_form.geometry(window_size)

#functions####################################################
def list_remote_files():
    list_files = Ftp.list_files()
    lbx_target.delete(0,END)
    for file in list_files:
        lbx_target.insert(END,file)

def bt_upload_click():
    list_files = File.list_files("origin")
    lbx_origin.delete(0,END)
    for file in list_files:
        lbx_origin.insert(END,file)
        list_remote_files()

#components####################################################
lbx_origin = Listbox(main_form)
lbx_target = Listbox(main_form)

bt_upload = Button(main_form,text= "Run", command= lambda: bt_upload_click())
bt_upload.config(**Style.button_ok())

lb_top = Label(main_form, text="Atualize a pasta production e clique em RUN",padx=30,pady=30)
lb_top.config(**Style.label())

ed_port = Entry(main_form,text="Port")
ed_port.focus()

lb_top["text"] = "Bola"

#pack####################################################
lb_top.grid(row=0,column=0,sticky=N)
bt_upload.grid(row=3,column=9,sticky='WE')
ed_port.grid(row=0,column=3,sticky=N)
lbx_origin.grid(row=1, column=0,columnspan=7,rowspan=23, sticky='nsew')
lbx_target.grid(row=1, column=16,columnspan=9,rowspan=23,sticky='nswe')

for i in range(24):
    main_form.grid_rowconfigure(i, weight=1)
    main_form.grid_columnconfigure(i, weight=1)

main_form.mainloop()
