# ex2_2.py
hex_number1 = "a0ff"
hex_number2 = "121ab"
hex_number3 = "acd123"
print('(a) 16進位轉10進位:')
print('   ',hex_number1,'->', int(hex_number1, 16))
print('   ',hex_number2,'->', int(hex_number2, 16))
print('   ',hex_number3,'->', int(hex_number3, 16))

oct_number1 = "7231"
oct_number2 = "754"
oct_number3 = "567"
print('\n(b) 8進位轉10進位:')
print('   ',oct_number1,'->', int(oct_number1, 8))
print('   ',oct_number2,'->', int(oct_number2, 8))
print('   ',oct_number3,'->', int(oct_number3, 8))

bin_number1 = "11001010"
bin_number2 = "1001001"
bin_number3 = "110101000100010110"
print('\n(c) 2進位轉10進位:')
print('   ',bin_number1,'->', int(bin_number1, 2))
print('   ',bin_number2,'->', int(bin_number2, 2))
print('   ',bin_number3,'->', int(bin_number3, 2))

'''output---------------------------------
(a) 16進位轉10進位:
    a0ff -> 41215
    121ab -> 74155
    acd123 -> 11325731

(b) 8進位轉10進位:
    7231 -> 3737
    754 -> 492
    567 -> 375

(c) 2進位轉10進位:
    11001010 -> 202
    1001001 -> 73
    110101000100010110 -> 217366
---------------------------------------'''