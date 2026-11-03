"""Список задач команды."""

tasks = []


def add_task(title):
    """Добавляет задачу."""
    tasks.append({"title": title, "done": False})


def show_tasks():
    """Печатает задачи."""
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task['title']}")


if __name__ == "__main__":
    add_task("Настроить репозиторий")
    add_task("Написать тесты")
    show_tasks()
