### Ejercicios

'''
1. Declare an empty list
#-------------------------------------------------------------
'''
print('-----------------------------------------------------')
lista = [] 
print(len(lista)) 
print('-----------------------------------------------------')
'''
2. Declare a list with more than 5 items
#-----------------------------------------------------------
'''
print('-----------------------------------------------------')
Aminoacidos = ['Alanina', 'Arginina', 'Cisteína', 'Glutamina','Histidina','Leucina','Lisina','Metionina','Tirosina'] 
print('Aminoacidos:', Aminoacidos)
print('-----------------------------------------------------')

''''



3. Find the length of your list
#----------------------------------------------------------
'''
print('-----------------------------------------------------')
print('Número de Aminoacidos encontrados:', len(Aminoacidos))
print('-----------------------------------------------------')
'''
4. Get the first item, the middle item and the last item of the list
#-------------------------------------------------------------
'''

print('Primer elemento:')
primer_Amino = Aminoacidos[0] # estamos accediendo al primer elemento usando su índice
print(primer_Amino)  

print('Elemento de en medio:')
Elemento_m=Aminoacidos[4]
print(Elemento_m)

print('Ultimo elemento:')
Elemento_f=Aminoacidos[-1]
print(Elemento_f)
print('-----------------------------------------------------')



''''
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
#----------------------------------------------------------
'''


tipos_de_datos_mixtos=['Alberto','22 años','1.76cm','Soltero','Facultad de economia num 68.']
print(tipos_de_datos_mixtos)
print('-----------------------------------------------------')

''''
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
#-------------------------------------------------------------

'''
Empresas=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print('-----------------------------------------------------')
'''


7. Print the list using _print()_
#--------------------------------------------------------------------
'''
print(Empresas)
''''


8. Print the number of companies in the list
#-------------------------------------------------------------------
'''
print('Numero de empresas:',len(Empresas))
print('-----------------------------------------------------')
'''



9. Print the first, middle and last company
#-----------------------------------------------------------------------
'''
primera=(Empresas[0])
medio=(Empresas[3])
final=(Empresas[-1])
print('Primera empresa adscrita:',primera)
print('Empresa de en medio:',medio)
print('Ultima empresa adscrita:',final)
print('-----------------------------------------------------')

'''
26. Join the following lists:
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

Lista_final= front_end + back_end
print(Lista_final)
print('-----------------------------------------------------')


'''
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
'''


