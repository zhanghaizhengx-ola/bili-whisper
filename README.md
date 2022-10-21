# Bilili 视频全字幕

课程自动笔记



过程是这样的，利用 `yt_dlp` 下载 `bili` 视频。利用 `whisper` 转写人声，为文字恢复标点。

`yt-dlp` 能够下载非常多的视频网站，这里我们用 `bili` 做例子。理论上yt-支持的其他网站也能用在这里。

`whisper` 是 `openai` 最近开源的 语音识别项目， 引发广泛讨论。它支持非常多种语言，在英语识别上性能卓越。但我们主要利用它的中文语音识别。

标点恢复 是 `ppasr` 公布的预训练模型， `ppasr` 在 `paddlespeech` 的基础上做了些优化。 模型在这里获取 `oss://xs-emr-data/user/hzane/paddle/pun_models.zip`


这里没有做成实时字幕流，是因为代码要多写一些才行，我不想写了。


## Install

```bash
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
conda install paddlepaddle-gpu==2.3.2 cudatoolkit=11.6 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge 
conda install transformers -c conda-forge
conda install yt-dlp -c conda-forge
pip install paddlenlp
pip install git+https://github.com/openai/whisper.git

python app.py

```

![Screenshot from 2022-10-21 17-44-23](https://raw.githubusercontent.com/hzane/md-images/main/typora/2022/10/21/17-45-39-8116bdcb838ee046b1ae67935b3702e5-9e0367.png)