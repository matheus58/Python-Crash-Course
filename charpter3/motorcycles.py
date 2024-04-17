motorcycles = ['honda','yamaha', 'suzuki']


#ADICIONAR ELEMENTOS NA LISTA 
def adicionando_usando_APPEND(lista,adicionado):
    #o append adiciona o elemento no final da lista
    lista.append(adicionado);

def adicionando_usando_INSERT(lista,adicionado,indice):
    #o insert pode inserir o elemento em qualquer lugar da lista que voce desejar
    lista.insert(indice,adicionado);

motorcycles[0]='ducati'#adicionando pelo indice

#REMOVER ELEMENTOS NA LISTA
def remover_usando_DEL(lista , indice):
    # se voce sabe a posisos do item que voce que remover voce pode usar o del para deletar o item da lista 
    del lista [indice];

def remover_usando_POP(lista):
    # o pop serve para remover o ultimo item da lista na sua forma pura 'pop()'
    lista.pop();

def remover_usando_POP_no_indice_especifico(lista ,indice):
    # O POP tambem pode remover um item especifico basta pasar o indice dese item como parametro 'pop(indice)'
    lista.pop(indice)

def remover_usando_REMOVE(lista,nome):
    #as vezes voce so sabe o nome do elemento na lista e nao onde ele esta localizado ai com o remove e posivel deletalo pelo o seu nome 
    lista.remove(nome)

#Brincando com a lista

print(f'lista : {motorcycles}')
print('Adicionando novo elemento : como o append : "ninja"')
adicionando_usando_APPEND(motorcycles,'ninja');
print(motorcycles)
print('Adicionando novo elemento : como o insert no indice [0]: "bugat"')
adicionando_usando_INSERT(motorcycles , 'bugate', 0);
print(motorcycles)
print('----------------------------------------------------------------------------------------')
print('Deletando  elemento : como o del no indice [0]: "bugat"')
remover_usando_DEL(motorcycles,0)
print(motorcycles)
print('Deletando  elemento : como o pop() no: "bugat"')
remover_usando_POP(motorcycles)
print(motorcycles)
print('Deletando  elemento : como o pop() no indice [1]: "yamaha"')
remover_usando_POP_no_indice_especifico(motorcycles,1)
print(motorcycles)
print('Deletando  elemento : como o remove :com nome : "suzuki"')
remover_usando_REMOVE(motorcycles,'suzuki')
print(motorcycles)








