import random

# START dengan fungsi
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
# END dengan fungsi

def penjumlahan(angka1, angka2):
    hasil_penjumlahan = angka1 + angka2
    return hasil_penjumlahan
    
def pengurangan(angka1, angka2):
    hasil_pengurangan = angka1 - angka2
    return hasil_pengurangan

def perkalian(angka1, angka2):
    hasil_perkalian = angka1 * angka2
    return hasil_perkalian