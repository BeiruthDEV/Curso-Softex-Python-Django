def contagem_palavras(texto):
    palavras = texto.lower().split()
    frequencia = {}
    
    for palavra in palavras:
        palavra = palavra.strip(".,!?")
        try:
            frequencia[palavra] += 1
        except KeyError:
            frequencia[palavra] = 1
            
    return frequencia


texto_exemplo = "Python é legal. Python é poderoso. Programar em Python é divertido."
print(contagem_palavras(texto_exemplo))