"""Set the confirmed public URL and optional Google HTML verification token."""
import argparse, html, re
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, help='Confirmed public HTTPS URL, including any hosting subpath')
parser.add_argument('--google-token', help='Content value from Google Search Console HTML verification tag')
a = parser.parse_args()
u = urlsplit(a.url)
if u.scheme != 'https' or not u.hostname or u.username or u.password or u.query or u.fragment:
    parser.error('Provide a public HTTPS URL without credentials, query or fragment.')
root = Path(__file__).resolve().parents[1]
url = a.url.rstrip('/') + '/'
p = root / 'index.html'
s = p.read_text()
s = re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>', '', s)
s = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*', lambda m: m[1] + html.escape(url + 'assets/social-card.jpg', quote=True), s)
head = '<link rel="canonical" href="' + html.escape(url, quote=True) + '"><meta property="og:url" content="' + html.escape(url, quote=True) + '">'
if a.google_token:
    s = re.sub(r'<meta name="google-site-verification"[^>]*>', '', s)
    head += '<meta name="google-site-verification" content="' + html.escape(a.google_token, quote=True) + '">'
p.write_text(s.replace('</head>', head + '</head>'))
(root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + escape(url) + '</loc></url></urlset>\n')
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + url + 'sitemap.xml\n')
print('Updated canonical, social image URLs, sitemap.xml and robots.txt.' + (' Google verification tag added; verification must be completed in Search Console.' if a.google_token else ' No Google verification token supplied.'))
