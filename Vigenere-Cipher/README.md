# Tugas Praktikum Kriptografi - Pertemuan 3

**Nama:** GABRIELLA MARIE KEIRA WIBAWA  
**NPM:** 140810240086  
**Kelas:** Praktikum Kriptografi 2026  

---

## Struktur Direktori
- `Vigenere-Cipher/vigenerecipher.py`: Source code program enkripsi dan dekripsi menggunakan metode Vigenere Cipher.

## Penjelasan Alur Program (Vigenere Cipher)
Program `vigenerecipher.py` mengimplementasikan algoritma Vigenere Cipher klasik dengan bahasa pemrograman Python. Alur kerjanya adalah sebagai berikut:
1. **Pembersihan Input:** Program menerima input string dari user, kemudian menghapus semua spasi dan mengubah huruf menjadi kapital (uppercase) agar sesuai dengan metode Vigenere standard.
2. **Perulangan (Looping):** Program melakukan iterasi untuk setiap karakter pada teks yang diberikan.
3. **Konversi ASCII:** Karakter huruf diubah menjadi angka 0-25 dengan cara mengurangi nilai ASCII karakter tersebut dengan nilai ASCII huruf 'A'.
4. **Eksekusi Rumus:**
   - Untuk fungsi `vigenere_encrypt`, program menjalankan operasi $(P + K) \pmod{26}$.
   - Untuk fungsi `vigenere_decrypt`, program menjalankan operasi $(C - K) \pmod{26}$.
5. **Penyesuaian Index Key:** Index pada Key di-modulo dengan panjang key `(key_index % len(key))` sehingga key akan terus berulang menyesuaikan panjang teks.
6. **Output:** Angka hasil perhitungan dikembalikan menjadi karakter huruf dan digabungkan menjadi teks utuh.

