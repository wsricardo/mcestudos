import PyPDF2
import os
import os.path

def traduz(f):
  pdfFileObj = open(f, 'rb')
  try:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  except:
    print (f, 'corrompido')
    return
  
  f = f.replace('.pdf', '.txt')
  out = open(f, 'w')
  try:
    content = ''
    numPages = pdfReader.getNumPages()
    for i in range(numPages):
      content += pdfReader.getPage(i).extractText() + '\n'
    out.write(content)
  except:
    print (f, 'não conseguiu gravar o texto')
  out.close()

dirList = os.listdir(".")
for f in dirList:
  if f.endswith('.pdf'):
    t = f.replace('.pdf', '.txt')
    print (f)
    traduz(f)

