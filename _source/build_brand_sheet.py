# -*- coding: utf-8 -*-
"""Writes ../assets/logo/brand-sheet.html (the logo presentation page). Run build_logo.py first."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.abspath(os.path.join(HERE, "..", "assets", "logo"))

def svg(name):
    s = open(os.path.join(LOGO, "svg", name), encoding="utf-8").read()
    s = re.sub(r'\swidth="\d+"\sheight="\d+"', "", s, count=1)
    s = re.sub(r"<style>.*?</style>", "", s, flags=re.S)
    return s.strip()

INK, AMBER, CREAM, DEEP = "#14121A", "#F2A100", "#FBF1DC", "#9A5200"
def mark(l=AMBER, r=INK, extra=""):
    return (f'<svg viewBox="0 0 120 120" aria-hidden="true" {extra}><path d="M58 3A50 50 0 0 0 58 103Z" fill="{l}"/>'
            f'<path d="M62 17A50 50 0 0 1 62 117Z" fill="{r}"/></svg>')

H, HR, HB, HW = svg("pe-logo-horizontal.svg"), svg("pe-logo-horizontal-reversed.svg"), svg("pe-logo-horizontal-black.svg"), svg("pe-logo-horizontal-white.svg")
S, SR = svg("pe-logo-stacked.svg"), svg("pe-logo-stacked-reversed.svg")

construction = f'''<svg viewBox="-34 -14 188 148" class="constr" aria-label="Construction of the mark">
<circle cx="60" cy="60" r="50" fill="none" stroke="{DEEP}" stroke-width=".7" stroke-dasharray="2 3"/>
<line x1="60" y1="-8" x2="60" y2="128" stroke="{DEEP}" stroke-width=".5" stroke-dasharray="2 3"/>
<g opacity=".95"><path d="M58 3A50 50 0 0 0 58 103Z" fill="{AMBER}"/><path d="M62 17A50 50 0 0 1 62 117Z" fill="{INK}"/></g>
<g stroke="{DEEP}" stroke-width=".5"><line x1="-10" y1="3" x2="58" y2="3"/><line x1="-10" y1="103" x2="58" y2="103"/><line x1="62" y1="17" x2="130" y2="17"/><line x1="62" y1="117" x2="130" y2="117"/></g>
<g font-family="DM Sans,Helvetica,Arial,sans-serif" font-size="5.2" fill="{DEEP}">
 <text x="-32" y="56">left half</text><text x="-32" y="63">r = 50</text>
 <text x="118" y="66">right half</text><text x="118" y="73">r = 50</text>
 <text x="126" y="12" font-weight="700">↑ 7</text><text x="126" y="125" font-weight="700">↓ 7</text>
 <text x="52" y="-5" font-weight="700">gap 4</text></g></svg>'''

dont = [
    ("Don't stretch", mark(extra='style="transform:scaleX(1.55)"')),
    ("Don't recolor", mark("#E0457B", "#6B4EFF")),
    ("Don't swap the halves", mark(INK, AMBER)),
    ("Don't rotate", mark(extra='style="transform:rotate(28deg)"')),
]
dont_html = "".join(f'<figure><div class="dtile">{m}</div><figcaption>✕ {t}</figcaption></figure>' for t, m in dont)

sizes = "".join(f'<div class="sz">{mark()}<span>{n}px</span></div>'.replace("<svg ", f'<svg style="width:{n}px;height:{n}px" ', 1) for n in (16, 24, 32, 48, 72))

files = [
    ("Mark", "pe-mark.svg · -reversed · -black · -white", "png/pe-mark-1024.png"),
    ("Horizontal logo", "pe-logo-horizontal.svg · -reversed · -black · -white", "png/pe-logo-horizontal-1520x480.png"),
    ("Stacked logo", "pe-logo-stacked.svg · -reversed", "png/pe-logo-stacked-1040x912.png"),
    ("App icon", "pe-app-icon.svg · pe-app-icon-dark.svg", "png/pe-app-icon-512.png"),
    ("Favicon + touch icon", "favicon.svg · favicon-32.png · apple-touch-icon-180.png", "png/favicon-32.png"),
    ("Profile picture", "pe-avatar-400.png", "png/pe-avatar-400.png"),
    ("Link preview image", "pe-share-1200x630.png", "png/pe-share-1200x630.png"),
]
files_html = "".join(f'<tr><td><b>{a}</b></td><td><code>{b}</code></td><td><a href="{c}" download>PNG ↓</a></td></tr>' for a, b, c in files)

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project Equinox — Logo &amp; Brand Sheet</title>
<link rel="icon" href="svg/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=DM+Sans:wght@400;500;700&display=swap">
<style>
:root{{--bg:{CREAM};--ink:{INK};--soft:#5E5645;--line:rgba(20,18,26,.13);--amber:{AMBER};--deep:{DEEP};--disp:'Bricolage Grotesque','Helvetica Neue',Arial,sans-serif;--body:'DM Sans','Helvetica Neue',Arial,sans-serif}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 var(--body);-webkit-font-smoothing:antialiased}}
.w{{max-width:1120px;margin:0 auto;padding:0 28px}}h1,h2,h3{{font-family:var(--disp);margin:0;letter-spacing:-.02em;line-height:1.08;text-wrap:balance}}
h2{{font-size:clamp(1.7rem,3.2vw,2.4rem);font-weight:700}}h3{{font-size:1.1rem;font-weight:700}}p{{margin:0}}
.sec{{padding:80px 0;border-top:1px solid var(--line)}}.tag{{font-size:.76rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--deep);display:block;margin-bottom:12px}}
.lede{{color:var(--soft);font-size:1.1rem;max-width:620px;margin-top:14px}}
.hero{{padding:72px 0 80px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}}
.hero h1{{font-size:clamp(2.4rem,5.4vw,4rem);font-weight:800}}.hero .big svg{{width:min(100%,340px);height:auto;margin:0 auto;display:block}}
.three{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}}.card{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px}}.card p{{color:var(--soft);font-size:.96rem;margin-top:8px}}
.explore{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:34px}}.ex{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;text-align:center}}.ex svg{{width:84px;height:84px}}.ex b{{display:block;margin-top:10px;font-size:.92rem}}.ex span{{display:block;font-size:.8rem;color:var(--soft);margin-top:4px}}.ex.win{{border:2px solid var(--amber);box-shadow:0 12px 30px -16px rgba(154,82,0,.5)}}.ex.win em{{display:inline-block;font-style:normal;font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;background:var(--amber);padding:3px 10px;border-radius:99px;margin-bottom:8px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}}.constr{{width:100%;max-width:520px;height:auto;background:#fff;border:1px solid var(--line);border-radius:18px;padding:12px}}
.tiles{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}}.tile{{border-radius:18px;display:flex;align-items:center;justify-content:center;padding:44px 28px;min-height:200px;border:1px solid var(--line)}}.tile svg{{width:100%;max-width:320px;height:auto}}
.t-cream{{background:{CREAM}}}.t-white{{background:#fff}}.t-ink{{background:{INK}}}.t-amber{{background:linear-gradient(120deg,#FFB83D,#FFD25E 55%,#FFC93C)}}
.stk svg{{max-width:170px}}
.p{{font:600 19px var(--disp);letter-spacing:6.5px}}.e{{font:800 60px var(--disp);letter-spacing:-1.5px}}
.sizes{{display:flex;flex-wrap:wrap;gap:30px;align-items:flex-end;margin-top:30px}}.sz{{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:.78rem;color:var(--soft)}}
.icons{{display:flex;flex-wrap:wrap;gap:22px;align-items:center;margin-top:30px}}.icons img{{border-radius:22px;box-shadow:0 14px 30px -16px rgba(0,0,0,.4)}}
.swatches{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:34px}}.sw{{border-radius:16px;overflow:hidden;border:1px solid var(--line);background:#fff}}.sw i{{display:block;height:92px}}.sw div{{padding:12px 14px;font-size:.84rem;line-height:1.4}}.sw b{{display:block;font-size:.92rem}}.sw code{{color:var(--soft)}}
.donts{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px}}.donts figure{{margin:0}}.dtile{{background:#fff;border:1px solid var(--line);border-radius:16px;height:150px;display:grid;place-items:center;overflow:hidden}}.dtile svg{{width:72px;height:72px}}.donts figcaption{{font-size:.84rem;color:var(--soft);margin-top:8px;text-align:center}}
.clear{{position:relative;display:inline-block;padding:34px;border:1.5px dashed var(--deep);border-radius:6px;background:#fff}}.clear svg{{width:300px;height:auto;display:block}}
.ctx{{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;margin-top:34px}}.ctx .nav{{display:flex;align-items:center;justify-content:space-between;padding:14px 26px;border-bottom:1px solid var(--line);background:var(--bg)}}.ctx .nav svg{{height:46px;width:auto}}.ctx .nav span{{font-size:.9rem;font-weight:500}}.ctx .nav a{{background:linear-gradient(180deg,#FFBE2E,#F2A100);color:var(--ink);font-weight:700;font-size:.9rem;padding:10px 20px;border-radius:99px;text-decoration:none}}.ctx .body{{padding:34px 26px 40px;color:var(--soft)}}
table{{width:100%;border-collapse:collapse;margin-top:28px;font-size:.94rem}}td{{padding:14px 10px;border-top:1px solid var(--line)}}td:last-child{{text-align:right}}code{{font-size:.84rem}}a{{color:var(--deep);font-weight:700}}
.note{{font-size:.9rem;color:var(--soft);margin-top:20px;max-width:760px}}
@media(max-width:860px){{.hero,.two{{grid-template-columns:1fr}}.three{{grid-template-columns:1fr}}.explore,.donts{{grid-template-columns:1fr 1fr}}.tiles{{grid-template-columns:1fr}}.swatches{{grid-template-columns:repeat(2,1fr)}}.hero{{padding-top:40px}}.sec{{padding:56px 0}}}}
</style></head><body>

<div class="w hero"><div><span class="tag">Logo &amp; brand sheet</span><h1>Two perspectives.<br>One whole.</h1>
<p class="lede">The new Project Equinox mark is a circle cut in two and slid apart — a warm half and a dark half, each seen from a slightly different height, still together as one. It is the whole idea of Gender Intelligence in a shape you can draw in one breath.</p></div>
<div class="big">{mark()}</div></div>

<section class="sec"><div class="w"><span class="tag">The idea</span><h2>Three meanings, one shape.</h2>
<div class="three">
<div class="card"><h3>Equinox</h3><p>The moment day and night are exactly equal. Amber is daylight, ink is night — neither one bigger, neither one winning.</p></div>
<div class="card"><h3>Perspective</h3><p>Each half sits at a different height. That is the lesson Andre teaches: the same moment looks different from the other side. “When men can understand women and women can understand men.”</p></div>
<div class="card"><h3>Whole</h3><p>Slide the halves together and they are one circle. It also evolves the yin-yang in the original logo into something simpler and more modern.</p></div></div></div></section>

<section class="sec"><div class="w"><span class="tag">Directions explored</span><h2>Four ideas, one chosen.</h2>
<div class="explore">
<div class="ex">{mark()}<b>A · Mirror Sun</b><span>Read like a smiley face. Dropped.</span></div>
<div class="ex win"><em>Chosen</em>{mark()}<b>B · Two Perspectives</b><span>Bold, simple, works at 16px and in one color.</span></div>
<div class="ex"><svg viewBox="0 0 120 120"><clipPath id="cc"><circle cx="60" cy="60" r="56"/></clipPath><g clip-path="url(#cc)"><rect width="120" height="120" fill="{INK}"/><path d="M0 0H120V60C100 78 82 80 60 60S20 42 0 60z" fill="{AMBER}"/></g></svg><b>C · Evolved yin-yang</b><span>Nice heritage, but generic wave art.</span></div>
<div class="ex"><svg viewBox="0 0 120 120"><circle cx="45" cy="60" r="34" fill="{AMBER}"/><circle cx="75" cy="60" r="34" fill="{INK}"/><path d="M60 31.7a34 34 0 0 1 0 56.6a34 34 0 0 1 0-56.6z" fill="{DEEP}"/></svg><b>D · Two voices</b><span>Clear, but the most common idea.</span></div></div></div></section>

<section class="sec"><div class="w two"><div><span class="tag">Construction</span><h2>Built from two half-circles.</h2>
<p class="lede">Two identical half-discs (radius 50) with a 4-unit gap between them, one lifted 7 units and one dropped 7 units. Nothing else — no gradients, no effects — so it prints, embroiders and shrinks cleanly.</p></div>
<div>{construction}</div></div></section>

<section class="sec"><div class="w"><span class="tag">Logo lockups</span><h2>Horizontal and stacked.</h2>
<p class="lede">The wordmark sets “PROJECT” small and tracked above “Equinox” in Bricolage Grotesque ExtraBold — friendly, confident, and a touch editorial. Use the horizontal logo by default, the stacked one for square spaces.</p>
<div class="tiles">
<div class="tile t-cream">{H}</div><div class="tile t-white">{H}</div>
<div class="tile t-ink">{HR}</div><div class="tile t-amber">{HB}</div>
<div class="tile t-cream stk">{S}</div><div class="tile t-ink stk">{SR}</div></div></div></section>

<section class="sec"><div class="w"><span class="tag">Small sizes &amp; icons</span><h2>Holds up from 16 pixels to a billboard.</h2>
<div class="sizes">{sizes}</div>
<div class="icons"><img src="png/pe-app-icon-512.png" width="120" height="120" alt="App icon, light"><img src="png/pe-app-icon-dark-512.png" width="120" height="120" alt="App icon, dark"><img src="png/pe-avatar-400.png" width="96" height="96" alt="Profile picture" style="border-radius:50%"><img src="png/favicon-32.png" width="32" height="32" alt="Favicon" style="border-radius:8px"><img src="png/pe-share-1200x630.png" width="300" alt="Link preview image" style="border-radius:12px"></div></div></section>

<section class="sec"><div class="w"><span class="tag">Color</span><h2>Sunlight, ink and cream.</h2>
<div class="swatches">
<div class="sw"><i style="background:{AMBER}"></i><div><b>Equinox Amber</b><code>{AMBER}</code></div></div>
<div class="sw"><i style="background:{INK}"></i><div><b>Night Ink</b><code>{INK}</code></div></div>
<div class="sw"><i style="background:{CREAM}"></i><div><b>Dawn Cream</b><code>{CREAM}</code></div></div>
<div class="sw"><i style="background:{DEEP}"></i><div><b>Deep Amber</b><code>{DEEP}</code></div></div>
<div class="sw"><i style="background:#FFBE2E"></i><div><b>Sun</b><code>#FFBE2E</code></div></div></div>
<p class="note">Type: Bricolage Grotesque (wordmark and headings) with DM Sans for text — both free Google Fonts.</p></div></section>

<section class="sec"><div class="w two"><div><span class="tag">Clear space &amp; minimum size</span><h2>Give it room.</h2>
<p class="lede">Keep clear space around the logo equal to half the height of the mark. Minimum sizes: mark 16px, horizontal logo 120px wide, stacked logo 90px wide.</p></div>
<div><div class="clear">{H}</div></div></div></section>

<section class="sec"><div class="w"><span class="tag">Keep it clean</span><h2>A few things not to do.</h2><div class="donts">{dont_html}</div></div></section>

<section class="sec"><div class="w"><span class="tag">In context</span><h2>On the new site.</h2>
<div class="ctx"><div class="nav">{H}<span>About &nbsp;·&nbsp; Programs &nbsp;·&nbsp; Events &nbsp;·&nbsp; Media &nbsp;·&nbsp; Stories</span><a href="#">Book a Free Call</a></div>
<div class="body">End the confusion. Create love that actually works.</div></div></div></section>

<section class="sec"><div class="w"><span class="tag">Files</span><h2>Everything you need.</h2>
<table>{files_html}</table>
<p class="note">All SVG files are in <code>svg/</code> and PNG exports in <code>png/</code>. The mark SVGs are pure shapes. The lockup SVGs set the text live in Bricolage Grotesque (loaded from Google Fonts) — for print or design software, use the PNGs, or ask for the text to be converted to outlines.</p></div></section>
</body></html>'''
open(os.path.join(LOGO, "brand-sheet.html"), "w", encoding="utf-8").write(html)
print("wrote brand-sheet.html")
