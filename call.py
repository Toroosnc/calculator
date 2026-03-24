import ctypes
import sys
import os

nama_lib = 'calculator.dll' if sys.platform == 'win32' else './calculator.so'

try:
    calc_lib = ctypes.CDLL(os.path.abspath(nama_lib))
except OSError:
    print(f"Ga bisa memuat {nama_lib}")
    sys.exit(1)

calc_lib.tambah.argtypes = [ctypes.c_double, ctypes.c_double]
calc_lib.tambah.restype = ctypes.c_double

calc_lib.kurang.argtypes = [ctypes.c_double, ctypes.c_double]
calc_lib.kurang.restype = ctypes.c_double

calc_lib.kali.argtypes = [ctypes.c_double, ctypes.c_double]
calc_lib.kali.restype = ctypes.c_double

calc_lib.bagi.argtypes = [ctypes.c_double, ctypes.c_double]
calc_lib.bagi.restype = ctypes.c_double
def main():
    while True:
        print("\nKalkulator")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu 1-5: ")

        if pilihan == '5':
            print("Program selesai.")
            break

        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("input 1: "))
                angka2 = float(input("input 2: "))
            except ValueError:
                print("Bukan angka")
                continue
            if pilihan == '1':
                hasil = calc_lib.tambah(angka1, angka2)
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = calc_lib.kurang(angka1, angka2)
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = calc_lib.kali(angka1, angka2)
                print(f"Hasil: {angka1} * {angka2} = {hasil}")
            elif pilihan == '4':
                if angka2 == 0:
                    print("Tidak bisa membagi dengan nol.")
                else:
                    hasil = calc_lib.bagi(angka1, angka2)
                    print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Pilihan ga ada.")

if __name__ == "__main__":
    main()