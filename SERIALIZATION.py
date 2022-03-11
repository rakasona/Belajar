# PYTHON SERIALIZATION
# WHAT IS SERIALIZATION IN PYTHON?
"""Seperti dikatakan di atas, serialisasi adalah proses mengubah data ke dalam bentuk, aliran byte, di mana data dapat disimpan. Proses ini juga disebut pickling atau flattening atau marshaling. Dan proses kebalikan dari mengubah aliran byte menjadi bentuk objek disebut deserialization atau unpickling. """
"""Untuk tujuan ini, Python menyediakan tiga modul berikut:
1. Pickle Module
2. JSON Module
3. Marshal Module
Artikel ini terutama membahas modul Pickle yang secara operasional merupakan cara paling sederhana untuk menyimpan data kompleks dalam bentuk khusus."""


"""Pickle adalah modul dalam Python untuk membuat serial dan deserializing. Ini adalah pilihan yang lebih cepat dan sederhana untuk tujuan ini jika kita tidak memerlukan format yang dapat dibaca manusia. Untuk menggunakan ini kita harus terlebih dahulu mengimpor menggunakan perintah berikut."""


# PYTHON PICKLE INTERFACES
"""Modul pickle berisi konstanta berikut:

1. pickle.HIGHEST_PROTOCOL: Ini adalah bilangan bulat yang mewakili versi protokol tertinggi yang tersedia. Ini adalah nilai protokol yang umumnya diteruskan ke fungsi yang digunakan untuk pengawetan dan penguraian.

2. pickle.DEFAULT_PROTOCOL: Ini adalah bilangan bulat yang mewakili protokol default yang digunakan untuk pengawetan. Nilai ini mungkin kurang dari nilai protokol tertinggi.

Kita dapat menemukan nilai-nilai ini dengan cara yang ditunjukkan pada contoh di bawah ini.
Contoh pendanaan konstanta modul pickle: """

import pickle
import pickle
print("highest protocol")
pickle.highest_PROTOCOL)
print("Default protocol")
pickle.DEFAULT_PROTOCOL
# PICKLE MODULE IN PYTHON


"""Modul ini menyediakan empat metode berikut:

1. dump(): Metode ini digunakan untuk membuat serial ke objek file yang terbuka
2. dumps(): Metode ini digunakan untuk membuat serial ke string
3. load(): Metode ini deserializes dari objek seperti terbuka.
4. load(): Ini melakukan deserialization dari string.

Kami akan membahas masing-masing metode ini di bagian selanjutnya."""

# PYTHON DUMP FUNCTIONS
"""Seperti dikatakan di atas, fungsi dump digunakan untuk menulis versi objek yang diawetkan ke dalam file. Sintaks dari fungsi ini adalah:

pickle.dump(obj, file, protokol = Tidak ada, *, fix_imports = Benar)

1. Obj adalah objek yang akan diserialkan

2. File adalah nama file tempat hasil konversi akan disimpan

3. Protokol argumen opsional mendefinisikan protokol yang akan digunakan saat memproses objek. Kami dapat memberikan versi apa pun dari 0 hingga HIGHEST_PROTOCOL. Jika tidak disebutkan, protokol default digunakan.

4. Jika fix_imports adalah True dan protokolnya kurang dari 3, maka pemetaan dilakukan dari nama Python 3 baru ke nama modul lama yang digunakan di Python 2. Ini memungkinkan aliran data acar dapat dibaca dengan versi Python 2."""

content='PythonGeeks'
f = open('file.txt','wb') #opened the file in write and binary mode
#dumping the content in the variable 'content into the file pickle.dump(content.f)
f.close() #closing file

# PYTHON DUMPS FUNCTION
"""This function returns the pickled representation of the given data in bytes object form. The syntax of the function is : 

pickle.dumps(obj, protocol = None, *, fix_imports = True)

This syntax is similar to the dump() function, except we do not have a file argument here."""

content = [{'a':1,'b':2,'c':3.0}]
pickle.dumps(content)#dumping the content in the variable


# PYTHON LOAD FUNCTION
"""Fungsi ini digunakan untuk membaca informasi dalam bentuk yang diambil dari file dan merekonstruksinya ke dalam bentuk aslinya. Sintaks dari fungsi ini adalah:

pickle.load(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”) 

Fungsi ini mengambil file dari mana data harus dibaca. Argumen lain bersifat opsional dan memiliki nilai default. Mari kita lihat contoh membaca data yang kita simpan di contoh fungsi dump(). """



# PYTHON LOADS FUNCTION
"""Fungsi ini digunakan untuk membaca representasi acar dari suatu objek dan mengembalikan versi yang direkonstruksi. Sintaksnya adalah:

pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”) 

Ini mirip dengan fungsi dumps() kecuali bahwa di sini kita melewatkan objek byte daripada objek normal. """



# EXCEPTIONS IN PYTHON PICKLE
"""Ada tiga pengecualian penting dalam Pickle yang perlu kita ketahui dan ini adalah:

1. pengecualian pickle.PickleError: Pengecualian ini mewarisi dari Pengecualian. Ini adalah kelas induk untuk semua pengecualian lain yang diangkat dalam modul ini.

2. pengecualian pickle.PicklingError: Pengecualian ini mewarisi dari PickleError. Ketika Pickler menemukan objek yang tidak dapat diawetkan, itu menimbulkan kesalahan ini.

3. exception pickle.UnpicklingError: Pengecualian ini juga diturunkan dari PickleError. Ini muncul ketika masalah seperti korupsi data atau pelanggaran keamanan terjadi saat membongkar objek.

Beberapa eksekusi lainnya termasuk:
1. EOFError
2. TypeError
3. ValueError
4. AttributeError
5. ImportError
6. IndexError"""
