import requests
import run_inference
from googletrans import Translator
translator = Translator()

def analyze_image(filename):

  # change the locations if this program is running on the other computer or server.
  FLAGS = {
    "checkpoint_path": "/home/hkh/sources/im2txt/im2txt/model/train",
    "vocab_file": "/hdd/data/mscoco/tfdata/word_counts.txt",
    "input_files": "/home/hkh/sources/im2txt/webdemo"+filename,
  }

  captions = run_inference.analyze(FLAGS)
  google_captions = google_translate(captions)
  naver_captions = naver_translate(captions)
  return captions, google_captions, naver_captions

def google_translate(captions):

  translated = []
  for caption in captions:
    try:
      translation = translator.translate(caption, dest='ko')
      translated += [translation.text]
    except:
      pass
  return translated

def naver_translate(captions):
  # replace this with your own naver api "Client ID" and "Client Secret"
  # client_id = "43IVWkgERKH9Dc_Bw8s9"
  # client_secret = "kq8CC9v9RG"
  client_id = "43IVWkgERKH9Dc_Bw8s9"
  client_secret = "kq8CC9----"
  url = "https://openapi.naver.com/v1/language/translate"

  headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
  }
  translated = []
  for caption in captions:
    data = {
      "source": "en",
      "target": "ko",
      "text": caption,
    }
    req = requests.post(url, headers=headers, data=data)
    print(req.status_code)
    try:
      translated_text = req.json()['message']['result']['translatedText']
      translated += [translated_text]
    except:
      pass
  return translated