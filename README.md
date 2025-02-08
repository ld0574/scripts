# 项目简介

该项目包含了一系列 Python 脚本，每个脚本都用来完成特定的任务。下面是每个脚本的简要介绍：

## 文件列表

| 文件名              | 简介                                  |
| ------------------- | ------------------------------------- |
| 01video_classify.py | 用来分类视频的脚本。                  |
| 02mp3_split.py      | 用来将 MP3 文件分割成多个部分的脚本。 |
| 03transcription.py  | 用来进行语音识别文字的脚本。          |
| plugin-bar.html     | notion 时间进度插件。                 |

## 使用说明

1. 确保已经安装了 Python 3.x 版本。
2. 克隆或下载该项目的代码到本地。
3. 更新配置文件，重命名.env.example 为.env，根据实际情况修改配置
4. 根据需要运行对应的脚本。例如，运行`01video_classify.py`：
   ```sh
   python 01video_classify.py
   ```

## 依赖项

部分脚本可能需要额外的 Python 库。请参考每个脚本的开头部分，那里通常会有关于依赖项的说明。例如，`02mp3_split.py`可能需要`pydub`和`audioop-lts`库：

```sh
pip install requests audioop-lts
```

## 贡献

如果你有任何改进或新的功能想要添加，欢迎提交 Pull Request。同时，你也可以在 Issues 部分提出问题和建议。

## 许可证

该项目遵循 MIT 许可证。详细信息请参阅 LICENSE 文件。
