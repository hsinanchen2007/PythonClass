# ch5_5.py, 剪裁數字
def clip(lst, minv, maxv):
    new_lst = []			# 存放剪裁後的數字
    for n in lst:
        if n < minv:
            new_lst.append(minv)   # n<minv,將minv添加到new_lst
        elif n > maxv:
            new_lst.append(maxv)   # n>maxv,將maxv添加到new_lst
        else:
            new_lst.append(n)      # 添加原來的元素到new_lst
    return new_lst

# 主程式,測試函數
nums = [3, 7, 2, 9, 5, 12, 1]
print(clip(nums, 4, 10))