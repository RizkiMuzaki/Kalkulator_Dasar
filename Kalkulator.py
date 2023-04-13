# Kalkulator sederhana dengan Python

# Import modul colorama untuk warna pada output
from colorama import init, Fore, Style
init()

# Import modul tabulate untuk membuat tabel
from tabulate import tabulate

# Fungsi penjumlahan
def tambah(x, y):
    return x + y

# Fungsi pengurangan
def kurang(x, y):
    return x - y

# Fungsi perkalian
def kali(x, y):
    return x * y

# Fungsi pembagian
def bagi(x, y):
    return x / y

# Tampilan menu
print(Fore.BLUE + "=======================================")
print(Fore.BLUE + "            KALKULATOR SEDERHANA        ")
print(Fore.BLUE + "=======================================")
print("SELAMAT DATANG DI APLIKASI KALKULATOR DASAR RIZKI MUZAKI")
def menu():
    print(Fore.YELLOW + "Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar" + Style.RESET_ALL)

# Loop utama
while True:
    menu()

    # Meminta input dari user
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    # Validasi input
    if pilihan not in ('1', '2', '3', '4', '5'):
        print(Fore.RED + "Pilihan tidak valid" + Style.RESET_ALL)
        continue

    # Keluar dari program
    if pilihan == '5':
        print(Fore.GREEN + "Terima kasih telah menggunakan kalkulatornya" + Style.RESET_ALL)
        print(Fore.GREEN + "by Rizki Muzaki" + Style.RESET_ALL)
        break

    num1 = float(input("Masukkan bilangan pertama: "))
    num2 = float(input("Masukkan bilangan kedua: "))

    if pilihan == '1':
        hasil = tambah(num1, num2)
        operator = '+'

    elif pilihan == '2':
        hasil = kurang(num1, num2)
        operator = '-'

    elif pilihan == '3':
        hasil = kali(num1, num2)
        operator = '*'

    elif pilihan == '4':
        # Validasi pembagian dengan nol
        if num2 == 0:
            print(Fore.RED + "Tidak dapat membagi dengan nol." + Style.RESET_ALL)
            continue
        else:
            hasil = bagi(num1, num2)
            operator = '/'

    # Menampilkan hasil perhitungan dalam bentuk tabel
    table = [["Bilangan Pertama", num1], ["Bilangan Kedua", num2], ["Operator", operator], ["Hasil", hasil]]
    headers = ["Keterangan", "Nilai"]
    print("\n" + Fore.CYAN + tabulate(table, headers, tablefmt="grid") + "\n" + Style.RESET_ALL)
