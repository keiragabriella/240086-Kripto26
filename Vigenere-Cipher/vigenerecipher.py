def vigenere_encrypt(plaintext, key):
    # Menghapus spasi dan mengubah ke huruf kapital
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Konversi huruf ke angka (0-25)
            p = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            
            # Rumus Enkripsi: C = (P + K) mod 26
            c = (p + k) % 26
            
            # Konversi kembali ke huruf dan tambahkan ke ciphertext
            ciphertext += chr(c + ord('A'))
            key_index += 1
        else:
            # Jika bukan huruf, tambahkan karakter asli
            ciphertext += char
            
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    # Menghapus spasi dan mengubah ke huruf kapital
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Konversi huruf ke angka (0-25)
            c = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            
            # Rumus Dekripsi: P = (C - K) mod 26
            p = (c - k) % 26
            
            # Konversi kembali ke huruf dan tambahkan ke plaintext
            plaintext += chr(p + ord('A'))
            key_index += 1
        else:
            # Jika bukan huruf, tambahkan karakter asli
            plaintext += char
            
    return plaintext

# --- Bagian Main Program ---
if __name__ == "__main__":
    print("=== PROGRAM VIGENERE CIPHER ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == '1':
        pt = input("Masukkan Plaintext: ")
        key = input("Masukkan Key: ")
        hasil = vigenere_encrypt(pt, key)
        print(f"\n[+] Hasil Ciphertext: {hasil}")
        
    elif pilihan == '2':
        ct = input("Masukkan Ciphertext: ")
        key = input("Masukkan Key: ")
        hasil = vigenere_decrypt(ct, key)
        print(f"\n[+] Hasil Plaintext: {hasil}")
        
    else:
        print("Pilihan tidak valid!")