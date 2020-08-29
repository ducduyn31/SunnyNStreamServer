import os, subprocess, math


# create folder to store chunks; folder same name as file
"""
parent_dir = "C:/Users/Hoang/Documents/project1/SunnyNStreamServer"
# get video name to src         then        src = 'videos/' + src       OR
src = 'videos/test2.mp4'
dir = src.replace('.mp4', '')

path = os.path.join(parent_dir, dir)            
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)
"""


src = 'videos/test2.mp4'
cmd = 'ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 ' + src
output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


len = math.ceil(float(output.stdout))
chunks = math.ceil((len/5))

# ffmpeg -i videos/test.mp4 -vf scale=640:480 -ss 0 -t 5 -strict -2 videos/test/480_00000.mp4
# ffmpeg -i videos/test.mp4 -vf scale=1280:720 -ss 0 -t 5 -strict -2 videos/test/720_00000.mp4
# ffmpeg -i videos/test.mp4 -vf scale=1280:1024 -ss 0 -t 5 -strict -2 videos/test/1080_00000.mp4

video = '  ffmpeg -i "src" -vf scale=640:480 -ss start -t 5 -strict -2 "des" ' # aac is experimental, use -strict -2 BEFORE the last argument

for i in range(chunks):
    
    # modify cmd    
    num = str(i).zfill(5)                               # file name suffix    
    cmd = video.replace('src', src)                     # source file path
    cmd = cmd.replace('start', str(i*5))                # starting position for cutting
    des = src.replace('.mp4', '/480_' + num + '.mp4')   # destination file name
    cmd = cmd.replace('des', des)                       # destination file path    
    subprocess.run(cmd, shell=True)
    
    cmd = cmd.replace('640:480', '1024:720')            # resolution
    cmd = cmd.replace('480_', '720_')                   # destination file name
    subprocess.run(cmd, shell=True)

    cmd = cmd.replace('1024:720', '1280:1024')    
    cmd = cmd.replace('720_', '1024_')
    subprocess.run(cmd, shell=True)










"""
for i in range(chunks):

    # modify cmd
    num = str(i).zfill(5) # file name suffix
    des = src.replace('.mp4', '/480_' + num + '.mp4') # modify destination files
    cmd = video.replace('src', src)  # get the source file
    cmd = cmd.replace('start', str(i*5))# get the starting position for cutting
    cmd = cmd.replace('des', des)  # get the destination file
    subprocess.run(cmd, shell=True)

    cmd = cmd.replace('480', '720')  # get the destination file
    subprocess.run(cmd, shell=True)

    cmd = cmd.replace('720', '1080')  # get the destination file
    subprocess.run(cmd, shell=True)
"""




# not working 
"""

src = 'videos/test.mp4'
f = open(src, 'r')
# subprocess.run("mkdir videos/test", shell=True) # not working
# to do - create a folder with the same name as the file
# possible: use grep to find extension and delete it, then use the name to create a folder

video = 'ffmpeg -i src -an -acodec copy des'
audio = 'ffmpeg -i src -f mp3 -ab 192000 -vn des'


# ' ffmpeg -i src -f mp3 -ab 192000 -vn des '
# " ffmpeg -i src -vn -acodec copy des "

for i in range(chunks):
    num = str(i).zfill(5) # file name suffix
    #vDes = src.replace('.mp4', '/' + num + '.mp4') # modify destination files
    aDes = src.replace('.mp4', '/' + num + '.mp3')  # modify destination files
    cmd = video.replace('src', src) # get the source file
    cmd = cmd.replace('start', str(i*5))# get the starting position for cutting
    cmd = cmd.replace('des', aDes)  # get the destination file

print(cmd)
# subprocess.run(cmd, shell=True)

"""

# working
"""
temp = '  ffmpeg -i "src" -ss start -t 5 -strict -2 "des" '

for i in range(chunks):

# modify cmd

num = str(i).zfill(5) # file name suffix
des = src.replace('.mp4', '/' + num + '.mp4') # modify destination files

cmd = temp.replace('src', src)  # get the source file
cmd = cmd.replace('start', str(i*5))# get the starting position for cutting
cmd = cmd.replace('des', des)   # get the destination file
subprocess.run(cmd, shell=True)
"""

