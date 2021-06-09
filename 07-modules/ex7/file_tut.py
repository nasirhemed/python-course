import os


def replace_name(filename, original, replaced):

    f = open(filename, 'r')
    content = f.read()
    replaced = content.replace(original, replaced)
    f.close()
    # open (filename) as read
    # var = read the contents of the file as str
    # replaced = var.replace(original, replaced)
    # close this file

    with open(filename, 'w') as f:
        f.write(replaced)


    # open (filename) as write
    # write the contents
    # close this file






story_files = os.listdir('./story/')


name = "Nasir" # You can put your name here instead

print(story_files)
for filename in story_files:
    replace_name('story/{}'.format(filename), 'OLIVER', name)
