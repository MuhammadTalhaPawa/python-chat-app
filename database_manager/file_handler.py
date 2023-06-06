def make_new_file(file_name):
    with open(file_name,'w') as file:
        print('new file created with name :',file_name)


def append_in_file(file_name,text_to_append):
    with open(file_name,'a') as file:
        file.write(text_to_append + '\n')
        print('File :',file_name, 'apended with :',text_to_append)
