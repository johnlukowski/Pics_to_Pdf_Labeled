"""
#   generate_docx.py
#   By John Lukowski (lukowskijohn@gmail.com)
#   December 25, 2017
#
#   For the purpose of programatically inserting photos into a
#   formatted docx, to be converted later into a pdf file.
#   Used in the program 'pics2pdf'
#
#   Last edited 12/29/2017 by John Lukowski
"""

"""
#   Delete the paragraph passed as a param
#   Be careful not to try to access the deleted paragraph again
#   Source: https://github.com/python-openxml/python-docx/issues/33#issuecomment-77661907
#   From scanny, Mar 6, 2015
#   Accessed on December 25, 2017
"""
def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None


### Imports
import os
from os import listdir
from os.path import isfile, join
from docx import Document
from docx.shared import Inches

### Variables (table_width and incriment)
t_w = 2
i = 0

### Get the photo path
path = os.path.abspath('..') + "\\Photos\\"

### Import the photos to a list, get the length
photos = [f for f in listdir(path) if isfile(join(path, f))]
num_photos = len(photos)

### Create a word docx
### Make a table using the saved format (no borders)
document = Document('template.docx')
delete_paragraph(document.paragraphs[0])
table = document.add_table(1,t_w)
table.style = 'blank'
table.autofit = True

### Extend the table based on num_photos,
### blank rows for between each photo row
while(len(table.rows) <= num_photos/t_w*2):
    table.add_row()

### Add each photo into a table cell (controls formating)
for photo in photos:
    print(str(100*i/num_photos) + '% complete')
    ### Edit in the first paragraph of each cell
    p = table.rows[i/t_w*2].cells[i%t_w].paragraphs[0]
    r = p.add_run()
    
    ### Add a scaled picture to the current paragraph
    r.add_picture(path + photo, width=Inches(6.0/t_w))
    r.add_text(photo)
    i += 1

### Save and close the document
document.save('output.docx')
