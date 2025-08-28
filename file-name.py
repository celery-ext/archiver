import os
file_names = os.listdir('./')
new_list = file_names[2]

new_file_name = os.listdir('./'+file_names[2])
print(new_file_name)