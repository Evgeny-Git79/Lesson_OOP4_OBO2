class User():
    def __init__(self, name, id):
        self.name = name
        self._id = id
        self._dostup = 'user'

    def get_user_id (self):
        return self._id

    def get_name (self):
        return self.name

    def get_dostup(self):
        return self._dostup

    def set_name(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, id):
        super().__init__(name, id)
        self._dostup = 'admin'

    def add_user(self, spisok, name):
        spisok.append(name)

    def delete_user(self, spisok, name):
        spisok.remove(name)




sotrudniki =[]
admin = Admin('Katya', '1')
polzovatel = User('Petya', '2')
polzovatel2 = User('vasya', '3')

print(polzovatel.get_name(), polzovatel.get_dostup())
print(polzovatel2.get_name(), polzovatel2.get_dostup())
admin.add_user(sotrudniki, polzovatel)
admin.add_user(sotrudniki, polzovatel2)

print(sotrudniki)



