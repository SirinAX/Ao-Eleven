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

6. **Menambahkan Fungsi Views untuk JSON dan XML**

   * Saya menambahkan empat fungsi baru di `views.py`:

     * `products_json` → menampilkan semua produk dalam format JSON.
     * `products_xml` → menampilkan semua produk dalam format XML.
     * `product_json` → menampilkan detail satu produk berdasarkan ID dalam format JSON.
     * `product_xml` → menampilkan detail satu produk berdasarkan ID dalam format XML.
   * Fungsi ini menggunakan serializer bawaan Django untuk mengubah queryset ke dalam format JSON/XML.

7. **Menambahkan Routing URL di `urls.py`**

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

---

# TUGAS 4 - Implementasi Autentikasi, Session, dan Cookies pada Django

---

## ❓ Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya !
`AuthenticationForm` adalah form bawaan Django yang digunakan untuk proses **login** pengguna. Form ini secara otomatis menyediakan field **username** dan **password**, serta melakukan validasi apakah pasangan kredensial tersebut sesuai dengan data di basis data pengguna (`User model`).

**Kelebihan:**
- Sudah terintegrasi dengan sistem autentikasi Django sehingga aman dan minim konfigurasi.
- Menangani validasi login secara otomatis, termasuk pengecekan akun yang tidak aktif.
- Mudah digunakan karena hanya perlu di-*import* dan dirender di template.

**Kekurangan:**
- Terbatas pada field username dan password (perlu kustomisasi jika ingin login dengan email atau multi-field).
- Tampilan default sederhana, sehingga biasanya perlu ditambahkan styling sesuai kebutuhan aplikasi.

---
## 2. 🔑 Perbedaan Autentikasi dan Otorisasi

- **Autentikasi (Authentication)**: Proses verifikasi identitas pengguna.  
  📌 Contoh: memastikan bahwa pengguna benar-benar “Andi” dengan memeriksa username dan password.

- **Otorisasi (Authorization)**: Proses pemberian hak akses setelah identitas diverifikasi.  
  📌 Contoh: setelah login, hanya admin yang boleh mengakses halaman dashboard tertentu.

**Implementasi di Django:**
- ✅ **Autentikasi**:  
  Django menyediakan `django.contrib.auth`, termasuk fungsi `authenticate()` dan `login()` untuk memverifikasi identitas.
- ✅ **Otorisasi**:  
  Django memiliki sistem *permissions* dan *groups* yang bisa mengatur akses per pengguna. Misalnya, decorator `@login_required` atau `@permission_required` digunakan untuk membatasi akses pada view tertentu.

---

## 3. 🍪 Session vs Cookies dalam Menyimpan State

**Cookies**: data kecil yang disimpan di sisi *client* (browser).  
**Session**: data pengguna yang disimpan di server, sementara browser hanya menyimpan *session ID* di dalam cookies.

### ⚡ Kelebihan Cookies:
- 📦 Ringan dan tidak membebani server karena data disimpan di sisi client.
- 🌐 Dapat digunakan lintas sesi browser (jika tidak dihapus).
- 🔍 Mudah diakses dari sisi client untuk kebutuhan tertentu (misalnya *remember me*).

### ⚠️ Kekurangan Cookies:
- 🔓 Rentan dimanipulasi oleh pengguna jika tidak dienkripsi.
- 📏 Ukuran terbatas (± 4 KB per cookie).
- 🚫 Tidak cocok untuk menyimpan data sensitif.

### ⚡ Kelebihan Session:
- 🔒 Lebih aman karena data utama disimpan di server.
- 📂 Mendukung penyimpanan data dalam jumlah lebih besar dibanding cookies.
- 🔗 Django memiliki manajemen session bawaan yang terintegrasi.

### ⚠️ Kekurangan Session:
- 🖥️ Membebani server jika banyak pengguna aktif secara bersamaan.
- 🍪 Tetap bergantung pada cookies (karena session ID disimpan di dalam cookie).

---

## 4. 🔐 Apakah Cookies Aman Secara Default?

Penggunaan cookies **tidak sepenuhnya aman** secara default. Ada risiko yang perlu diperhatikan, seperti:
- 🕵️ **Cookie theft (pencurian cookies)** melalui serangan XSS (*Cross-Site Scripting*).  
- 🎭 **Session hijacking**: pencuri mengambil alih identitas pengguna melalui session ID.  
- ✍️ **Manipulasi cookies**: data bisa diubah oleh client jika tidak dilindungi.  

**Penanganan di Django:**
- ✅ Opsi `HttpOnly` untuk mencegah akses cookie melalui JavaScript.  
- ✅ Mendukung `Secure` flag agar cookies hanya dikirim melalui HTTPS.  
- ✅ Mekanisme **CSRF protection** untuk mencegah serangan berbasis form.  
- ✅ Konfigurasi `SESSION_COOKIE_AGE`, `SESSION_COOKIE_SECURE`, dan `SESSION_COOKIE_SAMESITE` di `settings.py` untuk meningkatkan keamanan.  

---
# 📋 Implementasi Autentikasi, Relasi User–Product, & Cookies

## 1. Registrasi, Login, Logout
- Membuat `register`, `login_user`, dan `logout_user` di `views.py`.
- Menggunakan `UserCreationForm`/`AuthenticationForm` dan menyesuaikan tampilan dengan `home.html`.
- Login menyimpan cookie `last_login`, logout menghapus cookie tersebut.

## 2. Relasi User–Product
- Tambahkan field `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model `Product`.
- Pada view create, simpan `ent.user = request.user` sebelum `ent.save()`.

## 3. Informasi User & Cookies
- `home` menampilkan `request.user.username` dan cookie `last_login`.
- Tambahkan tombol filter “All” dan “My” untuk membedakan item milik semua user atau hanya user yang login.

## 4. Dummy Data
- Registrasi 2 akun pengguna langsung melalui form `register`.
- Login dengan masing-masing akun dan buat 3 data `Product` menggunakan form input yang sudah ada.
- Dengan demikian, setiap akun memiliki 3 data dummy secara manual melalui antarmuka aplikasi.

## 5. Penyesuaian Form
- `login.html` dan `register.html` disusun dengan struktur dan class CSS yang konsisten dengan `home.html`.

## 6. Verifikasi
- Login → cek halaman utama menampilkan username dan `last_login`.
- Tambah produk → otomatis terhubung dengan user.
- Filter → tampil sesuai pemilik akun.
- Logout → cookie `last_login` terhapus.

---
## 👩‍🏫 Feedback untuk asisten dosen Tutorial 3

Pada saat sesi tutorial 3, saya juga tidak menemui kendala berarti. Materi yang disampaikan asisten dosen runtut dan mudah dipahami, sehingga saya dapat mengikuti alur praktik dengan baik. Penjelasan yang diberikan membantu saya memahami konsep baru sekaligus mempraktikkannya secara langsung, sehingga tugas yang diberikan pun dapat saya kerjakan dengan lebih lancar.

---

# 🌐 TUGAS 5 — Desain Web menggunakan HTML, CSS, dan Framework CSS

---

## 🎨 Urutan Prioritas CSS Selector

Ketika ada banyak selector yang mengatur satu elemen, browser menentukan **siapa yang menang** berdasarkan spesifisitas & urutan.

Urutan prioritas:

1. 🚨 **`!important`** → *tertinggi*, override semua (hindari kecuali sangat perlu).
2. 🎯 **Inline style** → `style="..."` langsung di elemen.
3. 🆔 **ID selector** → `#idku`.
4. 🏷️ **Class / attribute / pseudo-class** → `.classku`, `[type="text"]`, `:hover`.
5. 📄 **Element / pseudo-element** → `div`, `p`, `::after`.
6. ⏳ Jika sama → aturan yang muncul **terakhir** akan dipakai (cascade).

**Contoh:**

```css
button { color: blue; }       /* element */
.btn { color: green; }        /* class */
#submitBtn { color: red; }    /* id */
```

```html
<button id="submitBtn" class="btn" style="color: purple">Klik Aku</button>
```

➡️ Hasil: warna **ungu**, karena inline style menang. Kalau ada `!important`, itu akan override semuanya.

---

## 📱 Pentingnya Responsive Design

Kenapa harus responsive?

* 📏 **Ukuran layar beragam**: HP, tablet, laptop, desktop.
* 😀 **User experience**: lebih nyaman, gampang navigasi.
* 🔎 **SEO friendly**: Google lebih suka website mobile-friendly.
* 🛠️ **Lebih mudah maintenance**: satu codebase untuk semua device.
* ♿ **Aksesibilitas**: teks terbaca, tombol gampang ditekan.

**Contoh aplikasi responsive:**
Google, Wikipedia, Twitter, Tokopedia → tampilan otomatis menyesuaikan device.

---

## 📦 Margin, Border, dan Padding

**Box model CSS**:

```
margin → border → padding → content
```

* 🔲 **Margin** → ruang luar, pisahkan elemen dengan elemen lain.
* 🖼️ **Border** → garis di sekeliling padding & content.
* 🧩 **Padding** → ruang dalam antara konten dan border.

**Tips modern:**
Gunakan `box-sizing: border-box;` → width/height sudah termasuk border & padding → lebih gampang atur layout.

**Contoh:**

```css
.card {
  margin: 16px;             /* ruang luar */
  border: 1px solid #ddd;   /* garis */
  padding: 12px;            /* ruang dalam */
  width: 280px;             /* total width termasuk padding & border */
  box-sizing: border-box;
}
```

⚠️ Catatan: margin vertikal antar block bisa *collapse* → hanya margin terbesar yang berlaku.

---

## 🔀 Flexbox vs Grid

### 📌 Flexbox (1D layout)

* Fokus ke **satu dimensi**: baris *atau* kolom.
* Cocok untuk: navbar, bar tombol, card row.
* Properti utama:

  * Container: `display: flex; flex-direction; justify-content; align-items; gap;`
  * Item: `flex-grow; flex-shrink; align-self;`

**Contoh:**

```css
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

### 🗂️ Grid (2D layout)

* Fokus ke **dua dimensi**: baris *dan* kolom.
* Cocok untuk: gallery, dashboard, grid produk.
* Properti utama:

  * Container: `display: grid; grid-template-columns; grid-template-rows; gap;`
  * Item: `grid-column; grid-row;`

**Contoh:**

```css
.products {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
}
```

📍 **Kapan pakai apa?**

* Susunan linear sederhana → Flexbox.
* Layout kompleks baris + kolom → Grid.

---

## 📝 Alur Implementasi Checklist Tugas 5

1. 🔧 **Fitur Edit & Delete Produk**

   * Tambah fungsi `edit_product` & `delete_product` di `views.py`.
   * Tambah routing di `urls.py`.
   * Buat template `edit_product.html`.
   * Tambah tombol **Edit** & **Delete** di card produk → hanya muncul untuk **owner** atau **superuser**.

2. 🎨 **Kustomisasi Tampilan**

   * Tambah Tailwind CDN di `base.html`.
   * Atur layout dasar dengan **flexbox** & **grid**.

3. 🖼️ **Styling Halaman**

   * Login, Register, Tambah Produk, Edit Produk, Detail Produk, Home.
   * Semua dibuat **responsif** + seragam (warna, tombol interaktif, card rapi).

4. 📋 **Daftar Produk**

   * Jika kosong → tampilkan pesan *“Belum ada produk yang terdaftar”*.
   * Jika ada → tampilkan card grid (gambar, deskripsi, tombol Detail/Edit/Delete).

5. 🧭 **Navbar Responsif**

   * Buat `navbar.html` → include di semua halaman.
   * Isi: Home, Add Product, Login/Logout/Register.
   * Tambah menu hamburger untuk mobile.

6. 📂 **Static Files**

   * Konfigurasi WhiteNoise di `settings.py`.
   * Supaya CSS & file statis tetap ter-load dengan baik saat deploy.

✅ Hasil akhir: semua halaman **rapi, konsisten, responsif, dan interaktif** 🎉

---
#  TUGAS 6 — Javascript dan AJAX
---

## 🔄 1. Synchronous vs Asynchronous

* **Synchronous (cara lama)**

  * Request dikirim → tunggu server → halaman reload full.
  * Contoh: submit form → langsung pindah atau reload halaman.
* **Asynchronous (AJAX)**

  * Request jalan di background → halaman tetap di tempat.
  * Server balikin data (biasanya JSON) → langsung update bagian tertentu.
  * Contoh: klik tombol “Like” → angka like nambah, tanpa refresh.

---

## 🛠 2. Alur AJAX di Django

1. User klik tombol / isi form.
2. JavaScript (`fetch`, `axios`, dll) kirim request ke URL Django.
3. Django `views.py` proses data → balikin `JsonResponse`.
4. JavaScript terima response → update tampilan (DOM).

➡️ Intinya: **user → JS → Django → JSON → JS update DOM**

---

## ⚡ 3. Kenapa Pake AJAX?

* Lebih **cepat** karena nggak reload full page.
* Lebih **hemat** (cuma kirim/terima data penting).
* Lebih **interaktif** dan terasa modern.
* Bisa bikin fitur real-time kayak chat, live search, notifikasi.

---

## 🔒 4. Keamanan Login & Register

Kalau main di fitur sensitif, jangan lupa:

* Sertakan **CSRF Token** di tiap request.
* Pakai **HTTPS** biar data login aman.
* **Validasi di server tetap wajib**, jangan cuma di JS.
* Jangan kasih pesan error yang terlalu detail.
* Kalau perlu, tambahin **rate limiting** biar brute force susah.

---

## 🎨 5. Dampak ke User Experience

* User ngerasa web **lebih ringan & responsif**.
* Interaksi jadi **seamless**, nggak keganggu reload.
* Bikin web berasa kayak **aplikasi mobile/desktop**.
* Tapi kalau AJAX error **tanpa feedback**, user bisa bingung.

---

