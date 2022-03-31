from googletrans import Translator

translator = Translator()
kalimat = translator.translate("jeremy anaknya jul seventa")
print(kalimat.text)

kalimat2 = translator.translate('kiel suka mengendarai sepeda', dest = 'da')
print(kalimat2.text)

kalimat3 = translator.translate('i have a friend, his name is dandy, but his brain is dumb like a crocodile', dest = 'da')
print(kalimat3.text)
