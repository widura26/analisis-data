# inputUser = float(input("masukkan anagka yang bernilai\ndari 3\natau\nlebih besar dari 10\n"))

# isKurangDari = (inputUser < 3)
# print("Kurang dari 3 =", isKurangDari)

# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 =", isLebihDari)

# isCorrect = isKurangDari or isLebihDari
# print("angka yang anda masukkan: ", isCorrect) 

#kasus irisan
inputUser = float(input("masukkan angka yang bernilai : \n"))
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect) 