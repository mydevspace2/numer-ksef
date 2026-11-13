import json,zxingcpp,glob
from PIL import Image
for f in sorted(glob.glob('qr*.txt')):
    d=json.load(open(f)); rows=d['rows']; n=len(rows); s=6; b=4
    im=Image.new('L',((n+2*b)*s,)*2,255); px=im.load()
    for y,r in enumerate(rows):
        for x,c in enumerate(r):
            if c=='1':
                for dy in range(s):
                    for dx in range(s): px[(x+b)*s+dx,(y+b)*s+dy]=0
    res=zxingcpp.read_barcodes(im)
    ok = bool(res) and res[0].text==d['t']
    print(f,'v',d['v'],'mask',d['mask'], 'OK' if ok else ('FAIL',[r.text[:40] for r in res]))
