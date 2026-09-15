import math

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def mod_inverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def clean_text(text):
    return "".join([c.upper() for c in text if c.isalpha()])

def encrypt_hill(plaintext, K):
    plaintext = clean_text(plaintext)
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        p1 = char_to_num(plaintext[i])
        p2 = char_to_num(plaintext[i+1])
        c1 = (K[0][0] * p1 + K[0][1] * p2) % 26
        c2 = (K[1][0] * p1 + K[1][1] * p2) % 26
        ciphertext += num_to_char(c1) + num_to_char(c2)
    return ciphertext

def decrypt_hill(ciphertext, K):
    ciphertext = clean_text(ciphertext)
    det = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError(f"Determinan ({det}) tidak memiliki invers modulo 26! Kunci tidak valid.")
    
    # Invers Matriks 2x2 mod 26
    K_inv = [
        [(K[1][1] * det_inv) % 26, (-K[0][1] * det_inv) % 26],
        [(-K[1][0] * det_inv) % 26, (K[0][0] * det_inv) % 26]
    ]
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        c1 = char_to_num(ciphertext[i])
        c2 = char_to_num(ciphertext[i+1])
        p1 = (K_inv[0][0] * c1 + K_inv[0][1] * c2) % 26
        p2 = (K_inv[1][0] * c1 + K_inv[1][1] * c2) % 26
        plaintext += num_to_char(p1) + num_to_char(p2)
    return plaintext

def find_key(plaintext, ciphertext):
    plaintext = clean_text(plaintext)
    ciphertext = clean_text(ciphertext)
    if len(plaintext) < 4 or len(ciphertext) < 4:
        raise ValueError("Dibutuhkan minimal 4 karakter (2 blok) untuk mencari kunci 2x2!")

    # Matriks P dan C ordo 2x2
    p = [[char_to_num(plaintext[0]), char_to_num(plaintext[2])],
         [char_to_num(plaintext[1]), char_to_num(plaintext[3])]]
    c = [[char_to_num(ciphertext[0]), char_to_num(ciphertext[2])],
         [char_to_num(ciphertext[1]), char_to_num(ciphertext[3])]]
    
    det = (p[0][0] * p[1][1] - p[0][1] * p[1][0]) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return None
        
    p_inv = [
        [(p[1][1] * det_inv) % 26, (-p[0][1] * det_inv) % 26],
        [(-p[1][0] * det_inv) % 26, (p[0][0] * det_inv) % 26]
    ]
    
    K = [
        [(c[0][0]*p_inv[0][0] + c[0][1]*p_inv[1][0]) % 26, (c[0][0]*p_inv[0][1] + c[0][1]*p_inv[1][1]) % 26],
        [(c[1][0]*p_inv[0][0] + c[1][1]*p_inv[1][0]) % 26, (c[1][0]*p_inv[0][1] + c[1][1]*p_inv[1][1]) % 26]
    ]
    return K

def input_matrix():
    print("Masukkan elemen matriks kunci 2x2:")
    k11 = int(input("  Baris 1 Kolom 1: "))
    k12 = int(input("  Baris 1 Kolom 2: "))
    k21 = int(input("  Baris 2 Kolom 1: "))
    k22 = int(input("  Baris 2 Kolom 2: "))
    return [[k11, k12], [k21, k22]]

def main():
    while True:
        print("\n=== PROGRAM HILL CIPHER (2x2) ===")
        print("1. Enkripsi Teks")
        print("2. Dekripsi Teks")
        print("3. Cari Kunci (Known-Plaintext Attack)")
        print("4. Jalankan Tes Otomatis (Demo Slide)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            pt = input("Masukkan Plaintext: ")
            K = input_matrix()
            try:
                hasil = encrypt_hill(pt, K)
                print(f"\n-> Hasil Ciphertext: {hasil}")
            except Exception as e:
                print(f"Error: {e}")

        elif pilihan == '2':
            ct = input("Masukkan Ciphertext: ")
            K = input_matrix()
            try:
                hasil = decrypt_hill(ct, K)
                print(f"\n-> Hasil Plaintext: {hasil}")
            except Exception as e:
                print(f"Error: {e}")

        elif pilihan == '3':
            pt = input("Masukkan Plaintext (min 4 huruf): ")
            ct = input("Masukkan Ciphertext (min 4 huruf): ")
            try:
                K = find_key(pt, ct)
                if K:
                    print("\n-> Matriks Kunci yang ditemukan:")
                    print(f"[{K[0][0]}, {K[0][1]}]")
                    print(f"[{K[1][0]}, {K[1][1]}]")
                else:
                    print("Gagal: Determinan matriks plaintext tidak koprima dengan 26.")
            except Exception as e:
                print(f"Error: {e}")

        elif pilihan == '4':
            print("\n--- Uji Soal Latihan & Slide ---")
            K_test = [[7, 6], [2, 5]]
            pt_test = "MAGANG"
            ct_test = encrypt_hill(pt_test, K_test)
            dt_test = decrypt_hill(ct_test, K_test)
            print(f"1. Enkripsi '{pt_test}' K=[[7,6],[2,5]] -> {ct_test}")
            print(f"2. Dekripsi '{ct_test}' -> {dt_test}")
            
            K_found = find_key("FRIDAY", "PQCFKU")
            print(f"3. Cari Kunci dari FRIDAY -> PQCFKU: {K_found}")

        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()