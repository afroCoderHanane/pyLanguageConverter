#pip install --upgrade pip
#pip install googletrans
#pip install pypdf2==1.25.0
from PyPDF2 import PdfFileReader, PdfFileWriter
#from googletrans import Translator

file=open("dc-exam-study-guide.pdf",'rb')
reader = PdfFileReader(file)
num_pages = reader.numPages
for p in range(num_pages):
    page = reader.getPage(p)
    text = page.extractText()
    from googletrans import Translator
    translator = Translator()
    translate_text = translator.translate(text, dest='fr')
    #output= PdfFileWriter()
    #output_final = open("traduit.pdf", "wb")
    #output.write(output_final)
    print(translate_text)
