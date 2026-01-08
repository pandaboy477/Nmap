How to run this program? Just copy this command 
```bash
python3 Nmap.py
```

if you find this "Add custom Nmap options (space-separated):" in the custom menu in Nmap, just fill in with this prompt

Prompt yang digunakan untuk scanning Nmap selain script ini antara lain:

1. **Pemindaian port dan layanan**:
   - `-p-`: Memindai semua port (default).
   - `-p 80,443`: Memindai port tertentu.
   - `-sS`: Pemindaian TCP SYN (stealth).
   - `-sU`: Pemindaian UDP.
   - `-sV`: Deteksi versi layanan.
   - `-sC`: Jalankan skrip default Nmap.

2. **Deteksi sistem operasi**:
   - `-O`: Deteksi OS.
   - `--osscan-guess`: Tebak OS jika tidak pasti.

3. **Pengaturan waktu eksekusi**:
   - `-T0-T5`: Atur kecepatan eksekusi (paranoid-histeris).
   - `-T3`: Waktu normal.

4. **Skrip Nmap tambahan**:
   - `--script=exploit`: Jalankan skrip eksploitasi.
   - `--script=discovery`: Jalankan skrip penemuan.
   - `--script=vuln`: Jalankan skrip deteksi kerentanan.

5. **Output dan log**:
   - `-oX`: Simpan hasil dalam XML.
   - `-oN`: Simpan hasil dalam teks biasa.
   - `-oG`: Simpan hasil dalam format greppable.

6. **Lain-lain**:
   - `-Pn`: Nonaktifkan ping host.
   - `-f`: Fragmentasi paket.
   - `-v`: Verbose mode.
   - `-n`: Nonaktifkan resolusi DNS.

example of use:
Add custom Nmap options (space-separated): -Pn
