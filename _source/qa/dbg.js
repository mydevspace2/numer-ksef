const fs=require('fs'),path=require('path');const {JSDOM}=require('jsdom');
const ROOT=path.join(__dirname,'../site-v2');
const dom=new JSDOM(fs.readFileSync(ROOT+'/index.html','utf8'),{url:'https://numerksef.dpdns.org/'});
const w=dom.window;
for (const s of w.document.querySelectorAll('script[src]')){const p=ROOT+s.getAttribute('src').split('?')[0]; try{w.eval(fs.readFileSync(p,'utf8'));}catch(e){console.log('ERR',p,e.message)}}
console.log(typeof w.KSEF, typeof w.UI);
w.document.getElementById('k-ex').click(); console.log(w.document.getElementById('k-res').className, w.document.getElementById('k-res').textContent.slice(0,80));
