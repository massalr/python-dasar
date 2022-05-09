# a = 10, a adalah variable dengan nilai 10

# tipe data angka satuan (integer)
data_integer = 1
print(f"data : {data_integer} bertipe", type(data_integer))

# tipe data angka dengan koma (float)
data_float = 1.5
print(f"data : {data_float} bertipe", type(data_float))

# tipe data string atau kumpulan karakter (string)
data_string = "ini string"
print(f"data : {data_string} bertipe", type(data_string))

# tipe data biner true/false (boolean)
data_bool = True
print(f"data : {data_bool} bertipe", type(data_bool))

# tipe data complex
data_complex = complex(5,6)
print(f"data : {data_complex} bertipe", type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(11.3)
print(f"data : {data_c_double} bertipe", type(data_c_double))