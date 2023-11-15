# MPI-Numeric dan MPI-Bubble-Sort
MPI, atau Message Passing Interface, adalah sebuah standar komunikasi yang digunakan dalam pemrograman paralel. MPI memungkinkan komunikasi antara proses-paralel yang berjalan pada sistem komputasi terdistribusi. Ini adalah salah satu alat yang umum digunakan dalam komputasi paralel dan terutama diterapkan dalam pengembangan aplikasi ilmiah dan rekayasa yang memerlukan pemrosesan sejajar (parallel processing).
## Daftar Isi
- [Program yang dibutuhkan](#program-yang-dibutuhkan)
- [Package yang dibutuhkan](#package-yang-dibutuhkan)
- [Konfigurasi SSH](#konfigurasi-ssh)
- [Konfigurasi NFS](#konfigurasi-nfs)
- [Menjalankan MPI Numeric pada Python(#menjalankan-mpi-numeric-pada-python)
## Program yang dibutuhkan
1. [Ubuntu 20.04.6 Desktop](https://releases.ubuntu.com/focal/)
   - Ubuntu Master
   - Ubuntu Slave 1
   - Ubuntu Slave 2
   - Ubuntu Slave 3
3. MPI (Master dan Slave)
4. SSH (Master dan Slave)
5. NFS (Master dan Slave)
6. Kode Python
## Package yang dibutuhkan
1. Master
   - OpenSSH Server :
   ```bash
   sudo apt install openssh-server
   ```
   - NFS Kernel Server :
   ```bash
   sudo apt install nfs-kernel-server
   ```
   - Open MPI :
   ```bash
   sudo apt install openmpi-bin libopenmpi-dev
   ```
   - MPI4PY :
   ```bash
   sudo apt install python3-pip
   ```
   ```bash
   pip install mpi4py
   ```
2. Slave
   -  OpenSSH Server :
   ```bash
   sudo apt install openssh-server
   ```
   - NFS Common :
   ```bash
   sudo apt install nfs-common
   ```
   - Open MPI :
   ```bash
   sudo apt install openmpi-bin libopenmpi-dev
   ```
   - MPI4PY :
   ```bash
   sudo apt install python3-pip
   ```
   ```bash
   pip install mpi4py
   ```
## Konfigurasi SSH
1. Sebelum melakukan konfigurasi SSH, hal yang harus pertama kali dilakukan adalah menentukan 1 buah master dan 3 buah slave yang akan digunakan. Caranya adalah dengan menggunakan perintah `sudo nano /etc/hosts` pada semua master dan slave.
![sudo nano etc hosts](https://github.com/SyahrulWijaya/MPI-Numeric-dan-MPI-Bubble-Sort/blob/2be5d00f7a520aebe0fc313915d2331d95f83f69/sudo%20nano%20etc%20hosts.png)
2. Pada device master lakukan generate ssh key dengan menggunakan perintah
   ```bash
   ssh-keygen -t rsa
   ``` 
3. Pada device master copy key ssh yang sudah di generate pada direktori `.ssh` sebelumnya kesemua slave yang ada. Jangan Lupa untuk menyesuaikan `<namauser>` dengan nama user yang anda miliki dan `<namaslave>` dengan nama slave yang anda miliki. Lakukan perintah tersebut untuk semua slave yang anda gunakan. 
   ```bash
   cd .ssh
   ```
   ```bash
   cat id_rsa.pub | ssh <namauser>@<namaslave> "mkdir .ssh; cat >> .ssh/authorized_keys"
   ```
## Konfigurasi NFS
1. Buat shared direktori pada master dan slave. Sesuaikan `<namauser>` dengan nama user anda dan `<namadirektori>` sesuai keinginan anda.
   ```bash
   mkdir /home/<namauser>/<namadirektori>
   ```
2. Pada master lakukanlah konfigurasi pada `sudo nano /etc/exports` dengan menambahkan baris perintah berikut.
   ```bash
   /home/<namauser>/<namadirektori> *(rw,sync,no_root_squash,no_subtree_check)
   ```
3. Restart NFS Server pada master.
   ```bash
   sudo exportfs -a
   ```
   ```bash
   sudo systemctl restart nfs-kernel-server
   ```
4. Lakukan mount pada direktori yang telah dibuat sebelumnya, lakukanlah pada semua slave.
   ```bash
   sudo mount master:/home/<namauser>/<namadirektori> /home/<namauser>/<namadirektori>
   ```
## Menjalankan MPI Numeric pada Python
222
