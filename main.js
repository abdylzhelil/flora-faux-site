// Каталог: добавляйте новые букеты сюда
const bouquets = [
  {name: 'Жёлтый букет', desc: 'Каллы, ранункулюсы и хризантемы в стеклянной вазе', img: 'img/yellow.jpg'},
  {name: 'Голубой букет', desc: 'Маки и гортензия в вазе в стиле гжель', img: 'img/blue.jpg'},
  {name: 'Голубой с жёлтым', desc: 'Яркий контраст: гортензия, антуриум, гладиолус', img: 'img/blue-yellow.jpg'},
  {name: 'Розовый букет', desc: 'Гортензия, маки и антуриумы в расписной вазе', img: 'img/pink.jpg'},
];
const grid = document.getElementById('grid');
for (const b of bouquets) {
  const card = document.createElement('article');
  card.className = 'card';
  const img = document.createElement('img');
  img.src = b.img; img.alt = b.name; img.loading = 'lazy';
  const body = document.createElement('div');
  const h = document.createElement('h3'); h.textContent = b.name;
  const p = document.createElement('p'); p.textContent = b.desc;
  const a = document.createElement('a');
  a.href = 'https://www.instagram.com/flora.faux/'; a.target = '_blank'; a.rel = 'noopener';
  a.textContent = 'Заказать →';
  body.append(h, p, a);
  card.append(img, body);
  grid.append(card);
}
