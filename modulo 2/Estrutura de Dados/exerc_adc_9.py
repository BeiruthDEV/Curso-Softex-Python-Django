"""
Removendo Duplicatas de uma Lista: Dada a lista de e-mails emails = ['a@mail.com',
'b@mail.com', 'a@mail.com', 'c@mail.com'], use um conjunto para criar uma nova lista
contendo apenas os e-mails únicos.

"""

emails = ['a@mail.com', 'b@mail.com', 'a@mail.com', 'c@mail.com']


emails_unicos = list(set(emails))

print(emails_unicos)
