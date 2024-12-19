from pydub import AudioSegment  
import math  
import os  

#把一个mp3文件，分隔成20M大小的文件，码率128kbps，并且按顺序重命名
def split_mp3(file_path, output_dir, target_size_mb=19, bitrate="128k"):
    audio = AudioSegment.from_mp3(file_path)
    target_size_bytes = target_size_mb * 1024 * 1024
    segment_duration_ms = (target_size_bytes * 8) / (int(bitrate[:-1]) * 1000) * 1000

    total_segments = math.ceil(len(audio) / segment_duration_ms)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    for i in range(total_segments):
        start_time = i * segment_duration_ms
        end_time = start_time + segment_duration_ms
        segment = audio[start_time:end_time]
        segment.export(f"{output_dir}/part{i+1}.mp3", format="mp3", bitrate=bitrate)
        print(f"Exported part{i+1}.mp3")  
  
# Example usage  
input_mp3_file = "/Users/ld/Downloads/IP增长/02产品搭建篇.mp3"  
output_directory = "/Users/ld/Downloads/IP增长/tmp"  
split_mp3(input_mp3_file, output_directory)  
