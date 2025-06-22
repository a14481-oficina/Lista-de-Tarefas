# Lista de Tarefas no Terminal

Um gerenciador de tarefas simples que roda no terminal.  
Permite adicionar, listar, marcar como concluída e remover tarefas, salvando tudo em um arquivo JSON para manter o histórico.

---

## Funcionalidades

- Adicionar nova tarefa
- Listar tarefas pendentes e concluídas
- Marcar tarefa como concluída
- Remover tarefa
- Salvar e carregar tarefas automaticamente em arquivo JSON (`todo_list.json`)

---

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/a14481-oficina/Lista-de-Tarefas
2. Execute o script:

```bash
python main.py
```
3. Escolha as opções no menu para gerenciar suas tarefas:
    - Adicionar tarefa
    - Listar tarefas
    - Marcar tarefa como concluída
    - Remover tarefa
    - Sair

---

## Requisitos
Python 3.x

---

## Estrutura do arquivo de tarefas

As tarefas são salvas no arquivo todo_list.json no formato JSON, contendo uma lista de objetos com as chaves:
```
desc: descrição da tarefa (string)  
done: status da tarefa (boolean)
```
