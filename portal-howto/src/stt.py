import glob, json, os, subprocess, uuid, urllib.request, concurrent.futures as cf, pathlib
KEY=open('/mnt/user-data/attachments/c9e3f274-8675-52a7-8549-56918566b6d9/02684b3f-ELEVENLABS_API.txt').read().strip()
def run(f):
    n=pathlib.Path(f).stem.rsplit('_',1)[0]
    mp3=f'stt/{n}.mp3'; subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vn','-ac','1','-ar','16000','-b:a','48k',mp3],check=True)
    b=uuid.uuid4().hex; data=open(mp3,'rb').read()
    parts=[('model_id','scribe_v1'),('timestamps_granularity','word'),('tag_audio_events','false')]
    body=b''
    for k,v in parts: body+=f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    body+=f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode()+data+f'\r\n--{b}--\r\n'.encode()
    r=urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text',data=body,headers={'xi-api-key':KEY,'Content-Type':f'multipart/form-data; boundary={b}'})
    try: j=json.load(urllib.request.urlopen(r,timeout=300))
    except Exception as e: return n,'ERR '+str(e).replace(KEY,'***')
    open(f'stt/{n}.json','w').write(json.dumps(j)); open(f'stt/{n}.txt','w').write(j.get('text',''))
    return n,j.get('text','')
with cf.ThreadPoolExecutor(4) as ex:
    for n,t in ex.map(run,sorted(glob.glob('vid/*.mp4'))): print('==',n,'\n',t,'\n')
