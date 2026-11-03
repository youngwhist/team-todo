"""Список задач команды."""

tasks = []


def add_task(title):
    """Добавляет задачу."""
    tasks.append({"title": title, "done": False})


def complete_task(number):
    """Отмечает задачу выполненной (нумерация с 1)."""
    tasks[number - 1]["done"] = True


def show_tasks():
    """Печатает задачи."""
    for number, task in enumerate(tasks, 1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


if __name__ == "__main__":
    add_task("Настроить репозиторий")
    add_task("Написать тесты")
    complete_task(1)
    show_tasks()
