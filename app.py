import gradio as gr
from pytube import YouTube

def do(url):
  yt = YouTube(url)
  stream = yt.streams.filter(only_audio=True).first()
  out=stream.download(filename='output.mp3')
  return 'output.mp3'
iface=gr.Interface(fn=do,title='yt轉mp3',description='這是一個讓你可以傳入一個yt網址然後下載成mp3的網站（使用時請注意版權等問題），請在下面輸入網址（需要等一下），下載完後按輸出格右上方的下載即可。',inputs='text',outputs='audio')
iface.launch(share=True)
