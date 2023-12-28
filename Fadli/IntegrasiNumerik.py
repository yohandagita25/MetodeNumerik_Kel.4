import numpy as np #Import modul NumPy untuk manipulasi matriks dan vektor secara efisien.
import sympy as sp #Import modul SymPy untuk manipulasi ekspresi matematika simbolis.

def trapesium(a, b, h, f):
    # Fungsi trapesium untuk menghitung integral numerik menggunakan metode trapesium.
    # Input: batas bawah a, batas atas b, lebar trapesium h, dan fungsi f.
    # Output: hasil integral numerik menggunakan metode trapesium.
    n = int((b - a) / h)
    nilai_x = [] #Inisialisasi list untuk menyimpan nilai titik-titik pada sumbu x.

    for i in range(0,n+1):
        nilai_x.append(a + (i * h)) #Mengisi list nilai_x dengan titik-titik pada sumbu x.

    jumlah = f(nilai_x[0]) + f(nilai_x[n]) #Inisialisasi jumlah dengan nilai fungsi pada titik awal dan titik akhir.

    for i in range(1, n):
        jumlah += 2 * f(nilai_x[i]) #Menambahkan nilai fungsi yang berada di tengah-tengah interval (dikali 2 karena akan dijumlah dua kali).

    return jumlah * h/2 #Mengembalikan hasil integral numerik metode trapesium.

def pias(a, b, h, f):
    # Fungsi pias untuk menghitung integral numerik menggunakan metode pias (titik tengah).
    # Input: batas bawah a, batas atas b, lebar subinterval h, dan fungsi f.
    # Output: hasil integral numerik menggunakan metode pias.
    n = int((b - a) / h)
    nilai_x = [] # Inisialisasi list untuk menyimpan nilai titik-titik pada sumbu x.

    for i in range(0, n):
        nilai_x.append(a + ((i + 1/2) * h))  # Mengisi list nilai_x dengan titik-titik pada sumbu x sesuai dengan metode pias.

    for i in range(0,n):
        nilai_x.append(a + ((i+1/2) * h))

    jumlah=0
    for i in range(0, n):
        jumlah += f(nilai_x[i]) # Menghitung jumlah nilai fungsi pada titik-titik tengah interval.

    return jumlah * h  #Mengembalikan hasil integral numerik metode pias.

    return jumlah*h #Mengembalikan hasil integral numerik metode pias.

def simpson(a, b, h, f):
    #Fungsi simpson untuk menghitung integral numerik menggunakan metode Simpson 1/3.
    #Input: batas bawah a, batas atas b, lebar subinterval h, dan fungsi f.
    #Output: hasil integral numerik menggunakan metode Simpson 1/3.
    n = int((b - a) / h)
    nilai_x = [] #Inisialisasi list untuk menyimpan nilai titik-titik pada sumbu x.

    if n%2==0:
      for i in range(0,n+1):
          nilai_x.append(a + (i * h)) #Mengisi list nilai_x dengan titik-titik pada sumbu x sesuai dengan metode Simpson 1/3.

      jumlah=f(nilai_x[0]) + f(nilai_x[n])
      for i in range(1, n):
          if i%2 != 0:
            jumlah +=4*f(nilai_x[i])
          else:
            jumlah +=2*f(nilai_x[i]) # Menghitung jumlah nilai fungsi pada titik-titik interval sesuai dengan rumus Simpson 1/3.

      return jumlah*h/3 #Mengembalikan hasil integral numerik metode Simpson 1/3.
    else:
      return "tidak bisa menggunakan metode simpson 1/3 karena partisi berjumlah ganjil"


a = input("masukkan nilai a: ")
a = float(a)
b = input("masukkan nilai b: ")
b = float(b)
h = input("masukkan nilai h: ")
h = float(h)
fungsi = input("masukkan fungsi: ")

x = sp.symbols('x')
f = sp.sympify(fungsi)
f = sp.lambdify(x, f) #Membuat fungsi lambda dari ekspresi simbolik untuk evaluasi numerik.

hasil_integral1 = trapesium(a, b, h, f)
hasil_integral2 = pias(a,b,h,f)
hasil_integral3 = simpson(a, b, h, f)
print("Hasil integral dengan metode trapesium:", hasil_integral1)
print("Hasil integral dengan metode pias(titik tengah):", hasil_integral2)
print("Hasil integral dengan metode simpson 1/3:", hasil_integral3)