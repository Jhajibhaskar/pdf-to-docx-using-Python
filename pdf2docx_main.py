# First run 'pip install ' in terminal of pycharm then execute the below program
from pdf2docx import Converter
pdf_file='Example1.pdf'
docx_file='pdf2docx1.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()