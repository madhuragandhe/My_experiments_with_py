import PyPDF2

name=input("Enter the pdf name ") # WHITE PAPER
pdfname=name+".pdf"
pdfobj = open(pdfname,'rb')
pdfread = PyPDF2.PdfFileReader(pdfobj)
total_pages=pdfread.numPages
print(total_pages)
filename=name+".txt"
for i in range(1,total_pages):
    pageobj = pdfread.getPage(i)
    data=pageobj.extractText()
    print(data)
    with open(filename,'a') as txtfile:
        txtfile.write(data)
    print ("Page {} copied".format(i))
pdfobj.close()