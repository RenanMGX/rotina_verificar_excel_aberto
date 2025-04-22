import xlwings as xw
from xlwings.main import Book
from datetime import datetime, timedelta
from .files_control import FilesControl

class ExcelVerify:
    @staticmethod
    def close_excel(time:timedelta=timedelta(hours=2)):
        file_control = FilesControl()
        file_control.limpar()
        for app in xw.apps:
            try:
                for book in app.books:
                    book:Book
                    if file_control.verify_file(book.name, time=time, deleteIfTrue=True):
                        book.close()
                    if len(xw.apps) <= 0:
                        app.kill()
            except:
                pass
                    
if __name__ == "__main__":
    ExcelVerify.close_excel()