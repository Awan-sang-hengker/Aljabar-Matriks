import wan073 as wn

wn.lybrary()

baris = int(input("Masukkan jumlah baris matriks: "))
kolom = int(input("Masukkan jumlah kolom matriks: "))

matriks1 = wn.intrix(baris, kolom, "A")
matriks2 = wn.intrix(baris, kolom, "B")

hasil = wn.mathrix(matriks1, matriks2)

print("\nMatriks A:")
wn.lybview(matriks1)

print("\nMatriks B:")
wn.lybview(matriks2)

print("\nHasil Penjumlahan Matriks:")
wn.lybview(hasil)