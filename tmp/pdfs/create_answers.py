from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
import fitz
pages=[('TASK 2','Crystal AI Brand Manager','Opportunity discovery and content creation for Studio COKA',[
('What I would build',"I would build Crystal AI Brand Manager for Studio COKA: an AI assistant that finds relevant architecture bidding opportunities and drafts content that showcases the practice. It would serve Crystal and her business development team, helping them reach prospective clients while reducing manual research and content work."),
('How it would work',"I would monitor publicly accessible Nigerian federal government procurement notices and tender pages from leading firms. The tool would identify architecture, interior design, and construction opportunities, then summarise scope, eligibility, deadlines, required documents, and source links. Crystal could filter a dashboard by service, location, and deadline, shortlist opportunities, and receive alerts."),
('Content creation',"Alongside tender discovery, I would generate two daily content drafts: conversational video scripts, carousels, or captions for LinkedIn and Instagram. I would ground these in approved projects and Crystal's insights, with publication subject to her approval."),
('Technology and first version',"I would use Python with Scrapy or Playwright to collect permitted public content, and the Claude API to extract tender details and draft posts. This separates reliable collection from AI interpretation. I would build a Next.js dashboard with a PostgreSQL database, scheduled checks, duplicate detection, and email alerts. My first version would cover five verified sources and one content approval queue, then expand after testing with Crystal."),
('Limitations and safeguards',"I would respect website access rules, avoid bypassing logins, and link every opportunity to its original notice. I would flag uncertain details and recheck deadlines. Crystal would verify eligibility before applying; the tool would never submit bids automatically. I would protect confidential information and prevent invented project claims or testimonials.")]),
('TASK 3','Measuring website performance','Google Analytics tracking and enquiry conversion',[
('What I would track',"I would judge performance by qualified enquiries and useful visitor actions, not traffic alone. Using Google Analytics 4 with Google Tag Manager, I would track traffic sources, landing pages, device types, engagement, CTA clicks, form starts, and confirmed successful submissions. I would mark enquiries as key events and compare their quality against actual enquiry records."),
('How I would use the data',"I would review the journey from landing page to enquiry, comparing channels and devices to identify where visitors drop off. I would validate tracking through Tag Manager Preview and GA4 DebugView, keep personal information out of analytics, and use the findings to prioritise clearer copy, better CTA placement, faster pages, and simpler forms."),
('Scenario: 5,000 visitors, five enquiries',"I would calculate a 0.1% visitor-to-enquiry conversion rate, assuming five unique enquirers. First, I would confirm tracking accuracy, exclude internal and obvious bot traffic, and test that enquiries actually reach the inbox."),
('What I would do next',"I would investigate traffic relevance, mobile usability, loading speed, CTA visibility, form errors, unnecessary fields, and whether the offer inspires trust. I would compare form views, starts, and completions to locate the biggest drop-off. I would fix technical issues first, then make targeted improvements and compare qualified enquiries over comparable periods. With only five conversions, I would avoid drawing conclusions from small fluctuations or running an A/B test without enough data.")])]
out=Path('output/pdf/Crystal-Kizor-Final-Answers.pdf')
c=canvas.Canvas(str(out),pagesize=(595.28,841.89));c.setTitle('Crystal Kizor | AI Tool Proposal and Website Performance');c.setAuthor('')
body=ParagraphStyle('body',fontName='Helvetica',fontSize=10.5,leading=16,textColor=HexColor('#353a35'))
heading=ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=10.5,leading=14,textColor=HexColor('#202720'))
for i,(task,title,subtitle,sections) in enumerate(pages):
 words=len((' '.join(h+' '+t for h,t in sections)+' '+title+' '+subtitle).split());assert words <= (300 if i==0 else 250),words;print(task,words,'words including headings')
 c.setFillColor(HexColor('#fcfcf8'));c.rect(0,0,595.28,841.89,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#d6dacd'));c.setLineWidth(.7);c.lines([(30,787,30,813),(30,813,100,813),(565,28,495,28),(565,28,565,55)])
 c.setFillColor(HexColor('#626c58'));c.setFont('Helvetica-Bold',9);c.drawString(48,779,'CRYSTAL KIZOR  /  '+task)
 c.setFillColor(HexColor('#172017'));c.setFont('Helvetica-Bold',25);c.drawString(48,740,title)
 c.setFont('Helvetica',10);c.setFillColor(HexColor('#646b60'));c.drawString(48,717,subtitle)
 c.setStrokeColor(HexColor('#ff572c'));c.setLineWidth(2);c.line(48,696,98,696)
 y=671
 for h,t in sections:
  p=Paragraph(h,heading);w,ht=p.wrap(499,800);p.drawOn(c,48,y-ht);y-=ht+6
  p=Paragraph(t,body);w,ht=p.wrap(499,800);p.drawOn(c,48,y-ht);y-=ht+19
 assert y>65,y
 c.setStrokeColor(HexColor('#d6dacd'));c.setLineWidth(.5);c.line(48,59,547,59)
 c.setFillColor(HexColor('#6c7267'));c.setFont('Helvetica',8);c.drawString(48,42,'AI TOOL PROPOSAL & WEBSITE PERFORMANCE');c.drawRightString(547,42,f'{i+1} / 2')
 c.showPage()
c.save()
d=fitz.open(out);assert len(d)==2
for i,p in enumerate(d):
 p.get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(f'tmp/pdfs/page-{i+1}.png')
 assert len(p.get_text())>1000
print(out.resolve())
