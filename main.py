import math, argparse, ffmpeg, os
import numpy as np



parser = argparse.ArgumentParser(description='Cut videos')
parser.add_argument('-src', '--source', type=str, metavar='', required=True, dest='src', help='file path')
args = parser.parse_args()



def cut_vid(src):
    # How many chunks?
    probe = ffmpeg.probe(src)
    duration = math.ceil(float(next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')['duration']))
    chunks = math.ceil(duration/5)
    clen = 1        # chunk length
    
    # create directory for cut videos, same name as the source videos
    path = src.replace('.mp4', '/')
    if not os.path.exists(path):
        os.mkdir(path)

    # cut video: create a name, then join video+audio
    for i in range (chunks):    
                
        input = ffmpeg.input(src, ss=i*clen, t=clen)
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