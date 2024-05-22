print('uas segitiga-1,keliling segitiga-2')

operation = input('choose operation between 1 and 2')

if operation == '1':
   print('menghitung luas segitiga')

   a=int(input('masukkan nilai alas  '))
   t=int(input('masukkan nilai tinggi'))
   
   luas =int(0.5*a*t)
   print('luas dari segitiga tersebut adalah',luas)

elif operation =='2':
     print('menghitung keiling segitiga')
    
     sisi1= int(input('masukan sisi1'))
     sisi2= int(input('masukan sisi2'))
     sisi3= int(input('masukan sisi3'))
   
     
     keliling= int(sisi1+sisi2+sisi3)
     print('keliling dari segitiga tersebut adalah',keliling)
