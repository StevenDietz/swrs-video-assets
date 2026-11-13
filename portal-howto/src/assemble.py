import importlib.util, json, pathlib, subprocess, concurrent.futures as cf
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
A=json.load(open(B/'audio_map3.json'))
(B/'seg3').mkdir(exist_ok=True); (B/'out3').mkdir(exist_ok=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
def clip(png,aud,out):
    d=dur(aud)+0.6
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','25','-i',png,'-i',aud,'-t',f'{d:.2f}','-af','loudnorm=I=-16:TP=-1.5:LRA=9,apad','-vf',f'fade=t=in:st=0:d=0.25,fade=t=out:st={d-0.25:.2f}:d=0.25,format=yuv420p','-c:v','libx264','-crf','20','-preset','veryfast','-r','25','-c:a','aac','-b:a','160k','-ar','44100','-ac','2',out],check=True)
    return d
jobs=[];plans={}
for t in m.TOPICS:
    items=[(f'slides2/{t["id"]}_title.png',A[f"{t['title']}. {t['sub']}."],f'seg3/{t["id"]}_title.mp4')]
    for i,sc in enumerate(t['scenes']): items.append((f'slides2/{t["id"]}_{i}.png',A[sc['say']],f'seg3/{t["id"]}_{i}.mp4'))
    items.append(('slides2/end.png',A[m.END_SAY],f'seg3/{t["id"]}_end.mp4'))
    plans[t['id']]=items; jobs+=items
with cf.ThreadPoolExecutor(4) as ex: res=list(ex.map(lambda j: clip(str(B/j[0]),j[1],str(B/j[2])),jobs))
dmap={j[2]:r for j,r in zip(jobs,res)}
meta={}
for t in m.TOPICS:
    lst=B/f'seg3/{t["id"]}.txt'; lst.write_text(''.join(f"file '{B/i[2]}'\n" for i in plans[t['id']]))
    out=B/'out3'/f'SWRS_Portal_{t["id"]}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(lst),'-c','copy','-movflags','+faststart',str(out)],check=True)
    ch=[];c=0
    for i in plans[t['id']]: ch.append(c); c+=dmap[i[2]]
    meta[t['id']]={'file':out.name,'dur':round(dur(str(out)),1),'size_mb':round(out.stat().st_size/1e6,1),'chapters':[round(x,1) for x in ch]}
    print(t['id'],meta[t['id']]['dur'],meta[t['id']]['size_mb'])
json.dump(meta,open(B/'out/meta.json','w'),indent=1)
