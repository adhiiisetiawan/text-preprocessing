#mengimport regex
import re

# disini saya menggunakan pySastrawi dalam hal stemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

document = "Pembatasan Sosial Berskala Besar di ibu kota hampir berakhir—dan sepertinya benar-benar tak bakal " \
           "diperpanjang—seiring bergaungnya tatanan hidup baru yang disebut new normal. " \
           "Presiden Joko Widodo—dan WHO—telah menyatakan secara eksplisit bahwa kita, umat manusia, " \
           "harus siap hidup bersama virus corona—untuk selamanya, anggaplah begitu untuk saat ini karena obat maupun " \
           "vaksin corona belum selesai diracik.  PSBB selama ini menjadi salah satu strategi pemerintah RI untuk menghambat " \
           "laju penularan virus corona. PSBB mensyaratkan warga untuk untuk bekerja dan belajar dari rumah, tak keluar rumah " \
           "untuk urusan yang tak mendesak, dan menghindari kontak fisik serta menjaga jarak dengan orang lain. Namun, seperti segalanya, " \
           "semua masa ada ujungnya. Pula PSBB."

# pada bagian ini digunakan untuk casefolding
caseFolding = document.lower()
print("Case Folding:\n")
print(caseFolding)
print("==============================================================")


# ***ini digunakan untuk tokenisasi, disini saya menggunakan regex untuk
# membersihkan tanda baca yang sekiranya mengganggu ***
tokenization = re.findall(r"[\w']+", caseFolding)
print("Tokenisasi:\n")
print(tokenization)
print("==============================================================")


# proses stopwords removal dimulai dari sini
file = open('stopword_tala.txt', 'r') #disini saya membuka dokumen stopword tala
stopWordsList = file.read() #kemudian membacanya dan disimpan pada variable stopwordsList
hasilStopwords = [] #saya membuat sebuah list kosong yang nantinya akan disimpan sebuah hasil dari stopwords

for w in tokenization: #melakukan perulangan variable w pada hasil tokenisasi
    if w not in stopWordsList: #memberikan seleksi kondisi jika nilai w tidak ada dalam stopwordsList
        hasilStopwords.append(w) #nilai dari w yang sudah diseleksi pada baris sebelumnya akan dimasukkan ke variable hasilStopwords
print("Filtering/Stopword Removal:\n")
removeDuplicate = list(dict.fromkeys(hasilStopwords)) #menghapus duplikasi kata dalam list pada variable hasilStopwords
print(removeDuplicate) #print removeduplicate
print("\n")
string = " " #membuat sebuah varible kosong bernama string dengan tipe string juga yang nantinya akan digunakan untuk mengkonversi list ke string
stopwordListToString = string.join(removeDuplicate) #menggabungkan string pada list
print("Stopword Removal diubah jadi String:\n")
print(stopwordListToString)
print("==============================================================")

# membuat stemmer dari library pySastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# proses stemming yang digunakan
hasilStemming   = stemmer.stem(stopwordListToString)
print("Stemming:\n")
print(hasilStemming)


