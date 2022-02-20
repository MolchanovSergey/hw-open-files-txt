list_files = ['1.txt', '2.txt','3.txt']
for file_name in list_files:
    with open(file_name, 'r', encoding='UTF-8') as fr, open('4.txt', 'a', encoding='UTF-8') as fw:
        count = 0
        fw.write(f'\n{file_name}\n')
        # fw.write(f'\n{len(file_name)}\n')
        for line in fr:
            count += 1
            fw.write(f'\n{count}\n')
            fw.write(line)

file = open('4.txt', encoding='UTF-8')
data = file.read()
print(data)
