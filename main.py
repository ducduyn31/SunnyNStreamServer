import math, argparse, ffmpeg
import numpy as np

parser = argparse.ArgumentParser(description='Cut videos')
parser.add_argument('-src', '--source', type=str, metavar='', required=True, dest='src', help='file path')
args = parser.parse_args()

def cut_vid(src):
    # How many chunks?
    probe = ffmpeg.probe(src)
    info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    duration = math.ceil(float(info['duration']))
    chunks = math.ceil(duration/5)
    clen = 1        # chunk length
    

    for i in range (chunks):    
                
        input = ffmpeg.input('videos/test.mp4', ss=i*clen, t=clen)
        audio = input.audio.filter('atrim')
        
        num = str(i).zfill(5)        
        h = '360'
        des = src.replace('.mp4', '/' + h + '_'  + num + '.mp4')        
        vid = input.video.filter('scale', '-2', h)        
        ffmpeg.output(audio, vid, des, strict='experimental').run()

        h = '480'
        des = src.replace('.mp4', '/' + h + '_'  + num + '.mp4')
        vid = input.video.filter('scale', '-2', h)    
        ffmpeg.output(audio, vid, des, strict='experimental').run()
        
        h = '720'
        des = src.replace('.mp4', '/' + h + '_'  + num + '.mp4')
        vid = input.video.filter('scale', '-2', h) 
        ffmpeg.output(audio, vid, des, strict='experimental').run()
    

if __name__ == '__main__':
    cut_vid(args.src)
























# backup, working program as of 2020 sep 01
"""
src = input('Please enter the file path: ')
# How many chunks?
probe = ffmpeg.probe(src)
info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
duration = math.ceil(float(info['duration']))
chunks = math.ceil(duration/5)
clen = 1        # chunk length


for i in range (chunks):    
    num = str(i).zfill(5)
    des = src.replace('.mp4', '/' + h + '_'  + num + '.mp4')
    #des = "videos/test/" + h + '_'  + num + '.mp4'

    input = ffmpeg.input('videos/test.mp4', ss=i*clen, t=clen)
    audio = input.audio.filter('atrim')
    vid = input.video.filter('scale', '-2', '360')
    
    ffmpeg.output(audio, vid, des, strict='experimental').run()

    # h = '480'
    # vid = input.video.filter('scale', '-2', h)    
    # ffmpeg.output(audio, vid, des, strict='experimental').run()
    # h = '720'
    # vid = input.video.filter('scale', '-2', h) 
    # ffmpeg.output(audio, vid, des, strict='experimental').run()
"""


