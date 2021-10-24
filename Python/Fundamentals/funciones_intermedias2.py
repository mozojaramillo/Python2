# 1.- Actualiza los valores en diccionarios y listas.

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

sports_directory['basketball'][1]="Bryant"
sports_directory['soccer'][0]="Andres"

print(sports_directory)
z[0]['y']=30
print(z)

#2.- Itera a través de una lista de diccionarios

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(lista):
    
    for i in range(0,len(lista)):
        resumen = []
        for j,k in lista[i].items():
            print(f'{j} - {k },', end=" ")
            
        print("")
            
    
iterateDictionary(students)