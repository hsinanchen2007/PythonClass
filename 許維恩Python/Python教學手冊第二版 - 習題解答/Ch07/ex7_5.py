# ex7_5.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"{self.title} 作者為 {self.author}，共{self.pages}頁。")

# 測試
book = Book('Python', 'Jerry', 180)
book.summary()  # 輸出: Python 作者為 Jerry，共180頁。

'''output----------------------------------------
Python 作者為 Jerry，共180頁。
----------------------------------------------'''