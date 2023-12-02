a = 5
b = 2

#operasi penjumlahan
hasil = a + b
print(a, ' + ', b, ' = ', hasil )
#operasi perkalian
hasil = a * b
print(a, ' x ', b, ' = ', hasil )
#operasi pengurangan
hasil = a - b
print(a, ' - ', b, ' = ', hasil )
#operasi pembagian
hasil = a / b
print(a, ' / ', b, ' = ', hasil )
#operasi eksponen(pangkat)
hasil = a ** b
print(a, ' ** ', b, ' = ', hasil )
#operasi modulus
hasil = a % b
print(a, ' % ', b, ' = ', hasil )
#operasi floor division
hasil = a // b
print(a, ' // ', b, ' = ', hasil )

#prioritas operasi, operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(hasil)