def adicionar_permissao(banco_usuarios, usuario, nova_permissao):
    if usuario in banco_usuarios:
        if nova_permissao not in banco_usuarios[usuario]:
            banco_usuarios[usuario].append(nova_permissao)
            print(f"Permissão '{nova_permissao}' adicionada para {usuario}.")
        else:
            print(f"Usuário {usuario} já tem a permissão '{nova_permissao}'.")
    else:
        print(f"Erro: Usuário {usuario} não encontrado.")


usuarios = {
    'admin': ['ler', 'escrever', 'deletar'],
    'convidado': ['ler']
}

adicionar_permissao(usuarios, 'convidado', 'escrever')
adicionar_permissao(usuarios, 'admin', 'ler') 
adicionar_permissao(usuarios, 'hacker', 'tudo') 
print(f"Banco atualizado: {usuarios}")