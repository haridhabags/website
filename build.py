import json,os
from PIL import Image
U='/mnt/user-data/uploads/pomelli_'
B='https://haridha.co.in'; WA='919769646583'
P=[
dict(id='gdc',slug='girls-dont-cry-tote-bag',name="Girls Don't Cry Tote Bag",short="Girls Don't Cry",price=699,pub=True,
 src=['catalog-1','catalog-5','catalog-6','catalog-7','catalog-8'],
 alt=["Girls Don't Cry cotton tote bag hanging on wood","Woman carrying Girls Don't Cry canvas tote","Girls Don't Cry tote bag studio shot","Girls Don't Cry tote on armchair","Girls Don't Cry tote bag carried in a studio"],
 d="A bold retro-script statement tote in natural cotton canvas. Big black print, roomy body, strong shoulder handles. Pairs with everything from college to coffee runs.",tags="Statement"),
dict(id='bird',slug='quirky-fluffy-bird-tote-bag',name="Quirky Fluffy Bird Tote Bag",short="Fluffy Bird",price=699,pub=True,
 src=['catalog-2'],alt=["Hand-drawn fluffy bird printed on cotton tote bag"],
 d="A scribbly, wide-eyed little bird that makes every commute smile. Illustrated print on natural cotton canvas, a fun gift for friends and colleagues.",tags="Illustrated"),
dict(id='bn',slug='bengali-last-train-tote-bag',name="Bengali Typography Tote Bag - Shesh Trene",short="Bengali Last Train",price=699,pub=True,
 src=['catalog-4'],alt=["Bengali typography tote bag with vintage train illustration"],
 d="Bengali lettering paired with a vintage steam-train illustration, made for Bangla lovers, travellers and nostalgia seekers. Printed on a natural linen-look cotton tote.",tags="Bengali"),
dict(id='stamp',slug='india-postage-stamps-tote-bag',name="India Postage Stamps Black Tote Bag",short="India Stamps",price=699,pub=True,
 src=['photoshoot-1_1','photoshoot-2_1','photoshoot-4_1'],
 alt=["Black cotton tote bag with India stamp print carried by a woman","India stamps black tote bag product shot","Black India stamp tote bag styled with cotton and lavender"],
 d="Nine colourful vintage-style stamps: Taj Mahal, sitar, India Gate, Lotus Temple, auto-rickshaw and more, on a sturdy black cotton tote. A souvenir or gift that says India.",tags="India"),
dict(id='kpop',slug='kpop-cap-girl-tote-bag',name="K-pop Style Cap Girl Tote Bag",short="Cap Girl",price=699,pub=False,
 src=['catalog-3','catalog-9','catalog-10','catalog-11'],alt=["Illustrated cap girl tote bag"]*4,
 d="Illustrated girl in a cap with a finger heart, on natural cotton canvas.",tags="Illustrated"),
]
def img(n):
    o=f'assets/img/{n}.webp'
    return o
for p in P:
    p['imgs']=[]
    for i,s in enumerate(p['src']):
        f=U+s+'.png'; n=f"{p['slug']}-{i+1}"
        im=Image.open(f).convert('RGB'); im.thumbnail((1100,1100)); im.save(f'assets/img/{n}.webp',quality=80)
        p['imgs'].append(f'/assets/img/{n}.webp')
json.dump([{k:v for k,v in p.items() if k!='src'} for p in P],open('products.json','w'),indent=1)
L=[p for p in P if p['pub']]
def head(t,d,u,im,extra=''):
    return f'''<!DOCTYPE html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{B}{u}">
<meta property="og:type" content="website"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{B}{u}"><meta property="og:image" content="{B}{im}">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/brand/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Lora:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="/style.css?v=3">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GH2HVYL601"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-GH2HVYL601')</script>{extra}</head><body>
<header class="hd"><a href="/" class="brand"><img src="/assets/brand/logo.png" alt="Haridha logo" style="height:44px;width:auto;max-width:180px;border-radius:0;display:block"></a><nav><a href="/#shop">Shop</a><a href="/#why">Why Haridha</a><a href="/#faq">FAQ</a><a class="btn" href="https://wa.me/{WA}?text=Hi%20Haridha%2C%20I%20want%20to%20order%20a%20tote">Order on WhatsApp</a></nav></header>'''
foot=f'''<footer><p><b>Haridha</b> - printed cotton tote bags, made in Maharashtra.</p><p>WhatsApp <a href="https://wa.me/{WA}">+91 97696 46583</a> · Instagram <a href="https://instagram.com/haridhabags" rel="noopener">@haridhabags</a></p><p>&copy; 2026 Haridha</p></footer>
<a class="fab" href="https://wa.me/{WA}?text=Hi%20Haridha%2C%20I%20want%20to%20order%20a%20tote" aria-label="Order on WhatsApp">Chat to order</a></body></html>'''
def card(p): return f'<a class="card" href="/p/{p["slug"]}.html"><img src="{p["imgs"][0]}" alt="{p["alt"][0]}" loading="lazy" width="500" height="500"><h3>{p["name"]}</h3><p class="pr">&#8377;{p["price"]}</p></a>'
faq=[("What are Haridha tote bags made of?","Natural cotton canvas with durable stitched handles, sized for books, laptops and groceries."),
("How do I order?","Tap Order on WhatsApp, send the design name and quantity, and we confirm price, delivery and payment with you."),
("Do you deliver across India?","Yes, we ship across India. Delivery time and charges are shared when you order."),
("Can I get a custom design or bulk order?","Yes. Message us for custom prints, corporate gifting, wedding favours and bulk pricing."),
("How do I wash a printed tote bag?","Hand wash gently in cold water, turn it inside out and dry in shade to keep the print sharp.")]
S=lambda o:'<script type="application/ld+json">'+json.dumps(o)+'</script>'
org={"@context":"https://schema.org","@type":"Organization","name":"Haridha","url":B,"logo":B+"/assets/brand/logo.png","sameAs":["https://instagram.com/haridhabags"],"contactPoint":{"@type":"ContactPoint","telephone":"+91-9769646583","contactType":"sales","areaServed":"IN"}}
fq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
h=head("Printed Cotton Tote Bags India | Quirky, Bengali & Statement Designs | Haridha","Buy printed cotton tote bags online in India. Quirky, Bengali typography, India stamp and statement designs from Rs 699. Made in Maharashtra, order on WhatsApp.","/",L[0]['imgs'][0],S(org)+S(fq))
h+=f'''<main><section class="hero"><div><p class="eye">Made in Maharashtra</p><h1>Printed cotton tote bags with a story to carry</h1><p>Quirky, Bengali, desi and statement designs on sturdy natural cotton. Gifts, college bags and everyday carry from &#8377;699.</p><p><a class="btn big" href="#shop">Shop totes</a> <a class="btn ghost big" href="https://wa.me/{WA}?text=I%20want%20a%20custom%20tote">Custom &amp; bulk orders</a></p></div><img src="{L[0]['imgs'][1]}" alt="{L[0]['alt'][1]}" width="500" height="650"></section>
<section id="shop"><h2>Shop all tote bags</h2><div class="grid">{''.join(card(p) for p in L)}</div></section>
<section id="why" class="why"><h2>Why choose Haridha</h2><div class="cols"><div><h3>Sturdy cotton canvas</h3><p>Strong handles and stitching built for daily use.</p></div><div><h3>Designs you will not find everywhere</h3><p>Original illustrations, Bengali typography and desi themes.</p></div><div><h3>Easy WhatsApp ordering</h3><p>Talk to a real person, get quick answers, order in minutes.</p></div><div><h3>Custom &amp; bulk</h3><p>Corporate gifts, events, weddings and return gifts.</p></div></div></section>
<section id="faq"><h2>Frequently asked questions</h2>{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)}</section>
<section class="cta"><h2>Ready to order?</h2><p><a class="btn big" href="https://wa.me/{WA}?text=Hi%20Haridha%2C%20I%20want%20to%20order%20a%20tote">Message us on WhatsApp</a></p></section></main>'''+foot
open('index.html','w').write(h)
for p in L:
    u=f'/p/{p["slug"]}.html'
    pj={"@context":"https://schema.org","@type":"Product","name":p['name'],"image":[B+i for i in p['imgs']],"description":p['d'],"brand":{"@type":"Brand","name":"Haridha"},"material":"Cotton canvas","offers":{"@type":"Offer","url":B+u,"priceCurrency":"INR","price":str(p['price']),"availability":"https://schema.org/InStock","itemCondition":"https://schema.org/NewCondition"}}
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":B+"/"},{"@type":"ListItem","position":2,"name":p['name'],"item":B+u}]}
    t=f"{p['name']} - Buy Online in India | Haridha"
    q=f"https://wa.me/{WA}?text="+"I%20want%20to%20order%20"+p['name'].replace(' ','%20').replace("'",'%27')
    g=head(t,f"{p['name']} for Rs {p['price']}. {p['d'][:100]} Order on WhatsApp.",u,p['imgs'][0],S(pj)+S(bc))
    g+=f'''<main class="pd"><div class="gal">{''.join(f'<img src="{i}" alt="{a}" width="800" height="800" {"" if k==0 else "loading=lazy"}>' for k,(i,a) in enumerate(zip(p['imgs'],p['alt'])))}</div><div><p class="eye"><a href="/">Home</a> / Tote bags</p><h1>{p['name']}</h1><p class="pr big">&#8377;{p['price']}</p><p>{p['d']}</p><ul><li>Natural cotton canvas, stitched handles</li><li>Printed design, roomy everyday size</li><li>Made in Maharashtra, ships across India</li></ul><p><a class="btn big" href="{q}">Order on WhatsApp</a></p><h2>More totes</h2><div class="grid sm">{''.join(card(x) for x in L if x is not p)}</div></div></main>'''+foot
    open(f'p/{p["slug"]}.html','w').write(g)
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {B}/sitemap.xml\n')
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{B}{u}</loc></url>' for u in ['/']+[f'/p/{p["slug"]}.html' for p in L])+'</urlset>')
open('CNAME','w').write('haridha.co.in')
