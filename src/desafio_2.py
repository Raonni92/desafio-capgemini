def verificar_senha_forte(senha: str) -> int:
    """Verifica se a senha possui requisitos de uma senha forte.

    Args:
        senha (str): a senha a ser verificada.

    Returns:
        int: quantidade de caracteres para se ter uma senha forte.
    """
    regra_especial = {"maiscula": 1, "minuscula": 1, "digito": 1, "especial": 1}
    regra_tamanho = 6
    letras_especiais = "!@#$%^&*()-+"

    for c in senha:
        if c.isdigit() and regra_especial["digito"] > 0:
            regra_especial["digito"] -= 1
        elif c in letras_especiais and regra_especial["especial"] > 0:
            regra_especial["especial"] -= 1
        elif c.islower() and regra_especial["minuscula"] > 0:
            regra_especial["minuscula"] -= 1
        elif c.isupper() and regra_especial["maiscula"] > 0:
            regra_especial["maiscula"] -= 1

        if regra_tamanho > 0:
            regra_tamanho -= 1

    pendencia_regra_especial = sum(regra_especial.values())
    if pendencia_regra_especial > regra_tamanho:
        pendencia_caracter = pendencia_regra_especial - regra_tamanho
    else:
        pendencia_caracter = regra_tamanho

    return pendencia_caracter


if __name__ == "__main__":
    senha = input("Digite a senha: ")
    pendencia = verificar_senha_forte(senha)
    print(pendencia)
