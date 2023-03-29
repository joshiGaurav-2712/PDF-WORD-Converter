#PDF to WORD
from pdf2docx import Converter


old_pdf="sample.pdf"

name=input("Enter the name by which you want to save the word file:")

new_doc=f"{name}.docx"

obj=Converter(old_pdf)  #making object of Converter class

obj.convert(new_doc)    #using convert method of Converter class

obj.close()



# WORD TO PDF

# from docx2pdf import convert
# pdf_name=input("Enter the name by which you want to save the pdf file:")
# convert("sample.docx",f"{pdf_name}.pdf")