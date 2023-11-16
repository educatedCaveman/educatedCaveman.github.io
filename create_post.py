import datetime
import pytz
import os
import subprocess

def get_dirs(path):
    ls = os.listdir(path)
    dirs = []
    for x in ls:
        relative_path = '/'.join([path, x])
        if os.path.isdir(relative_path) and relative_path.split('/')[-1] != "_posts":
            dirs.append(x)

    return dirs


def yes_no_to_bool(input):
    if input == 'y':
        return True
    else:
        return False


# collect basic info
title = input('what is the title of the post?:  ')
tz_str = 'America/New_York'
tz = pytz.timezone(tz_str)
current_date = tz.localize(datetime.datetime.now())
date_string = current_date.strftime('%F %T %z')
category_tag = input('what categories/tags should be added to the post (comma separated)?:  ')
docs_root = 'documentation'


#! defer creating the post text until after we know the file path to save

# interactively get the save path
prompt = True
working_path = [docs_root]
while prompt:

    dirs = get_dirs('/'.join(working_path))
    header = (f"select a directory (0-{len(dirs)+1}:\n"
        "(x: exit, b: back/up, t: file tree, c: create directory)\n")
    print(header)

    print(f'\t0\t(current directory)')
    for i in range(0, len(dirs)):
        print(f"\t{i+1}\t{dirs[i]}")

    choice = input('\nselection:  ').lower()

    # determine if the choice is an int
    try:
        int(choice)
        int_choice = True
        choice = int(choice)
    except:
        int_choice = False

    # selecting a directory
    if int_choice:
        # current directory
        if choice == 0:
            confirm = yes_no_to_bool(input('use current directory? (y/n)  '))
            if confirm:
                prompt = False

        # other selected directory
        else:
            if choice > len(dirs):
                print('invalid directory selection. try again.')
            else:
                working_path.append(dirs[choice -1])
    
    # one of the other special options
    else:
        if choice == 'x':
            confirm = yes_no_to_bool(input('confirm exit? (y/n)  '))
            if confirm:
                prompt = False

        elif choice == 'b':
            if len(working_path) > 1:
                working_path.pop()
            else:
                print('invalid directory selection. try again.')

        elif choice == 't':
            tree = subprocess.check_output(['tree', '/'.join(working_path)], text=True)
            print(tree)

        elif choice == 'c':
            new_dir = input('name of directory to create?:  ')
            working_path.append(new_dir)
            os.mkdir('/'.join(working_path))



# add paths to tags/categories
path_tags = ', '.join(working_path)
category_tag += path_tags

header = f"""---
title: {title}
date: {date_string}
categories: [{category_tag}]
tags: [{category_tag}]
---
"""

# write file
suggest_file = f"{current_date.date().strftime('%F')}-{title}.md"
print(f'suggested file path:  {suggest_file}')
confirm = yes_no_to_bool(input('use this file name?: (y/n)  ').lower())
if confirm:
    filename = suggest_file
else:
    filename = input('what file name to use:  ')
working_path.append(filename)
full_path = '/'.join(working_path)
with open(full_path, 'w') as f:
    f.write(header)
