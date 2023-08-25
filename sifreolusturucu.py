import random
import string

def sifre_olustur(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    desired_length = int(input("Şifre uzunluğunu girin: "))
    if desired_length <= 0:
        print("Geçerli bir pozitif uzunluk giriniz.")
    else:
        password = sifre_olustur(desired_length)
        print("Oluşturulan şifre:", password)
except ValueError:
    print("Geçerli bir sayı girmelisiniz.")
