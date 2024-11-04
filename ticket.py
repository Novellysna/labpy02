vip = 100000
reguler = 50000

jenis = input("Pilih jenis ticket anda (vip/reguler): ")

if jenis == "vip":
    harga_ticket = vip
elif jenis == "reguler":
    harga_ticket = reguler
else:
    print("Input tidak valid")
    exit()

member = input("Apakah anda punya kartu member (ya/tidak): ")
harga_ticket -= harga_ticket * 0.20 if member == "ya" else 0

print(f"Harga ticket anda {int(harga_ticket)}")
