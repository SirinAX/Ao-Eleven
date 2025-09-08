# Ao Eleven ⚽✨

Halo👀!  
Ini adalah repositori untuk project Ao Eleven, sebuah aplikasi web sederhana bertemakan football shop berbasis Django.  
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

## 📊 Bagan Alur Request & Response Django
![yg bener](https://github.com/user-attachments/assets/cc488d9c-dbf9-43b7-8271-efd3655719b8)


## ⚙️ Peran `settings.py`

File `settings.py` itu semacam pusat konfigurasinya Django.
Isinya antara lain:

* Info database (pakai SQLite, PostgreSQL, dll).
* Installed apps (app apa aja yang dipakai di project).
* Middleware (alat bantu seperti keamanan & session).
* Konfigurasi static file & template.

Tanpa file ini, Django nggak tau harus connect ke database mana, app apa yang aktif, atau nyari template di folder mana.

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

* Django itu *“batteries included”* → banyak fitur penting udah ada (login, admin panel, keamanan).
* Dokumentasi jelas & komunitasnya besar.
* Konsep MVC/MVT bikin gampang belajar alur aplikasi web.
* Sangat relevan dipakai di industri, jadi ilmunya bisa langsung kepake.

Makanya Django sering dipilih sebagai framework pertama buat belajar pengembangan web dan software.

---
## 📌 Ringkasan Alur Pengerjaan

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
   - Membuat `home.html` untuk daftar produk dan `product_detail.html` untuk detail produk.( fitur buat nanti)

7. **Menambahkan Static Files**
   - Setup `STATIC_URL` dan `STATIC_ROOT` di `settings.py`.

8. **Deploy ke PWS**
   - Membuat `requirements.txt` yang mencantumkan `Django` dan `gunicorn`.
   - Membuat `Procfile` dengan perintah `gunicorn configure.wsgi:application`.
   - Push repository ke PWS hingga build berjalan otomatis.

9. **Mengatasi Masalah**
   - `TemplateDoesNotExist`: memindahkan template ke folder `main/templates/main/`.
   - `ImportError`: memperbaiki import di `urls.py`.
   - `gunicorn not found`: menambahkan `gunicorn` di `requirements.txt`.

10. **Hasil Akhir**
    - Aplikasi berhasil di-deploy ke PWS.
    - Halaman home menampilkan daftar produk.(belum)

---
