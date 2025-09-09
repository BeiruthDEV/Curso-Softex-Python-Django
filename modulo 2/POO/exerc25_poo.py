def analisar_texto(texto):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    palavras = texto.split()
    cont_vogais = sum(1 for letra in texto if letra in vogais)
    cont_consoantes = sum(1 for letra in texto if letra in consoantes)
    return {
        "palavras": len(palavras),
        "vogais": cont_vogais,
        "consoantes": cont_consoantes
    }

resultado = analisar_texto("Exemplo de análise de texto")
print(resultado)
