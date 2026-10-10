from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
import fitz
pages=[('PART 1','One brand. Connected work.','Landing page submission',[
('My thinking and key decisions',"I designed the page around Crystal as the person connecting architecture, design, education, ideas, and community. I introduced her first, then used a linked bento overview to help visitors understand the ecosystem before exploring individual initiatives."),
('Hierarchy and visitor journeys',"I gave Studio COKA and ELEvated space to demonstrate their work visually, grouped the community initiatives together, and brought education, writing, and speaking into a shared ideas section. I used About, Work, Brands, and Contact navigation to keep the page easy to explore. I directed prospective clients toward relevant work, learners toward TEA, and collaborators toward enquiry actions."),
('Visual system and technology',"I used consistent typography, spacing, card treatments, and an orange, charcoal, and neutral palette. Portraits keep the personal brand visible; subtle architectural pencil animations add character. I retained clear labels for temporary imagery and adapted the layout for mobile."),
('Implementation',"I built the page with Next.js, React, CSS, and lightweight JavaScript, using static export for Netlify. I used local WebP imagery, lazy loading, semantic sections, keyboard-accessible controls, and reduced-motion support. I checked the production build, image assets, and internal links.")],200),
('PART 2','Studio COKA Tender Scout','AI opportunity discovery and proposal drafting',[
('What I would build and why',"I would build Studio COKA Tender Scout, an AI web crawler and proposal assistant for Crystal and her business development team. It would find architecture, interior design, and construction bidding opportunities in Nigeria and internationally, reducing manual searching and helping the studio avoid missed deadlines."),
('How Crystal would use it',"I would let Crystal set preferred countries, services, project sizes, and eligibility criteria. Every 12 hours, the system would check approved procurement portals, government notices, development organisations, and corporate tender pages, then email her a ranked digest of new or updated opportunities. Each result would include scope, location, deadline, eligibility, required documents, and the original source."),
('Proposal support',"From the digest, Crystal could open a dashboard, shortlist a tender, and request a proposal draft. I would combine the tender requirements with approved Studio COKA credentials and project information to generate an outline, relevant experience section, methodology, and submission checklist. Missing facts, fees, and commitments would be flagged for her input."),
('Technology and first working version',"I would use Python with Scrapy, adding Playwright where JavaScript rendering is necessary, and prefer official feeds or APIs when available. I would use the Claude API to interpret tender documents and draft proposals, with PostgreSQL for records and duplicate detection. I would build a Next.js dashboard, a scheduled job running every 12 hours, and email delivery through Resend. My first version would cover five verified Nigerian and international sources, then expand after testing relevance and extraction accuracy."),
('Limitations and safeguards',"I would respect access restrictions, verify deadlines against source notices, and flag uncertain eligibility. I would protect confidential documents and prevent fabricated qualifications. Crystal would review every proposal; the tool would never submit bids automatically. Coverage would depend on accessible sources.")],300),
('PART 3','Turning visits into enquiries','Website analytics and continuous improvement',[
('What I would track',"I would measure qualified enquiries alongside traffic sources, landing pages, device types, engagement, CTA clicks, form starts, and successful submissions. I would use Google Analytics 4 with Google Tag Manager to track these actions and mark confirmed enquiries as key events, rather than counting button clicks as leads."),
('Tools and how I would use the data',"I would validate events through Tag Manager Preview and GA4 DebugView, compare submissions with actual enquiry records, and keep names, emails, and message contents out of analytics. I would segment the visitor journey by channel and device to identify weak pages and drop-offs. I would also use PageSpeed Insights to investigate loading issues."),
('Scenario: 5,000 visitors, five enquiries',"I would calculate a 0.1% visitor-to-enquiry conversion rate, assuming five unique enquirers. Before redesigning anything, I would verify tracking, check for irrelevant or bot traffic, and test that the form works and delivers messages."),
('What I would do next',"I would investigate whether visitors match the intended audience, understand the offer, see the CTA, and trust the business. I would compare form views, starts, and completions, then check mobile usability, slow pages, errors, and unnecessary fields."),
('Measuring improvement',"I would fix technical problems first, then improve the largest drop-off through clearer copy, stronger proof, better CTA placement, or a shorter form. I would compare conversion rates and qualified enquiries over comparable periods. With only five enquiries, I would avoid claiming success from small fluctuations.")],250)]
output=Path('output/pdf/Crystal-Kizor-Final-Answers.pdf')
c=canvas.Canvas(str(output),pagesize=(595.28,841.89));c.setTitle('Crystal Kizor | Landing Page, AI Product & Analytics');c.setAuthor('')
body=ParagraphStyle('body',fontName='Helvetica',fontSize=10.5,leading=15.5,textColor=HexColor('#353a35'))
heading=ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=10.5,leading=14,textColor=HexColor('#202720'))
for i,(part,title,subtitle,sections,limit) in enumerate(pages):
 count=len((' '.join(h+' '+t for h,t in sections)).split());print(part,count,'words');assert count<=limit
 c.setFillColor(HexColor('#fcfcf8'));c.rect(0,0,595.28,841.89,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#d6dacd'));c.setLineWidth(.7);c.lines([(30,787,30,813),(30,813,100,813),(565,28,495,28),(565,28,565,55)])
 c.setFillColor(HexColor('#626c58'));c.setFont('Helvetica-Bold',9);c.drawString(48,779,'CRYSTAL KIZOR / '+part)
 c.setFillColor(HexColor('#172017'));c.setFont('Helvetica-Bold',25);c.drawString(48,740,title)
 c.setFont('Helvetica',10);c.setFillColor(HexColor('#646b60'));c.drawString(48,717,subtitle)
 c.setStrokeColor(HexColor('#ff572c'));c.setLineWidth(2);c.line(48,696,98,696)
 y=673
 if i==0:
  c.setFillColor(HexColor('#eef1e7'));c.roundRect(48,581,499,90,10,fill=1,stroke=0)
  for label,url,yy in [('LIVE WEBSITE','https://crystalkizo.netlify.app/',648),('SOURCE CODE / GITHUB','https://github.com/cercuit-ola/CRYSTAL-KIZOR.',608)]:
   c.setFillColor(HexColor('#626c58'));c.setFont('Helvetica-Bold',8);c.drawString(63,yy,label)
   c.setFillColor(HexColor('#172017'));c.setFont('Helvetica',10);c.drawString(63,yy-16,url);c.linkURL(url,(63,yy-20,532,yy-4),relative=0)
  y=557
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
 p.get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(f'tmp/pdfs/final-{i+1}.png')
 assert len(p.get_text())>900
print(output.resolve())
