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

--------------------------------------------------------------------------------------------------------------
TUGAS 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan Django yang digunakan untuk melakukan autentikasi pengguna. Form ini memvalidasi username dan password, dan jika valid, akan mengembalikan objek user yang terautentikasi. Nahh untuk ini itu dipakainya kpn? ini itu bakal dipakai di views.py utk ngebuat form tanpa harus nulis kode dari awal krn udh disediain sama django nya

Kelebihan:
    1) Sudah terintegrasi dengan sistem autentikasi Django (jadi initnya udh teruji dan aman secara default nya)
    2) Melakukan validasi secara otomatis
    3) Aman terhadap serangan seperti SQL injection
    4) Gampang di custom
    5) Integrasi nya baik dengan middleware dan session sjango.

Kekurangan:
    1) Biasanya terlalu sederhana untuk kebutuhan kompleks
    2) Perlu penyesuaian jika ingin menambahkan field tambahan (dibatasin field nya)
    3) Tidak ideal kalo mau login bukan dengan username (misal pake email gitu)
    4) Tidak otomatis membuat session, form itu hanya memvalidasi

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

    1) Autentikasi (Authentication)
    Proses verifikasi identitas pengguna (ngecek siapa kamu). 
    Cara implementasi: Contoh nya di django/proyek ini di django udh disediain import-an django.contrib.auth yg nyediain model User, authenticate(), login(), dll.

    2) Otorisasi (Authorization)
    Proses menentukan apa yang boleh dilakukan oleh pengguna yang telah terautentikasi (apa yang boleh kamu lakukan).
    Cara implementasi: Contoh nya didjango/proyek ini di django udh disediain import-an django.contrib.auth.decorators import login_required yg gunanya utk autentikasi pengguna yg udh login doang yg bisa akses fungsi tersebut.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

    1) Cookies (client-side)
    Intinya data nya disimpen sisi klien/browser pengguna.

        Kelebihan:
        a. Mudah diakses di client, cocok buat data kecil yang gk sensitif (misal utk cek last login nya kyk di proyek ini).
        b. Stateless untuk server (tidak perlu penyimpanan server jika simpan data di cookie).

        Kekurangan:
        a. Batas ukuran (4 KB), ini itu lebih kecil kalo dibandingin sama Local Storage dan Sessions.
        b. Mudah dimanipulasi oleh client (kecuali ditandatangani/dienkripsi)

    2) Sessions (server-side, + cookie pointer)
    Intinya data nya disimpen di sisi server nya

        Kelebihan:
        a. Data nya disimpan server-side, jadinya lebih aman dari modifikasi client.
        b. Bisa nyimpen lebih banyak data (5 MB), dan server yg memutuskan validita nya.

        Kekurangan:
        a. Menggunakan lebih banyak resource dari server nya.
        b. Memerlukan mekanisme pembersihan (expired sessions) (pokonya perlu manajemen sessions yg baik).

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

    Jadi intinya penggunaan cookies ini gk sepenuhnya aman secara default. Django ini udh ngurangin beberapa risiko secara default nya, tapi kita harus tetap setting/mengonfigurasi untuk produksi secara lebihi aman dan terstruktur.

    Risiko yg harus diwaspadai:
    1) Cross-Site Scripting (XSS): Penyerang/hacker bisa mencuri cookies.
    2) Cross-Site Request Forgery (CSRF): Memanipulasi request dengan cookies yang valid.

    Cara Django utk menanganinya antara lain:
    1) CSRF protection: middleware & template tag {% csrf_token %} default.
    2) Django nyediain setting SESSION_COOKIE_SECURE untuk mastiin cookies hanya dikirim melalui HTTPS.
    3) Untuk session cookies, Django secara default udh nyetel flag HttpOnly = True yang mencegah akses melalui JavaScript.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Jadi pertama2 di tugas 4 ini aku bakal ngebuat fungsi dan form buat registrasi dulu, pertama aku buat form nya dulu dengan cara buat fungsi di views.py di folder app “main” nya aku dulu pakai form user yg udh dibuatin django dengan cara import UserCreationForm, nahhh import-an tersebut bakal ngebuat aku bisa buat form registrasi dengan mudah (tambahan: selain itu aku juga import messages dari django utk nampilin2 message2 gitu).

    2. Setelah itu aku bisa lanjut ke buat html buat registrasi nya dengan nama file register.html dan connect-in file html itu ke views nya serta set up urls nya, trus jadi dehh buat bikin page registrasi nya

    3. Karena aku udh buat page registrasinya aku bakal lanjut buat page login nya. Ini intinya sihh sama aja kayak pas buat registrasi diatas. Jadi intinya aku buat fungsi login nya dulu di views.py pakai import-an django untuk form autentikasi nya (AuthenticationForm), trus tinggal buat login.html dan connect-in ke views.py  dan urls.py nya.

    4. Lanjut ke buat fungsi logout nya. Caranya kyk biasa buat fungsi baru di views.py nya dengan bantuan import logout dari django. Stlh ini selesai artinya adalah aku udh selesai buat sistem autentikasi buat proyek football shop aku ini

    5. Langkah selanjutnya setelah autentikasi adalah merestriksi akses halaman main dan product detail. Caranya adalah menggunakan decorator dari django import login_required.

    6. Step selanjutnya adalah gunain data dari cookies, nahh di sini itu aku bakal pakai cookie utk tandain kapan aku terakhir kali login di web aku tersebut. Jadi krn aku bakal pakai cookie nya utk tandain kapan aku terakhir kali login, di sini aku bakal otak-atik kode fungis login_user nya di views.py. Stlh ini aku bisa lanjut gonta-ganti kode nya dikit lagi, seperti: tambahin context last login nya dan ubah fungsi logout nya utk apus cookie nya. 

    7. Terakhir aku bakal hubungin model product nya dengan user nya. Caranya itu: import User dari django, tambahin var baru user di dlm model product nya yg bakal hubungin user dengan product nya. Setelah itu tinggal ubah2 dikit kode di views.py nya dan beberpa file2 html nya dan selesai.

-------------------------------------------------------------------------------------------------------------
TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

    Urutan prioritas CSS selector dari yang tertinggi ke terendah:
    1) Inline styles = CSS yang langsung ditulis di dalam HTML nya menggunakan atribut style (style tag)
    2) ID selector = Selector yang menggunakan #id --> itu syntax nya, pakai # kalau id
    3) Classes selector = Selector yang menggunakan .class --> itu syntax nya, pakai . kalau class
    tambahan yang setara dengan Class selector: Attribute selector dan Pseudo-class, contoh: [type="text"] dan :hover
    4) Element selector = Selector yang menggunakan elemet nya --> contoh: h1,p,div,...
    tambahan yang setara dengan Element selector: Pseudo-element, contoh: ::before

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Pertama-tama mungkin aku beri penjelasan tentang apa itu responsive design. Responsive design adalah pendekatan dalam web design agar tampilan website kita bisa menyesuaikan otomatis dengan ukuran layar (HP, tablet, laptop, desktop). Nahh ini itu merupakan salah satu konsep yang sangat penting di pengembangan aplikasi web karena dengan adanya responsive design ini konten di web kita akan tetap mudah dibaca, diakses, dan digunakan di semua perangkat.

Contoh aplikasi yang sudah responsive:
    1) Google --> Bisa kita lihat bahwa layout google menyesuaikan ukuran layar
    2) Spotify --> Menu navigasi (navbar) nya berubah jadi hamburger menu kalo di mobile
    3) ...

Contoh aplikasi yang belum responsive:
    Utk aplikasi yang belum responsive biasanya itu adalah
    1) web pemerintah yang lama --> biasanya itu udh fixed gitu width nya yg bikin kita pengguna mobile harus zoom manual gitu
    2) web legacy --> nahh kalo web legacy ini itu biasanya dibuatnya cuman utk 1 ukuran layar doang (biasanya buat desktop doang)

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    1) Margin: intinya ini itu ruang luar antara elemen dan elemen lain (yg plg luar nya)
    2) Border: garis/pembatas yang mengelilingi/membatasi margin dan padding
    3) Padding: ruang antara konten elemen dengan border nya (di dlm border) (membatasi konten dan border)

Dari lapisan terluar ke dalam: Margin, Border, Padding, Isi/Content

Cara implementasinya mungkin bisa dilihat dari kode berikut --> ini itu kode di css nya:
form {
    margin: 20px;
    padding: 25px;
    border: 2px solid black; 
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Intinya itu flexbox dan grid merupakkan teknik layout yg digunakan di pembuatan aplikasi web.
    1) Flexbox: layout nya itu satu dimensi doang, digunakan untuk mengatur elemen dlm satu baris ATAU kolom
                - Kegunaan: ideal nya untuk komponen2 kecil, seperti: navigasi, card, form elements, dll

    2) Grid: layout dua dimensi yang digunakan untuk mengatur elemen dalam baris DAN kolom
            - Kegunaan: cocok utk layout halaman yang kompleks (main page nya), gallery, dashboard, dll

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1) Jadi pertama aku nambahin tailwind css pake script cdn di base html nya (intinya ini buat ntar pas bikin2 css nya dipakenya)

    2) Selanjutnya, aku mencoba buat fitur Edit product gitu utk bisa edit2 product yg udh pernah dibikin sblmnya, disini normal aja cuman tambahin views.py pasang url yang pas, dan buat tambahin html nya agar munculin edit product nya.

    3) Stlh itu, aku lanjut buat fitur hapus news nya. Langkah2 yg diubah sama seperti yg diatas intinya

    4) Baru stlh itu aku bakal nambahin navbar (untuk navigasi fitur2nya gitu)

    5) Dan terakhir ini aku bakal nambahin css nya, disini aku bakal buat file baru global.css yang ada di folder static/css yang ada di root. Nahh tapi aku bakal implement css nya itu kebanyakan dari html nya langsung, disini aku lumayan mirip dengan tutorial tapi ada beebrapa hal yang aku ganti seperti warna/color pallatenya dan di card (card_product.html) nya aku juga ubah template bentuknya agar lebih sesuai dengan tema shop nya
