# معلم البلاط والدهانات بالدمام

Static bilingual multipage website for tile installation, painting, gypsum board, plastering, and restoration services in Dammam and the Eastern Province.

## Business details

- Phone: `+966 54 891 2491`
- WhatsApp: `https://wa.me/966548912491`
- Service areas: Dammam, Saihat, Dhahran, Al Qatif, Al Jubail, Al Khobar
- On-site service only; no walk-in address

## Site

Serve this folder with a static HTTP server. Arabic is the default. The language switch stores the visitor's choice locally across pages. Images in `assets/images/` are illustrative generated photos, compressed to WebP. They do not represent completed customer projects.

Pages: `index.html`, `tiles.html`, `painting.html`, `plastering.html`, `gypsum-board.html`, `service-areas.html`, and `contact.html`. The six subpages are generated from bilingual content in `build_pages.py`; run `python3 build_pages.py` after changing that content. Shared styling is in `css/style.css`, while `js/main.js` and `js/detail.js` handle each page's language switch.

The floating contact button uses the WhatsApp-authored `assets/whatsapp-logo.svg` file, sourced from the [Wikimedia file page](https://meta.wikimedia.org/wiki/File:WhatsApp_Logo_green.svg) that identifies its Meta brand-resource origin. The logo artwork is unchanged.

No canonical URL or sitemap is included because a final website domain was not provided. Add them after the domain is confirmed.
