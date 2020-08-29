import os, subprocess, math


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
