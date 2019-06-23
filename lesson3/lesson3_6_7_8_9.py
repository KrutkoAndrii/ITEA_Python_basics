'''Реализовать интерактивное меню с двумя опциями выбора:
а) добавление в справочник
б) вывод номера телефона по имени
в) вывод имени по номеру телефона

Пример
Add to dict
Get telephone
Get name
    1
    John, +380953336667
    1
    Alan, +36674490
    2
    Alan
    +36674490
3
+380953336667
John
Посчитать количество номеров телефонов в предыдущем примере,
в которых есть 3 или более одинаковых цифр подряд
Добавить возможность удаления человека из справочника
Добавить возможность редактирования номера\имени
'''

from tkinter import *
from tkinter import messagebox as mb
from tkinter import Tk, Frame, Menu


class frame_window(Frame):
    dict_phone = {}

    def __init__(self):
        super().__init__()
        self.entry_name = Entry()
        self.entry_phone = Entry()
        self.l_nom = Label(text="Name", font="Arial 10")
        self.l_phone = Label(text="Phone", font="Arial 10")
        self.text_go = Text(height=30, width=70, font='Arial 10', wrap=WORD)
        self.main_menu = Menu(self.master)
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.dict_menu = Menu(self.main_menu, tearoff=0)
        self.init_gui()

    def init_gui(self):
        self.entry_name.pack(pady=10)
        self.entry_name.place(x=50, y=1)
        self.entry_phone.pack(pady=10)
        self.entry_phone.place(x=250, y=1)
        self.l_nom.place(x=1, y=1)
        self.l_phone.place(x=200, y=1)
        self.text_go.pack()
        self.text_go.place(x=1, y=30)
        self.master.config(menu=self.main_menu)
        self.dict_menu.add_command(label="Show all dict", command=self.show_dict)
        self.dict_menu.add_command(label="Add to dict", command=self.add_to_dict)
        self.dict_menu.add_command(label="Find by name", command=self.find_by_name)
        self.dict_menu.add_command(label="Find by phone", command=self.find_by_phone)
        self.dict_menu.add_command(label="Find repetition", command=self.find_repetition)
        self.dict_menu.add_command(label="Delete item by name", command=self.delete_name)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Dictionary", menu=self.dict_menu)

    def exit_app(self):
        quit()

    def show_dict(self):
        self.text_go.delete('1.0', END)
        for item_phone in self.dict_phone:
            str_output = "Name " + str(item_phone)\
                         + " phone " + str(self.dict_phone[item_phone])+'\n'
            self.text_go.insert(1.0, str_output)

    def delete_name(self):
        self.text_go.delete('1.0', END)
        try:
            del_item = self.entry_name.get()
            del self.dict_phone[del_item]
        except Exception:
            self.text_go.insert(1.0, 'Nothing to delete')
        else:
            self.text_go.insert(1.0, 'Well done!')
            self.entry_name.delete(0, END)

    def add_to_dict(self):
        if not (self.entry_name.get() == '' or self.entry_phone.get() == ''):
            self.dict_phone[self.entry_name.get()] = self.entry_phone.get()
            self.entry_name.delete(0, END)
            self.entry_phone.delete(0, END)
        else:
            mb.showerror("Error", "Enter Name and Phone before")

    def find_by_name(self):
        self.text_go.delete('1.0', END)
        try:
            str_output = "Name " + str(self.entry_name.get()) + " phone " + \
                         str(self.dict_phone[self.entry_name.get()]) + '\n'
        except Exception:
            self.text_go.insert(1.0, 'Nothing')
        else:
            self.text_go.insert(1.0, str_output)

    def find_by_phone(self):
        self.text_go.delete('1.0', END)
        for item_index, item_value in self.dict_phone.items():
            if item_value == self.entry_phone.get():
                self.text_go.insert(1.0, "Phone "
                                    + str(self.entry_phone.get())
                                    + " Name " + str(item_index) + '\n')
                return
        self.text_go.insert(1.0, 'Nothing')

    def find_repetition(self):
        self.text_go.delete('1.0', END)
        total = 0
        rep = 0
        for item_index, item_value in self.dict_phone.items():
            x = ''
            for i in item_value:
                if x == i:
                    rep += 1
                if rep == 2:
                    total += 1
                    rep = 0
                    self.text_go.insert(1.0, 'Phone '
                                        + str(item_value) + " Name "
                                        + item_index + '\n')
                    break
                x = i
        self.text_go.insert(1.0, 'Total: ' + str(total) + '\n')


def main():
    root = Tk()
    root.title("Dictionary")
    root.geometry('500x400')
    root.resizable(False, False)
    app = frame_window()
    root.mainloop()


if __name__ == "__main__":
    main()
