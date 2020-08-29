import os, subprocess, math, argparse, ffmpeg


# How many chunks?
probe = ffmpeg.probe('videos/test.mp4')
info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
duration = math.ceil(float(info['duration']))
chunks = math.ceil(duration/5)


for i in range (chunks):    
    num = str(i).zfill(5)
    des = "videos/test/480_"  + num + '.mp4'

    input = ffmpeg.input('videos/test.mp4', ss=i*5, t=5)
    audio = input.audio.filter('atrim')
    vid1 = input.video.filter('scale', '640', '480')        # -1:480 doesn't work, but 480:-1 does
    vid2 = input.video.filter('scale', '1280', '720')
    vid3 = input.video.filter('scale', '1280', '1024')      # 1920:1080 cause malloc error
    
    
    ffmpeg.output(audio, vid1, des, strict='-2').run()
    des = des.replace('480_', '720_')
    ffmpeg.output(audio, vid2, des, strict='-2').run()
    des = des.replace('720_', '1024_')
    ffmpeg.output(audio, vid3, des, strict='-2').run()
