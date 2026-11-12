"""빌드된 index.html(한국어)에서 번역 단위(한글이 들어간 문자열)를 뽑아 i18n/ko.json으로 저장합니다."""
import json, re, pathlib
from bs4 import BeautifulSoup, NavigableString, Comment
ROOT = pathlib.Path(__file__).resolve().parent.parent
HANGUL = re.compile(r'[가-힣]')

def units(soup):
    seen, out = set(), []
    def add(s):
        s = s.strip()
        if s and HANGUL.search(s) and s not in seen:
            seen.add(s); out.append(s)
    if soup.title: add(soup.title.string)
    for m in soup.find_all('meta'):
        add(m.get('content', ''))
    for sc in soup.find_all('script', type='application/ld+json'):
        def walk(o):
            if isinstance(o, dict): [walk(v) for v in o.values()]
            elif isinstance(o, list): [walk(v) for v in o]
            elif isinstance(o, str): add(o)
        walk(json.loads(sc.string))
    for el in soup.body.find_all(True):
        for a in ('alt', 'aria-label', 'title'):
            if el.has_attr(a): add(el[a])
    def visit(el):
        if el.name in ('script', 'style'): return
        direct = any(isinstance(c, NavigableString) and not isinstance(c, Comment) and HANGUL.search(c) for c in el.children)
        if direct:
            add(el.decode_contents()); return
        for c in el.children:
            if getattr(c, 'name', None): visit(c)
    visit(soup.body)
    return out

if __name__ == '__main__':
    soup = BeautifulSoup((ROOT / 'index.html').read_text(), 'html.parser')  # 빌드된 한국어 페이지 기준
    u = units(soup)
    (ROOT / 'i18n/ko.json').write_text(json.dumps(u, ensure_ascii=False, indent=1))
    print(len(u), 'units,', sum(len(x) for x in u), 'chars')
