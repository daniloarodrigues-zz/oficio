def cnpj(numero):
    conversao = str(numero)
    #print("{}.{}.{}/{}-{}".format(conversao[:2],conversao[2:5],conversao[5:8],conversao[8:12],conversao[12:14]))
    return "{}.{}.{}/{}-{}".format(conversao[:2],conversao[2:5],conversao[5:8],conversao[8:12],conversao[12:14])