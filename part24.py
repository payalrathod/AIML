# zip function
lst1 = ["sam", "pam", "lam"]
lst2 = ["a", "b", "c"]
lst3 = [1,2,3,4]
for i in lst1:
    print(i)

output = zip(lst1,lst2)
print(output)
print(list(output))

# zip object is an iterartor
# print(next(output))
output = zip(lst1,lst2,lst3)
for i, j, k in output:
    print(i,j,k)

print(list(zip()))

dict1 = {'name':'Pam','age':20,'city':'lay'}
dict2 = {'name':'Lam','age':19,'city':'pay'}
dictio = zip(dict1.items(),dict2.items())
for (i,j),(i1,j1) in dictio:
    print(i,j)
    print(i1,j1)


# password in pdf
from PyPDF2 import PdfFileReader,PdfFileWriter
#  open current pdf
file_pdf = PdfFileReader('AdditionalSicknessLeaves-FAQ.pdf')
pdf1 = PdfFileWriter()
print(file_pdf)
print(file_pdf.numPages)
for i in range(file_pdf.numPages):
    page_details = file_pdf.getPage(i)
    pdf1.addPage(page_details) # add to output page
password = 'Pass@123'
pdf1.encrypt(password)
with open("encryotedpdf.pdf","wb") as filename:
    pdf1.write(filename)

# logging implementation
import logging

logging.basicConfig(filename="Pay.txt",filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
for i in range(0,15):
    if (i%2==0):
        logging.warning('LOg warning msg')
    elif (i%3==0):
        logging.critical('log critical msg')
    else:
        logging.error('log error msg')

j = 10
try:
    j=j/0
except:
    logging.error('division by zero')





