class Mahasiswa():
    def __init__(self, nama, umur, jurusan):
        self.nama= nama
        self.umur= umur
        self.jurusan= jurusan
 
    def pengecekan(self):
        print("Hi,", self.nama, "dari", self.jurusan, "mari lakukan pengecekan kesehatan")
 

 
jumlah_normal= 0
banyak_orang= int(input("Berapa formulir mahasiswa yang ada di lab: "))
for i in range(banyak_orang):
    print("Mahasiswa ke-",i+1)
    orang= Mahasiswa(input("Siapa namanya: "), int(input("Berapa umurnya: ")), input("Dari jurusan apa: "))
    orang.pengecekan()
    kondisi= Kondisi(float(input("Dari formulir, berat badan kamu: ")), float(input("Tinggi badan kamu: ")))
    print("BMI kamu", kondisi.bmi())
    print("----------------------------------------------------------")
    bmi=0.0
    bmi+= kondisi.hasil_bmi()
    if bmi>= 18.5 and bmi<= 24.9:
        jumlah_normal+= 1
 
def lulus_tes():
    print(jumlah_normal, "/", banyak_orang, "mahasiswa lulus tes kesehatan")
 
lulus_tes()
