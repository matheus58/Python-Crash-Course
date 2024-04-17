def printar_os_covidados(mensagem, lista):
    for lista in lista:
        print(mensagem , lista.title());

convidados = ['matheus' , 'maria' , 'pedro' , 'yan']

printar_os_covidados('Lista desatualizada :', convidados)
novo_convidado_inicio_da_lista = 'bruno'
novo_convidado_meio_da_lista = 'thiago'
convidados.insert(0 , novo_convidado_inicio_da_lista)
metade_da_lista = round(len(convidados)/2)# o round serve para arendondar os numeros 
print(metade_da_lista)
convidados.insert(metade_da_lista , novo_convidado_meio_da_lista )
final_da_lista = 'surya'
convidados.append(final_da_lista)
printar_os_covidados('lista atualizada', convidados)




