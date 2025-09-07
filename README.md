
````markdown
# Ao Eleven ⚽✨

Halo!  
Ini adalah repositori untuk project **Ao Eleven**, sebuah aplikasi web sederhana bertemakan **Football Shop** berbasis **Django**.  
Project ini dibuat oleh **Andi Hakim Himawan** dari kelas **PBP-D Fasilkom UI** dengan **NPM: 2406495792**.  

🔗 **Link Aplikasi:** [Klik di sini untuk coba Ao Eleven](https://andi-hakim42-aoeleven.pbp.cs.ui.ac.id/)

---

## 🚀 Cara Deploy Secara Lokal

Kalau mau jalanin project ini di local komputer kamu, langkah-langkahnya:

1. **Clone repository**
   ```bash
   git clone https://github.com/username/Ao-Eleven.git
   cd Ao-Eleven
````

2. **Buat dan aktifkan virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Lakukan migrasi database**

   ```bash
   python manage.py migrate
   ```

5. **(Opsional) Buat superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Jalankan server**

   ```bash
   python manage.py runserver
   ```

7. **Akses aplikasi di browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📌 Step-by-Step Implementasi

1. **Setup Project Django**

   * Inisialisasi environment dan install Django.
   * Buat project `AoEleven` dan aplikasi `main`.

2. **Membuat Model**

   * Tambah model `Product` di `main/models.py` untuk menyimpan data produk.
   * Daftarkan `main` ke `INSTALLED_APPS` di `settings.py`.

3. **Migrasi Database**

   * Jalankan `makemigrations` lalu `migrate` untuk membuat tabel otomatis sesuai model.

4. **Membuat Views & Template**

   * `views.py` digunakan untuk ambil data dari model.
   * Buat template HTML di folder `templates` untuk menampilkan data produk.

5. **Mengatur URL**

   * Di `urls.py`, mapping URL agar request dari user diarahkan ke views yang sesuai.

6. **Deploy ke PWS**

   * Push repo dengan `requirements.txt` dan `Procfile`.
   * Hubungkan repo ke PWS, build otomatis jalan → aplikasi langsung online.

---

## ⚙️ Peran `settings.py`

File ini pusat konfigurasi Django.
Isinya antara lain:

* `INSTALLED_APPS` → aplikasi yang digunakan.
* `DATABASES` → konfigurasi database.
* `TEMPLATES` → letak file HTML.
* `STATICFILES_DIRS` → file statis (CSS, JS, gambar).
* `SECRET_KEY` & `DEBUG` → keamanan & mode development.

---

## 🗂️ Cara Kerja Migrasi Database

Migrasi adalah cara Django menyinkronkan **model Python** ke **database**:

* `makemigrations` → bikin file perubahan (migration file).
* `migrate` → eksekusi perubahan ke database.

Dengan migrasi, kita tidak perlu bikin tabel SQL manual — Django otomatis generate berdasarkan model.

---

## 🎯 Kenapa Django Dipilih?

* **All-in-one**: sudah ada admin panel, autentikasi, ORM, templating, sampai proteksi keamanan.
* **Cocok buat belajar**: konsep jelas tapi tetap powerful.
* **DRY Principle**: kode lebih rapi dan gampang dirawat.
* **Komunitas besar**: dokumentasi lengkap, banyak tutorial, gampang cari solusi.

---

