import PyPDF2 as pd
from nbconvert.exporters import pdf
pdfiles = ["dsa1.pdf" , "insemSE.pdf" ]
merger = pd.PdfMerger()

for filename in pdfiles:
    pdfile = open(filename , 'rb')
    pdfReader = pd.PdfReader(pdfile)
    merger.append(pdfReader)
pdfile.close()
merger.write('merged1.pdf')
