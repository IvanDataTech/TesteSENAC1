print("Digite 'ajuda' para ver os comandos")

comando = input("Digite o comando: ")

match comando:
    case "oi":
        print("Olá, como posso lhe ajudar?")
    case "ajuda":
        print("Os comandos: 'oi', 'ajuda', 'tchau'.")
    case "tchau":
        print("Até mais!")
    case _:
        print("Comando inválido!")