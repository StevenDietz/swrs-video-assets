import importlib.util, hashlib, json, pathlib, time, urllib.request, concurrent.futures as cf
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
VOICE='hpp4J3VqNfWAUOO0d1Us'
(B/'audio3').mkdir(exist_ok=True)
def tts(text):
    h=hashlib.md5(text.encode()).hexdigest()[:12]; out=B/'audio3'/f'{h}.mp3'
    if out.exists() and out.stat().st_size>2000: return str(out)
    body=json.dumps({"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.7,"similarity_boost":0.75,"style":0.0,"use_speaker_boost":True,"speed":0.96}}).encode()
    for a in range(4):
        try:
            r=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128',data=body,headers={'xi-api-key':KEY,'Content-Type':'application/json','Accept':'audio/mpeg'})
            d=urllib.request.urlopen(r,timeout=120).read(); out.write_bytes(d); return str(out)
        except Exception as e:
            err=str(e).replace(KEY,'***'); time.sleep(3*(a+1))
    raise RuntimeError('tts failed: '+err)
texts=[]
for t in m.TOPICS:
    t['intro']=f"{t['title']}. {t['sub']}."
    texts.append(t['intro'])
    for sc in t['scenes']: texts.append(sc['say'])
texts.append(m.END_SAY)
texts=list(dict.fromkeys(texts))
with cf.ThreadPoolExecutor(6) as ex: res=dict(zip(texts,ex.map(tts,texts)))
json.dump(res,open(B/'audio_map3.json','w'))
print(len(res),'clips')
