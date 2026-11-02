// Gemini Notebook capture, run in the notebook page (devtools console, or a browser agent's JS tool).
//
// Defines on window:
//   __reset()            delete the chat history (the notebook's own menu item and confirm dialog)
//   __ask(q)             type q into the chat box, send, wait until the answer is finished
//   __capture()          expand collapsed markers, read the answer text with each marker as [n],
//                        and for every distinct marker open its citation panel and read the source
//                        name and the chunk text it shows
//   __save(name, q, tag) download the capture as gf-cc-{name}.json (the browser must allow the
//                        site to download several files) and keep a copy in localStorage
//   __run(name, q, tag)  reset, ask, capture, save; progress in window.__status
//
// What is captured is Gemini's own output: the rendered answer and its citation panels. Studio
// files aren't touched here; check the Studio panel by eye and delete anything there before a run.
const sleep = ms => new Promise(r => setTimeout(r, ms));
const esc = () => document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));

window.__reset = async () => {
  if (document.querySelectorAll('chat-message').length === 0) return 'empty';
  const cfg = [...document.querySelectorAll('button')].find(b => /Notebook configuration/i.test(b.getAttribute('aria-label') || ''));
  cfg.click(); await sleep(600);
  const item = [...document.querySelectorAll('[role=menuitem], button')].find(b => /Delete chat history/i.test(b.innerText));
  if (!item) throw 'no delete item';
  item.click(); await sleep(800);
  const del = [...document.querySelectorAll('mat-dialog-container button, [role=dialog] button')].find(b => b.innerText.trim() === 'Delete');
  if (!del) throw 'no dialog delete';
  del.click();
  for (let k = 0; k < 30 && document.querySelectorAll('chat-message').length; k++) await sleep(300);
  return 'cleared ' + document.querySelectorAll('chat-message').length;
};

window.__ask = async (q) => {
  const ta = [...document.querySelectorAll('textarea')].find(t => /Ask a question/i.test(t.placeholder));
  ta.focus();
  Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(ta, q);
  ta.dispatchEvent(new Event('input', { bubbles: true }));
  await sleep(400);
  [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-label') === 'Submit').click();
  await sleep(3000);
  const t0 = Date.now();
  while (Date.now() - t0 < 300000) {
    const box = [...document.querySelectorAll('textarea')].find(t => /Ask a question|Responding/i.test(t.placeholder));
    const last = [...document.querySelectorAll('chat-message')].pop();
    const busy = /Responding/i.test(box?.placeholder || '') || /Connecting the evidence|Reading|Thinking/i.test(last?.innerText.slice(0, 200) || '');
    if (!busy && document.querySelectorAll('chat-message').length >= 2) break;
    await sleep(2000);
  }
  await sleep(4000);
  return Math.round((Date.now() - t0) / 1000);
};

window.__capture = async () => {
  const cm = [...document.querySelectorAll('chat-message')].pop();
  const msg = cm.querySelector('.to-user-message-card-content');
  for (let k = 0; k < 30; k++) {
    const more = [...msg.querySelectorAll('button.citation-marker')].find(b => b.innerText.trim() === 'more_horiz');
    if (!more) break;
    more.click(); await sleep(300);
  }
  esc(); await sleep(200);
  const body = [...msg.querySelectorAll('.message-text-content')].pop();
  const clone = body.cloneNode(true);
  clone.querySelectorAll('button.citation-marker').forEach(b => { const t = b.innerText.trim(); b.replaceWith(/^\d+$/.test(t) ? `[${t}]` : ''); });
  clone.style.position = 'absolute'; clone.style.left = '-99999px'; clone.style.width = '700px';
  document.body.appendChild(clone);
  const text = clone.innerText;
  clone.remove();
  const nums = [...body.querySelectorAll('button.citation-marker')].filter(b => /^\d+$/.test(b.innerText.trim()));
  const occ = nums.map(b => {
    const blk = b.closest('p, li') || b.parentElement.parentElement;
    const r = document.createRange(); r.setStart(blk, 0); r.setEndBefore(b);
    return { n: +b.innerText.trim(), context: r.toString().replace(/\s+/g, ' ').trim().slice(-250) };
  });
  const legend = {};
  for (const b of nums) {
    const n = b.innerText.trim();
    if (legend[n]) continue;
    esc(); await sleep(250);
    b.scrollIntoView({ block: 'center' }); b.click();
    let p = null;
    for (let k = 0; k < 25; k++) { await sleep(200); p = document.querySelector('.citation-tooltip-panel'); if (p && p.innerText.trim()) break; }
    const lines = (p ? p.innerText : '').replace(/\nView source\s*$/, '').split('\n');
    legend[n] = { source: lines[0], chunk: lines.slice(1).join('\n') };
    esc(); await sleep(150);
  }
  return { text, occ, legend };
};

window.__save = (name, question, tag) => {
  const r = window.__last;
  const body = JSON.stringify({
    id: name, notebook_tag: tag, question, captured_at: new Date().toISOString(),
    sources_ticked: document.body.innerText.match(/(\d+) sources/)?.[1],
    text: r.text.replace(/^Thoughts\nexpand_more\n/, ''), occurrences: r.occ, legend: r.legend,
  }, null, 1);
  try { localStorage.setItem('gfcc-' + name, body); } catch (e) {}
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([body], { type: 'application/json' }));
  a.download = 'gf-cc-' + name + '.json';
  document.body.appendChild(a); a.click(); a.remove();
  return body.length;
};

window.__run = async (name, q, tag) => {
  window.__status = name + ': reset';
  const studioEmpty = /Studio output will be saved here/.test(document.body.innerText);
  const rs = await window.__reset();
  window.__status = name + ': asking';
  const secs = await window.__ask(q);
  window.__status = name + ': capturing';
  window.__last = await window.__capture();
  const user = [...document.querySelectorAll('chat-message .from-user-message-card-content')].pop()?.innerText.trim();
  const len = window.__save(name, q, tag);
  window.__status = name + ': saved ' + JSON.stringify({ rs, studioEmpty, secs, cites: Object.keys(window.__last.legend).length, sameQ: user === q, len });
};
'capture.js loaded';
