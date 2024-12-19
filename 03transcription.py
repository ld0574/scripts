import os  
from dotenv import load_dotenv
import requests  
  
#1.遍历指定的文件夹路径以查找所有 MP3 文件。
#2.对找到的 MP3 文件进行排序。
#3.调用指定的 API 将音频文件转换为文本。
#4.将生成的文本拼接成一个完整的字符串。
#5.将结果导出为一个 TXT 文件。
def get_sorted_mp3_files(directory):  
    """获取排序后的MP3文件列表"""  
    files = [f for f in os.listdir(directory) if f.endswith('.mp3')]  
    files.sort()  
    return [os.path.join(directory, f) for f in files]  
  
def transcribe_audio(file_path):  
    """调用API将音频文件转换为文本"""  
    authorization = os.getenv('Siliconflow_Authorization')
    url = 'https://api.siliconflow.cn/v1/audio/transcriptions'  
    headers = {  
        'Authorization': 'Bearer ' + authorization,  
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',  
        'Accept': '*/*',  
        'Host': 'api.siliconflow.cn',  
        'Connection': 'keep-alive',  
    }  
    files = {  
        'file': open(file_path, 'rb'),  
    }  
    data = {  
        'model': 'FunAudioLLM/SenseVoiceSmall',  
    }  
      
    response = requests.post(url, headers=headers, files=files, data=data)  
    response.raise_for_status()  
    return response.json().get('text', '')  
  
def generate_transcription(directory, output_file):  
    """生成转录文本并保存为TXT文件"""  
    mp3_files = get_sorted_mp3_files(directory)  
    full_text = ""  
      
    for file_path in mp3_files:  
        print(f"Transcribing {file_path}...")  
        text = transcribe_audio(file_path)  
        full_text += text + "\n"  
      
    with open(output_file, 'w', encoding='utf-8') as f:  
        f.write(full_text)  
      
    print(f"Transcription complete. Output saved to {output_file}")  
  
# 示例使用  
load_dotenv()
directory = '/Users/ld/Downloads/IP增长/tmp'  
output_file = '/Users/ld/Downloads/IP增长/tmp/transcription_output.txt'  
generate_transcription(directory, output_file)  
