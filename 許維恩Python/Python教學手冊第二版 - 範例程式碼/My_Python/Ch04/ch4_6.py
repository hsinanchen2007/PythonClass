# ch4_6.py, 根據氣溫提供適當的穿衣或防護建議
temp = int(input('請輸入氣溫: \xB0C): ')) 
humidity = int(input('請輸入濕度(%): '))

if temp < 15:  # 若氣溫低於15度
    if humidity > 80:  # 若濕度高於80%
        print('很冷且潮濕，穿厚外套和防水衣')
    else:
        print('很冷，穿厚外套')
elif temp <= 30:  # 若氣溫介於15到30度
    if humidity > 80:  # 若濕度高於80%
        print('舒適但潮濕，穿輕便防水衣')
    else:
        print('舒適，輕便穿搭')
else:  # 若氣溫高於30度
    if humidity > 80:  # 若濕度高於80%
        print('炎熱且潮濕，多喝水並穿輕便防水衣')
    else:
        print('炎熱，多喝水並防曬')