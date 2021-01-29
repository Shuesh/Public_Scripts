import PyPDF2                                   #work with data from PDF files
import xlsxwriter                               #create a new xcel sheet comparison
import getpass                                  #this module to get the user's username so that the new excel file can be placed in Downloads

workbookName = input('New workbook name: ')     #initialize new workbook
username = getpass.getuser()
workbookFullPath = 'C:\\Users\\' + str(username) + '\\Downloads\\' + str(workbookName) + '.xlsx'
workbook = xlsxwriter.Workbook(workbookFullPath)
worksheet = workbook.add_worksheet()            #add exception handler for invalid characters and names

while True:                                     #force the user to specify how many documents (as an integer)
    try:
        numPDFs = int(input('How many documents? '))
        break
    except:
        print('Please enter an integer. ')

pdfList = []                                    #collect all the PDF paths in a list
openPDFsList = []
for i in range(numPDFs):
    j = i+1
    pdfPath = input(f"Full path of document {j}: ")
    while True:
        try:
            openPdfDoc = PyPDF2.PdfFileReader(pdfPath)
            openPDFsList.append(openPdfDoc)
            break
        except Exception as e:
            print(e)
            pdfPath = input(f"Please enter a valid path for the document {j}: ")   
    pdfList.append(pdfPath)

worksheet.write('A1', 'This workbook compares the following PDF documents:') #put a header at the top of the document and list the compared PDFs
cellrow = 1
for pdf in pdfList:
    cellrow += 1
    cell = 'A' + str(cellrow)
    worksheet.write(cell, pdf)


for pdf in openPDFsList: #close everything
    pdf.close()
workbook.close()