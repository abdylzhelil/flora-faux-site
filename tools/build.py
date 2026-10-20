#!/usr/bin/env python3
"""Сборка index.html из data/bouquets.json и data/site.json.

Запуск из корня репозитория:  python3 tools/build.py
Тексты букетов попадают прямо в HTML (их видит Яндекс без JavaScript).
"""
import html
import json
import pathlib
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / 'data/site.json').read_text(encoding='utf-8'))
BOUQUETS = json.loads((ROOT / 'data/bouquets.json').read_text(encoding='utf-8'))
TEMPLATE = (ROOT / 'tools/template.html').read_text(encoding='utf-8')

e = html.escape
WA = SITE['whatsapp']
IG = SITE['instagram']
BASE = SITE['url']


def wa_link(text):
    return f'https://wa.me/{WA}?text={quote(text)}'


ICON_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>')
ICON_IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>')


def contact_buttons(text, short=False):
    """Кнопки WhatsApp + Direct. Работают и без JavaScript."""
    wa_label = 'WhatsApp' if short else 'Написать в WhatsApp'
    ig_label = 'Direct' if short else 'Написать в Direct'
    return (f'<a class="btn wa" href="{e(wa_link(text))}" target="_blank" rel="noopener">{ICON_WA}{wa_label}</a>'
            f'<a class="btn ghost" href="{e(IG)}" target="_blank" rel="noopener" data-copy="{e(text)}">{ICON_IG}{ig_label}</a>')


def picture(b, sizes, cls='', loading='lazy', alt=None):
    img = b['img'][:-4]
    alt = alt if alt is not None else f'Композиция «{b["name"]}»'
    return (f'<picture{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'
            f'<source type="image/webp" srcset="{img}-480.webp 480w, {img}-900.webp 900w" sizes="{sizes}">'
            f'<img src="{b["img"]}" alt="{e(alt)}" width="{b["w"]}" height="{b["h"]}" loading="{loading}" decoding="async">'
            f'</picture>')


def dots(colors):
    return ''.join(f'<i style="background:{c}" title="{e(n)}"></i>' for n, c in colors)


def card(b, i):
    return (f'<a class="card" href="#{b["id"]}" data-open="{b["id"]}">'
            f'<span class="card-ph">{picture(b, "(max-width:760px) 50vw, 360px")}</span>'
            f'<span class="card-body"><span class="card-name">{e(b["name"])}</span>'
            f'<span class="card-dots" aria-hidden="true">{dots(b["colors"])}</span>'
            f'<span class="card-more">Подробнее</span></span></a>')


def sheet(b, i, total):
    desc = ''.join(f'<p>{e(p)}</p>' for p in b['desc'])
    adv = ''.join(f'<li>{e(a)}</li>' for a in b['adv'])
    chips = ''.join(f'<span class="chip"><i style="background:{c}"></i>{e(n)}</span>' for n, c in b['colors'])
    return f'''<dialog class="sheet" id="{b["id"]}" aria-labelledby="t-{b["id"]}">
  <div class="sheet-in">
    <button class="close" type="button" data-close aria-label="Закрыть">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <div class="sheet-ph">{picture(b, "(max-width:760px) 100vw, 480px")}<span class="num">{i:02d} / {total:02d}</span></div>
    <div class="sheet-txt">
      <p class="eyebrow">Интерьерная композиция</p>
      <h3 id="t-{b["id"]}">«{e(b["name"])}»</h3>
      <div class="desc">{desc}</div>
      <ul class="leaf-list">{adv}</ul>
      <div><p class="eyebrow mb">Цветовая гамма</p><div class="palette">{chips}</div></div>
      <p class="vase-note">Можно заказать с вазой или без неё, а также собрать на ваш вкус.</p>
      <div class="btns">{contact_buttons("Здравствуйте! Интересует композиция «" + b["name"] + "».")}</div>
    </div>
  </div>
</dialog>'''


def json_ld():
    data = {
        '@context': 'https://schema.org',
        '@graph': [
            {'@type': 'Store', '@id': BASE + '#store', 'name': SITE['name'], 'url': BASE,
             'description': SITE['description'], 'image': BASE + 'img/yarkoe-nastroenie.jpg',
             'telephone': '+' + WA, 'sameAs': [IG]},
            {'@type': 'ItemList', 'name': 'Каталог композиций', 'itemListElement': [
                {'@type': 'ListItem', 'position': i, 'item': {
                    '@type': 'Product', 'name': b['name'], 'url': BASE + '#' + b['id'],
                    'image': BASE + b['img'], 'description': ' '.join(b['desc']),
                    'color': ', '.join(n for n, _ in b['colors']),
                    'brand': {'@type': 'Brand', 'name': SITE['name']}}}
                for i, b in enumerate(BOUQUETS, 1)]},
        ]}
    return json.dumps(data, ensure_ascii=False, separators=(',', ':'))


def main():
    total = len(BOUQUETS)
    hero = {b['id']: b for b in BOUQUETS}
    out = TEMPLATE
    repl = {
        '{{JSON_LD}}': json_ld(),
        '{{HERO_MAIN}}': picture(hero['yarkoe-nastroenie'], '(max-width:760px) 100vw, 560px', loading='eager').replace('<img ', '<img fetchpriority="high" '),
        '{{HERO_2}}': picture(hero['morskaya-prohlada'], '280px'),
        '{{HERO_3}}': picture(hero['solnechnyi-sad'], '280px'),
        '{{CARDS}}': '\n'.join(card(b, i) for i, b in enumerate(BOUQUETS, 1)),
        '{{SHEETS}}': '\n'.join(sheet(b, i, total) for i, b in enumerate(BOUQUETS, 1)),
        '{{CONTACTS}}': contact_buttons('Здравствуйте! Хочу заказать композицию.'),
        '{{CONTACTS_SHORT}}': contact_buttons('Здравствуйте! Хочу заказать композицию.', short=True),
        '{{WA_ORDER}}': e(wa_link('Здравствуйте! Хочу заказать композицию.')),
        '{{COUNT}}': str(total),
        '{{METRIKA_ID}}': str(SITE.get('metrika_id', '')),
    }
    for k, v in repl.items():
        out = out.replace(k, v)
    assert '{{' not in out, 'не все подстановки заполнены'
    (ROOT / 'index.html').write_text(out, encoding='utf-8')
    print('index.html собран:', len(out), 'байт,', total, 'композиций')


if __name__ == '__main__':
    main()
