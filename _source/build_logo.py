# -*- coding: utf-8 -*-
"""Generates the Project Equinox logo system into ../assets/logo (SVG + PNG) and the brand sheet.
Run: python3 build_logo.py     (PNG export uses Google Chrome headless; fonts load from Google Fonts)
"""
import os, subprocess, shutil, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.abspath(os.path.join(HERE, "..", "assets", "logo"))
SVG = os.path.join(LOGO, "svg"); PNG = os.path.join(LOGO, "png")
for d in (SVG, PNG): os.makedirs(d, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INK, AMBER, CREAM, DEEP, SUN = "#14121A", "#F2A100", "#FBF1DC", "#9A5200", "#FFBE2E"
FONT_IMPORT = "@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;800&display=swap');"
FONT_STACK = "'Bricolage Grotesque','Helvetica Neue',Arial,sans-serif"

# --- the mark: two half-discs (r=50) slid apart. left = amber (up 7), right = ink (down 7) ---
def mark_paths(left, right):
    return (f'<path d="M58 3A50 50 0 0 0 58 103Z" fill="{left}"/>'
            f'<path d="M62 17A50 50 0 0 1 62 117Z" fill="{right}"/>')

MARKS = {  # name -> (left, right)
    "": (AMBER, INK), "-reversed": (AMBER, CREAM), "-black": (INK, INK), "-white": ("#FFFFFF", "#FFFFFF"),
}
TEXT = {   # name -> (PROJECT colour, Equinox colour)
    "": (DEEP, INK), "-reversed": (SUN, CREAM), "-black": (INK, INK), "-white": ("#FFFFFF", "#FFFFFF"),
}

def svg_wrap(w, h, body, title, with_font=False):
    style = f"<style>{FONT_IMPORT}.p{{font:600 19px {FONT_STACK};letter-spacing:6.5px}}.e{{font:800 60px {FONT_STACK};letter-spacing:-1.5px}}</style>" if with_font else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{style}{body}</svg>\n')

def mark_svg(v):
    l, r = MARKS[v]
    return svg_wrap(120, 120, mark_paths(l, r), "Project Equinox mark")

def horizontal_svg(v):
    l, r = MARKS[v]; p, e = TEXT[v]
    body = (mark_paths(l, r) + f'<text class="p" x="146" y="40" fill="{p}">PROJECT</text>'
            f'<text class="e" x="143" y="94" fill="{e}">Equinox</text>')
    return svg_wrap(380, 120, body, "Project Equinox", True)

def stacked_svg(v):
    l, r = MARKS[v]; p, e = TEXT[v]
    body = (f'<g transform="translate(70 0)">{mark_paths(l, r)}</g>'
            f'<text class="p" x="130" y="156" fill="{p}" text-anchor="middle" style="letter-spacing:6.5px">PROJECT</text>'
            f'<text class="e" x="130" y="212" fill="{e}" text-anchor="middle">Equinox</text>')
    return svg_wrap(260, 228, body, "Project Equinox", True)

def icon_svg(bg, l, r, rx=112):
    s = 2.9; t = 256 - 60 * s
    body = (f'<rect width="512" height="512" rx="{rx}" fill="{bg}"/>'
            f'<g transform="translate({t:.1f} {t:.1f}) scale({s})">{mark_paths(l, r)}</g>')
    return svg_wrap(512, 512, body, "Project Equinox app icon")

files = {}
for v in MARKS:
    files[f"pe-mark{v}.svg"] = mark_svg(v)
    files[f"pe-logo-horizontal{v}.svg"] = horizontal_svg(v)
for v in ("", "-reversed"):
    files[f"pe-logo-stacked{v}.svg"] = stacked_svg(v)
files["pe-app-icon.svg"] = icon_svg(CREAM, AMBER, INK)
files["pe-app-icon-dark.svg"] = icon_svg(INK, AMBER, CREAM)
files["favicon.svg"] = icon_svg(CREAM, AMBER, INK, 96)
for n, c in files.items():
    open(os.path.join(SVG, n), "w", encoding="utf-8").write(c)
print("svg:", len(files))

# ---------------- PNG export via headless Chrome ----------------
def inline(svgtext):  # drop the width/height attrs so CSS can size it
    return svgtext

def export(name, svgtext, w, h, bg="transparent", extra_css="", wrapper=None):
    html = wrapper or f'''<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;800&family=DM+Sans:wght@500;700&display=swap">
<style>html,body{{margin:0;padding:0;background:{bg};overflow:hidden}}svg{{display:block;width:{w}px;height:{h}px}}{extra_css}</style>{svgtext}'''
    tmp = os.path.join(tempfile.gettempdir(), "pe_export.html")
    open(tmp, "w", encoding="utf-8").write(html)
    out = os.path.join(PNG, name)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--default-background-color=00000000", "--virtual-time-budget=6000",
                    f"--window-size={w},{h}", f"--screenshot={out}", "file://" + tmp],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    print("png", name, os.path.exists(out))

if os.environ.get("SKIP_PNG") != "1":
    for v in MARKS:
        export(f"pe-mark{v}-1024.png", mark_svg(v), 1024, 1024)
        export(f"pe-logo-horizontal{v}-1520x480.png", horizontal_svg(v), 1520, 480)
    for v in ("", "-reversed"):
        export(f"pe-logo-stacked{v}-1040x912.png", stacked_svg(v), 1040, 912)
    export("pe-app-icon-512.png", icon_svg(CREAM, AMBER, INK), 512, 512)
    export("pe-app-icon-dark-512.png", icon_svg(INK, AMBER, CREAM), 512, 512)
    export("apple-touch-icon-180.png", icon_svg(CREAM, AMBER, INK, 0), 180, 180)
    export("favicon-32.png", icon_svg(CREAM, AMBER, INK, 96), 32, 32)
    export("pe-avatar-400.png", icon_svg(CREAM, AMBER, INK, 0), 400, 400)
    # share image 1200x630
    og = f'''<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;800&family=DM+Sans:wght@500;700&display=swap">
<style>html,body{{margin:0}}body{{width:1200px;height:630px;background:{CREAM};position:relative;overflow:hidden;font-family:'DM Sans',sans-serif}}
.band{{position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(120deg,#FFB83D,#FFD25E 55%,#FFC93C)}}
.c{{position:absolute;left:0;right:0;top:120px;display:flex;flex-direction:column;align-items:center;gap:34px}}
.c svg{{width:760px;height:auto}}.t{{font-size:34px;color:#5E5645;font-weight:500;letter-spacing:-.01em}}
.b{{position:absolute;left:0;right:0;bottom:52px;text-align:center;font-size:30px;font-weight:700;color:{INK}}}</style>
<div class="c">{horizontal_svg("")}<div class="t">Relationship &amp; dating coaching with Andre Paradis</div></div>
<div class="band"></div><div class="b">Gender Intelligence · Los Angeles &amp; online</div>'''
    export("pe-share-1200x630.png", "", 1200, 630, wrapper=og)
