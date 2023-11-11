# ---------------------------------------------------------------------------------------------------- módulos importados
import string
import os
import secrets
import pyperclip


# ---------------------------------------------------------------------------------------------------- funções criadas
def gerarSenha(tamanho):
    pontuacao = ["!", "#", "$", "%", "&", "*", "?", "@"]
    caracteres = *string.ascii_letters, *string.digits, *pontuacao
    senha = []
    while len(senha) < tamanho:
        escolha = secrets.choice(caracteres)
        if escolha not in senha:
            senha.append(escolha)
    senha_gerada = "".join(senha)
    return senha_gerada


def limpaTela():
    os.system("cls")


def pulaLinha():
    print("")


# ---------------------------------------------------------------------------------------------------- menu
limpaTela()
print("Gerador de Senhas")
pulaLinha()
opcoes = {1: "Básica", 2: "Intermediária", 3: "Recomendada", 4: "Personalizada"}
for k, v in opcoes.items():
    print(f"{k}: {v}")
pulaLinha()


# ---------------------------------------------------------------------------------------------------- código principal
escolha = int(input("Escolha uma opção: "))
limpaTela()
match escolha:
    case 1:
        senha = gerarSenha(6)  # senha de 6 digitos
        print(f"Senha básica: {senha}")
    case 2:
        senha = gerarSenha(8)  # senha de 8 digitos
        print(f"Senha intermediária: {senha}")
    case 3:
        senha = gerarSenha(12)  # senha de 12 digitos
        print(f"Senha recomendada: {senha}")
    case 4:
        tamanho = int(input("Qual tamanho sua senha deve ter? "))
        senha = gerarSenha(tamanho)  # senha personalizada pelo usuário
        print(f"Senha personalizada de {tamanho} digitos: {senha}")
pulaLinha()
pyperclip.copy(senha)
print("Sua senha foi copiada para o clipboard.")


# o maximo de caracteres que uma senha pode ter no modelo atual sao 70 caracteres, preciso tratar o erro
