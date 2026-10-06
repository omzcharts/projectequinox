# -*- coding: utf-8 -*-
"""Builds the Project Equinox remake (7 static pages) from the content pulled from projectequinox.net.
Run:  python3 build_site.py     (writes the .html files one folder up, next to /assets)
"""
import os, html

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
E = lambda s: html.escape(s, quote=False)

BASE = "https://projectequinox.net/"
UP = BASE + "wp-content/uploads/"
LOGO = UP + "2019/08/Logo-AI-Vector-white-e.jpg"
HERO = UP + "2020/11/Andre-banner-gray-min.jpg"
ABOUT_IMG = UP + "2019/06/IMG_3399-Internet2.jpg"
T_MICHELLE = UP + "2023/07/358291712_230683983251696_4629571044598753434_n-160x160.jpg"
T_POLLY = UP + "2023/07/358497942_964773894855309_6445036850467037441_n-160x160.jpg"
T_SAM = UP + "2023/07/358164951_987103585655138_2968047475343616099_n-160x160.jpg"
SEL = [UP + "2025/09/" + n for n in ["IMG_5961-1.jpg", "IMG_5960.jpg", "IMG_5959-1.jpg", "IMG_5958-1.jpg", "IMG_2576.jpg", "IMG_2575.jpg"]]
WEDDING = [UP + "2023/10/andre-wedding-pic%d.jpg" % i for i in (1, 2, 3, 4)]
BOOK_PPP = UP + "2024/06/PPP-Bestseller-Front-Cover-4.jpg"
BOOK_SHSA = UP + "2024/06/120063929_10214356081490846_1703058579362396973_o.jpg"
EB9 = UP + "2024/06/9-Things-Cover2-1.png"
EB5 = UP + "2023/05/5thingsmockup.png"
WORKSHOP_VIDEO = UP + "2024/06/Love-v-Money_-Which-will-win-OR-can-you-have-both_-relationships-communication-relationshipcoach.mp4"
WORKSHOP_POSTER = UP + "2024/06/d71e9d95-904e-46e1-92bc-788a14978712-1709014917371-acrp.png"
WEDDING_VIDEO = UP + "2024/01/A-glimpse-of-our-Frio-River-wedding-magical.mp4"
PRESS_KIT = UP + "2024/05/Andre-Press-Kit-2-1.pptx"

CALENDLY = "https://calendly.com/andrecoaching1"
EMAIL = "andrecoaching1@gmail.com"
LIVE_EVENT = "https://projectequinox.us/live_event"
URL_WORKSHOP = "https://projectequinox.us/workshop_request"
URL_BOOKS = "https://projectequinox.us/book-request"
URL_9 = "https://projectequinox.us/9-things-ebook"
URL_5 = "https://projectequinox.us/5-things-ebook"
URL_PROGRAMS_PDF = "https://drive.google.com/file/d/1G43AK6E2uHThYXo5UYHjoZUKc9wiEEMY/view?usp=sharing"
YT_CHANNEL = "https://www.youtube.com/@ProjectEqinoxwithAndreParadis"
SOCIAL = [("Facebook", "https://www.facebook.com/ProjectEquinox/"), ("Instagram", "https://www.instagram.com/projectequinox"),
          ("LinkedIn", "https://www.linkedin.com/in/andre-paradis-16042249/"), ("YouTube", YT_CHANNEL), ("TikTok", "https://www.tiktok.com/@andre_paradis")]

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800"
         "&family=DM+Sans:wght@400;500;600;700&display=swap")

NAV = [("index.html", "Home"), ("about.html", "About"), ("programs.html", "Programs"),
       ("events.html", "Events & Speaking"), ("media.html", "Media"), ("stories.html", "Stories")]

MARK = ('<svg class="pe-mark" viewBox="0 0 120 120" aria-hidden="true"><path d="M58 3A50 50 0 0 0 58 103Z" fill="#F2A100"/>'
        '<path d="M62 17A50 50 0 0 1 62 117Z" fill="currentColor"/></svg>')
BRAND = ('<span class="wm"><span class="wm-top">Project</span><span class="wm-main">Equinox</span></span>')

CREDS = ["Certified Relationship Dynamics Coach", "Certified NLP Practitioner", "2× Amazon Best Seller",
         "TEDx Speaker", "Public Speaker & Workshop Leader", "Ordained Minister"]


def page(fname, title, desc, body, active=None, extra_head=""):
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == active else "", E(t)) for h, t in NAV)
    foot_nav = "".join('<li><a href="%s">%s</a></li>' % (h, E(t)) for h, t in NAV)
    soc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in SOCIAL)
    mcta = '' if fname == 'book.html' else '<div class="m-cta" aria-hidden="true"><a class="btn" href="book.html" tabindex="-1">Book Your Free Call</a></div>'
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#FBF1DC">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="assets/logo/svg/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/logo/png/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/logo/png/apple-touch-icon-180.png">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="assets/logo/png/pe-share-1200x630.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/styles.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Project Equinox — home">{MARK}{BRAND}</a>
    <ul class="nav-links" id="nav-links">{nav}<li class="nav-book"><a class="btn" href="book.html">Book a Free Call</a></li></ul>
    <div class="nav-cta"><a class="btn" href="book.html">Book a Free Call</a><button class="menu-btn" aria-expanded="false" aria-controls="nav-links">Menu</button></div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div><a class="brand foot-logo" href="index.html" aria-label="Project Equinox — home">{MARK}{BRAND}</a>
        <p class="foot-brand-p">Relationship &amp; dating coaching with Andre Paradis — teaching Gender Intelligence to singles and couples. Los Angeles &amp; online.</p></div>
      <div><h4>Explore</h4><ul>{foot_nav}<li><a href="book.html">Book a Free Call</a></li></ul></div>
      <div><h4>Free resources</h4><ul>
        <li><a href="{URL_9}" target="_blank" rel="noopener">9 Things Before You Marry</a></li>
        <li><a href="{URL_5}" target="_blank" rel="noopener">5 Feminine Qualities</a></li>
        <li><a href="programs.html#free">25-minute mini workshop</a></li>
        <li><a href="{PRESS_KIT}">Press kit (download)</a></li></ul></div>
      <div><h4>Connect</h4><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>{soc}</ul></div>
    </div>
    <div class="foot-bottom"><span>© Project Equinox · Andre Paradis. Coaching is educational and is not a substitute for therapy or medical care.</span><span>Remake concept</span></div>
  </div>
</footer>
{mcta}
<script src="assets/site.js" defer></script>
</body>
</html>'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", fname)


def final_cta(title="Your next conversation could go differently.", text="Book a complimentary strategy call with Andre. Choose the session for women or for men — it's a real conversation, not a sales pitch."):
    return f'''<section class="final"><div class="container">
  <h2>{E(title)}</h2><p>{E(text)}</p>
  <div class="cta-row"><a class="btn btn-lg" href="book.html">Book Your Complimentary Strategy Call</a></div>
</div></section>'''


# ---------------------------------------------------------------- DATA
SELF_TALK = ["There's always something wrong", "He makes me angry", "She makes me crazy",
             "I need so little, why can't he just give that to me?", "She doesn't appreciate or see everything I do for her",
             "We're fighting all the time!", "I can't live like this!", "I don't want to break up", "I wish I could fix this!"]

STEPS = [("Schedule your free breakthrough session", "Book a complimentary coaching call with Andre and choose the session for women or for men."),
         ("Learn what's really going on", "Learn all about men — and yourself — on a call with Andre, and hear what he has to offer you."),
         ("Join the program that fits", "Join one of Andre's programs so you can finally get the relationship you've been looking for.")]

PODCASTS = [("Don’t Ask Me Shit", "andre-paradis-on-dont-ask-me-shit/"), ("Be Awesome Network", "andre-paradis-on-be-awesome-network/"),
            ("Your I Got It Girl Podcast", "andre-paradis-on-the-your-i-got-it-girl-podcast/"), ("The Purple Passion Project", "andre-on-the-purple-passion-project/"),
            ("LifeVision Lab Podcast", "andre-paradis-on-lifevision-lab-podcast/"), ("Dear God, It’s Me", "andre-paradis-on-dear-god-its-me/"),
            ("The Men’s Roundtable Series", "andre-paradis-on-the-mens-roundtable-series/"), ("The Health Revolutions TV Show", "andre-paradis-on-the-health-revolutions-tv-show/"),
            ("They Call Me Mista Yu: Men’s Round Table", "andre-paradis-on-they-call-me-mista-yu-mens-round-table/"), ("Love in the Wild", "andre-paradis-on-love-in-the-wild/"),
            ("Marriage IQ", "andre-paradis-on-marriage-iq/"), ("The Momentum Shift Podcast and Radio Show", "andre-paradis-on-the-momentum-shift-podcast-and-radio-show/"),
            ("The Superhuman Academy Podcast", "andre-paradis-on-the-superhuman-academy-podcast/"), ("Just Enamoured Podcast", "andre-paradis-on-just-enamoured-podcast/"),
            ("Love Anarchy", "andre-paradis-on-love-anarchy/"), ("The Feminine Codes Podcast", "andre-paradis-on-the-feminine-codes-podcast/"),
            ("In My Humble Opinion", "andre-paradis-on-my-humble-opinion/"), ("Beyond Belief Podcast", "andre-paradis-on-beyond-belief-podcast/"),
            ("Heart to Heart with Abagaba", "andre-paradis-on-heart-to-heart-with-abagaba/"), ("Inspire & Impact The Podcast Interviews", "inspire-impact-podcast/"),
            ("One on One with Mista!", "andre-paradis-on-one-on-one-with-mista/"), ("Wisdom on the Front Porch", "andre-paradis-on-wisdom-on-the-front-porch/"),
            ("Embodied Wisdom Podcast", "andre-paradis-on-embodied-wisdom-podcast/"), ("Morning Tea with Coach Kennedy", "andre-paradis-on-morning-tea-with-coach-kennedy/"),
            ("Truth & Transcendence", "andre-paradis-on-truth-transcendence/"), ("The Unstuck Movement", "andre-paradis-on-the-unstuck-movement/"),
            ("Beyond I Do", "andre-paradis-on-beyond-i-do-part-1/"), ("The Behind the Shades Show", "andre-paradis-on-the-behind-the-shades-show-2/"),
            ("Vulnerability Muscle", "andre-paradis-on-vulnerability-muscle/"), ("What’s on Your Plate?", "andre-paradis-on-whats-on-your-plate/")]

VIDEOS = [("RzrYM6r6HUk", "Welcome to Project Equinox with Andre Paradis", "Project Equinox"),
          ("anmudOVYD5M", "“What Makes Me Different”", "Close-Up Television & Radio"),
          ("hzCbgaUZBMg", "“The Vision and Mission of Project Equinox”", "Close-Up Television & Radio"),
          ("amNJnLdRn70", "“Passion, Purpose & Profit”", "Close-Up Television & Radio"),
          ("1ORGRtYvGoc", "“Stepping Into Your Pain”", "Close-Up Television & Radio"),
          ("5_ky9iQ8shk", "CUTV News Spotlights Andre Paradis of Project Equinox", "Close-Up Television & Radio"),
          ("U-kxdyJs6y8", "Make Men Masculine Again | 5 Minute Video", "PragerU"),
          ("30hgeLI_SeA", "The cost of feminizing men on families and society, with Dr. Vibe", "Men and Masculinity"),
          ("V1gggmKbzEc", "Feminized men, masculine women: what's the cost? with Dr. Vibe", "Men and Masculinity"),
          ("33PM5ehssWM", "Interview with Erika De La Cruz", "Project Equinox"),
          ("OTPf4KG71Xw", "How the culture gets it wrong — with guest Paige Parker", "Project Equinox"),
          ("-JoQjslVuaA", "Gender Intelligence, Part 1 — with Calvin Chen", "Project Equinox"),
          ("3MWnDXLIUBw", "Gender Intelligence, Part 2 — with Calvin Chen", "Project Equinox"),
          ("9XZ-tVFg8eo", "Negotiating — with Calvin Chen", "Project Equinox"),
          ("_GDI5m5lOzM", "Safety for Women", "Project Equinox"),
          ("Kv5um0ek0BA", "Respect for Men", "Project Equinox"),
          ("8_FQchUgB60", "Chemistry in Men and Women", "Project Equinox"),
          ("QB_T6b07AUg", "Feelings for Men and Women", "Project Equinox"),
          ("wW7rone2VPc", "Masculine Women in Our Society", "Project Equinox"),
          ("AOAwhHAj5X4", "Emasculating Men in Our Society", "Project Equinox"),
          ("kt2h7_BG2Aw", "Project Equinox Moments — “Treat You Better”", "Project Equinox")]

W, M, T, P = "women", "men", "together", "patterns"
POSTS = [
    ("Decoding Women for the Man Who Has Done Everything “Right”", "decoding-women-for-the-man-who-has-done-everything-right", M),
    ("Why AI Is a Limited Tool for Relationship Advice", "why-ai-is-a-limited-tool-for-relationship-advice", P),
    ("You Know Your Femininity Deserves a High-Value Man… But Where Is He?", "you-know-your-femininity-deserves-a-high-value-man-but-where-is-he", W),
    ("Boys match energy… Men guide it!", "boys-match-energy-men-guide-it", M),
    ("There’s nothing lovely about a woman who is always burnt out", "theres-nothing-lovely-about-a-woman-who-is-always-burnt-out", W),
    ("What Women Were Never Taught About How To Treat A Man", "what-women-were-never-taught-about-how-to-treat-a-man", W),
    ("Cultural Identity Struggles: Explained", "cultural-identity-struggles-explained", P),
    ("Why So Many Women Feel Unfulfilled Later in Life", "why-so-many-women-feel-unfulfilled-later-in-life", W),
    ("A Path Back to Fulfillment for the Modern Woman", "a-path-back-to-fulfillment-for-the-modern-woman", W),
    ("What Feminine Women Do Not Respond to in Men", "what-feminine-women-do-not-respond-to-in-men", M),
    ("What Masculine Men Do Respond to in Relationships", "what-masculine-men-do-respond-to-in-relationships", W),
    ("Why Men Don’t Care About a Woman’s Success", "why-men-dont-care-about-a-womans-success", W),
    ("Ten Things Masculine Men Don’t Respond to in Relationships with Women", "ten-things-masculine-men-dont-respond-to-in-relationships-with-women", W),
    ("Stoicism in Men", "stoicism-in-men", M),
    ("How to Kill Men’s Attraction in Relationships", "how-to-kill-mens-attraction-in-relationships", W),
    ("How “Holding the Frame” Makes Her Feel Safe", "how-holding-the-frame-makes-her-feel-safe", M),
    ("5 Powerful First-Date Questions to Ask a Man", "5-powerful-first-date-questions-to-ask-a-man", W),
    ("Why “Being Independent” Can Push Away Masculine Men", "why-being-independent-can-push-away-masculine-men", W),
    ("Balancing Competence and Love: The Challenge for Modern Women", "balancing-competence-and-love-the-challenge-for-modern-women", W),
    ("Why “I Deserve Everything” Is So Off-putting", "why-i-deserve-everything-is-so-off-putting", W),
    ("Ten Traits of a Real Man", "ten-traits-of-a-real-man-2", M),
    ("Consequences for Women Who Reject Traditional Roles", "consequences-for-women-who-reject-traditional-roles", W),
    ("Can a Woman Be Too Independent for a Relationship?", "can-a-woman-be-too-independent-for-a-relationship", W),
    ("The Common Power Struggles in Love Relationships", "the-common-power-struggles-in-love-relationships", P),
    ("The Drama Triangle in Relationships", "the-drama-triangle-in-relationships", P),
    ("The Effects of Trauma in Relationships", "the-effects-of-trauma-in-relationships", P),
    ("Understanding Avoidant Relationship Attachment Styles", "understanding-avoidant-relationships-attachment-styles", P),
    ("Overcoming Anxious Relationship Styles", "overcoming-anxious-relationship-styles", P),
    ("How to Find a Good Man", "how-to-find-a-good-man", W),
    ("The Difference Between Male and Female Communication", "the-difference-between-male-and-female-communication", T),
    ("What If “Badass” Is Just… Bad? A Lady Boss’s Story", "what-if-badass-is-just-bad-a-lady-bosss-story", W),
    ("Communicating with Men: Understanding Their Natural Style", "communicating-with-men-an-insight-on-what-you-may-have-experienced", W),
    ("The Myth of Sexual Equality", "the-myth-of-sexual-equality", T),
    ("Women Are a Foreign Culture", "women-are-a-foreign-culture", T),
    ("Men Are a Foreign Culture", "men-are-a-foreign-culture", T),
    ("Why Do Men Seem To Just Want Sex?", "why-do-men-seem-to-just-want-sex", W),
    ("How to Kill a Man’s Attraction", "how-to-kill-a-mans-attraction", W),
    ("The 3 C’s: Essential for Lasting Relationships", "the-3-cs-for-deeper-love-and-relationships", T),
    ("Good Feminism vs. Bad Feminism", "good-feminism-vs-bad-feminism", T),
    ("Men and Easy Sex: It’s Not What You Think… Again!", "men-and-easy-sex-its-not-what-you-thinkagain", W),
    ("Femininity Is a Strength, Not a Weakness", "femininity-is-a-strength-not-a-weakness", W),
    ("What Do Men Want?", "what-do-men-want", W),
    ("Men, Women and the Natural Flow", "men-women-and-the-natural-flow", T),
    ("Men & Women: Finding the Perfect Balance", "men-women-finding-the-perfect-balance", T),
    ("A New Way", "a-new-way", T),
]
TOPIC_LABEL = {W: "For women", M: "For men", T: "For both", P: "Patterns & healing"}

# ---------------------------------------------------------------- HOME
def home():
    creds = "".join(f"<li>{E(c)}</li>" for c in CREDS)
    press = ["The Suzanne Venker Show", "WHKO 99.1 FM", "CUTV News & Radio", "PragerU", "Men and Masculinity", "Warrior Queen Tribe", "Health Revolutions TV", "VoyageLA", "Shout Out LA"]
    thoughts = "".join(f'<span class="thought">{E(t)}</span>' for t in SELF_TALK)
    steps = "".join(f'<div class="step"><div class="step-n">{i}</div><h3>{E(t)}</h3><p>{E(b)}</p></div>' for i, (t, b) in enumerate(STEPS, 1))
    pods = "".join(f'<li><a href="{BASE}{s}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, s in PODCASTS[:4])
    vids = "".join(f'<li><a href="https://www.youtube.com/watch?v={i}" target="_blank" rel="noopener">{E(t)}<small>{E(a)}</small></a></li>' for i, t, a in VIDEOS[:4])
    arts = "".join(f'<li><a href="{BASE}{s}/" target="_blank" rel="noopener">{E(t)}</a></li>' for t, s, _ in POSTS[:4])
    body = f'''
<section class="hero"><div class="container hero-grid">
  <div class="hero-copy">
    <span class="eyebrow">Relationship &amp; Dating Coach for Successful Business Men and Women</span>
    <h1>End the confusion. Create love that actually works.</h1>
    <p class="sub">Project Equinox teaches Gender Intelligence — how men and women really think, feel and communicate — so you can stop repeating the same fights and build a relationship that lasts.</p>
    <div class="cta-row"><a class="btn btn-lg" href="book.html">Book Your Complimentary Strategy Call</a><a class="btn btn-ghost btn-lg" href="{URL_9}" target="_blank" rel="noopener">Get the free guide</a></div>
  </div>
  <ul class="creds">{creds}</ul>
  <div class="hero-photo"><img src="{HERO}" alt="Andre Paradis, relationship coach" width="1920" height="1080" fetchpriority="high" decoding="async"></div>
</div></section>

<div class="strip"><div class="container strip-inner"><span class="strip-label">Heard &amp; seen on</span><ul>{"".join(f"<li>{E(p)}</li>" for p in press)}</ul></div></div>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Self talk</span><h2>Ever had these feelings and thoughts?</h2></div>
  <div class="thoughts">{thoughts}</div>
  <div class="thought-answer"><p>Project Equinox is dedicated to people looking to <strong>master their communication skills</strong> for successful relationships and to understand the radical differences between men and women. We know what it takes for a romantic relationship to work — straight, gay, or lesbian, it's all the same. <strong>Complementary dynamic is the magic.</strong></p>
  <p style="margin-top:20px"><a class="btn" href="book.html">Let's talk it out — book a call</a></p></div>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>Three steps from stuck to clear</h2></div>
  <div class="steps">{steps}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Stories</span><h2>What clients have to say</h2><p class="lede">Real words from people who worked with Andre — one-on-one, in groups, and at their weddings.</p></div>
  <div class="story-grid">
    <article class="story"><div class="story-top"><img src="{T_MICHELLE}" alt="Michelle" width="56" height="56"><div><b>Michelle</b><span>One-on-one coaching</span></div></div>
      <p>“I went from feeling an unbearable sadness every day, to feeling like there was something amazing waiting for me in my life… He made me feel safe, worthy and helped me to believe in myself.”</p></article>
    <article class="story"><div class="story-top"><img src="{T_POLLY}" alt="Polly" width="56" height="56"><div><b>Polly</b><span>One-on-one coaching</span></div></div>
      <p>“I spent years in traditional therapy, read hundreds of books, listened to hundreds of podcasts, and none of this holds a candle to being held and guided by Andre’s honed skill… From the very first introductory call, I felt like I was his only client.”</p></article>
    <article class="story"><div class="story-top"><img src="{T_SAM}" alt="Sam" width="56" height="56"><div><b>Sam</b><span>Coaching &amp; wedding</span></div></div>
      <p>“I wasn’t changing who I was, it was more like I was becoming more of who I was meant to be… It was magical when Andre came to Texas in May of 2023 and married me and my man.”</p></article>
  </div>
  <p style="margin-top:32px"><a class="link" href="stories.html">Read all client stories →</a></p>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">Programs</span><h2>Pick the way you like to learn</h2><p class="lede">Six programs, three formats. Every one starts with a complimentary call, so you never have to guess which fits.</p></div>
  <div class="group-grid">
    <div class="group"><span class="tag">Private</span><h3>Private coaching</h3><p>One-to-one with Andre for four months — VIP, designed around you, or master coaching with modules and live calls.</p><span class="meta">3 programs · 4 months</span></div>
    <div class="group"><span class="tag">Group</span><h3>Group coaching</h3><p>Modules with live group calls for four months, or a monthly community group that runs for a full year.</p><span class="meta">2 programs · 4 months or 1 year</span></div>
    <div class="group"><span class="tag">Self-paced</span><h3>Module coaching</h3><p>Work through the modules on your schedule, with one year of access and coaching calls designed for you.</p><span class="meta">1 program · 1 year access</span></div>
  </div>
  <p style="margin-top:32px"><a class="link" href="programs.html">Compare all six programs →</a></p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Free, right now</span><h2>Start learning before you book</h2></div>
  <div class="res-grid">
    <div class="res"><img src="{EB9}" alt="9 Things You Need to Know if You Want to Get Married" width="130" height="130" loading="lazy"><div><span class="tag">Free PDF · 19 pages</span><h3>9 Things You Need to Know if You Want to Get Married</h3><p>11 chapters on how men perceive women — and how to move forward.</p><a class="link" href="{URL_9}" target="_blank" rel="noopener">Get your copy →</a></div></div>
    <div class="res"><img src="{EB5}" alt="Five Feminine Qualities workbook" width="130" height="195" loading="lazy"><div><span class="tag">Free workbook · 22 pages</span><h3>Five Feminine Qualities High-Quality Men Find Absolutely Irresistible</h3><p>Reflection prompts after each chapter. Great for women and men.</p><a class="link" href="{URL_5}" target="_blank" rel="noopener">Get your copy →</a></div></div>
  </div>
  <p style="margin-top:28px"><a class="link" href="programs.html#free">Also: a free 25-minute mini workshop and Andre's two bestselling books →</a></p>
</div></section>

<section class="section dark"><div class="container event">
  <div>
    <span class="eyebrow">Live online workshop</span>
    <h2>Clarity on Love: modern relationships, decoded</h2>
    <p class="lede">A 90-minute workshop with Andre — TEDx speaker and 2× best-selling author — on the distinct ways men and women process information, feelings and desires, and how to replace common struggles with a blueprint for a healthy partnership.</p>
    <div class="cta-row" style="margin-top:28px"><a class="btn btn-lg" href="{LIVE_EVENT}" target="_blank" rel="noopener">Secure Your Spot</a><a class="btn btn-ghost btn-lg" href="events.html#clarity">See what you'll walk away with</a></div>
  </div>
  <div class="event-card"><dl>
    <div><dt>Format</dt><dd>Live online · replay available</dd></div>
    <div><dt>Length</dt><dd>90 minutes</dd></div>
    <div><dt>Ticket</dt><dd>$25</dd></div></dl></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Beyond coaching</span><h2>Bring Andre to your stage, school or wedding</h2></div>
  <div class="tile-grid">
    <a class="tile" href="events.html#speaking"><div class="tile-img"><img src="https://i.ytimg.com/vi/5_ky9iQ8shk/hqdefault.jpg" alt="Andre Paradis on CUTV News" loading="lazy"></div><div class="tile-body"><h3>Public speaking</h3><p>Keynotes, college lectures, business conventions, podcasts, radio and TV across Los Angeles and beyond.</p><span class="arrow">Explore speaking →</span></div></a>
    <a class="tile" href="events.html#schools"><div class="tile-img"><img src="{SEL[0]}" alt="The Dance of Relationships workshop" loading="lazy"></div><div class="tile-body"><h3>Schools: The Dance of Relationships</h3><p>A ballroom-based social-emotional learning workshop for high school students.</p><span class="arrow">Explore the school program →</span></div></a>
    <a class="tile" href="events.html#weddings"><div class="tile-img"><img src="{WEDDING[0]}" alt="Andre officiating a wedding" loading="lazy"></div><div class="tile-body"><h3>Wedding officiant</h3><p>An ordained minister who crafts a ceremony around your love story — and includes your guests.</p><span class="arrow">Explore officiant services →</span></div></a>
  </div>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">Media &amp; journal</span><h2>Listen, watch and read</h2></div>
  <div class="media-cols">
    <div class="media-col"><h3>Latest podcasts</h3><ul class="list">{pods}</ul><p style="margin-top:18px"><a class="link" href="media.html#podcasts">All podcasts →</a></p></div>
    <div class="media-col"><h3>Featured videos</h3><ul class="list">{vids}</ul><p style="margin-top:18px"><a class="link" href="media.html#videos">All videos →</a></p></div>
    <div class="media-col"><h3>Recent articles</h3><ul class="list">{arts}</ul><p style="margin-top:18px"><a class="link" href="media.html#articles">All articles →</a></p></div>
  </div>
</div></section>

<section class="section"><div class="container about-grid">
  <div class="portrait"><img src="{ABOUT_IMG}" alt="Andre Paradis" loading="lazy"></div>
  <div>
    <span class="eyebrow">Meet Andre Paradis</span>
    <h2>Educator, coach, artist and people person</h2>
    <p class="lede">Through a long journey of self-discovery and education, it has become my mission to help others create and maintain long-lasting and loving relationships. I created Project Equinox to alleviate the misunderstanding and pain between men and women by teaching <strong>Gender Intelligence</strong>.</p>
    <p class="lede">When men can understand the perspective of a woman and women can understand the perspective of a man, we can communicate with the understanding and respect that we deserve.</p>
    <p style="margin-top:28px"><a class="btn btn-ghost" href="about.html">Read Andre's story</a></p>
  </div>
</div></section>
{final_cta()}'''
    page("index.html", "Relationship & Dating Coach in Los Angeles | Andre Paradis — Project Equinox",
         "Certified relationship dynamics coach Andre Paradis teaches Gender Intelligence to singles and couples. Book a complimentary strategy call.", body, "index.html")


# ---------------------------------------------------------------- ABOUT
def about():
    body = f'''
<section class="page-hero"><div class="container page-hero-grid">
  <div><span class="eyebrow">About Andre Paradis</span><h1>Educator, coach, artist &amp; people person.</h1>
  <p class="lede">Andre's mission in life is to teach and empower people. A certified life coach, entrepreneur, business owner and artist, he now focuses his professional energy on teaching singles and couples how to create and maintain successful relationships.</p>
  <div class="cta-row" style="margin-top:28px"><a class="btn" href="book.html">Book a Free Call</a><a class="btn btn-ghost" href="{PRESS_KIT}">Download press kit</a></div></div>
  <div class="portrait"><img src="{ABOUT_IMG}" alt="Andre Paradis" width="600" height="800"></div>
</div></section>

<section class="section"><div class="container two-col">
  <div><span class="eyebrow">Always a teacher</span><h2>Teaching since 1986</h2></div>
  <div><p class="lede" style="margin-top:0">Andre began his teaching career in 1986, teaching English as a second language in Japan. The following year he began sharing his passion for dance — and still teaches dance regularly.</p>
  <p class="lede">In 2009, as part of his PAX Mastery and Leadership Program, he began sharing what he'd learned about relationships in his “Men vs. Women” workshop. A life-long learner, he's completed full programs with PAX Programs, Christopher Howard Training (Fast Track to Success) and Summit Training (Leadership Program), and is certified as both a Life Coach and an NLP Coach.</p></div>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">Three phases</span><h2>A life in three chapters</h2></div>
  <div class="timeline">
    <div class="phase"><span class="tag">Phase one · 1984–2000</span><h3>The dancer</h3><p>Andre danced professionally, performing on stage, at award shows and in music videos with world-renowned artists including Michael Jackson, Prince and Julio Iglesias. He toured and taught with Paula Abdul, and traveled the world from Bangkok to Costa Rica performing, teaching and choreographing.</p></div>
    <div class="phase"><span class="tag">Phase two · 1996</span><h3>The craftsman</h3><p>Andre opened AP Auto Body in North Hollywood, California, combining a life-long passion for cars into a successful shop that prides itself on operating with integrity and honesty.</p></div>
    <div class="phase"><span class="tag">Phase three · Today</span><h3>The coach</h3><p>Packed with knowledge and tools from his Mankind Project affiliation, PAX Programs and learnings from world-renowned therapist Dr. Pat Allen, Andre launched Project Equinox. He strives to change the world one person at a time, bringing hope, understanding and communication tools that have permanent, proven results.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Mission &amp; principle</span><h2>What Andre stands for</h2></div>
  <ul class="principles">
    <li>I am passionate about reaching and teaching relationship dynamics to all levels of society.</li>
    <li>I am dedicated to men and women and their wellbeing in understanding each other; closing the gap on pain, hurt feelings and confusion.</li>
    <li>My goal is to teach and empower people and society and to change our culture when it comes to human dynamics and relationships.</li>
    <li>I want to empower the people who are the most curious about the human condition and its challenges, and who want to learn how to create strong boundaries for themselves and lasting relationships in their world.</li>
    <li>I hold myself responsible and accountable for touching people's lives and am dedicated to making a difference in the world.</li>
    <li>I align myself with like-minded people who share my vision and passion for transforming the world.</li>
    <li>I am lighthearted in my approach and am always looking to enlighten and educate.</li>
    <li>I will reach out and ask for support and provide support for the sake of the mission and the ultimate goal of Peace and Harmony.</li>
    <li>Everyone is a player in this endeavor, life is good, and learning is fun. <strong>There is hope.</strong></li>
  </ul>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">The person</span><h2>Beyond the résumé</h2></div>
  <div class="facts">
    <div class="fact"><b>Family</b><p>Happily married for over 20 years to Nancy — a former professional dancer and current dance instructor. They live in the San Fernando Valley with their two children.</p></div>
    <div class="fact"><b>Roots</b><p>A proud French-Canadian, born and raised in Quebec City with three brothers and a sister.</p></div>
    <div class="fact"><b>Interests</b><p>People, relationships, cars, dancing, learning, jiu-jitsu, fitness, nutrition and body building.</p></div>
  </div>
  <div class="cta-row" style="margin-top:36px"><a class="link" href="media.html">See Andre in the media →</a><a class="link" href="stories.html">Read client stories →</a></div>
</div></section>
{final_cta("Ready to talk it out?")}'''
    page("about.html", "About Andre Paradis | Relationship Coach — Project Equinox",
         "Andre Paradis: professional dancer turned certified relationship dynamics coach, NLP practitioner, public speaker and 2× Amazon best-selling author.", body, "about.html")


# ---------------------------------------------------------------- PROGRAMS
def programs():
    progs = [
        ("Private coaching · 4 months", "VIP Private Coaching", ["One-to-one with Andre", "The most personal program", "4 months"], True),
        ("Private coaching · 4 months", "Private Coaching, Designed for You", ["One-to-one with Andre", "Designed around your goals", "4 months"], False),
        ("Private coaching · 4 months", "Private Master Coaching", ["One-to-one with Andre", "Modules plus live calls", "4 months"], False),
        ("Group coaching · 4 months", "Group Coaching with Modules", ["Modules", "Live group calls", "4 months"], False),
        ("Self-paced · 1 year", "Module Coaching, 1-Year Access", ["Modules, one year of access", "Coaching calls designed for you", "1 year"], False),
        ("Community · 1 year", "Community Group Coaching", ["Monthly group", "A community to learn alongside", "1 year"], False),
    ]
    cards = ""
    for i, (tag, name, items, feat) in enumerate(progs, 1):
        li = "".join(f"<li>{E(x)}</li>" for x in items)
        cards += f'<article class="program{" feature" if feat else ""}"><span class="tag">{E(tag)}</span><h3>{E(name)}</h3><ul>{li}</ul><p style="margin-top:auto"><a class="link" href="book.html" style="{"color:#FFBE2E;border-color:rgba(255,190,46,.4)" if feat else ""}">Ask about this program →</a></p></article>'
    body = f'''
<section class="page-hero"><div class="container narrow" style="max-width:860px">
  <span class="eyebrow">Programs</span><h1>Coaching that fits how you learn.</h1>
  <p class="lede">One of the most effective ways to learn, grow and reach your personal goals is private coaching. Andre offers private and group programs, from four months to a full year. Every path starts with a complimentary conversation.</p>
  <div class="cta-row" style="margin-top:28px"><a class="btn btn-lg" href="book.html">Book Your Complimentary Call</a><a class="btn btn-ghost btn-lg" href="{URL_PROGRAMS_PDF}" target="_blank" rel="noopener">Download the programs overview (PDF)</a></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Three formats</span><h2>Private, group or self-paced</h2></div>
  <div class="group-grid">
    <div class="group"><span class="tag">Private</span><h3>Private coaching</h3><p>Direct, one-to-one work with Andre. Choose VIP, a program designed around you, or master coaching with modules and live calls.</p><span class="meta">3 programs · 4 months</span></div>
    <div class="group"><span class="tag">Group</span><h3>Group coaching</h3><p>Learn alongside others with modules and live group calls — or join the monthly community group for a full year.</p><span class="meta">2 programs · 4 months or 1 year</span></div>
    <div class="group"><span class="tag">Self-paced</span><h3>Module coaching</h3><p>Move through the modules on your own schedule with one year of access and coaching calls designed for you.</p><span class="meta">1 program · 1 year</span></div>
  </div>
</div></section>

<section class="section tint"><div class="container">
  <div class="section-head"><span class="eyebrow">All six programs</span><h2>Compare at a glance</h2><p class="lede">Program pricing is shared on your complimentary call, so Andre can recommend the right fit before you commit to anything.</p></div>
  <div class="program-grid">{cards}</div>
</div></section>

<section class="section" id="free"><div class="container">
  <div class="section-head"><span class="eyebrow">Free resources &amp; books</span><h2>Start learning today</h2><p class="lede">Andre is the co-author of two bestsellers and has built free guides to get you started — no booking required.</p></div>
  <div class="workshop" style="margin-bottom:56px">
    <video controls preload="none" poster="{WORKSHOP_POSTER}"><source src="{WORKSHOP_VIDEO}" type="video/mp4"></video>
    <div><span class="tag">Free · Video</span><h3 style="font-size:1.6rem;margin:12px 0">Free 25-minute mini workshop</h3><p class="lede" style="margin-top:0">Watch a short preview — “Love vs. Money: which will win, or can you have both?” — then request your free 25-minute mini workshop.</p><p style="margin-top:22px"><a class="btn" href="{URL_WORKSHOP}" target="_blank" rel="noopener">Request my free mini workshop</a></p></div>
  </div>
  <div class="res-grid">
    <div class="res"><img src="{EB9}" alt="9 Things You Need to Know if You Want to Get Married" width="130" height="130" loading="lazy"><div><span class="tag">Free PDF · 19 pages</span><h3>“9 Things You Need to Know if You Want to Get Married”</h3><p>An action-packed introduction plus 11 chapters explaining the 9 reasons. End result: a deeper understanding of how men perceive women, and how to move forward.</p><a class="link" href="{URL_9}" target="_blank" rel="noopener">Request your copy →</a></div></div>
    <div class="res"><img src="{EB5}" alt="Five Feminine Qualities workbook" width="130" height="195" loading="lazy"><div><span class="tag">Free workbook · 22 pages</span><h3>“Five Feminine Qualities High-Quality Men Find Absolutely Irresistible”</h3><p>Five chapters with prompts for your own reflection. A valuable tool for women and men to understand feminine and masculine energy and its impact on relationships.</p><a class="link" href="{URL_5}" target="_blank" rel="noopener">Request your copy →</a></div></div>
    <div class="res"><img src="{BOOK_PPP}" alt="Purpose, Passion & Profit book cover" width="130" height="195" loading="lazy"><div><span class="tag">Amazon best seller</span><h3>Purpose, Passion &amp; Profit</h3><p>Read about overcoming financial ruin, battling health challenges and surviving tragedy and abuse — persistence, courage, redemption and unconventional approaches to challenges.</p><a class="link" href="{URL_BOOKS}" target="_blank" rel="noopener">Order your copy →</a></div></div>
    <div class="res"><img src="{BOOK_SHSA}" alt="Success Habits of Super Achievers book cover" width="130" height="195" loading="lazy"><div><span class="tag">Amazon best seller</span><h3>Success Habits of Super Achievers</h3><p>Apply today the experts' real-life lessons, strategies and great habits for success.</p><a class="link" href="{URL_BOOKS}" target="_blank" rel="noopener">Order your copy →</a></div></div>
  </div>
</div></section>

<section class="section tint"><div class="container narrow" style="max-width:860px">
  <div class="section-head"><span class="eyebrow">Good to know</span><h2>Questions before you book</h2></div>
  <div class="faq">
    <details><summary>Is the first call really free?</summary><p>Yes. The breakthrough call is complimentary. You'll choose a session for women or for men, learn what's going on in your relationships, and hear what Andre offers.</p></details>
    <details><summary>Do I need to have a partner?</summary><p>No. Andre works with singles and couples — both people looking for the right relationship and people trying to repair the one they have.</p></details>
    <details><summary>Is this only for straight couples?</summary><p>No. Project Equinox is for straight, gay and lesbian relationships — it's all the same. The complementary dynamic is the magic.</p></details>
    <details><summary>How much do programs cost?</summary><p>Pricing depends on the program. Andre shares the details on your complimentary call so you can compare before you decide.</p></details>
    <details><summary>Can I work with Andre online?</summary><p>Yes. Sessions are conveniently scheduled online, and Andre is based in Los Angeles.</p></details>
  </div>
</div></section>
{final_cta("Not sure which program? Start with a call.")}'''
    page("programs.html", "Coaching Programs & Free Resources | Project Equinox", "Six relationship coaching programs with Andre Paradis — private, group and self-paced — plus free guides, a mini workshop and two bestselling books.", body, "programs.html")


# ---------------------------------------------------------------- EVENTS
def events():
    speak_topics = ["How to speak rationally and never fight again. (really)", "How to communicate without power plays — no more games (we all do it)",
                    "Why she talks so much… why he seems secretive", "What commitment looks like for men… this one is BIG",
                    "The red buttons: Safety and Respect (this is huge)", "Man brain / woman brain: a tale of two worlds",
                    "Tools to protect yourself in emotional situations", "What men really want. It's not what you think.",
                    "Three must-haves for a long-term love relationship", "Men and women at work… why we collide, how to flow"]
    engagements = ["The Suzanne Venker Podcast — St. Louis, MO", "WHKO 99.1 FM — Dayton, OH (weekly guest speaker)",
                   "Warrior Queen Tribe Podcast — Salt Lake City, UT", "Men and Masculinity Podcast — Toronto, Canada",
                   "CUTV News and Radio — New York, NY", "Multicultural Day, Moorpark College — Moorpark, CA",
                   "Moorpark College — Moorpark, CA", "Pasadena High School — Pasadena, CA", "Venice High School — Venice, CA",
                   "Greek Orthodox Church — Los Angeles", "Dilbeck Realty, real estate sales team — Southern California",
                   "“Whispers of the Children” Foundation — keynote, Los Angeles", "“She Is” Fundraiser — keynote, Los Angeles",
                   "METal International Network — keynote, Los Angeles", "PHP Inc. — Downey, CA"]
    sel_photos = "".join(f'<img src="{u}" alt="Students in The Dance of Relationships workshop" loading="lazy">' for u in SEL)
    wed_photos = "".join(f'<img src="{u}" alt="Andre Paradis officiating a wedding" loading="lazy">' for u in WEDDING)
    body = f'''
<section class="page-hero"><div class="container narrow" style="max-width:860px">
  <span class="eyebrow">Events &amp; speaking</span><h1>Bring Gender Intelligence to your room.</h1>
  <p class="lede">A live workshop you can join online, speaking for your organization, a social-emotional learning program for schools, and wedding ceremonies with heart. All by Andre Paradis.</p>
</div></section>
<nav class="subnav" aria-label="On this page"><div class="container"><ul>
  <li><a href="#clarity">Clarity on Love</a></li><li><a href="#speaking">Public speaking</a></li><li><a href="#schools">Schools (SEL)</a></li><li><a href="#weddings">Wedding officiant</a></li></ul></div></nav>

<section class="section dark" id="clarity"><div class="container event">
  <div>
    <span class="eyebrow">Live online workshop</span><h2>Clarity on Love: modern relationships, decoded</h2>
    <p class="lede">What if everything you learned about love was backwards? Relationship coach Andre Paradis — TEDx speaker and 2× best-selling author — decodes modern relationships, including the distinct ways men and women process information, feelings and desires, to dismantle common communication struggles and replace them with a blueprint for a sustainable, healthy partnership.</p>
    <ul class="checks" style="margin-top:24px">
      <li><strong>The Communication Bridge:</strong> why men and women communicate differently, and how to translate your needs so they're finally understood.</li>
      <li><strong>The 4 Archetypes:</strong> a breakdown of the four types of men and women.</li>
      <li><strong>The Timewaster Filter:</strong> spot red flags early and stop investing in people who aren't a fit.</li>
      <li><strong>Relationship Reset:</strong> identify the hidden friction points in your current or past dynamics.</li>
    </ul>
    <div class="cta-row" style="margin-top:30px"><a class="btn btn-lg" href="{LIVE_EVENT}" target="_blank" rel="noopener">Get Your Ticket — $25</a></div>
  </div>
  <div class="event-card"><dl>
    <div><dt>What</dt><dd>90-minute live workshop</dd></div>
    <div><dt>Where</dt><dd>Online — live link provided on registration</dd></div>
    <div><dt>Cost</dt><dd>$25 · replay available</dd></div>
    <div><dt>Date</dt><dd>The most recent session was listed for July 28 at 5:30 PM Pacific — see the registration page for the next date.</dd></div></dl></div>
</div></section>

<section class="section" id="speaking"><div class="container">
  <div class="section-head"><span class="eyebrow">Public speaking</span><h2>Speaking for groups, campuses, conventions and media</h2>
  <p class="lede">Project Equinox offers speaking to existing groups, college and university lectures, personal development events, church community events, business conventions, women-in-business and networking events throughout Los Angeles — plus podcasts, radio and television interviews via the internet.</p></div>
  <div class="two-col">
    <div><h3>What Andre teaches</h3><p style="color:var(--ink-soft);margin-top:10px">Tools for every kind of relationship. Power struggles are natural between men and women, parent and child, employer and employee, teacher and student — the key is to learn:</p>
      <ul class="checks">{"".join(f"<li>{E(t)}</li>" for t in speak_topics)}</ul></div>
    <div><h3>Where Andre has spoken</h3><ul class="engage" style="columns:1">{"".join(f"<li>{E(e)}</li>" for e in engagements)}</ul>
      <p style="margin-top:24px"><a class="btn" href="book.html">Inquire about booking Andre</a></p></div>
  </div>
</div></section>

<section class="section tint" id="schools"><div class="container">
  <div class="section-head"><span class="eyebrow">For schools</span><h2>The Dance of Relationships</h2>
  <p class="lede">A dynamic, experiential workshop that uses ballroom dancing to teach high school students vital social-emotional learning (SEL) skills through movement, connection and real-time reflection.</p></div>
  <div class="group-grid">
    <div class="group"><h3>Conflict resolution</h3><p>Students learn to manage disagreements calmly and constructively through body language, emotional regulation and mutual respect.</p></div>
    <div class="group"><h3>Boundary setting</h3><p>Partnered exercises help students recognize, set and respect personal space — with teachers and peers — while practicing assertiveness and consent.</p></div>
    <div class="group"><h3>Mastering communication</h3><p>The lead-and-follow structure of ballroom dance builds active listening, clear expression and cooperation.</p></div>
  </div>
  <div class="two-col" style="margin-top:48px">
    <div><h3>Why ballroom dancing?</h3><p style="color:var(--ink-soft);margin-top:10px">It's a live, embodied metaphor for relationships: it reveals how we relate, respond and show up for others. It teaches leadership without domination, collaboration without passivity, and respect for individual space and timing. Engaging, inclusive and memorable — ideal for Health, Life Skills, PE or Advisory classes. No prior dance experience required.</p>
      <p style="margin-top:14px;color:var(--ink-soft)">All sessions align with California SEL competencies and LAUSD's student wellness goals.</p></div>
    <div><h3>Format options</h3><ul class="checks"><li>Single-period guest class</li><li>2–3 part SEL workshop series</li><li>Half-day or full-day experiential intensive</li></ul>
      <div class="quote-card" style="margin-top:26px"><p>“With Andre's guidance, my teenage son learned to communicate calmly, set healthy boundaries, and rebuild his relationships — becoming happier, more respectful, and more connected to his family.”</p><cite>— Hope, parent</cite></div></div>
  </div>
  <div class="photo-row">{sel_photos}</div>
  <div class="cta-row" style="margin-top:32px"><a class="btn" href="book.html">Schedule a call or demo for your school</a></div>
</div></section>

<section class="section" id="weddings"><div class="container">
  <div class="two-col">
    <div><span class="eyebrow">Wedding officiant</span><h2>A ceremony that blends your love story with everyone who loves you.</h2>
    <p class="lede">As a relationship coach, NLP coach and ordained minister, Andre guides couples away from fear and uncertainty and toward joy and harmony. He doesn't just plan a wedding — he cultivates a connection, getting to know your story to craft a bespoke ceremony that radiates warmth and authenticity.</p>
    <p class="lede">Picture a ceremony where the lines blur between spectators and participants — where the audience becomes a vital thread in the fabric of the day, and the ancestors are invited too, intertwining ancient wisdom with modern love.</p>
    <p style="margin-top:28px"><a class="btn" href="book.html">Talk to Andre about your ceremony</a></p></div>
    <div><video controls preload="none" style="width:100%;border-radius:20px;background:#000"><source src="{WEDDING_VIDEO}" type="video/mp4"></video>
    <p style="margin-top:10px;font-size:.88rem;color:var(--ink-soft)">Andre officiating Sam's wedding</p></div>
  </div>
  <div class="photo-row four">{wed_photos}</div>
  <div class="quote-card" style="margin-top:36px;max-width:820px"><p>“Our wedding day turned out better than we envisioned… The ceremony that he came up with was a memorable experience and truly unique and wonderfully intimate while also including all our guests… I can't imagine our very special day without him.”</p><cite>— Charlie P.</cite></div>
</div></section>
{final_cta("Have an event, school or ceremony in mind?", "Tell Andre what you're planning — he'll take it from there.")}'''
    page("events.html", "Events, Public Speaking, School Program & Wedding Officiant | Project Equinox",
         "Join the Clarity on Love live workshop, book Andre Paradis to speak, bring The Dance of Relationships SEL program to your school, or hire him as your wedding officiant.", body, "events.html")


# ---------------------------------------------------------------- MEDIA
def media():
    vids = "".join(f'<a class="video" href="https://www.youtube.com/watch?v={i}" target="_blank" rel="noopener"><span class="video-thumb"><img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" loading="lazy"></span><b>{E(t)}</b><small>{E(a)}</small></a>' for i, t, a in VIDEOS)
    pods = "".join(f'<a href="{BASE}{s}" target="_blank" rel="noopener"><span>{E(t)}</span><span>Listen →</span></a>' for t, s in PODCASTS)
    posts = "".join(f'<a class="post" data-topic="{tp}" href="{BASE}{s}/" target="_blank" rel="noopener"><b>{E(t)}</b><span class="tag">{TOPIC_LABEL[tp]}</span></a>' for t, s, tp in POSTS)
    body = f'''
<section class="page-hero"><div class="container narrow" style="max-width:860px">
  <span class="eyebrow">Media</span><h1>Listen, watch and read Andre.</h1>
  <p class="lede">Podcasts, television interviews, videos and articles — all in one place. I keep up with the latest teachings and ideas about relationship dynamics; check out the journal for new posts.</p>
</div></section>
<section class="section"><div class="container">
  <div class="tabs" role="tablist" aria-label="Media type">
    <button class="tab" role="tab" data-panel="podcasts" aria-selected="true">Podcasts</button>
    <button class="tab" role="tab" data-panel="videos" aria-selected="false">Videos</button>
    <button class="tab" role="tab" data-panel="articles" aria-selected="false">Articles</button>
    <button class="tab" role="tab" data-panel="press" aria-selected="false">In the press</button>
  </div>

  <div class="panel" id="podcasts"><div class="section-head"><h2>Podcasts &amp; radio</h2><p class="lede">Andre discusses gender intelligence in today's backwards culture. Here are the 30 most recent appearances.</p></div>
    <div class="pod-grid">{pods}</div>
    <p style="margin-top:28px"><a class="link" href="{BASE}category/podcasts/" target="_blank" rel="noopener">Browse the full podcast archive →</a></p></div>

  <div class="panel" id="videos" hidden><div class="section-head"><h2>Videos &amp; TV</h2><p class="lede">Interviews, series and short clips on YouTube.</p></div>
    <div class="video-grid">{vids}</div>
    <p style="margin-top:28px"><a class="link" href="{YT_CHANNEL}" target="_blank" rel="noopener">Visit the YouTube channel →</a></p></div>

  <div class="panel" id="articles" hidden><div class="section-head"><h2>The journal</h2><p class="lede">{len(POSTS)} articles on relationship dynamics — filter by who it's written for.</p></div>
    <div class="chips" data-filter-group="#post-list">
      <button class="chip" data-filter="all" aria-pressed="true">All</button><button class="chip" data-filter="women" aria-pressed="false">For women</button>
      <button class="chip" data-filter="men" aria-pressed="false">For men</button><button class="chip" data-filter="together" aria-pressed="false">For both</button>
      <button class="chip" data-filter="patterns" aria-pressed="false">Patterns &amp; healing</button></div>
    <div class="post-grid" id="post-list">{posts}</div></div>

  <div class="panel" id="press" hidden><div class="section-head"><h2>In the press</h2><p class="lede">Features, interviews and the press kit.</p></div>
    <a class="press-card" href="http://voyagela.com/interview/meet-andre-paradis-project-equinox-woodland-hills/" target="_blank" rel="noopener"><div><b>VoyageLA</b><span>Interview — Meet Andre Paradis, Project Equinox</span></div><span class="link">Read →</span></a>
    <a class="press-card" href="https://lifeblood.live/strong-relationships-with-andre-paradis/" target="_blank" rel="noopener"><div><b>LIFEBLOOD.LIVE</b><span>Article with podcast — Strong relationships with Andre Paradis</span></div><span class="link">Read →</span></a>
    <a class="press-card" href="https://shoutoutla.com/meet-andre-paradis-relationship-coach/" target="_blank" rel="noopener"><div><b>Shout Out LA</b><span>Meet Andre Paradis, relationship coach</span></div><span class="link">Read →</span></a>
    <a class="press-card" href="{BASE}andre-paradis-on-anything-for-love-with-omobola-stephen/" target="_blank" rel="noopener"><div><b>“Anything for Love” with Omobola Stephen</b><span>Podcast appearance</span></div><span class="link">Listen →</span></a>
    <a class="press-card" href="{PRESS_KIT}"><div><b>Press kit</b><span>Download Andre's press kit (PowerPoint)</span></div><span class="link">Download →</span></a></div>
</div></section>
{final_cta("Want Andre on your show?", "For interviews, podcasts and speaking, send a note — or book a call to talk it through.")}'''
    page("media.html", "Podcasts, Videos, Articles & Press | Andre Paradis — Project Equinox",
         "Listen to Andre Paradis on 100+ podcasts, watch his TV interviews and videos, and read his relationship articles and press features.", body, "media.html")


# ---------------------------------------------------------------- STORIES
def stories():
    S = [
        ("Michelle", T_MICHELLE, "coaching", "One-on-one coaching", [
            "Andre came into my life at a time when I was at my lowest point. I was thinking about ending my life. It took one conversation with him to see that there was hope for me. I spent years in therapy and never got very far compared to the life-changing results that I accomplished with Andre.",
            "I went from feeling an unbearable sadness every day, to feeling like there was something amazing waiting for me in my life. I had to work really hard to get there. At times, I wanted to give up because of all my self-destructive belief systems. However, I did not stop because I had Andre every step of the way working and supporting me.",
            "He made me feel safe, worthy and helped me to believe in myself. Of course, I still have bad days, and that is okay because it is perfectly normal, but I am finally free of the burden and pain I carried for so long.",
            "Working with Andre made me realize and understand that I was not responsible or to blame for the trauma I suffered. I am aware and present now and will never allow myself to go back to that dark place. I know that if I ever feel that way again, I can always and will reach out to Andre and he will be there for me.",
            "I am one of the fortunate ones. I am beyond grateful to have worked with Andre. He saved me and changed my life forever."]),
        ("Polly", T_POLLY, "coaching", "One-on-one coaching", [
            "I spent years in traditional therapy, read hundreds of books, listened to hundreds of podcasts, and none of this holds a candle to being held and guided by Andre’s honed skill and gift of truly seeing who I am and what I needed to understand myself, my destructive belief system and men.",
            "After the one-on-one coaching program with Andre, I learned to unwind from years of trauma and failed relationships which led me to be open to a real man. From the very first introductory call to the conclusion of my first program with Andre, I felt like I was his only client. This man walks his talk and has what it takes to get you to places you might be afraid to dream are possible."]),
        ("Sam", T_SAM, "coaching weddings", "Coaching & wedding", [
            "I felt like I was totally unlovable and would never find a man that I could trust. Why bother even dating because it would not ever work out – I was doomed to be single the rest of my life.",
            "Then I met Andre, the way that happened was pretty amazing – totally a God wink for sure. I started working with him and did what he guided me to do. As I did, I started to feel a shift in myself. I wasn’t changing who I was, it was more like I was becoming more of who I was meant to be. The healing and understanding I received from coaching with Andre not only helped me find and develop a healthy love relationship but has also helped me in all my relationships.",
            "It was magical when Andre came to Texas in May of 2023 and married me and my man. My life will never be the same because of what I learned from Andre. Truly."]),
        ("Helen G.", None, "coaching", "One-on-one coaching", [
            "Andre is really a man’s man, with an amazing insight on women. The fact that he’s been married to his wife Nancy for 20 plus years and they have two really well adjusted kids, spoke volumes to me about his experience in the area of relationships. I was looking for guidance and coaching and I’d just gone through a pretty significant loss.",
            "At times during my work with Andre I was in a dark place. He gently guided me with sensitivity, always gave me hope and made me feel safe. He’s gone beyond my expectations in helping me get rid of old baggage and step into my femininity with grace. My relationships have improved, not just in the area of romance but in all areas of my life, as a result of my work with him."]),
        ("Elizabeth P.", None, "coaching", "Coaching", [
            "Andre is right! After my divorce (15-year marriage, 4 children, and virtually no real dating experience ever) I had one terribly toxic relationship and knew I was in trouble. So I reorganized my mindset and treated dating like a research project… what I was doing wasn’t yielding the results I wanted and so I was willing to try a different approach.",
            "I examined my weekly schedule, set aside several opportunities with the intention to fill up my available openings, set ground rules for myself not to become emotionally attached, and did everything I could to LEARN about men. When I finally met my Warrior I was comfortable, confident, and capable of evaluating our situation with ease.",
            "Just like every skill in life, there is a competency factor that increases with experience. When you develop these skills, your confidence as a woman attracts the right kind of capable and respectful man. Thank you Andre for helping me understand!"]),
        ("Sara S.", None, "coaching", "Private sessions", [
            "I want to share the incredible, life-altering, positive experience I had with Andre. Initially I didn’t know what to expect. Honestly, I was a bit nervous, but Andre’s expertise in the dating world really allowed me to sit back and follow his lead. It created a safe space for me to speak, open up, and actively listen. Finally! A man who truly understands women! AND men! He is a lighthouse in the murky sea of modern dating.",
            "During our session, which was conveniently scheduled online, he would check in and see how I was feeling. He gave me homework and advice that I shockingly could implement right away. The next day I had results. Not only did Andre elevate my dating skills, he also brought my relationships with others to a whole new level — my sons, my male housemates, and family.",
            "After almost 40 years on this planet, I can’t believe he is teaching me things I never knew! Plus, I am getting pursued by men. He produces results, ladies."]),
        ("Davene", None, "coaching", "Coaching", [
            "I know I’ve said this so many times, but I still can’t thank you enough for how you’ve impacted my life and helped me find my prince. I am forever grateful."]),
        ("Don G.", None, "coaching", "Marriage", [
            "Listening to your words has already changed my marriage for the better. A lot more things make sense that were previously unfathomable. The best advice for a man – always take responsibility for sorting out the tough stuff, say “no” when needed, but always make her feel like her welfare is your greatest priority. Thanks again, Mate."]),
        ("Austin W.", None, "workshops", "Workshop attendee", [
            "I found it very fascinating how Andre described the different ways that men and women handle stress. I truly believe that high levels of stress are at the root of most diseases. The power of touch in the production of oxytocin is quite miraculous and immediately made me want to give my mom the biggest hug!",
            "Andre created a space that allowed people to be vulnerable and allow the healing process to take place… it was beautiful."]),
        ("Hope", None, "schools", "Parent · School program", [
            "Before meeting Andre Paradis, my teenage son bottled up his emotions until they erupted in anger and frustration. With Andre’s guidance, he learned to communicate calmly, set healthy boundaries, and rebuild his relationships — becoming happier, more respectful, and more connected to his family.",
            "Since my husband’s passing, I’ve prayed for strong male role models for my sons. None have had the lasting impact Andre has. He has taught them self-respect, how to treat women with honor, and given them the tools to face life’s challenges with confidence. To my boys, Andre is not only a mentor but a trusted friend and father figure. To me, he has been an answered prayer."]),
        ("Charlie P.", None, "weddings", "Wedding officiant", [
            "Our wedding day turned out better than we envisioned. If you don’t know Andre already he’s truly a one-of-a-kind gifted individual. After a few conversations with Andre we knew he would be the perfect choice to be our wedding officiant.",
            "Andre went “above and beyond” to make sure all the boring logistics of getting married were taken care of ahead of time. He gave us a lot of options to do a more traditional ceremony or something more contemporary. The ceremony that he came up with was a memorable experience and truly unique and wonderfully intimate while also including all our guests.",
            "One of the best parts to having Andre as our officiant is that we’ve been able to stay in touch, and have Andre as a friend and relationship coach. I can’t imagine our very special day without him."]),
    ]
    cards = ""
    for name, img, topic, role, paras in S:
        long = sum(len(p) for p in paras) > 520
        av = f'<img src="{img}" alt="{E(name)}" width="56" height="56">' if img else f'<span class="avatar" aria-hidden="true">{E(name[0])}</span>'
        ps = "".join(f"<p>{E(p)}</p>" for p in paras)
        cards += f'''<article class="story" data-topic="{topic}"><div class="story-top">{av}<div><b>{E(name)}</b><span>{E(role)}</span></div></div>
  <div class="body{" clamp" if long else ""}">{ps}</div>{'<button class="more" aria-expanded="false">Read the full story</button>' if long else ''}</article>'''
    body = f'''
<section class="page-hero"><div class="container narrow" style="max-width:860px">
  <span class="eyebrow">Stories</span><h1>What my clients have to say.</h1>
  <p class="lede">Unedited words from people who worked with Andre — in private coaching, workshops, schools and at their weddings.</p>
</div></section>
<section class="section"><div class="container">
  <div class="chips" data-filter-group="#story-list">
    <button class="chip" data-filter="all" aria-pressed="true">All stories</button><button class="chip" data-filter="coaching" aria-pressed="false">Coaching</button>
    <button class="chip" data-filter="weddings" aria-pressed="false">Weddings</button><button class="chip" data-filter="schools" aria-pressed="false">Schools &amp; families</button>
    <button class="chip" data-filter="workshops" aria-pressed="false">Workshops</button></div>
  <div class="masonry" id="story-list">{cards}</div>
  <p class="crisis">Some stories mention painful experiences. If you are in crisis or thinking about harming yourself, please call or text 988 (the U.S. Suicide &amp; Crisis Lifeline) or contact local emergency services.</p>
</div></section>
{final_cta("Write your own story.")}'''
    page("stories.html", "Client Testimonials & Stories | Andre Paradis — Project Equinox",
         "Read what Andre Paradis's clients say about relationship coaching, workshops, school programs and wedding ceremonies.", body, "stories.html")


# ---------------------------------------------------------------- BOOK
def book():
    soc = " · ".join(f'<a class="link" href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    body = f'''
<section class="page-hero"><div class="container narrow" style="max-width:860px">
  <span class="eyebrow">Book a call</span><h1>Let's talk it out.</h1>
  <p class="lede">Pick a time for your complimentary breakthrough session with Andre. Choose the session for women or for men when you book. It takes about a minute.</p>
</div></section>
<section class="section"><div class="container book-grid cal-first">
  <div>
    <h2 style="font-size:1.7rem">What happens next</h2>
    <ol class="steps" style="grid-template-columns:1fr;gap:16px;margin-top:22px;padding:0;list-style:none">
      <li class="step" style="padding:22px"><div class="step-n" style="font-size:1.6rem">1</div><h3 style="margin:8px 0 4px">Choose your time</h3><p>Pick a slot on the calendar and the session for women or for men.</p></li>
      <li class="step" style="padding:22px"><div class="step-n" style="font-size:1.6rem">2</div><h3 style="margin:8px 0 4px">Talk with Andre</h3><p>Learn about men — and yourself — and hear what he offers.</p></li>
      <li class="step" style="padding:22px"><div class="step-n" style="font-size:1.6rem">3</div><h3 style="margin:8px 0 4px">Decide your next step</h3><p>Join a program, or simply leave with clarity. No pressure.</p></li>
    </ol>
    <ul class="contact-list">
      <li><b>Email</b><a class="link" href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><b>Follow</b><span>{soc}</span></li>
    </ul>
  </div>
  <div>
    <a class="btn btn-lg cal-open" href="{CALENDLY}" target="_blank" rel="noopener">Open the full booking page</a>
    <div class="cal">
      <div class="calendly-inline-widget" data-url="{CALENDLY}?hide_gdpr_banner=1" style="min-width:320px;height:720px;"></div>
      <p class="cal-note">Calendar not loading? <a class="link" href="{CALENDLY}" target="_blank" rel="noopener">Open the booking page</a> or email Andre directly.</p>
    </div>
  </div>
</div></section>

<section class="section tint"><div class="container book-grid">
  <div><span class="eyebrow">Optional</span><h2 style="font-size:1.9rem">Help Andre prepare</h2>
  <p class="lede">Want to give Andre a head start? Share a little about where you are. This opens a pre-filled email — nothing is required to book.</p></div>
  <form class="form" id="prep-form">
    <div class="form-row"><label>Your first name<input name="name" autocomplete="given-name"></label>
    <label>I am a<select name="who"><option>Woman</option><option>Man</option><option>Couple</option></select></label></div>
    <label>Relationship status<input name="status" placeholder="Single, dating, married, divorced…"></label>
    <label>What would you most like help with?<textarea name="goal" placeholder="Describe your relationship over the last 6 months, or the obstacle you want to move past."></textarea></label>
    <label>How soon would you like to start?<select name="when"><option>As soon as possible</option><option>In the next month</option><option>Just exploring</option></select></label>
    <button class="btn" type="submit" style="justify-self:start">Email my note to Andre</button>
  </form>
</div></section>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>'''
    page("book.html", "Book a Complimentary Strategy Call | Andre Paradis — Project Equinox",
         "Book a free breakthrough call with relationship coach Andre Paradis. Choose the session for women or for men.", body, None)


for fn in (home, about, programs, events, media, stories, book):
    fn()
