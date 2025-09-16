# Ao Eleven ⚽✨

Halo👀!  
Ini adalah repositori untuk project Ao Eleven, sebuah aplikasi web bertemakan football shop berbasis Django.  
Dibuat oleh Andi Hakim Himawan (NPM: 2406495792) dari kelas PBP-D Fasilkom UI.  

🔗 Link Deployment:https://andi-hakim42-aoeleven.pbp.cs.ui.ac.id/

---

## 🚀 Cara Deploy Secara Lokal

Kalau mau jalanin project ini di komputer sendiri, ikuti langkah-langkah ini:

1. **Clone repository**
   ```bash
   git clone https://github.com/username/Ao-Eleven.git
   cd Ao-Eleven

2. **Buat virtual environment**

   ```bash
   python -m venv .venv
   ```

3. **Aktifkan virtual environment**

   * Windows:

     ```bash
     .venv\Scripts\activate
     ```
   * Mac/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan migrasi database**

   ```bash
   python manage.py migrate
   ```

6. **Jalankan server**

   ```bash
   python manage.py runserver
   ```

7. Buka browser dan akses:

   ```
   http://127.0.0.1:8000/
   ```

---
# TUGAS 2 - Implementasi Model-View-Template (MVT) pada Django
---
## 📊 Bagan Alur Request & Response Django
![yg bener](https://github.com/user-attachments/assets/cc488d9c-dbf9-43b7-8271-efd3655719b8)


## ⚙️ Peran `settings.py`
settings.py berfungsi sebagai pusat konfigurasi di Django. Di dalamnya terdapat pengaturan database, daftar aplikasi yang dipakai, middleware, hingga lokasi file statis dan template. Tanpa file ini, Django tidak akan tahu harus menggunakan database apa, aplikasi mana yang aktif, serta di mana mencari berkas HTML dan aset pendukung lainnya.

---

## 🗄️ Cara Kerja Migrasi Database di Django

1. Kita bikin/ubah `models.py`.
2. Jalankan:

   ```bash
   python manage.py makemigrations
   ```

   → Django bikin file migrasi (instruksi perubahan database).
3. Jalankan:

   ```bash
   python manage.py migrate
   ```

   → Django eksekusi instruksi itu ke database (buat tabel, ubah field, dll).

Migrasi ini bikin database tetap sinkron sama kode yang ada.

---

## ❓ Kenapa Django Cocok Jadi Framework Pertama?
Django cocok dijadikan framework pertama karena sifatnya yang sudah lengkap sejak awal. Fitur penting seperti autentikasi, admin panel, dan keamanan sudah tersedia tanpa harus membangun dari nol. Dokumentasinya jelas dan komunitasnya luas, sehingga memudahkan proses belajar. Selain itu, dengan konsep MVT yang terstruktur, mahasiswa dapat memahami alur pengembangan web dengan lebih cepat, sekaligus mendapatkan pengalaman yang relevan untuk kebutuhan industri.
Maka dari itu Django sering dipilih sebagai framework pertama buat belajar pengembangan web dan software.

---
## 👩‍🏫 Feedback untuk asisten dosen Tutorial 1
Pada saat sesi tutorial 1 di minggu ke-dua, asisten dosen sudah sangat baik dalam menjelaskan dan membantu mahasiswa saat ada masalah ketika mengerjakan tutorial 1. Jadi menurut saya sudah cukup baik.

---
## 📌 Ringkasan Alur Pengerjaan Tugas 2

1. **Inisialisasi Project & App**
   - Membuat project Django `AoEleven` dan app `main`.
   - Setup virtual environment, install Django, dan commit awal ke Git.

2. **Membuat Model**
   - Menambahkan model `Product` di `main/models.py` dengan field seperti `name`, `price`, `description`, `thumbnail`, `category`, `stock`, `brand`, dan `rating`.
   - Mendaftarkan app ke `INSTALLED_APPS` di `settings.py`.

3. **Migrasi Database**
   - Menjalankan `makemigrations` dan `migrate` agar Django otomatis membuat tabel sesuai model.

4. **Membuat Views**
   - `home` untuk menampilkan daftar produk.

5. **Routing**
   - Konfigurasi `urls.py` di project untuk include `main/urls.py`.
   - Mapping URL ke views sesuai kebutuhan.

6. **Membuat Template**
   - Menyimpan HTML di `main/templates/main/`.
   - Membuat `home.html` untuk menampilkan halaman utama dan daftar produk 

7. **Menambahkan Static Files**
   - Setup `STATIC_URL` dan `STATIC_ROOT` di `settings.py`.

8. **Deploy ke PWS**
   - Membuat `requirements.txt` yang mencantumkan `Django` dan `gunicorn`.
   - Membuat `Procfile` dengan perintah `gunicorn configure.wsgi:application`.(Terjadi error dan saya mencari solusi)
   - Push repository ke PWS hingga build berjalan otomatis.

9. **Mengatasi Masalah**
   - `TemplateDoesNotExist`: memindahkan template ke folder `main/templates/main/`.
   - `ImportError`: memperbaiki import di `urls.py`.
   - `gunicorn not found`: menambahkan `gunicorn` di `requirements.txt`.

10. **Hasil Akhir**
    - Aplikasi berhasil di-deploy ke PWS.
    - Halaman home menampilkan daftar produk.(belum di tugas 2)

---

# TUGAS 3 - Implementasi Form dan Data Delivery pada Django

---
