def atualizar_dicionario_interativo():
    meu_dicionario = {}
    while True:
        chave = input("Digite a chave (ou Enter para sair): ")
        if not chave:
            break
            
        valor_str = input(f"Digite o valor para '{chave}': ")
        
        try:
            if '.' in valor_str:
                valor = float(valor_str)
            else:
                valor = int(valor_str)
        except ValueError:
            valor = valor_str
            
        meu_dicionario[chave] = valor
        print(f"Dicionário atual: {meu_dicionario}\n")

atualizar_dicionario_interativo()