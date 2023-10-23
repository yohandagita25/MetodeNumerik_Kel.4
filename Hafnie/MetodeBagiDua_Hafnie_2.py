import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, e, max_iterations=100):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    for i in range(max_iterations):
        m = (a + b) / 2
        if np.abs(f(m)) < e:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m
    
    raise Exception('Metode Bagi Dua tidak konvergen dalam jumlah iterasi yang ditentukan')

# Input fungsi dari pengguna
expression = input("Masukkan fungsi (gunakan x sebagai variabel): ")
f = lambda x: eval(expression)

# Input batas akar dari pengguna
a = float(input("Masukkan batas awal a: "))
b = float(input("Masukkan batas akhir b: "))

# Input galat dari pengguna
e = float(input("Masukkan galat (contoh: 0.001): "))

# Input jumlah iterasi maksimal dari pengguna
max_iter = int(input("Masukkan jumlah iterasi maksimal: "))

try:
    root = bisection(f, a, b, e, max_iterations=max_iter)
    print("Akar =", root)
    print("f(Akar) =", f(root))
    
    # Membuat grafik akar
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='red', linestyle='--', label='f(x)=0')
    plt.scatter(root, f(root), color='green', label='Akar')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik Fungsi dan Akar')
    plt.grid()
    plt.show()

except Exception as e:
    print(e)
