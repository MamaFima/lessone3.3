#Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание
# задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, title, description, deadline, status="Не выполнена"):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display_task(self):
        print(f"Задача: {self.title}\n Описание: {self.description}\n Срок выполнения: {self.deadline}\n Статус: {self.status}")

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_as_done(self, title):
        for task in  self.tasks:
            if task.title == title:
                task.update_status("Выполнена")
                print(f"Задача \"{task.title}\" отмечена как выполненная")
                break
        else:
            print("Задачи нет")

    def display_tasks_by_status(self, status):
        print(f"Задачи со статусом \"{status}\":")
        for task in self.tasks:
            if task.status == status:
                task.display_task()

manager = TaskManager()

manager.add_task(Task("Догнать группу", "Прослушать 3 лекции и сделать домашки", "2024.04.08"))
manager.add_task(Task("Убраться в квартире", "Помыть пол, попылесосить и помыть посуду", "2024.04.06"))

manager.display_tasks_by_status("Не выполнена")

manager.mark_as_done("Убраться в квартире")

















