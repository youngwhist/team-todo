"""Список задач команды."""

tasks = []


def add_task(title, priority="обычный"):
    """Добавляет задачу с приоритетом: высокий, обычный, низкий."""
    tasks.append({"title": title, "done": False, "priority": priority})


def complete_task(number):
    """Отмечает задачу выполненной (нумерация с 1)."""
    tasks[number - 1]["done"] = True


def show_tasks():
    """Печатает задачи."""
    for number, task in enumerate(tasks, 1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']} [{task['priority']}]")


if __name__ == "__main__":
    add_task("Настроить репозиторий", "высокий")
    add_task("Написать тесты")
    complete_task(1)
    show_tasks()
