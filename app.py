import gradio as gr
import whisper
import yt_dlp
from punc import PunctuationExecutor


dlp = yt_dlp.YoutubeDL(dict(no_playlist=True))

punctor = PunctuationExecutor('pun_models', use_gpu=False)

loaded_model = whisper.load_model("base")
current_size = 'base'
def inference(link):
  try:    
    print(link)
    xinfo = dlp.extract_info(link, download=True) or {}
    # x['entries'][0]['requested_downloads'][0]['filepath']
    path = xinfo.get('entries', [{}])[0].get('requested_downloads', [{}])[0].get('filepath', '')
  except Exception as e:
    print(link, e)
    return str(e)
  # options = whisper.DecodingOptions(without_timestamps=True)
  results = loaded_model.transcribe(path)  
  txt = results['text']

  txt = punctor(txt)
  return txt

def change_model(size):
  if size == current_size:
    return
  loaded_model = whisper.load_model(size)
  current_size = size

def populate_metadata(link):
  link, title = link, ''
  try:        
    xinfo = dlp.extract_info(link, download=False) or {}
    title = xinfo.get("title",'')
  except Exception as e:
    # print(link, e)
    title = str(e)

  print(title)  
  return title

title="Bilibili Whisperer"
description="Speech to text transcription of Bilibili videos using OpenAI's Whisper"
block = gr.Blocks()

with block:
    gr.HTML(
        """
            <div style="text-align: center; max-width: 500px; margin: 0 auto;">
              <div>
                <h1>Youtube Whisperer</h1>
              </div>
              <p style="margin-bottom: 10px; font-size: 94%">
                Speech to text transcription of Bilibili videos using OpenAI's Whisper
              </p>
            </div>
        """
    )
    with gr.Group():
        with gr.Box():
          sz = gr.Dropdown(label="Model Size", choices=['base','small', 'medium', 'large'], value='base')
          
          link = gr.Textbox(label="YouTube Link", value='https://www.bilibili.com/video/BV1sG4y1p789/')
          
          with gr.Row().style(mobile_collapse=False, equal_height=True):
            title = gr.Label(label="Video Title", placeholder="Title")
          text = gr.Textbox(
              label="Transcription", 
              placeholder="Transcription Output",
              lines=5)
          with gr.Row().style(mobile_collapse=False, equal_height=True): 
              btn = gr.Button("Transcribe")       
          
          # Events
          btn.click(inference, inputs=[link], outputs=[text])
          link.change(populate_metadata, inputs=[link], outputs=[title])
          sz.change(change_model, inputs=[sz], outputs=[])

block.launch(debug=False)
# x = inference('https://www.bilibili.com/video/BV1sG4y1p789/')
# print(x)
