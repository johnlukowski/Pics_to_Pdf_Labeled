Pic_to_Pdf

Includes:
convert.bat, pics2pdf.bat, generate_docx.py, template.docx

Temporary Files:
output.docx

Dependencies:
Python 2.7 (may work with newer)
DOCX-0.8.6 for python

Written By John Lukowski (lukowskijohn@gmail.com)

For the purpose of assisting Lukowski Consulting Inc

Takes a folder of image files, feeds them through generate_docx to create a formatted
word document with the images in it. Each photo's name is written directly underneath 
it in the same table cell. Used a clear bordered table for the formatting.
The template.docx holds the formatting for the table. 

The output.docx is converted to a pdf using convert.bat and the docx is deleted.

convert.bat runs using unoconv and libre office to convert the output.docx to a pdf.

pics2pdf.bat handles both programs, and makes sure output.docx is saved before 
running the conversion. 

The resulting pdf is in the highest level directory (Pics_to_Pdf) titled 'Final_Product.pdf'

Ignore the multiple command window popups, I dont know how to hide them
