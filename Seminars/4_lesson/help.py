# import os
# path = 'folder' + os.sep + 'file.txt' # 1
# path = os.path.join('folder', 'file.txt') # 2

# from pathlib import Path
# path = Path('file.txt')

path = 'folder/file.txt'

# 'a' - добавить и читать
# 'w' - писать
# 'r' - читать

with open(path, 'r') as f: # f - имя переменой можно любое
    # for line in data:
    #     print(line)
    
    data = f.readline()
    print(data)