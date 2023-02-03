# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия

decompress = 'AABCCDDDDFEE'
compress = ''
count = 1
for i in range(len(decompress) - 1):
    if decompress[i] == decompress[i+1]:
        count += 1
    else:
        compress += str(count) + decompress[i]
        count = 1
else:
    compress += str(count) + decompress[i]
print(compress)