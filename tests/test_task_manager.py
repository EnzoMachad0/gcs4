import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from task_manager import Task, TaskManager


def test_criar_tarefa():
    t = Task("Testar sistema", "alta")
    assert t.title == "Testar sistema"
    assert t.priority == "alta"
    assert t.done is False


def test_completar_tarefa():
    manager = TaskManager()
    manager.add("Tarefa A", "media")
    result = manager.complete("Tarefa A")
    assert result is True
    assert manager.list_tasks()[0].done is True


def test_prioridade_invalida():
    try:
        Task("Tarefa inválida", "urgente")
        assert False, "Deveria lançar ValueError"
    except ValueError:
        pass


def test_resumo():
    manager = TaskManager()
    manager.add("T1", "alta")
    manager.add("T2", "baixa")
    manager.complete("T1")
    s = manager.summary()
    assert s["total"] == 2
    assert s["concluidas"] == 1
    assert s["pendentes"] == 1


if __name__ == "__main__":
    test_criar_tarefa()
    test_completar_tarefa()
    test_prioridade_invalida()
    test_resumo()
    print("Todos os testes passaram.")
