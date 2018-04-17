import os, shutil

#Friends.S03E01.576p.BluRay.DD5.1.x264-HiSD
#friends.s03e01.720p.bluray.x264-psychd

path = '/home/emre/Videolar/Diziler/Friends.S03.576p.BluRay.DD5.1.x264-HiSD/altyazi/'
new_path = '/home/emre/Videolar/Diziler/Friends.S03.576p.BluRay.DD5.1.x264-HiSD/'

def change(dir_path, old_srt, new_srt):
    for path, subdirs, files in os.walk(dir_path):
        for name in files:
            if(old_srt.lower() in name.lower()):
                os.rename(os.path.join(path,name), os.path.join(path, name.lower().replace(old_srt,new_srt)))

change(path, '720p', '576p')
change(path, 'psychd', 'HiSD')
change(path, 'bluray', 'BluRay.DD5.1')

srt_files = os.listdir(path)
srt_files.sort()
for f in srt_files:
    source=path+f
    destination=new_path+f
    shutil.move(source,destination)