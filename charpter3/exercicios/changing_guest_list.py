convidados = ['matheus' , 'maria' , 'pedro' , 'yan']

numeros = 0
for numeros in range(len(convidados)) :
    print(convidados[numeros])


#pessoas que nao vao mas
convidados.remove('matheus')
#novo convidado
convidados.insert(0, 'peixenalta')

print('*********')
numeros = 0
for numeros in range(len(convidados)) :
    print(convidados[numeros])
