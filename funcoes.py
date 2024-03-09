import string
import os
import secrets


def gerar_senha(tamanho: int):
    """
    Gera uma senha aleatória com caracteres que não se repetem.

    Args:
        tamanho: O tamanho que a senha deve conter (até 70 caracteres).

    Returns:
        string: Senha gerada
    """
    pontuacao = ["!", "#", "$", "%", "&", "*", "?", "@"]
    caracteres = *string.ascii_letters, *string.digits, *pontuacao
    senha = []
    while len(senha) < tamanho:
        escolha = secrets.choice(caracteres)
        if escolha not in senha:
            senha.append(escolha)
    senha_gerada = "".join(senha)
    return senha_gerada


def multiplas_senhas(qtd_senhas: int, qtd_caracteres: int):
    """
    Gera multiplas senhas aleatórias com caracteres que não se repetem.

    Args:
        qtd_senhas: A quantidade de senhas que deve ser gerada.
        qtd_caracteres: A quantidade de caracteres que cada senha deve conter.

    Returns:
        Diversas senhas geradas aleatóriamente na quantidade de vezes que o
        usuário definir, com o número de caracteres que o usuário definir.
    """
    for numero in range(1, qtd_senhas + 1):
        senha = gerar_senha(qtd_caracteres)
        print(f"Senha {numero:02d}: {senha}")


def limpa_tela():
    """Função que limpa o console"""
    os.system("cls")
