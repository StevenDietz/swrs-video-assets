import asyncio, pathlib, importlib.util, json, re
B=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('t',B/'topics.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
ms=importlib.util.spec_from_file_location('ms',B/'make_slides_lib.py');
from playwright.async_api import async_playwright
CSS="""
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;font-family:'Fira Sans','Helvetica Neue',Arial,sans-serif;background:linear-gradient(135deg,#0D2B4E 0%,#143a66 100%);color:#fff;overflow:hidden;position:relative}
.brand{position:absolute;left:96px;top:56px;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#cfe0f5;font-weight:500}
.brand b{color:#E8740C}
.left{position:absolute;left:96px;top:140px;width:720px;height:800px}
h1{font-size:68px;line-height:1.06;font-weight:700;margin-bottom:36px}
.step{display:flex;gap:22px;align-items:flex-start;margin-bottom:24px}
.num{flex:0 0 52px;height:52px;border-radius:50%;background:#E8740C;color:#fff;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;margin-top:2px}
.step p{font-size:34px;line-height:1.25;color:#f2f7fd}
.step p small{display:block;font-size:26px;line-height:1.3;color:#aac4e4;margin-top:4px}
.card{position:absolute;right:80px;top:110px;width:1000px;height:820px;border-radius:24px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;overflow:hidden;padding:20px}
.card img{max-width:100%;max-height:100%;border-radius:12px}
.foot{position:absolute;left:96px;bottom:44px;font-size:24px;color:#9fb9da}
.foot b{color:#fff}
.bar{position:absolute;left:0;bottom:0;height:10px;width:100%;background:#E8740C}
.center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 120px}
.big{font-size:128px;font-weight:700;color:#E8740C;margin:26px 0 10px}
.mid{font-size:48px;color:#fff}
.ctitle{position:absolute;left:96px;top:130px;right:96px;font-size:68px;font-weight:700;line-height:1.05}
.grid{position:absolute;left:96px;right:96px;top:260px;height:670px;display:grid;gap:28px;align-content:center}
.c{background:rgba(255,255,255,.09);border:2px solid rgba(255,255,255,.16);border-left:10px solid #E8740C;border-radius:18px;padding:30px 34px;min-width:0}
.c h3{font-size:46px;color:#fff;margin-bottom:12px;line-height:1.15}
.c p{font-size:36px;line-height:1.35;color:#d7e5f6}
.kick{font-size:30px;color:#E8740C;letter-spacing:.12em;text-transform:uppercase;font-weight:700;margin-bottom:26px}
"""
FOOT='<div class="foot">Still need help? Call <b>866-837-3065</b> or email <b>info@swrecovery.com</b> (Mon-Fri, 8 AM-5 PM CT)</div><div class="bar"></div>'
BR='<div class="brand">Southwest Recovery Services <b>&middot;</b> Client Portal</div>'
def steps(items):
    return ''.join(f'<div class="step"><div class="num">{i}</div><p>{t}'+(f'<small>{sm}</small>' if sm else '')+'</p></div>' for i,(t,sm) in enumerate(items,1))
def imgslide(sc): return f'{BR}<div class="left"><h1>{sc["title"]}</h1>{steps(sc["steps"])}</div><div class="card"><img src="file://{B}/img/{sc["img"]}"></div>{FOOT}'
def cardslide(sc):
    cols=sc.get('cols',2); n=len(sc['items'])
    cs=''.join(f'<div class="c"><h3>{a}</h3><p>{b}</p></div>' for a,b in sc['items'])
    return f'{BR}<div class="ctitle">{sc["title"]}</div><div class="grid" style="grid-template-columns:repeat({cols},1fr);{"font-size:1.15em" if cols==1 else ""}">{cs}</div>{FOOT}'
def title(t): return f'{BR}<div class="center"><div class="kick">How-to video</div><h1 style="font-size:104px;margin-bottom:34px">{t["title"]}</h1><div class="mid" style="color:#cfe0f5">{t["sub"]}</div></div><div class="bar"></div>'
END=f'{BR}<div class="center"><div class="mid">Still need help?</div><div class="big">866-837-3065</div><div class="mid">info@swrecovery.com</div><div class="mid" style="color:#aac4e4;margin-top:22px;font-size:38px">Mon-Fri, 8 AM-5 PM CT</div></div><div class="bar"></div>'
FIT="""()=>{const out=[];
 for(const sel of ['.left','.grid']){const el=document.querySelector(sel);if(!el)continue;
  let k=0;const lim=el.getBoundingClientRect().top+(sel==='.left'?800:670);
  const kids=[...el.querySelectorAll('h1,h3,p,small')];
  const base=new Map(kids.map(x=>[x,parseFloat(getComputedStyle(x).fontSize)]));
  let f=1;
  while(f>0.55){const last=el.lastElementChild.getBoundingClientRect().bottom;const sh=el.scrollHeight>el.clientHeight+2;
    if(last<=lim&&!sh)break; f-=0.04; kids.forEach(x=>x.style.fontSize=(base.get(x)*f)+'px');}
  out.push([sel,f]);}
 return out}"""
async def main():
    (B/'slides2').mkdir(exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1920,'height':1080})
        async def shot(name,html):
            f=B/'slides2'/f'{name}.html'; f.write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{html}')
            await pg.goto(f'file://{f}'); await pg.wait_for_timeout(200)
            r=await pg.evaluate(FIT)
            await pg.screenshot(path=str(B/'slides2'/f'{name}.png')); return r
        for t in m.TOPICS:
            await shot(f'{t["id"]}_title',title(t))
            for i,sc in enumerate(t['scenes']):
                r=await shot(f'{t["id"]}_{i}',imgslide(sc) if sc['t']=='img' else cardslide(sc))
                if r and r[0][1]<0.85: print('shrunk',t['id'],i,r)
        await shot('end',END)
        await b.close()
asyncio.run(main())
