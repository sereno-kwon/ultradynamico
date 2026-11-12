# Ultradynamico Korea

ultradynamico.rubiworkshop.com 원페이지 정적 사이트. quoc.rubiworkshop.com과 같은 구조와 디자인(영문 Pretendard · 한글 에스코어 드림, 웨이트 400, 흑백과 얇은 라인, 각진 버튼, 라이트/다크 자동)입니다. 영문 라벨은 대문자 변환 없이 대소문자로 표기합니다.

- `index.html` 한국어 원페이지 (Brand · Range · Cava · Brut · Rosé · Mars · Casings(+Comté 림) · Size & Pressure · Story · Showroom)
- `en/index.html`, `ja/index.html` 영어 · 일본어 페이지 (빌드로 생성, 직접 수정하지 않음)
- `index.src.html` 편집용 한국어 원본. 사이즈 표는 `{{SIZE_TABLE}}` 자리에 빌드 시 채워집니다 (`tools/build.py`의 `SIZES`).
- `i18n/` 번역 사전 (`ko.json` 원문 목록, `en.json` · `ja.json` 원문→번역)
- `tools/build.py` 한국어 페이지, 번역 페이지, sitemap.xml을 한 번에 생성
- `404.html` 하위 주소(/cava, /brut, /rose, /mars, /casings, /rozzo, /comte, /size, /pressure, /dealers 등)를 섹션으로 연결
- `images/` 섹션별 이미지 (`hero`, `brand`, `cava`, `brut`, `rose`, `mars`, `treads`, `casings`, `rims`)
- 로고는 Ultradynamico 공식 심볼을 인라인 SVG로 넣었고(`#i-ud`), 파비콘(`favicon.svg`, `favicon-48/96.png`, `apple-touch-icon.png`, `logo-512.png`)도 같은 심볼로 만들어 두었습니다.
- `.github/image-manifest.txt` + `fetch-images.yml` 공식 사이트(ultradynamico.com, Shopify CDN) 이미지 이전용 워크플로

## 처음 올릴 때
1. main에 푸시하면 `fetch-images.yml`이 매니페스트의 이미지를 받아 `images/`에 커밋합니다. Actions → Fetch images from Ultradynamico에서 FAIL이 있으면 해당 줄의 URL을 바꿔 다시 푸시합니다.
2. 배포: GitHub Pages(Settings → Pages → main / root) 또는 Cloudflare Pages(빌드 명령 없음, 출력 디렉터리 `/`)에 연결합니다.
3. 도메인 DNS에 `ultradynamico` CNAME 레코드를 추가합니다 (GitHub Pages는 `sereno-kwon.github.io`, Cloudflare Pages는 프로젝트 주소). CNAME 파일은 이미 들어 있습니다.

## 이미지
매니페스트를 수정해 main에 푸시하면 Actions가 이미지를 받아 `images/`에 커밋합니다.
이미 받은 파일은 건너뛰므로, 이미지를 교체할 때는 해당 파일을 지우거나 새 파일명으로 추가합니다.
루비에서 직접 촬영한 사진으로 바꿀 때는 같은 경로에 덮어쓰면 됩니다.

## 문구 수정과 번역
1. `index.src.html`의 한국어 문구를 고칩니다.
2. `python3 tools/build.py` 로 한국어 페이지를 만들고, `python3 i18n/extract.py` 로 `ko.json`을 갱신합니다.
3. 새로 생기거나 바뀐 한국어 문장을 `en.json` · `ja.json`에 같은 키로 추가합니다. HTML 태그는 원문과 똑같이 유지합니다.
4. 다시 `python3 tools/build.py` 를 실행하면 번역되지 않은 문장이 있을 때 목록으로 알려줍니다.

빌드에는 `beautifulsoup4`가 필요합니다 (`pip install beautifulsoup4`).

## 링크
- 헤더 SHOP, "루비워크샵에서 보기" 버튼: `https://rubiworkshop.com/ultradynamico`
- 거래처 문의: 루비서플라이 02-516-8465, 카카오톡 채널 `https://pf.kakao.com/_NFnBj/chat`
- 푸터 Instagram: `https://www.instagram.com/ultradynamico` (공식 글로벌 계정)
- 공기압 계산기: `https://ultradynamico.com/tools/pressure-calculator`
