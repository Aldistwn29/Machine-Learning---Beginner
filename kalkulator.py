def kalkulator(operasi, angka1, angka2):

    if operasi == 1:
        hasil = angka1 + angka2
    elif operasi == 2:
        hasil = angka1 - angka2
    elif operasi == 3:
        hasil = angka1 * angka2
    elif operasi == 4:
        hasil = angka1 / angka2
    elif operasi == 5:
        hasil = angka1 ** angka2
    else:
        return
    return hasil


inputan = int(input("Silahkan Pilih Menu di bawah ini: "))
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

angka1 = int(input("Masukkan Angka: "))
angka2 = int(input("Masukkan Angka: "))
hasil = kalkulator(inputan, angka1, angka2)
print("Hasilnya: ", hasil)