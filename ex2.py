print("Digite os seguintes animais: ")
print("cachorro\n gato\n leão\n tigre\n")
animal = input("Digite o nome de um dos animais listados: ")

match animal:
    case "cachorro" | "gato":
        print("Este é um animal domesticado.")
    case "leão" | "tigre":
        print("Esté é um animal selvagem.")
    case _:
        print("Animal inválido ou nome digitado incorretamente!")