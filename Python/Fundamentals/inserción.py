def ordenar(arr):    
    for i in range(1,len(arr)):
        valor = arr[i]
        for j in range(i-1,-1,-1):
            if valor < arr[j]:
                arr[j+1], arr[j] = arr[j], valor
    return arr
    
        
   
        
    


print(ordenar([9,8,17,6,5,4,33,2,1]))