"""
Comercio Padaria

1- o programa tem que rodar em loop infinito ate que seja parado
2- cliente pedir um tipo de pão (frances,doce,forma,australiano)
3- cada pao terá uma quantidade
4- valor do pao
5- pedir forma de pagamento(dinheiro,cartão)
6- forma de entrega
7- dados do cliente
8- valor do frete por bairro
9- nome do atendente
10- codigo da entrega

usar estruturas basicas apenas, como if e while e for 

"""

codigo_entrega = 1 

while True:
    print("Bem-vindo a Padaria")
    print("Tipos de pao disponiveis: Frances, Doce, Forma e Australiano")
    tipo_pão = input("Qual tipo de pao voce quer?:")
    if tipo_pão not in ["Frances","Doce","Forma","Australiano"]:
        print("Tipo de pao invalido! Tente novamente.")
        continue
    
    quantidade = input("Quantos paes deseja?")
    if not quantidade.isdigit():
        print("Quantidade inválida")
        continue
    quantidade = int(quantidade)
    
    if tipo_pão == "Frances":
        valor_pão = 1.5
    elif tipo_pão == "Doce":
        valor_pão = 2.0
    elif tipo_pão == "Forma":
        valor_pão = 3.0
    else:
        valor_pão = 4.0
        
    total_pao = valor_pão * quantidade
        
    pagamento = input("Forma de pagamento(dinheiro/cartao):").lower()
    if pagamento not in ["dinheiro","cartao"]:
        print("Pagamento inválido")
        continue
    
    nome_cliente = input("Digite seu nome:")
    endereco = input("Digite seu endereço:")
    bairro = input("Digite seu bairro:")
    if bairro.lower() in ["Itaipuaçu,Centro,São José,Ponta Negra,Flamengo"]:
        frete = 5.0
    else:
        frete = 10.0
        
    atendente = input("Digite o nome do atendente:")
    
    print("\n -------------- Resumo do Pedido --------------")
    
    print(f"Cliente:{nome_cliente}")
    print(f'Endereço:{endereco}')
    print(f'Bairro:{bairro}')
    print(f'Tipo de pão:{tipo_pão}')
    print(f'Quantidade de pães:{quantidade}')
    print(f'Total de paes: R${total_pao}')
    print(f'Frete:{frete}')
    print(f'Forma de pagamento:{pagamento}')
    print(f'Atendente: {atendente}')
    print(f'Codigo da entrega: {codigo_entrega}')
    
    codigo_entrega += 1
    
    sair = input("Deseja sair do programa? [sair/ficar]").lower()
    if sair == "sair":
        print("Sistema Encerrado!")
        break