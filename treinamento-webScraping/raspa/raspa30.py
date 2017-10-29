from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.psparser import PSEOF
from io import StringIO
from io import open
from urllib.request import urlopen

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

#pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
#se o arquivo é local basta trocar urlopen por open('arquivo', 'rb')
pdfFile = open('Marcelo.pdf', 'rb')
out = open ('Marcelo.txt', 'w')
try:
    outputString = readPDF(pdfFile)
    out.write(outputString)
except PSEOF:
    pass
pdfFile.close()
out.close()
