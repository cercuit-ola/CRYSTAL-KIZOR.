from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
import fitz
pages=[('PART 1', 'Website submission', 'Live website, source code and my design approach', [('My design process', "I took inspiration from architectural design: deliberate proportions, structured grids, generous whitespace, and pencil-line details. I wanted the page to express Crystal's creativity while making her work immediately understandable. I balanced that creative flair with intuitive navigation, clear calls to action, and an easy route to contact."), ('How I connected the ecosystem', 'I positioned Crystal as the person connecting the different initiatives, rather than presenting unrelated businesses. I introduced her first, followed with a linked work overview, and grouped architecture, products, community, education, writing, and speaking into a clear journey. I gave different visitors relevant next steps: explore a studio project, discover an initiative, or start a conversation.'), ('Technology and execution', 'I built the page with Next.js, React, CSS, and lightweight JavaScript, using static export for Netlify. I used local WebP images, lazy loading, responsive layouts, and reduced-motion support. I kept typography, spacing, buttons, and the orange-and-charcoal palette consistent across desktop and mobile. I checked the production build, image assets, and internal links.')], 200), ('PART 2', 'Crystal AI Opportunity Tracker', 'Architecture tenders and speaking opportunities', [('What I would build', "I would build an AI web tracker for Studio COKA and Crystal's team, focused on finding architecture bidding tenders in Nigeria and globally, alongside relevant speaking opportunities for Crystal. It would reduce time spent searching scattered websites and help the team focus on opportunities that match its expertise and eligibility."), ('How the team would use it', 'I would let the team define services, locations, project sizes, credentials, and speaking topics. Every 12 hours, the tracker would check approved government procurement portals, corporate tender pages, development organisations, and conference websites. I would email Crystal a ranked digest of new or changed opportunities, with source links, deadlines, eligibility, required documents, and reasons for each match.'), ('Helping the team choose well', 'I would provide a dashboard where the team could shortlist opportunities, assign an owner, and track deadlines. For tenders, I would surface mandatory requirements and potential qualification gaps. For speaking calls, I would highlight the audience, topic, event dates, and application process. The focus would remain discovery and qualification; the team would prepare and submit its own applications.'), ('Technology and first version', 'I would use Python with Scrapy for collection, Playwright where rendering is needed, and official APIs or feeds where available. I would use the Claude API to extract details and explain relevance, with PostgreSQL for records and duplicate detection. I would build a Next.js dashboard and scheduled email digest. My first version would cover a small verified mix of Nigerian and international tender and conference sources, testing accuracy with the team before expanding.'), ('Limitations and safeguards', 'I would respect access rules, verify deadlines against original notices, flag uncertain information, and protect team data. I would avoid invented opportunities, automatic applications, and promises of winning. Coverage would depend on accessible sources.')], 300), ('PART 3', 'Analytics and improvement', 'Understanding behaviour and improving enquiries', [('What I would track', 'I would embed Google Analytics 4 through Google Tag Manager to track visitor behaviour: traffic sources, landing pages, devices, engagement, CTA clicks, form starts, and confirmed enquiries. I would measure qualified leads, not just visits, and exclude personal information from analytics.'), ('How I would use the data', 'I would validate events with Tag Manager Preview and GA4 DebugView, compare leads with enquiry records, and use channel and device reports to identify drop-offs. I would use PageSpeed Insights for loading issues and Search Console for search visibility.'), ('SEO foundations', 'I would use robots.txt to guide crawling and reference the sitemap; it does not guarantee rankings. I would check titles, descriptions, canonical URLs, and indexing. On Netlify, I would configure redirects through netlify.toml or _redirects; .htaccess applies to Apache hosting.'), ('Scenario: 5,000 visitors, five enquiries', 'I would calculate a 0.1% conversion rate, assuming five unique enquirers. First, I would check tracking accuracy and test that forms deliver messages. I would investigate traffic quality, mobile usability, slow pages, unclear offers, weak trust signals, hidden CTAs, and unnecessary form fields.'), ('What I would do next', 'I would fix technical issues first, then address the largest drop-off with clearer messaging, stronger proof, better CTA placement, or a shorter form. I would compare qualified enquiries and conversion rates over comparable periods, avoiding conclusions from small fluctuations.')], 250)]
output=Path('output/pdf/Crystal-Kizor-Refined-Submission.pdf')
c=canvas.Canvas(str(output),pagesize=(595.28,841.89));c.setTitle('Crystal Kizor | Landing Page, AI Product & Analytics');c.setAuthor('')
body=ParagraphStyle('body',fontName='Helvetica',fontSize=10.5,leading=15.5,textColor=HexColor('#353a35'))
heading=ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=10.5,leading=14,textColor=HexColor('#202720'))
for i,(part,title,subtitle,sections,limit) in enumerate(pages):
 count=len((' '.join(h+' '+t for h,t in sections)).split());print(part,count,'words');assert count<=limit
 c.setFillColor(HexColor('#fcfcf8'));c.rect(0,0,595.28,841.89,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#d6dacd'));c.setLineWidth(.7);c.lines([(30,787,30,813),(30,813,100,813),(565,28,495,28),(565,28,565,55)])
 c.setFillColor(HexColor('#626c58'));c.setFont('Helvetica-Bold',9);c.drawString(48,779,'CRYSTAL KIZOR / '+part)
 c.setFillColor(HexColor('#172017'));c.setFont('Helvetica-Bold',25);c.drawString(48,610 if i==0 else 740,title)
 c.setFont('Helvetica',10);c.setFillColor(HexColor('#646b60'));c.drawString(48,587 if i==0 else 717,subtitle)
 c.setStrokeColor(HexColor('#ff572c'));c.setLineWidth(2);c.line(48,568 if i==0 else 696,98,568 if i==0 else 696)
 y=673
 if i==0:
  c.setFillColor(HexColor('#eef1e7'));c.roundRect(48,646,499,110,10,fill=1,stroke=0)
  for label,url,yy in [('LIVE WEBSITE','https://crystalkizo.netlify.app/',731),('SOURCE CODE / GITHUB','https://github.com/cercuit-ola/CRYSTAL-KIZOR.',681)]:
   c.setFillColor(HexColor('#626c58'));c.setFont('Helvetica-Bold',8);c.drawString(63,yy,label)
   c.setFillColor(HexColor('#172017'));c.setFont('Helvetica',10);c.drawString(63,yy-16,url);c.linkURL(url,(63,yy-20,532,yy-4),relative=0)
  y=547
 for h,t in sections:
  p=Paragraph(h,heading);w,ht=p.wrap(499,800);p.drawOn(c,48,y-ht);y-=ht+6
  p=Paragraph(t,body);w,ht=p.wrap(499,800);p.drawOn(c,48,y-ht);y-=ht+17
 assert y>65,(part,y)
 c.setStrokeColor(HexColor('#d6dacd'));c.setLineWidth(.5);c.line(48,59,547,59)
 c.setFillColor(HexColor('#6c7267'));c.setFont('Helvetica',8);c.drawString(48,42,'DESIGN / AI PRODUCT THINKING / ANALYTICS');c.drawRightString(547,42,f'{i+1} / 3');c.showPage()
c.save()
d=fitz.open(output);assert len(d)==3
assert len(d[0].get_links())==2
for i,p in enumerate(d):
 p.get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(f'tmp/pdfs/refined-{i+1}.png')
 assert len(p.get_text())>900
print(output.resolve())
