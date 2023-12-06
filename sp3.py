import argparse
import subprocess
import re
import os
import io
import numpy as np
import json


###################
### ALL METHODS ###
###################

class VideoConverter:
    def convert_video_resolution(input_file, output_file, resolution):
        command = f'ffmpeg -i {input_file} -vf "scale={resolution}" {output_file}'
        subprocess.run(command, shell=True)

    def convert_video_codec(input_file, output_file, codec):
        try:
            if codec.lower() == "vp8":
                cmd = f'ffmpeg -i "{input_file}" -c:v libvpx -b:v 0 {output_file}_{codec}.webm'
            elif codec.lower() == "vp9":
                cmd = f'ffmpeg -i "{input_file}" -c:v libvpx-vp9 -b:v 0 {output_file}_{codec}.webm'
            elif codec.lower() == "h265":
                cmd = f'ffmpeg -i "{input_file}" -c:v libx265 -b:v 0 {output_file}_{codec}.mp4'
            elif codec.lower() == "av1":
                cmd = f'ffmpeg -i "{input_file}" -c:v libaom-av1 -b:v 0 {output_file}_{codec}.mkv'
            subprocess.run(cmd, shell=True, check=True)
            print(f"Conversion to {codec} completed. Output file: {output_file}")

        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")   

class VideoComparison:
    def create_comparison_video(codec_1, codec_2):
        output_file = f'./InputFiles/VideoComparison/bbb_{codec_1}_vs_{codec_2}.mp4'
        if codec_1 == "vp8" or codec_1 == "vp9":
            codec1new = "webm"
            input_file_1 = f'./InputFiles/Codecs/bbb_{codec_1}.webm'
        if codec_2 == "vp8" or codec_2 == "vp9":
            input_file_2 = f'./InputFiles/Codecs/bbb_{codec_2}.webm'
            codec2new = "webm"
        if codec_1 == "h265":
            input_file_1 = f'./InputFiles/Codecs/bbb_{codec_1}.mp4'
            codec1new = "mp4"
        if codec_2 == "h265":
            input_file_2 = f'./InputFiles/Codecs/bbb_{codec_2}.mp4'
            codec2new = "mp4"
        if codec_1 == "av1":
            input_file_1 = f'./InputFiles/Codecs/bbb_{codec_1}.mkv'
            codec1new = "mkv"
        if codec_2 == "av1":
            input_file_2 = f'./InputFiles/Codecs/bbb_{codec_2}.mkv'
            codec2new = "mkv"
        try:
            #filter_complex [0:v][1:v]hstack -c:v libx264 -crf 23 -c:a aac -b:a 192k"
            subprocess.run(['ffmpeg', '-i', input_file_1, '-i', input_file_2, '-filter_complex', '[0:v]setpts=PTS-STARTPTS[left];[1:v]setpts=PTS-STARTPTS[right];[left][right]hstack[output]', '-map', '[output]', '-c:v', 'libx264', output_file], check=True)
            print(f"Comparison video created. Output file: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during video comparison: {e}")



##################
###    MAIN    ###
##################

resolutions = ['1280:720', '640:480', '320:240', '160:120']
codecs = ['vp8', 'vp9', 'h265', 'av1']


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="SCAV Video Lab 3")
    parser.add_argument("--convert_video_resolution", action="store_true", help="Convert Video to 4 different resolutions")
    parser.add_argument("--convert_video_codec", action="store_true", help="Convert Video to 4 different codecs")
    parser.add_argument("--compare_videos", nargs=2, help="Compare 2 videos codec")
    args = parser.parse_args()

    if args.convert_video_resolution:
        for resolution in resolutions:
            input_file = './InputFiles/original_bbb_60.mp4'
            width, height = resolution.split(':')
            output_file = f'./InputFiles/Resolutions/bbb_{width}x{height}p.mp4'
            VideoConverter.convert_video_resolution(input_file, output_file, resolution)
            print(f"Video Completed. Output file: {output_file}")
        
        #python3 sp3.py --convert_video_resolution

    if args.convert_video_codec:
        for codec in codecs:
            input_file = './InputFiles/original_bbb_60.mp4'
            output_file = f'./InputFiles/Codecs/bbb'
            VideoConverter.convert_video_codec(input_file, output_file, codec)
            print(f"Video Completed. Output file: {output_file}")
    
        #python3 sp3.py --convert_video_codec

    if args.compare_videos:
        codec_1, codec_2 = args.compare_videos
        VideoComparison.create_comparison_video(codec_1, codec_2)

        #python3 sp3.py --compare_videos vp8 vp9
        #python3 sp3.py --compare_videos libx265 libaom-av1    