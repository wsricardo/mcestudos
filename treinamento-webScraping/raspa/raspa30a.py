import PyPDF2
pdfFileObj = open('1609-2012.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
out = open('1609-2012.txt', 'w')
out.write(pageObj.extractText())
out.close()

