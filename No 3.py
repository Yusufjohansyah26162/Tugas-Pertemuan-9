kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

# Menghapus kata-kata yang memiliki panjang kurang dari lima karakter
kata = [k for k in kata if len(k) >= 5]

# Mengurutkan kata-kata secara alfabetis
kata.sort()

print(kata)
