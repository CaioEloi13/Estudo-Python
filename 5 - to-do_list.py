import json

tarefas = []


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Arquivo não existe ou está corrompido → cria vazio
        with open("tarefas.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=2)
        return []

tarefas = carregar_tarefas()


while True:
    print("\n" + "="*30)
    print("GERENCIADOR DE TAREFAS")
    print("="*30)
    print("[1] Ver tarefas")
    print("[2] Adicionar")
    print("[3] Concluir")
    print("[4] Sair")

    op = input("Escolha: ") 

    if op == "1":
        if not tarefas:
            print("Nenhuma tarefa!")
        else:
            for i, t in enumerate(tarefas):  # ← NOVA: enumerate()
                status = "✓" if t["feito"] else "☐"
                print(f"{i}: {status} {t['nome']}")

    elif op == "2":
        nome = input("Tarefa: ")
        tarefas.append({"nome": nome, "feito": False})
        print("Tarefa adicionada!")

    elif op == "3":
        if not tarefas:
            print("Nenhuma tarefa!")
            continue
        for i, t in enumerate(tarefas):
            status = "✓" if t["feito"] else "☐"
            print(f"{i}: {status} {t['nome']}")
        idx = int(input("Qual concluir? "))
        if 0 <= idx < len(tarefas):
            tarefas[idx]["feito"] = True
            print("Concluída!")
        else:
            print("Índice inválido!")

    elif op == "4":
        # === SALVAR NO ARQUIVO ===
        with open("tarefas.json", "w") as arquivo:
            json.dump(tarefas, arquivo, indent=2)  # ← NOVA: json.dump()
        print("Tarefas salvas. Até logo!")
        break