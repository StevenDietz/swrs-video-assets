import json,subprocess,uuid,urllib.request,re,difflib,importlib.util,pathlib,concurrent.futures as cf
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
B=pathlib.Path('build')
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def stt(f):
    mp3=f'stt/rt_{pathlib.Path(f).stem}.mp3'; subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vn','-ac','1','-ar','16000','-b:a','48k',mp3],check=True)
    b=uuid.uuid4().hex; d=open(mp3,'rb').read(); body=b''
    for k,v in [('model_id','scribe_v1'),('tag_audio_events','false')]: body+=f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    body+=f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode()+d+f'\r\n--{b}--\r\n'.encode()
    r=urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text',data=body,headers={'xi-api-key':KEY,'Content-Type':f'multipart/form-data; boundary={b}'})
    return json.load(urllib.request.urlopen(r,timeout=300))['text']
def norm(t): return re.findall(r"[a-z0-9']+",t.lower())
def one(t):
    got=stt(f'build/out3/SWRS_Portal_{t["id"]}.mp4')
    exp=f"{t['title']}. {t['sub']}. "+' '.join(x['say'] for x in t['scenes'])+' '+m.END_SAY
    a,b=norm(exp),norm(got); r=difflib.SequenceMatcher(None,a,b).ratio()
    miss=[(x[0],' '.join(a[x[1]:x[2]]),' '.join(b[x[3]:x[4]])) for x in difflib.SequenceMatcher(None,a,b).get_opcodes() if x[0]!='equal']
    return t['id'],round(r,3),[x for x in miss if not re.search(r"swrecovery|s w|a m|p m|portal|\b(and|it|2026|six|three)\b|multi|sw",str(x))]
with cf.ThreadPoolExecutor(4) as ex:
    for i,r,mi in ex.map(one,m.TOPICS): print(i,r,mi)
