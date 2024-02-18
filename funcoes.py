import string
import os
import secrets


def gerar_senha(tamanho):
    pontuacao = ["!", "#", "$", "%", "&", "*", "?", "@"]
    caracteres = *string.ascii_letters, *string.digits, *pontuacao
    senha = []
    while len(senha) < tamanho:
        escolha = secrets.choice(caracteres)
        if escolha not in senha:
            senha.append(escolha)
    senha_gerada = "".join(senha)
    return senha_gerada


def multiplas_senhas(qtd_senhas, qtd_caracteres):
    for numero in range(1, qtd_senhas + 1):
        senha = gerar_senha(qtd_caracteres)
        print(f"Senha {numero:02d}: {senha}")


def limpa_tela():
    os.system("cls")


def pula_linha():
    print("")
