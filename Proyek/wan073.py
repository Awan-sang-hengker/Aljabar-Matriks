def lybrary():
    print("Author : Thariq Ariq Setiawan")
    print("NPM : 2515061073")

def intrix(baris, kolom, nama):
    print(f"\nMasukkan elemen untuk Matriks {nama}")
    matrix = []

    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"Elemen [{i+1}][{j+1}] = "))
            row.append(nilai)
        matrix.append(row)

    return matrix


def mathrix(matrix1, matrix2):
    hasil = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        hasil.append(row)

    return hasil

def lybview(matrix):
    for row in matrix:
        print(row)