import os
import re

def organize(directory, keyword='(d|D)ay_?(\d+)', folder_name='Day_', regex=True):

    if not regex:
        folder_name=keyword
        keyword = re.escape(keyword)
        print(keyword)

    os.chdir(directory)
    folder_checks = []

    for item in os.listdir():
        if os.path.isdir(item):
            if re.match(keyword, item):
                print('match found')
                pass
            elif (item not in ['.git', 'README.md', ]):
                folder_checks.append(os.path.join(directory, item))
        else:
            finder = re.findall(keyword, item)
            if finder:
                try:
                    number = int(finder[0][1])
                except ValueError:
                    number = ''
                if len(str(number)) == 1:
                    number = '0' + str(number)
                try:
                    os.mkdir(folder_name + str(number))
                except FileExistsError:
                    pass

                os.rename(item, os.path.join(directory, folder_name + str(number), item))

    for folder in folder_checks:
        organize(folder)
