'''THIS IS A PYTHON 2 CODE'''

import pyPdf

from  pyPdf import PdfFileReader
file = PdfFileReader(open('path\to\file.pdf','rb'))  # First open the file and then pass the object as an args to the PdfFileReader
info = file.getDocumentInfo()  # Returns a dictionary

for meta_item in info:
    print "{}     Info: {}".format(meta_item,info[meta_item])
