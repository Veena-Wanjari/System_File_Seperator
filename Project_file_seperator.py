import os, shutil
#We can write every single extention inside tuples
# audio_extentions = ('.mp3', '.mp4', '.wav', '.flac')
# video_extentions = ('MP4', '.mkv', '.MKV', '.flv', '.mpeg')
# document_extentions = ('.doc', '.pdf', '.txt')
# image_extentions = ('png', '.gif', '.psd')

dict_extentions = {
    'audio_extentions' : ('.mp3', '.mp4', '.wav', '.flac'),
    'video_extentions' : ('.MP4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extentions' : ('.doc', '.pdf', '.txt'),
    'image_extentions' : ('png', '.gif', '.psd')

                   }


folder_path = input("Enter folder path: ")

def file_finder(folder_path, file_extentions):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files.append(file)
    return files

#print(file_finder(folder_path, image_extentions))

for extention_type, extention_tuple in dict_extentions.items():
    # print('calling file finder')
    # print(file_finder(folder_path, extention_tuple))
    folder_name = extention_type.split('-')[0] + 'Files'
    new_folder_path = os.path.join(folder_path, folder_name) 
    os.mkdir(new_folder_path)
for item in (file_finder(folder_path, extention_tuple)):
    item_path = os.path.join(folder_path, item)
    item_new_path = os.path.join(new_folder_path, item)
    shutil.move(item_path, item_new_path)
