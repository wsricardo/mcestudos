import PyPDF2
import os
import os.path

def traduz(f):
  pdfFileObj = open(f, 'rb')
  try:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
  except:
    print (f, 'corrompido')
    return
  
  f = f.replace('.pdf', '.txt')
  out = open(f, 'w')
  try:
    out.write(pageObj.extractText())
  except:
    print (f, 'não conseguiu gravar o texto')
  out.close()

dirList = os.listdir(".")
for f in dirList:
  if f.endswith('.pdf'):
    t = f.replace('.pdf', '.txt')
    print (f)
    if not os.path.isfile(t):
      traduz(f)

