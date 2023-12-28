import numpy as np # Import modul NumPy untuk manipulasi matriks dan vektor secara efisien.

# Fungsi untuk menghitung turunan maju suatu fungsi pada suatu titik x dengan langkah h:
def turunan_maju(fungsi, x, h):
    turunan = (fungsi(x + h) - fungsi(x)) / h
    return turunan

# Fungsi untuk menghitung turunan mundur suatu fungsi pada suatu titik x dengan langkah h:
def turunan_mundur(fungsi, x, h):
    turunan = (fungsi(x) - fungsi(x - h)) / h
    return turunan

# Fungsi untuk menghitung turunan tengah suatu fungsi pada suatu titik x dengan langkah h:
def turunan_tengah(fungsi, x, h):
    turunan = (fungsi(x + h) - fungsi(x - h)) / (2 * h)
    return turunan

# Input fungsi dari pengguna
fungsi_input = input("Masukkan fungsi: ")
fungsi = lambda x: eval(fungsi_input)

# Input nilai x dari pengguna sebagai array
x_array_input = input("Masukkan nilai x: ")
x_array = np.array([float(x) for x in x_array_input.split(',')])

# Input nilai h dari pengguna
h_input = float(input("Masukkan jarah dari nilai x: "))

# Hitung turunan pertama untuk setiap nilai x dalam array menggunakan ketiga metode
turunan_maju_array = np.vectorize(lambda x: turunan_maju(fungsi, x, h_input))(x_array[1:])  # elemen pertama tidak menggunakan turunan mundur
turunan_mundur_array = np.vectorize(lambda x: turunan_mundur(fungsi, x, h_input))(x_array[:-1])  # elemen terakhir tidak menggunakan turunan maju
turunan_tengah_array = np.vectorize(lambda x: turunan_tengah(fungsi, x, h_input))(x_array[1:-1])  # elemen pertama dan terakhir tidak diikutsertakan

# Tampilkan hasil
print(f"\nFungsi: {fungsi_input}")
print(f"Nilai x: {x_array}")
print(f"Nilai h: {h_input}")
print("\nTurunan Pertama (Maju):", turunan_maju_array)
print("Turunan Pertama (Mundur):", turunan_mundur_array)
print("Turunan Pertama (Tengah):", turunan_tengah_array)
