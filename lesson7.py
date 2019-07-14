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
Посчитать количество номеров телефонов в предыдущем примере, в которых есть 3
 или более одинаковых цифр подряд
Добавить возможность удаления человека из справочника
Добавить возможность редактирования номера - имени
с Использованием классов
'''


from tkinter import Tk
from visualisation_data.frame import FrameWindow


def main():
    root = Tk()
    root.title("Dictionary")
    root.geometry('500x400')
    root.resizable(False, False)
    app = FrameWindow()
    root.mainloop()


if __name__ == "__main__":
    main()
