def Kalkulator():
    a = int(input('Masukkan nilai "a" ;'))
    b = int(input('Masukkan nilai "b" ;'))
    
    c = a + b #tambah
    d = a - b #kurang
    e = a * b #kali
    f = a / b #bagi
    g = a // b #bagi integer (bilangan bulat)
    i = a % b #modulus (hasil bagi)
    h = a ** b #exponen

    print(f'{a} tambah {b} :{c}')
    print(f'{a} kurang {b} :{d}')
    print(f'{a} tambah {b} :{e}')
    print(f'{a} tambah {b} :{f}')
    print(f'{a} tambah {b} :{g}')
    print(f'{a} tambah {b} :{h}')
    print(f'{a} tambah {b} :{i}')
    
Kalkulator()