print("=====Aplikasi Rapot=======")
try :
    Nilai = float(input("Masukan Angka: "))


    if Nilai > 85:
        print("Grade A")
    elif Nilai >= 75:
        print("grade B")
    elif Nilai >= 65:
        print("Grade C")
    elif Nilai >= 50 :
        print("Grade D")
    else:
        print("Ngulang")
except ValueError :
    print("Mohan Maaf inputan tidak valid")
