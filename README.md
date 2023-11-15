# MPI-Numeric dan MPI-Bubble-Sort
MPI, atau Message Passing Interface, adalah sebuah standar komunikasi yang digunakan dalam pemrograman paralel. MPI memungkinkan komunikasi antara proses-paralel yang berjalan pada sistem komputasi terdistribusi. Ini adalah salah satu alat yang umum digunakan dalam komputasi paralel dan terutama diterapkan dalam pengembangan aplikasi ilmiah dan rekayasa yang memerlukan pemrosesan sejajar (parallel processing).
## Table of Contents
- [Program yang dibutuhkan](#program-yang-dibutuhkan)
- [Package yang dibutuhkan](#package-yang-dibutuhkan)
## Program yang dibutuhkan
1. Ubuntu 20.04.6 Desktop
   - Ubuntu Master
   - Ubuntu Slave 1
   - Ubuntu Slave 2
   - Ubuntu Slave 3
2. MPI (Master dan Slave)
3. SSH (Master dan Slave)
4. NFS (Master dan Slave)
5. Kode Python
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
2. slave
   -  OpenSSH Server :
   ```bash
   sudo apt install openssh-server
   ```
   - NFS Common :
   ```bash
   sudo apt install nfs-common
   ```
