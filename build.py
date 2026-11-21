#!/usr/bin/env python3
"""Builds index.html (English) and it/index.html (Italian) from one template. Edit the text here, then run:
python3 build.py"""
import json
from html import escape

BASE = "https://zxmc1100.github.io/ultimate-notes/"
STORE = "https://apps.apple.com/app/id6821194922"

EN = dict(
    lang="en", path="", up="", store=STORE, badge="en-us", badge_alt="Download on the App Store", share="share-en.png",
    title="Ultimate Notes: free handwritten notes for iPad, iPhone and Mac",
    description="Handwritten notes on iPad, iPhone and Mac. Search your handwriting, PDFs to study on, pages that grow as you write, live sync through your own iCloud Drive. Free, no ads, no account.",
    og_description="Free, no ads, no account. PDFs to study on, handwriting search, sync through your own iCloud Drive.",
    ld_description="Free handwritten notes app for iPad, iPhone and Mac. No ads, no account, no subscription. PDFs to study on, handwriting search, sync through your own iCloud Drive.",
    currency="USD", nav=("Features", "Questions", "Support", "Get"), other=("Italiano", "it/"),
    h1="Your handwriting, on every device.",
    sub="Free on iPad, iPhone and Mac. No ads, no account.",
    hero_alt=("A handwritten note about derivatives on iPad", "The same note on iPhone"),
    chapters=[
        dict(h="Every tool in one bar.",
             p=["Pens, highlighter, eraser, lasso, ruler and your colors, in the title bar. Tap a tool again for its thickness, line and colors.",
                "Hold the pen still at the end of a stroke for a clean line, circle or arrow. Scribble over something to delete it."],
             img=("bar.jpg", "The pen bar over a handwritten note"),
             tiles=[(["ink-light.jpg", "ink-dark.jpg"], "One pen for light and dark", "Black on white, white on black, automatically. Highlights dim on dark paper."),
                    (["paste.jpg"], "Copy and paste anything", "Lasso your writing and paste it in another note, or on another of your devices."),
                    (["text.jpg"], "Type where you write", "Text boxes anywhere on the page, or a whole page in Text mode.")]),
        dict(h="PDFs made for studying.",
             p=["Turn lecture slides or a whole book into pages to write on. Side notes give every slide room for your own."],
             img=("pdf-side.jpg", "A lecture PDF with handwritten side notes"),
             tiles=[(["pdf-contents.jpg"], "Chapters and bookmarks", "In Contents, and kept as chapters when you share a PDF."),
                    (["pdf-dark.jpg"], "Easy on the eyes at night", "Darken PDFs turns white slides dark, without touching the file.")]),
        dict(h="Read like a book. Find anything.",
             p=["Read mode puts pages side by side. Search finds words in typed text, in PDFs, and in what you wrote by hand, read on your device."],
             img=("read-find.jpg", "Read mode with the found words marked"),
             tiles=[(["find-handwriting.jpg"], "Search your handwriting", "Apple’s text recognition reads it on your device. Nothing leaves it.")]),
        dict(h="Organized your way.",
             p=["Quick Notes for anything, folders for your subjects, groups inside them. Drop one note on another to make a group, and type >> to link a note, a group or a bookmark."],
             img=("organize.jpg", "Folders and groups of notes"), narrow=True),
        dict(h="Sync that just works.",
             p=["Your notes on iPad, iPhone and Mac through your own iCloud Drive: no sign-up, nothing to host, nothing to pay.",
                "On the same Wi‑Fi or hotspot, a change arrives in about a second, even on the page you have open."],
             img=("sync.jpg", "The sync panel listing an iPhone nearby"), narrow=True,
             phones=[("hero-phone.jpg", "A note on iPhone"), ("phone-dark.jpg", "The same note in dark mode on iPhone"),
                     ("phone-venice.jpg", "A photo with a handwritten caption on iPhone")]),
    ],
    private_h="Your notes are yours.",
    private=[("No account.", "Nothing to sign up for, nothing to sign in to."),
             ("No tracking.", "No ads, no analytics, no data collected. Nothing is sent to us."),
             ("Your iCloud Drive.", "Notes stay on your devices and in your own iCloud. Deleted ones wait 60 days in the Recycle Bin.")],
    list_h="Everything’s included. Free.",
    list_p="No subscription, no locked features, no ads. All of it, on every device.",
    groups=[
        ("Write", [("Pages that grow", "The page grows down and to the right as you write. No page breaks."),
                   ("Clean shapes", "Hold the pen still at the end of a stroke: lines, circles, arrows and boxes."),
                   ("Erase part of a line", "An eraser for the bit you touch, or for whole strokes."),
                   ("Scribble to delete", "Scribble over something and it’s gone."),
                   ("Apple Pencil double-tap", "The eraser or your last tool, as set in your iPad’s Apple Pencil settings."),
                   ("Finger or mouse", "Write without an Apple Pencil too."),
                   ("Layers", "Bring pictures, text or lassoed ink over the others, or send them under.")]),
        ("PDFs", [("Side notes", "Room beside every slide for your own notes."),
                  ("Chapters and bookmarks", "In Contents, and kept when you share as PDF."),
                  ("Read mode", "Pages side by side, like a book, with find."),
                  ("Dark PDFs", "White slides turn dark at night."),
                  ("PDF copies in Files", "Each note can keep a PDF of itself, readable anywhere.")]),
        ("Find and organize", [("Search everything", "Folders, notes and the words in them: typed, in PDFs, written by hand."),
                               ("Links between notes", "Type >> to link a note, a group or a bookmark."),
                               ("Widgets", "Your latest note, or all of them, on the Home Screen."),
                               ("Recycle Bin", "Deleted notes wait 60 days, on every device.")]),
        ("Everywhere", [("iPad, iPhone and Mac", "The same app and the same tools on each."),
                        ("Sync without an account", "Your own iCloud Drive, about a second between devices nearby."),
                        ("Paired devices only", "Devices pair with a code, so no one else can connect."),
                        ("Five languages", "English, Italian, German, Spanish and French.")]),
    ],
    faq_h="Questions",
    faq=[("Is Ultimate Notes free?", "Yes. Every feature is included on iPad, iPhone and Mac: no subscription, no in-app purchases, no ads."),
         ("Do I need an account?", "No. There is nothing to sign up for. Your notes sync through your own iCloud Drive."),
         ("Does it work without an Apple Pencil?", "Yes. Write and draw with a finger on iPad and iPhone, or with the mouse or trackpad on Mac."),
         ("Can I write on PDFs and lecture slides?", "Yes. Import a PDF or a book and write on its pages, with room beside each slide for side notes. Share as PDF keeps chapters and bookmarks."),
         ("Can I bring my notes from another app?", "Export them as PDF from the app you use now and import the PDF into Ultimate Notes: you can keep writing on every page."),
         ("Can it search my handwriting?", "Yes. Search finds words you wrote by hand, in typed text and in PDFs. Handwriting is read on your device; nothing leaves it."),
         ("What data does it collect?", "None. No tracking, no analytics, nothing sent to us. Your notes stay on your devices and in your iCloud Drive."),
         ("Which devices and languages?", "iPad and iPhone with iPadOS or iOS 18 or later, and Mac with macOS 15 or later. The app is in English, Italian, German, Spanish and French.")],
    end_h="Start writing.", end_p="Free on the App Store for iPad, iPhone and Mac.",
    legal="Apple, the Apple logo, iPad, iPhone, Mac and Apple Pencil are trademarks of Apple Inc., registered in the U.S. and other countries. App Store is a service mark of Apple Inc.",
    support=("support.html", "Support"), privacy=("privacy.html", "Privacy"),
)

IT = dict(
    lang="it", path="it/", up="../", store="https://apps.apple.com/it/app/id6821194922", badge="it-it",
    badge_alt="Scarica su App Store", share="share-it.png",
    title="Ultimate Notes: appunti scritti a mano gratis per iPad, iPhone e Mac",
    description="Appunti scritti a mano su iPad, iPhone e Mac. Cerca nella tua scrittura, PDF su cui studiare, pagine che crescono mentre scrivi, sync dal vivo con il tuo iCloud Drive. Gratis, senza pubblicità, senza account.",
    og_description="Gratis, senza pubblicità, senza account. PDF su cui studiare, ricerca nella scrittura a mano, sync con il tuo iCloud Drive.",
    ld_description="App gratuita per appunti scritti a mano su iPad, iPhone e Mac. Senza pubblicità, senza account, senza abbonamento. PDF su cui studiare, ricerca nella scrittura a mano, sync con il tuo iCloud Drive.",
    currency="EUR", nav=("Funzioni", "Domande", "Assistenza", "Ottieni"), other=("English", ""),
    h1="La tua scrittura, su ogni dispositivo.",
    sub="Gratis su iPad, iPhone e Mac. Senza pubblicità, senza account.",
    hero_alt=("Una nota scritta a mano sulle derivate su iPad", "La stessa nota su iPhone"),
    chapters=[
        dict(h="Ogni strumento in una barra.",
             p=["Penne, evidenziatore, gomma, lazo, righello e i tuoi colori, nella barra del titolo. Tocca di nuovo uno strumento per spessore, linea e colori.",
                "Tieni ferma la penna alla fine di un tratto per una linea, un cerchio o una freccia puliti. Scarabocchia sopra qualcosa per cancellarlo."],
             img=("bar.jpg", "La barra delle penne sopra una nota scritta a mano"),
             tiles=[(["ink-light.jpg", "ink-dark.jpg"], "Una penna per chiaro e scuro", "Nero su bianco, bianco su nero, in automatico. Gli evidenziatori si attenuano sulla carta scura."),
                    (["paste.jpg"], "Copia e incolla tutto", "Prendi la tua scrittura con il lazo e incollala in un'altra nota, o su un altro dei tuoi dispositivi."),
                    (["text.jpg"], "Scrivi con la tastiera dove scrivi a mano", "Caselle di testo ovunque sulla pagina, o una pagina intera in Modalità testo.")]),
        dict(h="PDF fatti per studiare.",
             p=["Trasforma le slide di una lezione o un libro intero in pagine su cui scrivere. Le note a lato danno a ogni slide spazio per le tue."],
             img=("pdf-side.jpg", "Un PDF di una lezione con note a lato scritte a mano"),
             tiles=[(["pdf-contents.jpg"], "Capitoli e segnalibri", "Nel Sommario, e tenuti come capitoli quando condividi un PDF."),
                    (["pdf-dark.jpg"], "Riposante per gli occhi di sera", "Scurisci i PDF rende scure le slide bianche, senza toccare il file.")]),
        dict(h="Leggi come un libro. Trova tutto.",
             p=["La Modalità lettura mette le pagine affiancate. La ricerca trova le parole nel testo digitato, nei PDF e in quello che hai scritto a mano, letto sul dispositivo."],
             img=("read-find.jpg", "Modalità lettura con le parole trovate segnate"),
             tiles=[(["find-handwriting.jpg"], "Cerca nella scrittura a mano", "Il riconoscimento del testo di Apple la legge sul tuo dispositivo. Niente esce da lì.")]),
        dict(h="Organizzato a modo tuo.",
             p=["Note rapide per tutto, cartelle per le tue materie, gruppi al loro interno. Trascina una nota su un'altra per fare un gruppo, e scrivi >> per collegare una nota, un gruppo o un segnalibro."],
             img=("organize.jpg", "Cartelle e gruppi di note"), narrow=True),
        dict(h="Sync che funziona e basta.",
             p=["Le tue note su iPad, iPhone e Mac con il tuo iCloud Drive: niente iscrizione, niente da ospitare, niente da pagare.",
                "Sulla stessa Wi‑Fi o hotspot, una modifica arriva in circa un secondo, anche sulla pagina aperta."],
             img=("sync.jpg", "Il pannello di sync con un iPhone vicino"), narrow=True,
             phones=[("hero-phone.jpg", "Una nota su iPhone"), ("phone-dark.jpg", "La stessa nota in modalità scura su iPhone"),
                     ("phone-venice.jpg", "Una foto con una didascalia scritta a mano su iPhone")]),
    ],
    private_h="Le tue note sono tue.",
    private=[("Nessun account.", "Niente a cui iscriversi, niente in cui accedere."),
             ("Nessun tracciamento.", "Niente pubblicità, niente statistiche, nessun dato raccolto. Niente viene inviato a noi."),
             ("Il tuo iCloud Drive.", "Le note restano sui tuoi dispositivi e nel tuo iCloud. Quelle eliminate aspettano 60 giorni nel Cestino.")],
    list_h="Tutto incluso. Gratis.",
    list_p="Niente abbonamento, niente funzioni bloccate, niente pubblicità. Tutto, su ogni dispositivo.",
    groups=[
        ("Scrivere", [("Pagine che crescono", "La pagina cresce in basso e a destra mentre scrivi. Niente salti pagina."),
                      ("Forme pulite", "Tieni ferma la penna alla fine di un tratto: linee, cerchi, frecce e riquadri."),
                      ("Cancella parte di una linea", "Una gomma per il pezzo che tocchi, o per tratti interi."),
                      ("Scarabocchia per cancellare", "Scarabocchia sopra qualcosa e sparisce."),
                      ("Doppio tocco di Apple Pencil", "La gomma o l'ultimo strumento, come impostato nelle impostazioni di Apple Pencil dell'iPad."),
                      ("Dito o mouse", "Scrivi anche senza Apple Pencil."),
                      ("Livelli", "Porta immagini, testo o inchiostro preso con il lazo sopra gli altri, o mandali sotto.")]),
        ("PDF", [("Note a lato", "Spazio accanto a ogni slide per le tue note."),
                 ("Capitoli e segnalibri", "Nel Sommario, e tenuti quando condividi come PDF."),
                 ("Modalità lettura", "Pagine affiancate, come un libro, con la ricerca."),
                 ("PDF scuri", "Le slide bianche diventano scure di sera."),
                 ("Copie PDF in File", "Ogni nota può tenere un PDF di sé, leggibile ovunque.")]),
        ("Trovare e organizzare", [("Cerca ovunque", "Cartelle, note e le parole dentro: digitate, nei PDF, scritte a mano."),
                                   ("Link tra note", "Scrivi >> per collegare una nota, un gruppo o un segnalibro."),
                                   ("Widget", "La tua ultima nota, o tutte, nella schermata Home."),
                                   ("Cestino", "Le note eliminate aspettano 60 giorni, su ogni dispositivo.")]),
        ("Ovunque", [("iPad, iPhone e Mac", "La stessa app e gli stessi strumenti su ognuno."),
                     ("Sync senza account", "Il tuo iCloud Drive, circa un secondo tra dispositivi vicini."),
                     ("Solo dispositivi abbinati", "I dispositivi si abbinano con un codice, così nessun altro può collegarsi."),
                     ("Cinque lingue", "Italiano, inglese, tedesco, spagnolo e francese.")]),
    ],
    faq_h="Domande",
    faq=[("Ultimate Notes è gratis?", "Sì. Tutte le funzioni sono incluse su iPad, iPhone e Mac: niente abbonamento, niente acquisti in-app, niente pubblicità."),
         ("Serve un account?", "No. Non c'è niente a cui iscriversi. Le note si sincronizzano con il tuo iCloud Drive."),
         ("Funziona senza Apple Pencil?", "Sì. Scrivi e disegna con il dito su iPad e iPhone, o con mouse e trackpad su Mac."),
         ("Posso scrivere su PDF e slide delle lezioni?", "Sì. Importa un PDF o un libro e scrivi sulle sue pagine, con spazio accanto a ogni slide per le note a lato. Condividi come PDF tiene capitoli e segnalibri."),
         ("Posso portare le note da un'altra app?", "Esportale come PDF dall'app che usi ora e importa il PDF in Ultimate Notes: puoi continuare a scrivere su ogni pagina."),
         ("Cerca nella mia scrittura a mano?", "Sì. La ricerca trova le parole scritte a mano, nel testo digitato e nei PDF. La scrittura è letta sul tuo dispositivo; niente esce da lì."),
         ("Quali dati raccoglie?", "Nessuno. Niente tracciamento, niente statistiche, niente inviato a noi. Le tue note restano sui tuoi dispositivi e nel tuo iCloud Drive."),
         ("Su quali dispositivi e in quali lingue?", "iPad e iPhone con iPadOS o iOS 18 o successivi, e Mac con macOS 15 o successivi. L'app è in italiano, inglese, tedesco, spagnolo e francese.")],
    end_h="Inizia a scrivere.", end_p="Gratis su App Store per iPad, iPhone e Mac.",
    legal="Apple, il logo Apple, iPad, iPhone, Mac e Apple Pencil sono marchi di Apple Inc., registrati negli Stati Uniti e in altri Paesi. App Store è un marchio di servizio di Apple Inc.",
    support=("support.html#it", "Assistenza"), privacy=("privacy.html#it", "Privacy"),
)


def e(s):
    return escape(s, quote=True)


def page(t):
    up = t["up"]
    img = lambda name: f"{up}img/{name}"
    ld_app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Ultimate Notes",
              "description": t["ld_description"], "applicationCategory": "ProductivityApplication",
              "operatingSystem": "iPadOS 18, iOS 18, macOS 15", "url": BASE + t["path"], "downloadUrl": t["store"],
              "installUrl": t["store"], "image": BASE + "icon.png", "screenshot": BASE + "img/hero-ipad.jpg",
              "inLanguage": ["en", "it", "de", "es", "fr"], "isAccessibleForFree": True,
              "offers": {"@type": "Offer", "price": "0", "priceCurrency": t["currency"]}}
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    badge = (f'<a class="badge" href="{t["store"]}"><img src="https://tools.applemarketingtools.com/api/badges/'
             f'download-on-the-app-store/black/{t["badge"]}?size=250x83" alt="{e(t["badge_alt"])}" width="156" height="52"></a>')
    nav = t["nav"]

    chapters = []
    for i, c in enumerate(t["chapters"]):
        tiles = ""
        if c.get("tiles"):
            cells = []
            for imgs, h, p in c["tiles"]:
                pics = "".join(f'<img class="shot" src="{img(s)}" alt="" loading="lazy">' for s in imgs)
                cells.append(f'<figure><div class="pics{" split" if len(imgs) == 2 else ""}">{pics}</div><figcaption><h3>{e(h)}</h3><p>{e(p)}</p></figcaption></figure>')
            tiles = f'\n    <div class="tiles n{len(cells)}">{"".join(cells)}</div>'
        phones = ""
        if c.get("phones"):
            phones = '\n    <div class="phones">' + "".join(
                f'<img class="shot phone" src="{img(s)}" alt="{e(a)}" loading="lazy">' for s, a in c["phones"]) + '</div>'
        paras = "".join(f"<p>{e(p)}</p>" for p in c["p"])
        src, alt = c["img"]
        chapters.append(f'''<section class="chapter{'' if i % 2 else ' alt'}">
  <div class="inner">
    <h2>{e(c["h"])}</h2>
    <div class="copy">{paras}</div>
    <img class="shot hero-shot{' narrow' if c.get('narrow') else ''}" src="{img(src)}" alt="{e(alt)}" loading="lazy">{tiles}{phones}
  </div>
</section>''')

    private = "".join(f"<div><h3>{e(h)}</h3><p>{e(p)}</p></div>" for h, p in t["private"])
    groups = "".join(
        f'<div class="group"><h3>{e(name)}</h3><ul>' + "".join(f"<li><strong>{e(h)}</strong><span>{e(p)}</span></li>" for h, p in rows)
        + "</ul></div>" for name, rows in t["groups"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    home = "./" if t["lang"] == "it" else "index.html"

    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["description"])}">
<link rel="canonical" href="{BASE}{t["path"]}">
<link rel="alternate" hreflang="en" href="{BASE}">
<link rel="alternate" hreflang="it" href="{BASE}it/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<meta name="apple-itunes-app" content="app-id=6821194922">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ultimate Notes">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["og_description"])}">
<meta property="og:image" content="{BASE}img/{t["share"]}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}{t["path"]}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld_app, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>
<link rel="stylesheet" href="{up}style.css">
<link rel="icon" href="{up}icon.png">
<link rel="apple-touch-icon" href="{up}icon.png">
</head>
<body class="home">
<nav class="bar" aria-label="Ultimate Notes">
  <div class="bar-inner">
    <a class="name" href="{home}"><img src="{up}icon.png" alt="">Ultimate Notes</a>
    <div class="links">
      <a href="#features">{e(nav[0])}</a>
      <a href="#questions">{e(nav[1])}</a>
      <a href="{up}{t["support"][0]}">{e(nav[2])}</a>
      <a class="get" href="{t["store"]}">{e(nav[3])}</a>
    </div>
  </div>
</nav>

<header class="hero">
  <img class="app-icon" src="{up}icon.png" alt="" width="112" height="112">
  <h1>{e(t["h1"])}</h1>
  <p class="sub">{e(t["sub"])}</p>
  {badge}
  <div class="devices">
    <img class="shot" src="{img("hero-ipad.jpg")}" alt="{e(t["hero_alt"][0])}">
    <img class="shot phone" src="{img("hero-phone.jpg")}" alt="{e(t["hero_alt"][1])}">
  </div>
</header>

{chr(10).join(chapters)}

<section class="private">
  <div class="inner">
    <h2>{e(t["private_h"])}</h2>
    <div class="columns">{private}</div>
  </div>
</section>

<section class="included" id="features">
  <div class="inner">
    <h2>{e(t["list_h"])}</h2>
    <p class="lead">{e(t["list_p"])}</p>
    <div class="groups">{groups}</div>
  </div>
</section>

<section class="questions" id="questions">
  <div class="inner">
    <h2>{e(t["faq_h"])}</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="end">
  <img class="app-icon" src="{up}icon.png" alt="" width="88" height="88" loading="lazy">
  <h2>{e(t["end_h"])}</h2>
  <p class="sub">{e(t["end_p"])}</p>
  {badge}
</section>

<footer class="foot">
  <div class="inner">
    <nav>
      <a href="{up}{t["other"][1]}" hreflang="{"it" if t["lang"] == "en" else "en"}">{e(t["other"][0])}</a>
      <a href="{up}{t["support"][0]}">{e(t["support"][1])}</a>
      <a href="{up}{t["privacy"][0]}">{e(t["privacy"][1])}</a>
    </nav>
    <p>{e(t["legal"])}</p>
  </div>
</footer>
</body>
</html>
'''


for t, out in ((EN, "index.html"), (IT, "it/index.html")):
    open(out, "w").write(page(t))
    print("wrote", out)
