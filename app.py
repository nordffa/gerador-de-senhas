from funcoes import gerar_senha, multiplas_senhas, limpa_tela
from pyperclip import copy as copia_senha

# menu
menu = {
    1: "Básica",
    2: "Intermediária",
    3: "Recomendada",
    4: "Token",
    5: "Personalizado",
}

opcoes = {
    1: 8,
    2: 12,
    3: 20,
    4: 32,
}

# código principal
while True:
    limpa_tela()
    print("Gerador de Senhas\n")

    for k, v in menu.items():
        print(f"{k}: {v}")

    escolha = int(input("\nEscolha uma opção: "))
    limpa_tela()

    if escolha in opcoes:
        senha = gerar_senha(opcoes[escolha])
        print(f"Senha: {senha}")
        copia_senha(senha)
        print("\nSua senha foi copiada para o clipboard.\n")
        break

    elif escolha == 5:
        qtd_senhas = int(input("Quantas senhas quer gerar? "))
        limpa_tela()
        tamanho = int(input("Quantos caracteres deve ter as senhas? "))
        limpa_tela()
        if tamanho > 0 and tamanho <= 70:
            multiplas_senhas(qtd_senhas, tamanho)
        else:
            print("Tamanho máximo permitido é de 70 caracteres.")
        break
