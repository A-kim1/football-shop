PWS: https://amar-hakim-footballshop.pbp.cs.ui.ac.id/
Github: https://github.com/A-kim1/football-shop

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jwb:
    1. untuk step 1 itu aku membuat proyek django baru di dlm folder terluar yg bernama Football-Shop dengan cara buat virtual env nya, mengaktifkan virtual env nya dan terakhir install dependencies nya dan terakhir aku buat proyek django nya dengan nama football-shop jadi deh proyek Django nya

    2. nahh setelah proyek nya jadi, aku tinggal konfigurasi2 hal2 yg diperlukan untuk kedepannya, seperti: buat .env, buat .env.prod, dan ubah2 settingnya

    3. setelah itu aku bisa lanjut ke membuat aplikasi di dlm proyek nya dengan nama main dan setelah buat app main nya aku juga sekalian masukin 'main' ke dlm INSTALLED_APPS di setting proyek nya

    4. nahh krn udh buat app main nya aku tinggal buat2 file html buat templatenya, models.py untuk database (atribut2 yg dibutuhinnya), views.py nya untuk bisa sambungin nerima request dari user, ngambil data dari model, dan ngirim template nya ke user nya, terakhir aku juga buat routing nya utk setting2 urls nya agar user bisa liat template yg aku buat

    5. Langkah terakhir dari tugas 2 ini adalah deploy proyek nya ke PWS dan di unggah ke github, untuk step upload ke github nya aku cuman nambahin file .gitignore, buat branch master nya, dan terakhir tinggal add commit push aja. Untuk step deploy pws nya tinggal buat proyek baru, isi environs nya, tambahin ALLOWED_HOSTS nya di settings.py proyek, terakhir jalanin step2 project command nya dan selesai dehh


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

JWB:

Bagan: https://drive.google.com/drive/folders/1edbMjgJiybHH19vboz022Ni65Bj6p5H8?usp=sharing
Cara kerja berdasarkan bagan:

    1. User mengirim request lewat browser (misalnya http://domain.com/project/).

    2. Django URL Dispatcher (urls.py) cocokin request dengan pola URL yang ada, jadi intinya nanti URL ini bakal forward request yg ada ke view yg sesuai/yg menangani URL tersebut.
    Contoh: /project/ --> diarahin ke main.views

    3. Saat View (views.py) dijalankan:
        a. Kalo butuh data, view akan meminta ke Model (models.py).
        b. Model berhubungan dengan database untuk mengambil/menyimpan data, jadi intinya data nya itu ada di  database dan model nya itu untuk mengatur pengambilan/penyimpanan data nya gitu.
        c. View mengolah data dan menyiapkan context (variabel yang akan dipakai di template nya).

        d. Template (.html) digunain untuk nampilin halaman project dan data ke user.
           Contoh: {{ npm }}, {{ name }}.

    3. Response HTML dikirim kembali ke browser.

Jadi alurnya:
Request <-> URL <-> View <-> (Model + Template) <-> Response.

3. Jelaskan peran settings.py dalam proyek Django!

JWB:
File settings.py adalah pusat konfigurasi dari sebuah proyek Django. 
Artinya semua pengaturan untuk proyek kita ada di dlm file ini. Beberapa peran dari settings.py, antara lain:
    1. Konfigurasi Database
    2. Daftar Aplikasi yg Terinstal
    3. Konfigurasi Template
    4. Konfigurasi daftar host yg diizinkan untuk mengakses aplikasi web nya
    5. ...

4. Bagaimana cara kerja migrasi database di Django?

JWB:
Penjelasan migrasi di Django: Migrasi database di Django adalah cara untuk melacak perubahan yang kita buat di file model (models.py) ke dalam skema database dengan cara yang terkontrol dan versional.

cara kerja:
    1. Membuat Migration: kalo udh mengubah model (misalnya, menambah field/atribut baru), kita bisa jalanin perintah: python manage.py makemigrations

    2. Melakukan Migrasi: Selanjutnya, kita bakal jalanin perintah untuk menerapkan migrasi tersebut ke database (basis data lokal): python manage.py migrate

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

JWB:
Ada banyak hal yang membuat Django ini menjadi framework yang digunakan utk matkul PBP ini, beberapa keunggulannya adalah:

    1. Struktur jelas (MVT): mudah dipelajari & dipahami untuk pemula.
    2. Open Source dan gratis
    3. Menggunakan bahasa pemrograman Python, merupakan bahasa pemrograman yang simpel, mudah dipahami, dan populer
    4. Dokumentasi lengkap & komunitas besar
    5. Keamanan yang Tinggi: handling CSRF, XSS, SQL injection secara default (dengan best practice).
    6. ...

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

JWB: tidak ada sepertinya