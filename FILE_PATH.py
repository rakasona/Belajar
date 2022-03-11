# SET FILE PATH IN PYTHON
"""
1. Gunakan \ Karakter untuk Menentukan Jalur File dengan Python
2. Gunakan Literal String Mentah untuk Menentukan Jalur File dengan Python
3. Gunakan Fungsi os.path() untuk Menentukan Jalur File dengan Python
4. Gunakan Fungsi pathlib.Path() untuk Menentukan Jalur File dengan Python

Sebagian besar kami disediakan dengan variabel path default ketika kami menginstal Python. Namun terkadang, kita harus mengatur variabel-variabel ini secara manual, atau jika kita ingin mengatur jalur yang berbeda, kita harus melakukannya secara manual. Untuk menjalankan file yang disimpan di direktori kami, kami harus menyediakan path lengkap ke editor.

Jalur biasanya berupa string seperti C:\Folder. Tetapi dalam Python, karakter \ bisa ditafsirkan sebagai karakter pelarian.

Tutorial ini akan membahas cara mengatur path untuk file dengan Python di perangkat Windows."""

# USE THE \ CHARACTER TO SPECIFY THE FILE PATH IN PYTHON
"""Kita dapat menggunakan karakter \\ sebagai pengganti satu \ untuk menyediakan path dengan Python.

Sintaks untuk ini ditunjukkan di bawah ini.
'C:\\Directory\\File'"""

# USE THE RAW STRING LITERALS TO SPECIFY THE FILE PATH IN PYTHON
"""Kita dapat menggunakan literal string mentah untuk menyediakan jalur bagi file karena string mentah akan memperlakukan garis miring terbalik ini sebagai karakter literal.

Untuk membuat string mentah, kita harus menulis karakter r sebelum tanda kutip untuk string tersebut.

Sintaks untuk menggunakan literal string mentah ditunjukkan di bawah ini.
r'C:\Directory'"""

# USE THE OS.PATH() FUNCTION TO SPECIFY THE FILE PATH IN PYTHON
"""Kita juga dapat menggunakan fungsi path() dari modul os untuk menyiapkan path. Keuntungan menggunakan fungsi path() adalah kita tidak menentukan path lengkap file. Kita harus memberikan nama direktori dan nama file.


Metode ini sendiri akan memilih konfigurasi yang benar untuk OS yang Anda gunakan pada perangkat Anda. Kita harus menggunakan fungsi join() untuk menggabungkan direktori dan nama file.

Sebagai contoh,"""

from pathlib import path import os 
print(os.path.join('C:',os.sep,"Users"))

# USE THE PATHLIB.PATH() FUNCTION TO SPECIFY THE FILE PATH IN PYTHON
"""Dalam Python 3.4 dan di atasnya, kita dapat menggunakan fungsi Path() dari modul pathlib untuk menentukan path file dengan Python. Penggunaannya mirip dengan fungsi os.path().

Lihat kode di bawah ini."""

print(Pay=th('C:', '/', 'Users'))
