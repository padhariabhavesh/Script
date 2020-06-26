# # Programmer Bhavesh Padharia
# # PDF to Text converter
#
# import PyPDF2
# pdffileobj=open('padharia.pdf','rb')
# pdfreader=PyPDF2.PdffileReader(pdffileobj)
# x=pdfreader.numPages
# pageobj=pdfreader.getPage(x-1)
# text=pageobj.extractText()
#
# file1=open(r"(/home/bhavesh/PycharmProjects/github/Scripts/)\\padharia.txt","a")
# file1.writelines(text)
# file1.close()




import PyPDF2
pdffileobj=open('1.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"/home/bhavesh/PycharmProjects/github/Scripts/1.txt","a")
file1.writelines(text)
file1.close()
