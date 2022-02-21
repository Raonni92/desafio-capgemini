def escada_string(n: int) -> str:
    escada = ""
    rjust_len = n * 2 - 3
    for c in range(1, n + 1):
        if c < n:
            value = "* " * c
            value = value[:-1]
        else:
            value = "*" * c
        escada += value.rjust(rjust_len) + "\n"
    return escada[:-1]


if __name__ == "__main__":
    n = int(input("quantos andares tem a escada? "))
    escada = escada_string(n)
    print(escada)
