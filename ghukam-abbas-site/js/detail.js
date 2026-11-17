const pageData = JSON.parse(document.getElementById('page-data').textContent);
const languageSwitch = document.getElementById('languageSwitch');

function applyLanguage(lang) {
  const strings = pageData[lang];
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
  document.title = strings.metaTitle;
  document.querySelector('meta[name="description"]').content = strings.metaDescription;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    if (strings[element.dataset.i18n] !== undefined) element.innerHTML = strings[element.dataset.i18n];
  });
  document.querySelectorAll('[data-alt]').forEach(element => {
    element.alt = strings[element.dataset.alt];
  });
  document.querySelectorAll('[data-wa="service"]').forEach(element => {
    element.href = 'https://wa.me/966548912491?text=' + encodeURIComponent(strings.wa);
  });
  document.querySelectorAll('[data-wa-aria]').forEach(element => {
    element.setAttribute('aria-label', strings.whatsappQuote);
  });
  document.querySelector('[data-brand-aria]').setAttribute('aria-label', lang === 'ar' ? 'معلم البلاط والدهانات بالدمام' : 'Dammam Tile and Paint');
  languageSwitch.setAttribute('aria-pressed', String(lang === 'en'));
  languageSwitch.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
  try { localStorage.setItem('site-language', lang); } catch (_) {}
}

let initialLanguage = 'ar';
try { if (localStorage.getItem('site-language') === 'en') initialLanguage = 'en'; } catch (_) {}
applyLanguage(initialLanguage);
languageSwitch.addEventListener('click', () => applyLanguage(document.documentElement.lang === 'ar' ? 'en' : 'ar'));
document.getElementById('year').textContent = new Date().getFullYear();
