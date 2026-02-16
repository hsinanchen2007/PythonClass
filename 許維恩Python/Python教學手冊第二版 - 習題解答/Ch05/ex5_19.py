# ex5_19.py
x = 'amazing'  # 全域變數 x
def func():
    x = 'impressive'  # 區域變數 x
    print('Python is ' + x)

func()
print('Python is ' + x)  # 使用全域變數 x

'''output--------------------
Python is impressive
Python is amazing
--------------------------'''

'''說明----------------------------------------------------------------------
程式解析：
(a)	全域變數 x：
    在程式開始時，定義了全域變數 x 並設值 'amazing'。
(b)	在函數 func() 中的區域變數 x：
    在 func() 函數中，重新定義了變數 x，並設值 'impressive'。
    這是區域變數，它只在 func() 函數的範圍內有效，並不影響全域變數 x 的值。
(c)	print('Python is ' + x) 在 func() 裡的輸出：
    在 func() 函數內部，使用的是該函數內部的區域變數 x（即 'impressive'）。
    因此，執行 print('Python is ' + x) 時會印出 'Python is impressive'。
(d)	print('Python is ' + x) 在 func() 之外的輸出：
    在 func() 函數執行完畢後，程式繼續執行外部的 print 語句。
    這裡使用的是全域變數 x（其值是 'amazing'）。
    因此，執行 print('Python is ' + x) 時會印出 'Python is amazing'。
結果：
 	在 func() 函數內部，會印出：Python is impressive
 	在函數外部，會印出：Python is amazing
核對程式執行的結果：
 	func() 內部的 x 是 區域變數，它並不影響全域變數 x。
 	func() 外部的 x 是 全域變數，所以在 func() 以外，x 仍然是 'amazing'。
------------------------------------------------------------------------'''