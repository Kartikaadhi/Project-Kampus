Vending Machine

A. Deskripsi
Program ini adalah simulasi mesin penjual otomatis (vending machine) yang menggunakan Deterministic Finite Automaton (DFA) untuk memproses transaksi pembelian minuman.

B. Fitur
- Menjual tiga jenis minuman: 
  - Minuman A (Rp3.000)
  - Minuman B (Rp4.000)
  - Minuman C (Rp6.000)
- Menerima uang pecahan Rp1.000, Rp2.000, Rp5.000, dan Rp10.000.
- Menampilkan minuman yang dapat dibeli berdasarkan jumlah uang yang dimasukkan.
- Memiliki fitur penukaran uang, di mana uang Rp2.000, Rp5.000, atau Rp10.000
 dapat ditukarkan ke pecahan Rp1000
- Menghitung dan menampilkan kembalian jika uang yang dimasukkan lebih dari harga minuman.

C. Struktur Proyek
- `Vending Machine.py`: Skrip utama yang menjalankan mesin penjual otomatis.
- `vending_dfa.txt`: File konfigurasi yang mendefinisikan automata untuk mesin penjual otomatis.

D. Cara Menjalankan Program

1. Pastikan Python terinstal di komputer.
2. Simpan file `Vending Machine.py` dan `vending_dfa.txt` dalam satu folder.
3. Buka terminal atau command prompt.
4. Navigasikan ke folder tempat file disimpan.
5. Jalankan program dengan perintah:

   python "Vending Machine.py"

Atau gunakan path lengkap ke executable Python:

Misalkan :
& "C:\Users\Asus\AppData\Local\Programs\Python\Python313\python.exe" "Vending Machine.py"

Jika menggunakan terminal VSCode.

6. Setelah program berjalan, akan diminta untuk memasukkan uang atau memilih opsi untuk membeli minuman.
7. Inputkan sesuai perintah
8. Maka akan menghasilkan output dari program

file .exe, dapat dijakankan di sistem Windows tanpa perlu menginstal Python atau dependensi lainnya. Letak file .exe berada didalam folder dist dan untuk code program `Vending Machine.py` berada di folder Vending bersama file `vending_dfa.txt` nya.
