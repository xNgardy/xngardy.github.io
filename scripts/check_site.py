"""Check the actual Jekyll output for broken local URLs and leaked source files."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.has_title = False
        self.has_main = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'title':
            self.has_title = True
        if tag == 'main':
            self.has_main = True
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img':
            self.images.append(attrs)


root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
assert root.is_dir(), f'Missing Jekyll output: {root}'
pages = {}
errors = []
for path in root.rglob('*.html'):
    page = Page()
    source = path.read_text()
    page.feed(source)
    pages[path] = page
    if not page.has_title or not page.has_main:
        errors.append(f'{path.relative_to(root)}: missing title or main landmark')
    if '{{' in source or '{%' in source:
        errors.append(f'{path.relative_to(root)}: unrendered Liquid template')
    for image in page.images:
        if 'alt' not in image or 'width' not in image or 'height' not in image:
            errors.append(f'{path.relative_to(root)}: image lacks alt or dimensions')

for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or link.startswith('data:'):
            continue
        target = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path:
            target = path
        if target.is_dir():
            target = target / 'index.html'
        target = target.resolve()
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f'{path.relative_to(root)}: broken URL {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {link}')

for private in ['CONTENT_NOTES.md', 'scripts', 'Gemfile', 'manuscript-r0.pdf', 'CSE493_RIDGE_Graduation_Project_Report.pdf']:
    if (root / private).exists():
        errors.append(f'Non-site source leaked into output: {private}')
for required in ['index.html', 'cv/index.html', '404.html', 'sitemap.xml', 'robots.txt', 'assets/files/Pelinsu_Kaleli_CV.pdf']:
    if not (root / required).is_file():
        errors.append(f'Missing output: {required}')
if len(list((root / 'projects').glob('*/index.html'))) != 6:
    errors.append('Expected six project pages')
if errors:
    sys.exit('\n'.join(errors))
print(f'Checked {len(pages)} HTML pages: internal URLs, anchors, image attributes, expected outputs, and source exclusions passed.')
