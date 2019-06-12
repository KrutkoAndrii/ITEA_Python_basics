from tkinter import *
from tkinter import messagebox as mb


def exit_prg():
    quit()


def frame(dict_phone):

    def show_dict():
        text_go.delete('1.0', END)
        for item_phone in dict_phone:
            str_output = "Name " + str(item_phone) + " phone " + str(dict_phone[item_phone])+'\n'
            text_go.insert(1.0, str_output)

    def delete_name():
        entry_name.delete(0, END)
        try:
            del dict_phone[entry_name.get()]
        except Exception:
            text_go.insert(1.0, 'Nothing to delete')
        else:
            text_go.insert(1.0, 'Well done!')

    def add_to_dict():
        if not (entry_name.get() == '' or entry_phone.get() == ''):
            dict_phone[entry_name.get()] = entry_phone.get()
            entry_name.delete(0, END)
            entry_phone.delete(0, END)
        else:
            mb.showerror("Error", "Enter Name and Phone before")

    def find_by_name():
        text_go.delete('1.0', END)
        try:
            str_output = "Name " + str(entry_name.get()) + " phone " + str(dict_phone[entry_name.get()]) + '\n'
            text_go.insert(1.0, str_output)
        except Exception:
            text_go.insert(1.0, 'Nothing')
        else:
            text_go.insert(1.0, str_output)

    def find_by_phone():
        text_go.delete('1.0', END)
        dict_find = {v: k for k, v in dict_phone.items()}
        try:
            str_output = "Phone " + str(entry_phone.get()) + " Name " + str(dict_find[entry_phone.get()]) + '\n'
        except Exception:
            text_go.insert(1.0, 'Nothing')
        else:
            text_go.insert(1.0, str_output)

    def find_repetition():
        text_go.delete('1.0', END)
        dict_find = {v: k for k, v in dict_phone.items()}
        total = 0
        rep =0
        for item in dict_find:
            x = ''
            for i in item:
                if x == i:
                    rep += 1
                if rep == 2:
                    total += 1
                    rep = 0
                    text_go.insert(1.0, 'Phone ' + str(item) + " Name " + dict_find[item] + '\n')
                    break
                x = i
        text_go.insert(1.0, 'Total: ' + str(total) + '\n')

    root = Tk()
    root.title("Dictionary")
    root.geometry('500x400')
    root.resizable(False, False)
    entry_name = Entry()
    entry_name.pack(pady=10)
    entry_name.place(x=50,y=1)
    entry_phone = Entry()
    entry_phone.pack(pady=10)
    entry_phone.place(x=250,y=1)
    label = Label(text="Name", font="Arial 10")
    label.place(x=1, y=1)
    labe2 = Label(text="Phone", font="Arial 10")
    labe2.place(x=200, y=1)
    text_go = Text(root, height=30, width=70, font='Arial 10', wrap=WORD)
    text_go.pack()
    text_go.place(x=1, y=30)
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Exit", command=exit_prg)
    dict_menu = Menu(mainmenu, tearoff=0)
    dict_menu.add_command(label="Show all dict", command=show_dict)
    dict_menu.add_command(label="Add to dict", command=add_to_dict)
    dict_menu.add_command(label="Find by name", command=find_by_name)
    dict_menu.add_command(label="Find by phone", command=find_by_phone)
    dict_menu.add_command(label="Find repetition", command=find_repetition)
    dict_menu.add_command(label="delete name from dict", command=delete_name)
    mainmenu.add_cascade(label="File", menu=filemenu)
    mainmenu.add_cascade(label="Dictionary", menu=dict_menu)
    root.mainloop()


if __name__ == "__main__":
    dict_phone_all = {}
    frame(dict_phone_all)

