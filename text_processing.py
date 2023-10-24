# ##write to text file
# with open('file2.txt', 'w') as file:
#   file.write('First text\n\n')
#   file.write('Second text')

#   content = """
#   Text 1

#   Text 2"""

#   file.write(content)

# ##read to text file
# with open('file1.txt', 'r') as file:
#   content = file.read()
# print(content)

# ##update file
# with open('file3.csv', 'r') as file:
#   content = file.read()

# modified_content = content[:-1]

# with open('file3_update.csv', 'w') as file:
#   file.write(modified_content)

# ##read and rewrite multiple files
# from pathlib import Path

# files_dir = Path('files')

# for filepath in files_dir.iterdir():
#   with open(filepath, 'r') as file:
#     content = file.read()
#     new_content = content[:-1]
#     new_content = content.replace('amount', 'units')

#   with open(filepath, 'w') as file:
#     file.write(new_content)

##read and rewrite multiple files
from pathlib import Path

files_dir = Path('files')

merged = ''
for index, filepath in enumerate(files_dir.iterdir()):
  with open(filepath, 'r') as file:
    content = file.readlines()
    new_content = content[1:]

  if index == 0:
    content[0] = 'ID,AMOUNT,COST\n'
    merged += ''.join(content) + '\n'
  else:
    merged += ''.join(new_content) + '\n'

  with open('merged.csv', 'w') as file:
    file.write(merged)
