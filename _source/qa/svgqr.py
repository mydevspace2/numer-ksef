import re,zxingcpp
from PIL import Image
svg=open('qr-generated.svg').read(); link=open('qr-generated.txt').read()
n=int(re.search(r'viewBox="0 0 (\d+)',svg).group(1)); s=8
im=Image.new('L',(n*s,n*s),255); px=im.load()
for x,y in re.findall(r'M(\d+),(\d+)h1v1h-1z',svg):
    x,y=int(x),int(y)
    for dy in range(s):
        for dx in range(s): px[x*s+dx,y*s+dy]=0
r=zxingcpp.read_barcodes(im); print('decoded OK' if r and r[0].text==link else 'FAIL', r[0].text if r else None, r[0].ec_level if r else '')
im.save('qr-generated.png')
