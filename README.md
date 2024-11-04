# Sistem Pembelian Tiket
Program sederhana untuk menghitung harga tiket berdasarkan jenis tiket dan status member.

## Deskripsi Program
Program ini memungkinkan pengguna untuk:

Memilih jenis tiket (VIP/Reguler)
Menentukan status member
Mendapatkan perhitungan harga tiket final dengan diskon jika memiliki kartu member

## Flowchart Ticket
````mermaid
flowchart TD
    A[Start] --> B[Set harga tiket VIP = 100000]
    B --> C[Set harga tiket Reguler = 50000]
    C --> D{Input jenis tiket}
    A([Start]) --> B[Set Harga VIP = 100000]
    B --> C[Set Harga Reguler = 50000]
    C --> D[/Input Jenis Tiket/]
    
    D -->|vip| E[harga_ticket = 100000]
    D -->|reguler| F[harga_ticket = 50000]
    D -->|input lain| G[Print 'Input tidak valid']
    G --> H[Exit]
    D --> E{Jenis Tiket Valid?}
    E -->|VIP| F[Tetapkan Harga = 100000]
    E -->|Reguler| G[Tetapkan Harga = 50000]
    E -->|Tidak Valid| H[/Tampilkan Pesan Error/]
    
    E --> I{Input kartu member}
    F --> I
    F --> I[/Input Status Member/]
    G --> I
    H --> J([Exit])
    
    I -->|ya| J[Hitung diskon 20%]
    I -->|tidak| K[Tidak ada diskon]
    I --> K{Member?}
    K -->|Ya| N[harga_ticket -= harga_ticket * 0.20]
    K -->|Tidak| O[/Tampilkan Harga Akhir/]
    
    J --> L[Print harga akhir]
    K --> L
    
    L --> M[End]
    N --> O[/Tampilkan Harga Akhir/]
    O --> P([End])
````
