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

## ❓ Mengapa Kita Memerlukan Data Delivery?

Data delivery penting karena aplikasi web bukan cuma menampilkan halaman statis, tapi juga harus bisa bertukar informasi antara client (browser atau aplikasi lain) dan server. Contohnya: saat user mengisi form registrasi, data itu perlu dikirim ke server untuk disimpan ke database, lalu server mengirimkan respons balik ke client. Tanpa data delivery, aplikasi hanya sebatas HTML statis dan tidak interaktif.

## ⚖️ XML vs JSON

Menurut saya JSON lebih baik dibanding XML untuk konteks web modern. JSON lebih ringan, strukturnya sederhana (pakai objek dan array), dan lebih mudah diproses di bahasa pemrograman seperti Python atau JavaScript.
XML sebenarnya kuat karena mendukung skema, validasi, dan bisa lebih deskriptif, tapi sifatnya verbose (tag pembuka-penutup panjang).
JSON jadi populer karena:
- Lebih mudah dibaca oleh manusia dan dipahami developer.
- Didukung langsung oleh hampir semua bahasa pemrograman modern.
- Efisien untuk data API/web service.

## 📝 Fungsi is_valid() pada Django Form

Method is_valid() dipakai untuk memvalidasi data yang dikirim lewat form. Jadi, Django akan otomatis mengecek apakah input sesuai aturan field di model atau form.
Contoh: kalau ada field umur (IntegerField) lalu user isi dengan teks "abc", maka is_valid() akan mengembalikan False dan Django bisa menampilkan error ke user.
Tanpa is_valid(), kita harus melakukan validasi manual, yang bikin rawan bug dan lebih ribet.

## 🔒 Mengapa Perlu csrf_token?

csrf_token adalah token keamanan yang mencegah serangan Cross-Site Request Forgery (CSRF).
Kalau tidak ada token ini, penyerang bisa bikin user tanpa sadar mengirim request berbahaya ke server (misalnya klik link di website palsu yang ternyata mengirim request POST ke aplikasi kita).
Dengan csrf_token, setiap form punya token unik yang harus cocok dengan token di server. Jadi penyerang tidak bisa sembarangan submit data karena tokennya tidak valid.

## 📮 Postman Test — Data Delivery

Berikut hasil akses URL dengan Postman:

1. **All Products (JSON)**
   ![JSON All](https://github.com/user-attachments/assets/d6beb48b-5ada-4519-8518-9b4030f2089a)

2. **All Products (XML)**
   ![XML All](https://github.com/user-attachments/assets/52cf0e93-f848-4f56-a297-74b9530ff30c)

3. **Product by ID (XML)**
   ![XML by ID](https://github.com/user-attachments/assets/dbd394cb-e161-4033-8da6-835ea4854515)

4. **Product by ID (JSON)**
   ![JSON by ID](https://github.com/user-attachments/assets/819ecf8d-ff1d-4142-b517-985bfcb9d3af)

---

## 📌 Alur Pengerjaan Tugas 3

1. **Membuat Layout Utama (`base.html`)**

   * Saya membuat file `base.html` sebagai layout utama.
   * File ini berisi struktur dasar seperti header, navbar, dan footer.
   * Saya menambahkan block `{% block content %}{% endblock %}` agar halaman lain bisa mewarisi struktur dasar ini.

2. **Membuat Halaman Home (`home.html`)**

   * Halaman ini menampilkan daftar produk yang sudah ditambahkan ke dalam database.
   * Saya menambahkan tombol **"Add"** yang mengarahkan user ke halaman form untuk menambah produk baru.
   * Setiap produk yang ditampilkan juga memiliki tombol **"Detail"** yang akan membuka halaman detail produk tersebut.
   * Halaman ini menggunakan `{% extends 'base.html' %}` untuk mewarisi layout utama.

3. **Membuat Form di `forms.py`**

   * Saya membuat file `forms.py` dan mendefinisikan `ProductForm` berbasis `ModelForm`.
   * Form ini menggunakan model `Product` dan mengambil semua field yang sudah didefinisikan di model.
   * Form ini nantinya dipakai pada halaman tambah produk (`add_product.html`).

4. **Membuat Halaman Form (`add_product.html`)**

   * Halaman ini digunakan untuk menambahkan produk baru.
   * Form yang ditampilkan berasal dari `ProductForm`.
   * Setelah produk berhasil ditambahkan, user diarahkan kembali ke halaman home agar dapat langsung melihat data yang baru masuk.
   * Halaman ini juga extends dari `base.html`.

5. **Membuat Halaman Detail Produk (`product_detail.html`)**

   * Halaman ini menampilkan detail informasi dari setiap produk yang dipilih.
   * Data produk diambil berdasarkan `pk` yang dikirim melalui URL.
   * Saya juga menambahkan opsi untuk menghapus produk melalui tombol **"Delete"** yang akan mengarahkan ke halaman konfirmasi.
   * Halaman ini juga extends dari `base.html`.

6. **Membuat Halaman Konfirmasi Delete (`product_confirm_delete.html`)**

   * Halaman ini berfungsi untuk menampilkan pesan konfirmasi sebelum data produk benar-benar dihapus.
   * User akan diberikan dua opsi, yaitu **"Ya, Hapus"** untuk menghapus data atau **"Batal"** untuk kembali ke halaman detail.
   * Halaman ini juga extends dari `base.html`.

7. **Menambahkan Fungsi Views untuk JSON dan XML**

   * Saya menambahkan empat fungsi baru di `views.py`:

     * `products_json` → menampilkan semua produk dalam format JSON.
     * `products_xml` → menampilkan semua produk dalam format XML.
     * `product_json` → menampilkan detail satu produk berdasarkan ID dalam format JSON.
     * `product_xml` → menampilkan detail satu produk berdasarkan ID dalam format XML.
   * Fungsi ini menggunakan serializer bawaan Django untuk mengubah queryset ke dalam format JSON/XML.

8. **Menambahkan Routing URL di `urls.py`**

   * Saya menambahkan path baru untuk mengakses data dalam format JSON dan XML, baik untuk semua produk maupun produk berdasarkan ID.
   * Contoh:

     * `/products/json/` → semua produk dalam format JSON.
     * `/products/xml/` → semua produk dalam format XML.
     * `/products/json/<int:pk>/` → produk berdasarkan ID dalam format JSON.
     * `/products/xml/<int:pk>/` → produk berdasarkan ID dalam format XML.

Dengan langkah-langkah tersebut, aplikasi dapat menampilkan data produk dalam bentuk halaman HTML menggunakan form untuk menambah data, serta menyediakan endpoint JSON dan XML yang bisa digunakan untuk kebutuhan data delivery.

---
## 👩‍🏫 Feedback untuk asisten dosen Tutorial 2

Pada saat sesi tutorial 2, saya pribadi tidak mengalami masalah. Penjelasan asisten dosen sudah jelas dan alurnya mudah diikuti, sehingga saya bisa memahami materi serta menyelesaikan tugas dengan lancar.


