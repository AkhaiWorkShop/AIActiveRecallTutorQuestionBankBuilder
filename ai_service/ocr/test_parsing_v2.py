import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ocr.ocr_engine import QuestionParser
import json

raw_text = """c. suku Dayak, suku Banjar, suku
Melayu, serta berbagai suku pen-
datang lainnya
d. suku Bugis,suku Makassar,suku
Minahasa,Suku Toraja,dan seba
gainya
6. De remmah kabheereh? adalah kali-
mat sapaan dari daerah...
a. Solo
b.Lampung
c.Madura
d.Kei
Habarfalbehe?adalah kalimat sapaan
dari daerah...
a.Solo
b.Lampung
c. Madura
d. Kei
8.
a.Jawa
b. Sumatra
c.Kalimantan
d.Papua
Nyow kabar? adalah kalimat sapaan
9.
dari daerah ....
a.Solo
Madura
C.
d.Kei
b.Lampung
10. Gambar pulau berikut merupakan tem
pat tinggal ....
a.suku Melayu,suku Batak,suku
Aceh,suku Gayo,suku Nias,suku
Minang,dan suku Palembang
b. suku Jawa, suku Sunda, suku
Betawi,suku Madura,suku Tiong
hoa,dan suku Arab
suku Dayak, suku Banjar,suku
C.
Melayu, serta berbagai suku pen-
datang lainnya
d.suku Bugis,suku Makassar,suku
Minahasa,Suku Toraja,dan seba-
gainya
11.Nuwo Sesat adalah rumah adat dari
Provinsi....
a.Jawa Tengah
b.Gorontalo
c.Lampung
d.Maluku
a.Jawa Tengah
b. Gorontalo
c.Lampung
d. Maluku
97"""

parser = QuestionParser()
results = parser.parse(raw_text)

print(json.dumps(results, indent=2))
