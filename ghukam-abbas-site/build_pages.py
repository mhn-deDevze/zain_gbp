"""Generate the static Arabic-first detail pages from bilingual content."""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).parent

SERVICES = {
    "tiles": {
        "file": "tiles.html", "image": "service-tiles.webp", "kind": "tiles",
        "ar": {
            "metaTitle": "تركيب البلاط والسيراميك في الدمام | معلم البلاط والدهانات",
            "metaDescription": "تركيب سيراميك وبورسلين الأرضيات والجدران وإصلاح بلاط الحمامات والمطابخ في الدمام والمنطقة الشرقية. اتصل 0548912491.",
            "eyebrow": "تركيب البلاط والسيراميك", "headline": "تركيب بلاط مرتب للمساحات التي تعيش فيها", "lead": "نركب السيراميك والبورسلين للأرضيات والجدران، ونصلح بلاط الحمامات والمطابخ في الدمام والمدن المجاورة.",
            "pointTitle": "ما الذي يمكننا تنفيذه؟", "pointIntro": "أخبرنا بنوع البلاط ومساحة العمل، أو أرسل صورة للمكان لنفهم المطلوب.",
            "f1Title": "أرضيات سيراميك وبورسلين", "f1Text": "تركيب البلاط للأرضيات السكنية والتجارية مع الاهتمام بتوزيع القطع والتشطيب.",
            "f2Title": "جدران الحمامات والمطابخ", "f2Text": "تركيب بلاط الجدران في المساحات التي تحتاج إلى سطح عملي وسهل التنظيف.",
            "f3Title": "إصلاح البلاط", "f3Text": "إصلاح البلاط المتضرر في الحمامات والمطابخ بحسب حالة المكان.",
            "imageAlt": "تركيب بلاط بورسلين على جدار حمام", "wa": "السلام عليكم، أريد الاستفسار عن تركيب أو إصلاح البلاط"
        },
        "en": {
            "metaTitle": "Tile and Ceramic Installation in Dammam | Dammam Tile & Paint",
            "metaDescription": "Ceramic and porcelain floor and wall installation, plus bathroom and kitchen tile repairs in Dammam and nearby cities. Call 054 891 2491.",
            "eyebrow": "TILE & CERAMIC INSTALLATION", "headline": "Tile work made for the spaces you use", "lead": "We install ceramic and porcelain floor and wall tiles, and repair bathroom and kitchen tiles in Dammam and nearby cities.",
            "pointTitle": "What can we do?", "pointIntro": "Tell us the tile type and size of the space, or send a photo so we can understand the work.",
            "f1Title": "Ceramic and porcelain floors", "f1Text": "Floor tile installation for homes and commercial spaces with attention to layout and finish.",
            "f2Title": "Bathroom and kitchen walls", "f2Text": "Wall tiles for spaces that need a practical, easy-to-clean surface.",
            "f3Title": "Tile repairs", "f3Text": "Repairs to damaged bathroom and kitchen tiles based on the condition of the space.",
            "imageAlt": "Installing porcelain tile on a bathroom wall", "wa": "Hello, I would like to ask about tile installation or repair"
        }
    },
    "painting": {
        "file": "painting.html", "image": "service-paint.webp", "kind": "paint",
        "ar": {
            "metaTitle": "دهانات داخلية وخارجية في الدمام | معلم البلاط والدهانات",
            "metaDescription": "دهانات داخلية وخارجية وديكورية للمنازل والمباني التجارية في الدمام والمنطقة الشرقية. اتصل 0548912491.",
            "eyebrow": "الدهانات والتشطيبات", "headline": "لون وتشطيب يغيران إحساس المكان", "lead": "ننفذ الدهانات الداخلية والخارجية والدهانات الديكورية للمنازل والمساحات التجارية.",
            "pointTitle": "خدمات الدهان", "pointIntro": "أرسل لنا صورة الجدار أو المساحة، وأخبرنا باللون أو المظهر الذي تفضله.",
            "f1Title": "دهانات داخلية", "f1Text": "دهان غرف المعيشة والنوم والممرات والمساحات الداخلية الأخرى.",
            "f2Title": "دهانات خارجية", "f2Text": "تشطيب واجهات وجدران خارجية بحسب طبيعة السطح والعمل المطلوب.",
            "f3Title": "دهانات ديكورية", "f3Text": "تشطيبات تضيف طابعاً خاصاً للجدران الداخلية.",
            "imageAlt": "دهان جدار داخلي في منزل حديث", "wa": "السلام عليكم، أريد الاستفسار عن أعمال الدهانات"
        },
        "en": {
            "metaTitle": "Interior and Exterior Painting in Dammam | Dammam Tile & Paint",
            "metaDescription": "Interior, exterior and decorative painting for homes and commercial spaces in Dammam and the Eastern Province. Call 054 891 2491.",
            "eyebrow": "PAINTING & FINISHES", "headline": "A fresh finish for your space", "lead": "We handle interior, exterior and decorative painting for homes and commercial spaces.",
            "pointTitle": "Painting services", "pointIntro": "Send a photo of the wall or space and tell us the color or finish you have in mind.",
            "f1Title": "Interior painting", "f1Text": "Painting living rooms, bedrooms, corridors and other indoor spaces.",
            "f2Title": "Exterior painting", "f2Text": "Finishing exterior walls and facades according to the surface and work required.",
            "f3Title": "Decorative finishes", "f3Text": "Finishes that give interior walls a distinctive look.",
            "imageAlt": "Painting an interior wall in a modern home", "wa": "Hello, I would like to ask about painting work"
        }
    },
    "plastering": {
        "file": "plastering.html", "image": "service-plaster.webp", "kind": "plaster",
        "ar": {
            "metaTitle": "أعمال اللياسة والترميم في الدمام | معلم البلاط والدهانات",
            "metaDescription": "لياسة الجدران وترميم الأسطح للمنازل والمباني التجارية في الدمام والمنطقة الشرقية. اتصل 0548912491.",
            "eyebrow": "اللياسة والترميم", "headline": "سطح متماسك يبدأ بتجهيز صحيح", "lead": "ننفذ أعمال اللياسة وترميم الأسطح في المباني السكنية والتجارية، تمهيداً للتشطيبات التالية.",
            "pointTitle": "أعمال اللياسة والترميم", "pointIntro": "اشرح حالة الجدار أو أرسل صورة واضحة للسطح الذي يحتاج إلى عمل.",
            "f1Title": "لياسة الجدران", "f1Text": "تجهيز وتسوية الجدران الداخلية ضمن أعمال البناء والتشطيب.",
            "f2Title": "ترميم الأسطح", "f2Text": "معالجة مناطق السطح المتضررة بحسب حالة المكان ونوع العمل.",
            "f3Title": "منازل ومبانٍ تجارية", "f3Text": "أعمال للغرف والممرات والمساحات التجارية التي تحتاج إلى تجهيز أو ترميم.",
            "imageAlt": "تسوية اللياسة على جدار داخلي", "wa": "السلام عليكم، أريد الاستفسار عن أعمال اللياسة والترميم"
        },
        "en": {
            "metaTitle": "Plastering and Surface Repair in Dammam | Dammam Tile & Paint",
            "metaDescription": "Wall plastering and surface restoration for homes and commercial buildings in Dammam and the Eastern Province. Call 054 891 2491.",
            "eyebrow": "PLASTERING & RESTORATION", "headline": "Good finishing starts with the surface", "lead": "We carry out plastering and surface restoration in homes and commercial buildings, preparing spaces for the next finish.",
            "pointTitle": "Plastering and repair work", "pointIntro": "Describe the wall condition or send a clear photo of the surface that needs work.",
            "f1Title": "Wall plastering", "f1Text": "Preparing and smoothing interior walls as part of construction and finishing work.",
            "f2Title": "Surface restoration", "f2Text": "Working on damaged areas according to the condition of the space and the job required.",
            "f3Title": "Homes and commercial spaces", "f3Text": "Work for rooms, corridors and commercial areas needing preparation or repair.",
            "imageAlt": "Smoothing plaster on an interior wall", "wa": "Hello, I would like to ask about plastering and restoration"
        }
    },
    "gypsum": {
        "file": "gypsum-board.html", "image": "service-gypsum.webp", "kind": "gypsum",
        "ar": {
            "metaTitle": "تركيب الجبس بورد في الدمام | أسقف وجدران جبس بورد",
            "metaDescription": "أعمال الجبس بورد للأسقف والجدران وتشطيباتها في الدمام والمنطقة الشرقية. اتصل 0548912491 أو راسلنا على واتساب.",
            "eyebrow": "أعمال الجبس بورد", "headline": "جبس بورد يضيف شكلاً منظماً للمكان", "lead": "ننفذ أسقف وجدران الجبس بورد وتشطيباتها للمنازل والمساحات التجارية في الدمام والمدن المجاورة.",
            "pointTitle": "أعمال الجبس بورد", "pointIntro": "أرسل صورة للمساحة، واذكر إن كنت تحتاج إلى سقف أو جدار جبس بورد.",
            "f1Title": "أسقف جبس بورد", "f1Text": "تركيب أسقف جبس بورد للمساحات الداخلية حسب شكل المكان واحتياجه.",
            "f2Title": "جدران وتقسيمات", "f2Text": "أعمال جدران الجبس بورد وتقسيم المساحات الداخلية.",
            "f3Title": "تشطيب الجبس بورد", "f3Text": "تجهيز وتشطيب الأسطح لتظهر بصورة مرتبة ومتناسقة مع المكان.",
            "imageAlt": "تركيب سقف جبس بورد في منزل حديث", "wa": "السلام عليكم، أريد الاستفسار عن أعمال الجبس بورد"
        },
        "en": {
            "metaTitle": "Gypsum Board Installation in Dammam | Ceilings and Walls",
            "metaDescription": "Gypsum board ceilings, walls and finishing in Dammam and the Eastern Province. Call 054 891 2491 or message us on WhatsApp.",
            "eyebrow": "GYPSUM BOARD WORK", "headline": "Gypsum board that shapes your space", "lead": "We install and finish gypsum board ceilings and walls for homes and commercial spaces in Dammam and nearby cities.",
            "pointTitle": "Gypsum board services", "pointIntro": "Send a photo of the space and tell us whether you need a gypsum board ceiling or wall.",
            "f1Title": "Gypsum board ceilings", "f1Text": "Installing gypsum board ceilings for interior spaces according to the room's shape and needs.",
            "f2Title": "Walls and partitions", "f2Text": "Gypsum board walls and interior space division.",
            "f3Title": "Gypsum board finishing", "f3Text": "Preparing and finishing surfaces for a neat look that fits the space.",
            "imageAlt": "Installing a gypsum board ceiling in a modern home", "wa": "Hello, I would like to ask about gypsum board work"
        }
    }
}

COMMON_AR = {
    "skip":"تجاوز إلى المحتوى", "brand":"معلم البلاط والدهانات<br><small>بالدمام والمنطقة الشرقية</small>",
    "navHome":"الرئيسية", "navServices":"الخدمات", "navAreas":"مناطق الخدمة", "navContact":"اتصل بنا", "menu":"القائمة", "callNow":"اتصل الآن",
    "breadcrumbHome":"الرئيسية", "callNumber":"اتصل: 054 891 2491", "whatsappQuote":"راسلنا على واتساب", "coverage":"نخدم الدمام، سيهات، الظهران، القطيف، الجبيل والخبر",
    "nextTitle":"ابدأ برسالة أو مكالمة", "nextText":"أخبرنا بالخدمة المطلوبة وموقعك. يمكنك إرسال صورة للمكان عبر واتساب.",
    "relatedTitle":"خدمات أخرى قد تحتاجها", "moreServices":"جميع الخدمات", "footerBrand":"معلم البلاط والدهانات بالدمام", "footerTag":"تركيب البلاط • الدهانات • الجبس بورد • اللياسة والترميم", "rights":"جميع الحقوق محفوظة", "mobileWhatsApp":"واتساب"
}
COMMON_EN = {
    "skip":"Skip to content", "brand":"Dammam Tile & Paint<br><small>Eastern Province services</small>",
    "navHome":"Home", "navServices":"Services", "navAreas":"Service areas", "navContact":"Contact", "menu":"Menu", "callNow":"Call now",
    "breadcrumbHome":"Home", "callNumber":"Call: 054 891 2491", "whatsappQuote":"Message on WhatsApp", "coverage":"Serving Dammam, Saihat, Dhahran, Al Qatif, Al Jubail and Al Khobar",
    "nextTitle":"Start with a message or call", "nextText":"Tell us the service you need and your location. You can send a photo of the space on WhatsApp.",
    "relatedTitle":"Other services you may need", "moreServices":"All services", "footerBrand":"Dammam Tile & Paint", "footerTag":"Tile installation • Painting • Gypsum board • Plastering and restoration", "rights":"All rights reserved", "mobileWhatsApp":"WhatsApp"
}

def tr(key, value):
    return f'<span data-i18n="{key}">{value}</span>'

def header():
    return '''<header class="site-header"><div class="shell header-inner">
      <a class="brand" href="index.html" aria-label="معلم البلاط والدهانات بالدمام" data-brand-aria><span class="brand-mark" aria-hidden="true"><span></span><span></span><span></span><span></span></span><span class="brand-name" data-i18n="brand">معلم البلاط والدهانات<br><small>بالدمام والمنطقة الشرقية</small></span></a>
      <nav class="desktop-nav" aria-label="Main navigation"><a href="index.html" data-i18n="navHome">الرئيسية</a><a href="index.html#services" data-i18n="navServices">الخدمات</a><a href="service-areas.html" data-i18n="navAreas">مناطق الخدمة</a><a href="contact.html" data-i18n="navContact">اتصل بنا</a></nav>
      <details class="mobile-menu"><summary data-i18n="menu">القائمة</summary><nav aria-label="Mobile navigation"><a href="index.html" data-i18n="navHome">الرئيسية</a><a href="index.html#services" data-i18n="navServices">الخدمات</a><a href="service-areas.html" data-i18n="navAreas">مناطق الخدمة</a><a href="contact.html" data-i18n="navContact">اتصل بنا</a></nav></details>
      <div class="header-actions"><button class="language-switch" id="languageSwitch" type="button" aria-label="Switch to English" aria-pressed="false"><span>عربي</span><span class="switch-track" aria-hidden="true"><span></span></span><span>EN</span></button><a class="header-call" href="tel:+966548912491"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 3.5 9.8 3l1.7 4.1-2 1.8a15 15 0 0 0 5.6 5.6l1.8-2L21 14.2l-.5 3.2a3 3 0 0 1-3.3 2.5A16.5 16.5 0 0 1 4.1 6.8 3 3 0 0 1 6.6 3.5Z"/></svg><span data-i18n="callNow">اتصل الآن</span></a></div>
    </div></header>'''

def footer():
    return '''<footer class="site-footer"><div class="shell footer-inner"><div><strong data-i18n="footerBrand">معلم البلاط والدهانات بالدمام</strong><span data-i18n="footerTag">تركيب البلاط • الدهانات • الجبس بورد • اللياسة والترميم</span></div><div class="footer-links"><a href="index.html" data-i18n="navHome">الرئيسية</a><a href="index.html#services" data-i18n="navServices">الخدمات</a><a href="service-areas.html" data-i18n="navAreas">مناطق الخدمة</a><a href="contact.html" data-i18n="navContact">اتصل بنا</a><a href="tel:+966548912491" dir="ltr">+966 54 891 2491</a><span>© <span id="year"></span> <span data-i18n="rights">جميع الحقوق محفوظة</span></span></div></div></footer>
  <a class="floating-whatsapp" href="https://wa.me/966548912491" data-wa="service" data-wa-aria aria-label="راسلنا على واتساب" title="WhatsApp" target="_blank" rel="noopener noreferrer"><img src="assets/whatsapp-logo.svg" width="42" height="42" alt="" aria-hidden="true"></a>
  <div class="mobile-cta" aria-label="Contact options"><a href="tel:+966548912491"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 3.5 9.8 3l1.7 4.1-2 1.8a15 15 0 0 0 5.6 5.6l1.8-2L21 14.2l-.5 3.2a3 3 0 0 1-3.3 2.5A16.5 16.5 0 0 1 4.1 6.8 3 3 0 0 1 6.6 3.5Z"/></svg><span data-i18n="callNow">اتصل الآن</span></a><a class="mobile-whatsapp" href="https://wa.me/966548912491" data-wa="service" target="_blank" rel="noopener noreferrer"><span data-i18n="mobileWhatsApp">واتساب</span></a></div>'''

def document(page_id, content, body, structured=None, preload=None):
    ar = {**COMMON_AR, **content['ar']}
    en = {**COMMON_EN, **content['en']}
    payload = json.dumps({"ar": ar, "en": en}, ensure_ascii=False).replace('</', '<\\/')
    ld = f'<script type="application/ld+json">{json.dumps(structured,ensure_ascii=False)}</script>' if structured else ''
    preload_tag = f'<link rel="preload" as="image" href="assets/images/{preload}" fetchpriority="high">' if preload else ''
    return f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#163d39"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><title>{escape(ar['metaTitle'])}</title><meta name="description" content="{escape(ar['metaDescription'],quote=True)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">{preload_tag}<link rel="stylesheet" href="css/style.css">{ld}</head><body data-page="{page_id}"><a class="skip-link" href="#main" data-i18n="skip">تجاوز إلى المحتوى</a>{header()}<main id="main">{body}</main>{footer()}<script id="page-data" type="application/json">{payload}</script><script src="js/detail.js" defer></script></body></html>'''

def service_page(slug, item):
    ar = item['ar']
    chips = ''.join(f'<div class="detail-point"><span class="point-num">0{i}</span><h3 data-i18n="f{i}Title">{escape(ar[f"f{i}Title"])}</h3><p data-i18n="f{i}Text">{escape(ar[f"f{i}Text"])}</p></div>' for i in range(1,4))
    related = ''.join(f'<a class="related-card" href="{escape(other["file"])}"><img src="assets/images/{other["image"]}" alt="" loading="lazy" decoding="async"><span data-i18n="related_{key}">{escape(other["ar"]["eyebrow"])}</span><span aria-hidden="true">↗</span></a>' for key,other in SERVICES.items() if key != slug)
    for lang in ('ar','en'):
        item[lang].update({f'related_{key}':other[lang]['eyebrow'] for key,other in SERVICES.items() if key != slug})
    body = f'''<nav class="breadcrumb shell" aria-label="Breadcrumb"><a href="index.html" data-i18n="breadcrumbHome">الرئيسية</a><span aria-hidden="true">/</span><span data-i18n="eyebrow">{escape(ar['eyebrow'])}</span></nav>
    <section class="detail-hero"><div class="shell detail-hero-grid"><div class="detail-hero-copy"><span class="eyebrow" data-i18n="eyebrow">{escape(ar['eyebrow'])}</span><h1 data-i18n="headline">{escape(ar['headline'])}</h1><p data-i18n="lead">{escape(ar['lead'])}</p><div class="hero-actions"><a class="button button-primary" href="https://wa.me/966548912491" data-wa="service" target="_blank" rel="noopener noreferrer" data-i18n="whatsappQuote">راسلنا على واتساب</a><a class="button button-dark-outline" href="tel:+966548912491" data-i18n="callNumber">اتصل: 054 891 2491</a></div><div class="detail-coverage" data-i18n="coverage">{COMMON_AR['coverage']}</div></div><div class="detail-hero-photo"><img src="assets/images/{item['image']}" width="720" height="720" alt="{escape(ar['imageAlt'],quote=True)}" data-alt="imageAlt" fetchpriority="high"></div></div></section>
    <section class="detail-points section-pad"><div class="shell"><div class="section-heading"><div><span class="eyebrow" data-i18n="eyebrow">{escape(ar['eyebrow'])}</span><h2 data-i18n="pointTitle">{escape(ar['pointTitle'])}</h2></div><p data-i18n="pointIntro">{escape(ar['pointIntro'])}</p></div><div class="point-grid">{chips}</div></div></section>
    <section class="detail-next section-pad"><div class="shell detail-next-inner"><div><span class="eyebrow light" data-i18n="eyebrow">{escape(ar['eyebrow'])}</span><h2 data-i18n="nextTitle">{COMMON_AR['nextTitle']}</h2><p data-i18n="nextText">{COMMON_AR['nextText']}</p></div><div class="contact-actions"><a class="button button-primary" href="https://wa.me/966548912491" data-wa="service" target="_blank" rel="noopener noreferrer" data-i18n="whatsappQuote">راسلنا على واتساب</a><a class="button button-light" href="tel:+966548912491" data-i18n="callNow">اتصل الآن</a></div></div></section>
    <section class="related section-pad"><div class="shell"><div class="section-heading"><div><span class="eyebrow" data-i18n="moreServices">جميع الخدمات</span><h2 data-i18n="relatedTitle">خدمات أخرى قد تحتاجها</h2></div></div><div class="related-grid">{related}</div><a class="text-link" href="index.html#services" data-i18n="moreServices">جميع الخدمات</a></div></section>'''
    structured = {"@context":"https://schema.org","@type":"Service","name":ar['eyebrow'],"description":ar['lead'],"provider":{"@type":"HomeAndConstructionBusiness","name":"معلم البلاط والدهانات بالدمام","telephone":"+966548912491"},"areaServed":["Dammam","Saihat","Dhahran","Al Qatif","Al Jubail","Al Khobar"]}
    (ROOT/item['file']).write_text(document(slug,item,body,structured,item['image']))

for key,value in SERVICES.items():
    service_page(key,value)

AREAS = {
    "ar": {"metaTitle":"مناطق خدمة البلاط والدهانات في الدمام والمنطقة الشرقية","metaDescription":"خدمات تركيب البلاط والدهانات والجبس بورد واللياسة في الدمام، سيهات، الظهران، القطيف، الجبيل والخبر. خدمة في موقع العميل.","eyebrow":"مناطق الخدمة","headline":"نأتي إليك في الدمام والمنطقة الشرقية","lead":"خدمات البلاط والدهانات والجبس بورد واللياسة للمنازل والمباني التجارية في المدن التالية. الخدمة في موقع العميل ولا يوجد مقر لاستقبال الزوار.","areaHeading":"المدن التي نخدمها","areaNote":"أخبرنا بموقعك عند التواصل لنناقش العمل المطلوب.","dammam":"الدمام","saihat":"سيهات","dhahran":"الظهران","qatif":"القطيف","jubail":"الجبيل","khobar":"الخبر","wa":"السلام عليكم، أريد الاستفسار عن الخدمة في مدينتي"},
    "en": {"metaTitle":"Tile, Paint and Gypsum Board Service Areas | Eastern Province","metaDescription":"Tile, painting, gypsum board and plastering services in Dammam, Saihat, Dhahran, Al Qatif, Al Jubail and Al Khobar. On-site service.","eyebrow":"SERVICE AREAS","headline":"We come to you across the Eastern Province","lead":"Tile, painting, gypsum board and plastering for homes and commercial buildings in the cities below. Service takes place at your property; there is no walk-in location.","areaHeading":"Cities we serve","areaNote":"Tell us your location when you contact us so we can discuss the work you need.","dammam":"Dammam","saihat":"Saihat","dhahran":"Dhahran","qatif":"Al Qatif","jubail":"Al Jubail","khobar":"Al Khobar","wa":"Hello, I would like to ask about service in my city"}
}
areas_list = ''.join(f'<li data-i18n="{k}">{AREAS["ar"][k]}</li>' for k in ('dammam','saihat','dhahran','qatif','jubail','khobar'))
areas_body = f'''<nav class="breadcrumb shell" aria-label="Breadcrumb"><a href="index.html" data-i18n="breadcrumbHome">الرئيسية</a><span aria-hidden="true">/</span><span data-i18n="eyebrow">مناطق الخدمة</span></nav><section class="simple-hero"><div class="shell"><span class="eyebrow light" data-i18n="eyebrow">مناطق الخدمة</span><h1 data-i18n="headline">نأتي إليك في الدمام والمنطقة الشرقية</h1><p data-i18n="lead">{AREAS['ar']['lead']}</p></div></section><section class="section-pad area-page"><div class="shell"><div class="section-heading"><div><span class="eyebrow" data-i18n="eyebrow">مناطق الخدمة</span><h2 data-i18n="areaHeading">المدن التي نخدمها</h2></div><p data-i18n="areaNote">{AREAS['ar']['areaNote']}</p></div><ul class="area-page-list">{areas_list}</ul><div class="area-page-cta"><a class="button button-primary" href="https://wa.me/966548912491" data-wa="service" target="_blank" rel="noopener noreferrer" data-i18n="whatsappQuote">راسلنا على واتساب</a><a class="button button-dark-outline" href="tel:+966548912491" data-i18n="callNumber">اتصل: 054 891 2491</a></div></div></section>'''
(ROOT/'service-areas.html').write_text(document('areas',AREAS,areas_body))

CONTACT = {
    "ar": {"metaTitle":"اتصل بمعلم البلاط والدهانات بالدمام | 0548912491","metaDescription":"اتصل 0548912491 أو راسل معلم البلاط والدهانات بالدمام عبر واتساب لخدمات البلاط والدهانات والجبس بورد واللياسة.","eyebrow":"اتصل بنا","headline":"تواصل معنا لنناقش شغلك","lead":"اتصل مباشرة أو أرسل رسالة واتساب. أخبرنا بنوع الخدمة، مدينتك، وصورة للمكان إن أمكن.","phoneTitle":"اتصل بنا","phoneText":"للتحدث عن الخدمة المطلوبة مباشرة.","waTitle":"راسلنا على واتساب","waText":"أرسل التفاصيل وصورة للمكان في رسالة واحدة.","helpTitle":"ماذا تكتب في الرسالة؟","help1":"نوع الخدمة المطلوبة","help2":"المدينة أو الحي","help3":"صورة للمكان إن أمكن","wa":"السلام عليكم، أريد الاستفسار عن خدمات البلاط والدهانات والجبس بورد"},
    "en": {"metaTitle":"Contact Dammam Tile & Paint | 054 891 2491","metaDescription":"Call 054 891 2491 or message Dammam Tile & Paint on WhatsApp about tile, painting, gypsum board and plastering services.","eyebrow":"CONTACT","headline":"Tell us about the work you need","lead":"Call us directly or send a WhatsApp message. Tell us the service, your city, and include a photo of the space if you can.","phoneTitle":"Call us","phoneText":"Speak directly about the service you need.","waTitle":"Message on WhatsApp","waText":"Send the details and a photo of the space in one message.","helpTitle":"What to include in your message","help1":"The service you need","help2":"Your city or neighborhood","help3":"A photo of the space if possible","wa":"Hello, I would like to ask about tile, painting or gypsum board services"}
}
contact_body = f'''<nav class="breadcrumb shell" aria-label="Breadcrumb"><a href="index.html" data-i18n="breadcrumbHome">الرئيسية</a><span aria-hidden="true">/</span><span data-i18n="eyebrow">اتصل بنا</span></nav><section class="simple-hero"><div class="shell"><span class="eyebrow light" data-i18n="eyebrow">اتصل بنا</span><h1 data-i18n="headline">تواصل معنا لنناقش شغلك</h1><p data-i18n="lead">{CONTACT['ar']['lead']}</p></div></section><section class="section-pad contact-page"><div class="shell"><div class="contact-methods"><a class="contact-method" href="tel:+966548912491"><span class="method-icon">☎</span><h2 data-i18n="phoneTitle">اتصل بنا</h2><p data-i18n="phoneText">للتحدث عن الخدمة المطلوبة مباشرة.</p><strong dir="ltr">054 891 2491</strong></a><a class="contact-method" href="https://wa.me/966548912491" data-wa="service" target="_blank" rel="noopener noreferrer"><span class="method-icon">↗</span><h2 data-i18n="waTitle">راسلنا على واتساب</h2><p data-i18n="waText">أرسل التفاصيل وصورة للمكان في رسالة واحدة.</p><strong dir="ltr">wa.me/966548912491</strong></a></div><div class="contact-help"><span class="eyebrow" data-i18n="eyebrow">اتصل بنا</span><h2 data-i18n="helpTitle">ماذا تكتب في الرسالة؟</h2><ol><li data-i18n="help1">نوع الخدمة المطلوبة</li><li data-i18n="help2">المدينة أو الحي</li><li data-i18n="help3">صورة للمكان إن أمكن</li></ol></div></div></section>'''
(ROOT/'contact.html').write_text(document('contact',CONTACT,contact_body))
