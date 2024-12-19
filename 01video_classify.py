import re  
from collections import defaultdict  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.cluster import KMeans  
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS  
import numpy as np  
import os 
import json

# 脚本介绍
# 本脚本用于对指定目录下的文件夹进行聚类，输出每个类别的关键词。（适用于视频课程分类）
  
# 配置项：目录路径  
directory_path = '/Users/ld/Downloads'  
  
# 配置项：停用词
stop_words = {'合集', '全套', '课程', '训练营', '视频课', '实操', '教程', '合集'}
  
 # 获取指定目录下的所有文件夹名称  
def get_folder_names(directory):  
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]  
    return folders 
# 获取文件夹名称列表  
folders = get_folder_names(directory_path) 
# 数据预处理（去掉数字和特殊字符）  
def preprocess(text):  
    text = re.sub(r'\d+', '', text)  # 移除数字  
    text = re.sub(r'[^\w\s]', '', text)  # 移除特殊字符  
    return text  
  
folders_processed = [preprocess(folder) for folder in folders] 
folders_processed = [folder for folder in folders_processed if folder]  # 移除空字符串  
print("Processed folders:", folders_processed)  
 

# 使用TF-IDF向量化  
combined_stop_words = list(ENGLISH_STOP_WORDS.union(stop_words))  # 将集合转换为列表  
vectorizer = TfidfVectorizer(stop_words=combined_stop_words)  
X = vectorizer.fit_transform(folders_processed)  
  
# 使用KMeans聚类  
num_clusters = 7  # 你可以根据需要调整聚类数量  
kmeans = KMeans(n_clusters=num_clusters, random_state=0)  
kmeans.fit(X)  
  
# 获取每个类别的关键词  
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]  
terms = vectorizer.get_feature_names_out()  
category_keywords = defaultdict(list)  
  
for i in range(num_clusters):  
    category_name = f"Category {i+1}"  
    for ind in order_centroids[i, :10]:  # 获取每个聚类前10个关键词  
        category_keywords[category_name].append(terms[ind])  

# 格式化输出为指定格式的字典  
categories = {}  
for i, (category, keywords) in enumerate(category_keywords.items()):  
    category_name = f"Category {i+1}"  
    categories[category_name] = keywords  
  
# 打印结果  
print(json.dumps(categories, ensure_ascii=False, indent=4))  
