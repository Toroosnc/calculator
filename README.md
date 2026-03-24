# Hybrid Calculator (Python & C++)

Proyek kalkulator Command Line Interface (CLI) yang menggunakan C++ sebagai mesin penghitung (core logic) dan Python sebagai antarmuka pengguna. Kedua bahasa ini dihubungkan menggunakan library `ctypes`.

## Fitur Utama
* Arsitektur hybrid memisahkan logika matematika (C++) dan UI (Python).
* Operasi dasar: Penjumlahan, Pengurangan, Perkalian, dan Pembagian.

## Prasyarat
* Python 3.x
* Compiler C++ (g++ / MinGW / GCC)

## Cara Menjalankan

### 1. Kompilasi File C++
Buka terminal dan jalankan perintah berikut sesuai sistem operasi:

**Windows:**
```bash
g++ -shared -o calculator.dll calculator.cpp

python main.py
