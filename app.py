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


def multiplasSenhas(qtd_senhas, qtd_caracteres):
    for _ in range(1, qtd_senhas + 1):
        senha = gerarSenha(qtd_caracteres)
        print(f"Senha {_}: {senha}")


def limpaTela():
    os.system("cls")


def pulaLinha():
    print("")


# ---------------------------------------------------------------------------------------------------- menu
limpaTela()
print("Gerador de Senhas")
pulaLinha()
opcoes = {
    1: "Básica",
    2: "Intermediária",
    3: "Recomendada",
    4: "Personalizado",
}
for k, v in opcoes.items():
    print(f"{k}: {v}")
pulaLinha()


# ---------------------------------------------------------------------------------------------------- código principal
escolha = int(input("Escolha uma opção: "))
limpaTela()
match escolha:
    case 1:  # senha de 6 digitos
        senha = gerarSenha(6)
        print(f"Senha básica: {senha}")
        pyperclip.copy(senha)
        pulaLinha()
        print("Sua senha foi copiada para o clipboard.")

    case 2:  # senha de 8 digitos
        senha = gerarSenha(8)
        print(f"Senha intermediária: {senha}")
        pyperclip.copy(senha)
        pulaLinha()
        print("Sua senha foi copiada para o clipboard.")

    case 3:  # senha de 12 digitos
        senha = gerarSenha(12)
        print(f"Senha recomendada: {senha}")
        pyperclip.copy(senha)
        pulaLinha()
        print("Sua senha foi copiada para o clipboard.")

    case 4:  # senhas personalizadas
        qtd_senhas = int(input("Quantas senhas quer gerar? "))
        limpaTela()
        tamanho = int(input("Quantos caracteres deve ter as senhas? "))
        limpaTela()
        if tamanho > 0 and tamanho <= 70:
            multiplasSenhas(qtd_senhas, tamanho)
        else:
            print("Tamanho máximo permitido é de 70 caracteres.")

pulaLinha()
