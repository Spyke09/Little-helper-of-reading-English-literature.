import PyPDF2
from program.utils import get_root


def choice(path: str) -> str:
    t = path.split('.')[-1]
    if t == 'txt':
        return path
    if t == 'pdf':
        return converter_pdf(path)


def converter_pdf(path: str) -> str:
    pdffileobj = open(path, 'rb')
    d = path.split('/')[-1].split('\\')[-1].split('.')[0]
    dir_txt = str(get_root(f"program/converted/{d}.txt"))
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    file1 = open(dir_txt, "w")
    failures = 0
    for i in range(pdfreader.numPages):
        pageobj = pdfreader.getPage(i - 1)
        try:
            file1.writelines(pageobj.extractText())
        except:
            failures += 1

    pdffileobj.close()
    file1.close()
    return dir_txt
