class PhoneBook:
    '''Class for phone'''
    __subscribers_lists = []

    def __init__(self, name="N/A", number="N/A"):
        ''' init variables '''
        self._name = name
        self._number = number

    def get_item(self):
        ''' return item '''
        return self._name, self._number

    def set_item(self, name, number):
        ''' set item '''
        self._name = name
        self._number = number

    def add_dict(self, new_subscriber):
        self.__subscribers_lists.append(new_subscriber)

    def is_delete_by_name(self, look_name):
        for line in self.__subscribers_lists:
            name, phone = line.get_item()
            if name == look_name:
                self.__subscribers_lists.remove(line)
                return True
        return False

    def get_all_dict(self):
        return self.__subscribers_lists

    def find_by_name(self, look_name):
        for line in self.__subscribers_lists:
            name, phone = line.get_item()
            if name == look_name:
                return "Name {} Phone {}\n".format(name, phone)
        else:
            return "Nothing\n"

    def find_by_phone(self, look_phone):
        for line in self.__subscribers_lists:
            name, phone = line.get_item()
            if phone == look_phone:
                return "Name {} Phone {}\n".format(name, phone)
        else:
            return "Nothing\n"

    def find_repetition(self):
        total = 0
        rep = 0
        result = ''
        for line in self.__subscribers_lists:
            name, phone = line.get_item()
            x = ''
            for i in phone:
                if x == i:
                    rep += 1
                else:
                    rep = 0
                if rep == 2:
                    total += 1
                    rep = 0
                    result += ('Phone ' + str(phone) +
                               ' Name ' + name + '\n')
                    break
                x = i
        result += ('Total: ' + str(total) + '\n')
        return result


if __name__ == "__main__":
    print(" This module not for running!")
