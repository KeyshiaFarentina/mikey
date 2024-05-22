print('pertambahan -1 , pengurangan -2')

operation = input ('choose operation between 1 and 2')

if operation == '1': 
    print('menghitung pertambahan')

    angkal=int(input('enter angka1')) 
    angka2=int(input('enter angka2'))

    result=int(angkal+angka2)
    print('pertambahan result is',result)

elif operation =='2':
     print('calculate pengurangan ') 
         
     angkal=int(input('enter angkal')) 
     angka2=int(input('enter angka2'))

     result=int(angkal-angka2) 
     print('pegurangan result is',result)


    