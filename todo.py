"""Список задач команды."""

tasks = []


def add_task(title, priority="обычный"):
    """Добавляет задачу с приоритетом: высокий, обычный, низкий."""
    tasks.append({"title": title, "done": False, "priority": priority})


def show_tasks():
    """Печатает задачи."""
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task['title']} [{task['priority']}]")


if __name__ == "__main__":
    add_task("Настроить репозиторий", "высокий")
    add_task("Написать тесты")
    show_tasks()
