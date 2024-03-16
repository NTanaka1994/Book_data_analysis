from googletrans import Translator
import glob
import os

trans = Translator(service_urls=['translate.googleapis.com'])

files = glob.glob("english/*")

for file in files:
    f = open(file, "r", encoding="utf-8")
    text = f.read()
    f.close()
    while True:
        try:
            transed = trans.translate(text, dest="ja")
            break
        except Exception as e:
            trans = Translator(service_urls=['translate.googleapis.com'])
    f = open("japanese/"+os.path.split(file)[1], "w", encoding="utf-8")
    f.write(transed.text)
    f.close()
