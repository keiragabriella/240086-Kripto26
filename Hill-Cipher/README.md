# Hill Cipher Implementation (Tugas Praktikum Kriptografi)

**Nama:** GABRIELLA MARIE KEIRA WIBAWA  
**NPM:** 140810240086  
**Kelas:** Praktikum Kriptografi 2026  

---

## Deskripsi Program
Program ini merupakan implementasi algoritma kriptografi klasik **Hill Cipher (Ordo 2x2)** menggunakan bahasa pemrograman **Python**. 

Program mendukung 3 fitur utama:
1. **Enkripsi**: Mengonversi plainteks menjadi cipherteks menggunakan perkalian matriks modulo 26:
   $$C = (K \times P) \pmod{26}$$
2. **Dekripsi**: Mengembalikan cipherteks menjadi plainteks menggunakan invers matriks kunci modulo 26:
   $$P = (K^{-1} \times C) \pmod{26}$$
3. **Mencari Kunci (*Known-Plaintext Attack*)**: Menemukan matriks kunci $K$ jika diketahui pasangan minimal 4 karakter plainteks dan cipherteks:
   $$K = (C \times P^{-1}) \pmod{26}$$

---

## Alur Kerja Program

### 1. Tahap Enkripsi
- Mengubah teks menjadi huruf kapital dan membuang karakter non-alfabet.
- Jika panjang teks ganjil, ditambahkan karakter padding `'X'` di akhir teks.
- Teks dikelompokkan ke dalam blok matriks berukuran $2 \times 1$.
- Setiap blok dikalikan dengan matriks kunci $K$ lalu di-modulo 26 untuk menghasilkan cipherteks.

### 2. Tahap Dekripsi
- Menghitung nilai determinan kunci: $\det(K) = (ad - bc) \pmod{26}$.
- Mencari invers determinan modulo 26 ($\gcd(\det(K), 26) = 1$).
- Membentuk matriks kunci invers ($K^{-1}$) dengan rumus adjoin.
- Mengalikan setiap blok cipherteks dengan $K^{-1}$ lalu di-modulo 26.

### 3. Tahap Mencari Kunci
- Mengambil 2 blok pertama (4 karakter) dari plainteks dan cipherteks untuk menyusun matriks $P$ dan $C$ berukuran $2 \times 2$.
- Menghitung invers dari matriks plainteks ($P^{-1} \pmod{26}$).
- Menghitung matriks kunci $K = C \times P^{-1} \pmod{26}$.

---

## Cara Menjalankan Program

1. Masuk ke direktori `Hill-Cipher`:
   ```bash
   cd Hill-Cipher