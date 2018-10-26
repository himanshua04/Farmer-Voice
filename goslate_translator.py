#pip install goslate
import goslate

text = "Hello World"

gs = goslate.Goslate()
translatedText = gs.translate(text,'hi')

print(translatedText)
