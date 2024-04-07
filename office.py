class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен в список")

   
    def remove_user(self, name):
        self.user_list = [user for user in self.user_list if user.get_name() != name]
        print(f"Пользователь удален из списка")
    def info_users(self):
        for user in self.user_list:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


user1 = User("u.101", "Иванов Иван Иванович")
user2 = User("u.103", "Егорова Лариса Ивановна")
admin1 = Admin("a.102", "Петров Петр Петрович")

admin1.add_user(user1)

admin1.info_users()

admin1.add_user(user2)
admin1.info_users()

admin1.remove_user("Егорова Лариса Ивановна")
admin1.info_users()