# Вечный букет (flora.faux) — www.flora-faux.ru

Лендинг-каталог интерьерных композиций. Хостинг: GitHub Pages, DNS: Cloudflare (DNS only), домен: Рег.ру.

## Как устроено
- `data/bouquets.json` — композиции (название, фото, описание, преимущества, цвета).
- `data/site.json` — контакты (WhatsApp, Instagram), номер Яндекс Метрики (`metrika_id`).
- `tools/template.html` — вёрстка и стили; `tools/build.py` — собирает `index.html`.
- `index.html` — готовая страница (генерируется, руками не править).
- `img/` — фото: `*.jpg` (оригинал, для превью ссылок) + `*-480.webp` / `*-900.webp` (для сайта).
- `fonts/` — шрифты (с сайта, без Google Fonts).
- `privacy.html` — политика конфиденциальности. `PLAN.md` — план работ и сроки.

## Как изменить
1. Поправить `data/*.json` (или `tools/template.html`).
2. `python3 tools/build.py`
3. Закоммитить и запушить в `main` — сайт обновится за 1–2 минуты.

Новое фото: положить `img/<id>.jpg` и сделать WebP-версии 480 и 900 px (см. историю коммитов).
