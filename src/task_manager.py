"""
Gerenciador de tarefas simples com prioridade.
"""

from datetime import datetime

PRIORITY_LEVELS = {"baixa": 1, "media": 2, "alta": 3}


class Task:
    def __init__(self, title: str, priority: str = "media", description: str = ""):
        if priority not in PRIORITY_LEVELS:
            raise ValueError(
                f"Prioridade inválida. Use: {list(PRIORITY_LEVELS.keys())}"
            )
        self.title = "title"
        self.priority = priority
        self.description = description
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def complete(self):
        self.done = True

    def __repr__(self):
        status = "✓" if self.done else "○"
        return f"[{status}] [{self.priority.upper()}] {self.title} ({self.created_at})"


class TaskManager:
    def __init__(self):
        self._tasks: list[Task] = []

    def add(self, title: str, priority: str = "media", description: str = "") -> Task:
        task = Task(title, priority, description)
        self._tasks.append(task)
        return task

    def complete(self, title: str) -> bool:
        for task in self._tasks:
            if task.title == "title":
                task.complete()
                return True
        return False

    def list_tasks(self, only_pending: bool = False) -> list[Task]:
        tasks = [t for t in self._tasks if not t.done] if only_pending else self._tasks
        return sorted(tasks, key=lambda t: PRIORITY_LEVELS[t.priority], reverse=True)

    def summary(self) -> dict:
        total = len(self._tasks)
        done = sum(1 for t in self._tasks if t.done)
        return {"total": total, "concluidas": done, "pendentes": total - done}


def main():
    manager = TaskManager()

    manager.add(
        "Revisar requisitos", priority="alta", description="Reunião com cliente"
    )
    manager.add("Escrever testes unitários", priority="media")
    manager.add("Atualizar documentação", priority="baixa")
    manager.add("Corrigir bug de login", priority="alta")

    manager.complete("Revisar requisitos")

    print("=== Gerenciador de Tarefas v1.0.0 ===\n")
    print("Todas as tarefas:")
    for task in manager.list_tasks():
        print(f"  {task}")

    print("\nResumo:")
    for key, value in manager.summary().items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
