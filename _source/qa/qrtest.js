const QR=require('../site-v2/assets/qr.js'); const fs=require('fs');
const tests=['https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE','HELLO','a'.repeat(200),'Zażółć gęślą jaźń '+'x'.repeat(400)];
tests.forEach((t,i)=>{const q=QR.encode(t,'M'); const rows=q.modules.map(r=>r.map(b=>b?1:0).join('')); fs.writeFileSync('qr'+i+'.txt',JSON.stringify({t,rows,v:q.version,mask:q.mask}));});
