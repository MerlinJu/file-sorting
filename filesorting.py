import os

sorterfile = 'filesorting.py'
dircategories = ['documents', 'images', 'videos', 'audios']
category_extension = {
    'documents': ['.pdf', '.docx', '.txt'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'videos': ['.mp4', '.avi', '.mkv'],
    'audios': ['.mp3', '.wav', '.flac', '.ogg'],
}

allfiles = []
directory = os.getcwd()


#create directories for file categories
for categories in dircategories:
    try:
        os.makedirs(os.path.join(directory, categories), exist_ok=False)
    except OSError:
        print('Error creating directory')
        break


#put all files into a list except the py files and directories
for file in os.listdir(directory):
    if file == sorterfile:
        continue
    if os.path.isfile(file):
        allfiles.append(file)

#move files to the defined directories
for file in allfiles:
    file_extension = '.' + file.split('.')[-1].lower()
    print(file_extension)
    #go through all categories
    for category in dircategories:
        #and check if file extension matches the category specifed extensions ( if not it goes to the next catgeory in the loop)
        if file_extension in category_extension.get(category, []):
            #sets up the destination of current directory, the destiantion category name and the file which is moved
            destination = os.path.join(directory, category, file)
            #renames or assigns the old file the the new destiantion 
            os.rename(file, destination)