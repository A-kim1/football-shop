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

---------------------------------------------------------------------------------------------------------
TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

JWB:
Menurut aku data delivery dalam mengembangkan sebuah platform itu sangat penting karena platform itu terdiri dari banyak bagian (frontend, backend, database, ...), oleh karena itu data delivery sangat membantu dalam hal mentransfer data dengan aman, cepat, dan konsisten. Contoh dari data delivery yang aku sudah pakai adalah: HTML, JSON, XML

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JWB:
Menurutku JSON itu lebih baik dari pada XML karena beberapa hal, yaitu:
    1. JSON lebih aman dibandingkan dengan XML.
    2. JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
    3. JSON bersifat sederhana dan lebih fleksibel.
    4. Json itu parsingnya lebih cepat dibanding sama XML.
    5. ...

Dari beberapa hal yang aku sebutkan diatas sudah dapat dilihat bahwa JSON memiliki lebih banyak keunggulannya jika dibandingkan dengan XML, oleh karena itu JSON lebih populer dibandingkan dengan XML.

sumber: https://aws.amazon.com/id/compare/the-difference-between-json-xml/

3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

JWB:
Method is_valid() itu intinya ada untuk ngecek apakah data yang diisi user di form sudah benar semua sesuai aturan (seperti data terisi/tidak ada data yg kosong, sesuai tipe datanya, panjangnya juga sesuai, dll). Nahh utk penerapan method ini itu bisa dilihat di dalam views.py yang ada di dir main pada fungsi create_product.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh

JWB:
csrf_token itu adalah token keamanan untuk mencegah CSRF (Cross Site Request Forgery) attack.
Kalo kita gk ada token itu, maka penyerang/hacker bisa menipu seorang user yg udh pernah login/masuk ke web aku dan ngirim2 request yg berbahaya (contoh: ngapus data, ganti password, transfer uang, dll).

Jadi intinya itu dengan adanya csrf_token ini, Django bisa mastiin request yg dikirim itu benar2 berasal dari form yang sah di aplikasi/web yg aku buat, bukan dari luar.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

JWB:
    1. Pertama2 aku buat base template nya dulu yg digunain untuk dasar dari template3 lainnya, caranya aku buat folder templates di root folder dan isi dengan base.html yg isinya boilerplate html doang yg ditambah dengan template tags “block” yg nanti bisa aku masuk2in html buat app2 nya.
    
    2. Stlh itu aku setting2in template2 nya dan ubah2 dikit template main.html di app nya.

    3. Lalu, aku mulai buat form nya, di bagian buat form ini aku bakal tambah2in dan ubah2 kode di file views.py , models.py , file2 .html yang ada di dalam app nya.

    4. Selain langkah ketiga tadi aku juga sempet coba2 pake css di proyek aku ini, jadi langkah2 nya kurang lebih adalah: 
        a. buat folder static di root proyek, trus di dlm nya ada folder css, lalu di dlm folder itu ada file2 css nya. 
        b. stlh itu jgn lupa tambahin static file tadi ke settings.py nya. 
        c. baru deh aku bisa buat2 css nya dan masuk2in css nya ke template2 nya yg bersesuaian.

    5. Nahh setelah selesai buat form dan coba2 css aku sekarang bakal lanjut ke pebuatan xml dan json nya, di sini aku bakal tambah2in fungsi baru di views.py (yg ada di folder main) nya dan tambah2in kode di urls.py (yg ada di folder main) nya juga.

    6. Setelah seelsai buat kode tambahan untuk xml dan json nya aku langsung push saja ke github dan pws nya.

    CTT: nahh di PWS nya taunya css aku gk jalan, cuman di local doang jalannya, paling aku nunggu di tutorial nanti aja buat lanjut ke step css nya.
 
6.  Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

JWB: sepertinya tidak ada