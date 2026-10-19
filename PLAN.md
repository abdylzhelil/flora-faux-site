# План: сайт «Вечный букет» (flora.faux)

Адрес сайта: **www.flora-faux.ru** (без www перенаправляет на www).
Сайт: GitHub Pages, репозиторий `abdylzhelil/flora-faux-site`, ветка `main`.
Домен: Рег.ру, оплачен до 08.10.2027.

## Этапы

| # | Этап | Статус |
|---|------|--------|
| 1 | Сайт-лукбук: 6 композиций, WhatsApp + Direct, белый фон, свайп | ✅ готово |
| 2 | Публикация на GitHub Pages | ✅ готово |
| 3 | Домен flora-faux.ru: куплен, DNS настроен | ✅ готово |
| 4 | **HTTPS-сертификат** | ⏳ в работе: DNS перенесён на Cloudflare 19.10.2026, ждём переключения |
| 5 | Яндекс Метрика: счётчик + цели «WhatsApp» и «Direct» | ⏸ после HTTPS |
| 6 | Яндекс Вебмастер: подтверждение, sitemap.xml, регион | ⏸ после HTTPS |
| 7 | Яндекс Директ: кампания, тексты, ключевые слова | ⏸ после 5–6 |

## HTTPS: что было и что делаем

**Проблема.** GitHub не выпускает сертификат: на странице Pages «DNS check unsuccessful (InvalidDNSError)»,
сертификат завис на шаге «1 of 3». Для www.flora-faux.ru — то же самое («DNS Check in Progress» > 10 часов).

**Проверено (19.10.2026):**
- DNS-записи правильные: A @ → 185.199.108–111.153, CNAME www → abdylzhelil.github.io.
- Официальная библиотека GitHub `pages-health-check`: домен valid, https_eligible = true.
- Записи DNS у flora-faux.ru и obyavleniya-dagestan.ru (где HTTPS работает) одинаковые.
- Вывод: серверы GitHub не получают ответ от DNS-серверов Рег.ру (ns1/ns2.reg.ru),
  хотя Google/Cloudflare/AdGuard получают. Сертификат Дагестана, вероятно, выпущен раньше.

**Решение — шаг А (основной): DNS на Cloudflare, бесплатно, режим «DNS only».**

Статус 19.10.2026 21:25 МСК: аккаунт Cloudflare создан, зона flora-faux.ru добавлена (тариф Free),
все 5 записей в режиме DNS only, в Рег.ру указаны серверы **louis.ns.cloudflare.com** и **susan.ns.cloudflare.com**.
В GitHub Pages указан домен **www.flora-faux.ru**.

1. Регистрация на dash.cloudflare.com, тариф Free, включить 2FA.
2. Добавить flora-faux.ru, записи (все с серым облачком «DNS only»):
   - A @ → 185.199.108.153 / .109.153 / .110.153 / .111.153
   - CNAME www → abdylzhelil.github.io
3. В Рег.ру: DNS-серверы → «Свой список» → два сервера `*.ns.cloudflare.com`.
4. Ждать переключения (1–24 ч), проверить «DNS check successful» на странице Pages.
5. Поставить галочку **Enforce HTTPS**.
6. Заменить в сайте адрес на `https://www.flora-faux.ru/` (canonical, og:url, og:image, sitemap.xml, robots.txt).

**Запасной вариант — шаг Б (если с Cloudflare не получится): Yandex Cloud.**
- DNS-зона в Yandex Cloud DNS (платно, десятки ₽/мес) вместо Cloudflare, те же записи.
- Если GitHub всё равно не выпустит сертификат — перенести сайт в Yandex Cloud
  (Object Storage + Certificate Manager, бесплатный сертификат Let's Encrypt) или на хостинг Рег.ру.

**Откат:** в Рег.ру вернуть DNS-серверы ns1.reg.ru / ns2.reg.ru (записи там сохранены).

## Деньги / Рег.ру

- В аккаунте домен flora-faux.ru отображается 2 раза и 4 услуги «Премиум DNS для flora-faux.ru» (до 08.10.2027).
  Написать в поддержку (бесплатная заявка): отключить дубли и лишний «Премиум DNS», вернуть деньги.
- После переноса DNS на Cloudflare «Премиум DNS» не нужен — не продлевать.

## Контакты на сайте

- WhatsApp: +7 967 403-09-70 (константа `WHATSAPP` в index.html)
- Instagram: @flora.faux (кнопки Direct открывают профиль и копируют текст сообщения)
