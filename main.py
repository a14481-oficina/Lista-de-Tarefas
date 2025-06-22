import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(tasks, description):
    tasks.append({'desc': description, 'done': False})
    save_tasks(tasks)
    print(f'Tarefa adicionada: {description}')

def list_tasks(tasks):
    if not tasks:
        print('Nenhuma tarefa encontrada.')
        return
    for i, t in enumerate(tasks):
        status = '[x]' if t['done'] else '[ ]'
        print(f'{i+1}. {status} {t["desc"]}')

def mark_done(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks[idx]['done'] = True
        save_tasks(tasks)
        print(f'Tarefa marcada como concluída: {tasks[idx]["desc"]}')
    else:
        print('Índice inválido.')

def unmark_done(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks[idx]['done'] = False
        save_tasks(tasks)
        print(f'Tarefa desmarcada como concluída: {tasks[idx]["desc"]}')
    else:
        print('Índice inválido.')

def remove_task(tasks, idx):
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f'Tarefa removida: {removed["desc"]}')
    else:
        print('Índice inválido.')

def main():
    tasks = load_tasks()
    while True:
        print('\n1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Marcar tarefa como concluída')
        print('4. Desmarcar tarefa como concluída')
        print('5. Remover tarefa')
        print('6. Sair')
        op = input('Escolha uma opção: ')
        if op == '1':
            desc = input('Descrição da tarefa: ')
            add_task(tasks, desc)
        elif op == '2':
            list_tasks(tasks)
        elif op == '3':
            list_tasks(tasks)
            idx = int(input('Número da tarefa para marcar como concluída: ')) - 1
            mark_done(tasks, idx)
        elif op == '4':
            list_tasks(tasks)
            idx = int(input('Número da tarefa para desmarcar como concluída: ')) - 1
            unmark_done(tasks, idx)
        elif op == '5':
            list_tasks(tasks)
            idx = int(input('Número da tarefa para remover: ')) - 1
            remove_task(tasks, idx)
        elif op == '6':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
