#konversi / casting data

data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0

print("---int---")
print("Angka int : ", data_int)

print("float = ", data_float)
print("string = ", data_str)
print("bool = ", data_bool)

#float
data_float = 9.9
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("---float---")
print("Angka Float : ", data_float)
print("int = ", data_int);
print("string = ", data_str);
print("bool = ", data_bool);

#boolean
data_boolean = True
data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = float(data_boolean)

print("---boolean---")
print("boolean : ", data_boolean)
print("int = ", data_int);
print("string = ", data_str);
print("float = ", data_float);

#string
data_string = "Halo"
data_int = int(data_string)
data_bool = str(data_string)
data_float = float(data_string)

print("---string---")
print("string : ", data_string)
print("int = ", data_int);
print("bool = ", data_bool);
print("float = ", data_float);