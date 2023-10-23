import numpy as np

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

# Fungsi pertama: f(x) = x^3 - 2x + 1
f1 = lambda x: x**3 - 2*x + 1
root1 = bisection(f1, -2, 2, 0.001)
print("Akar pertama =", root1)
print("f(root1) =", f1(root1))

# Fungsi kedua: f(x) = e^x - x
f2 = lambda x: np.exp(x) - x
root2 = bisection(f2, 0, 1, 0.001)
print("Akar kedua =", root2)
print("f(root2) =", f2(root2))