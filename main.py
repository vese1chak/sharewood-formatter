import os
# В качестве значения указать адрес необходимой директории (папки)
necessary_directory_name = r'C:\Users\vlad\PycharmProjects\formatter\mock-data - Copy - Copy' + '/'
# В качестве значения указать приписку у папок и файлов. В конце обязательно ставить пробел
removable_prefix = '[SW.BAND] '
# В качестве значения передать массив строк, содержащих названия рекламок. В конце обязтельно указать расширение
removable_filenames = ['[DMC.RIP] Качай редкие курсы!.url',
                       '[WWW.SW.BAND] 150000 курсов ждут тебя!.url',
                       '[WWW.SW.BAND] Прочти перед изучением!.docx']

def main():
    files = os.listdir(necessary_directory_name)
    for filename in files:
        if os.path.isdir(necessary_directory_name + filename):
            if removable_prefix in filename:
                new_filename = filename.replace(removable_prefix, '')
                os.rename(necessary_directory_name + filename, necessary_directory_name + new_filename)
                cur_directory = necessary_directory_name + new_filename + '/'
            else:
                cur_directory = necessary_directory_name + filename + '/'
            deep(cur_directory)
        elif removable_prefix in filename:
            new_filename = filename.replace(removable_prefix, '')
            os.rename(necessary_directory_name + filename, necessary_directory_name + new_filename)
        elif filename in removable_filenames:
            os.remove(necessary_directory_name + filename)


def deep(directory):
    files = os.listdir(directory)
    for filename in files:
        if os.path.isdir(directory + filename):
            if removable_prefix in filename:
                new_filename = filename.replace(removable_prefix, '')
                os.rename(directory + filename, directory + new_filename)
                cur_directory = directory + new_filename + '/'
            else:
                cur_directory = directory + filename + '/'
            deep(cur_directory)
        elif removable_prefix in filename:
            new_filename = filename.replace(removable_prefix, '')
            os.rename(directory + filename, directory + new_filename)
        elif filename in removable_filenames:
            os.remove(directory + filename)


if __name__ == '__main__':
    main()
    print('Успешно выполнено!')
