const data={coka:['01 / SPACES','Studio COKA','Architecture, interior design, and construction focused on thoughtful, climate-responsive design. A practice concerned with the relationship between spaces, people, and the environments they inhabit.','Architecture or design'],elevated:['02 / OBJECTS','ELEvated','Contemporary furniture and product design rooted in African context, materials, and ideas. Functional, well-designed objects that bring intention to everyday living.','Furniture or product design'],tea:['03 / IDEAS','The Effective Architect','An architecture education and media platform helping architects and built-environment professionals learn, grow, and build better careers.','Education and media'],speaking:['03 / IDEAS','Bring a new perspective.','Talks and conversations around architecture, climate-responsive design, African cities, design, entrepreneurship, and the built environment.','Speaking invitation'],writing:['03 / IDEAS','A curious mind, at work.','Personal research, authorship, writing, and content: a home for the ideas Crystal develops across architecture, design, and the way we live.','Research or writing'],ako:['04 / PEOPLE','AKO Alliance','An initiative focused on expanding access to education and creating opportunities for children and young people.','AKO Alliance'],alive:['04 / PURPOSE','Alive and Free','A Christian youth movement helping young people walk in truth, healing, freedom, identity, purpose, and life in Christ.','Alive and Free']};const dialog=document.querySelector('dialog'),title=document.querySelector('#modal-title'),body=document.querySelector('#modal-body'),label=document.querySelector('#modal-label');function show(){if(!dialog.open)dialog.showModal()}const inquiryDrafts=new Map();
function enquiry(topic){
  label.textContent='CONTACT CRYSTAL';
  title.textContent=topic;
  body.innerHTML='<form id="inquiry-form"><p id="inquiry-help"></p><label for="message">Your message</label><textarea id="message" name="message" rows="6" maxlength="4000" required placeholder="Tell Crystal about your project, question or invitation…" aria-describedby="inquiry-help inquiry-status"></textarea><p id="inquiry-status" role="status"></p><button type="submit" class="pill" id="send-enquiry">Send inquiry</button><div id="inquiry-fallback"></div></form>';
  const field=document.querySelector('#message');
  const status=document.querySelector('#inquiry-status');
  const email=window.CRYSTAL_CONTACT_EMAIL;
  document.querySelector('#inquiry-help').textContent=email?'Send inquiry opens your email app with your message ready to review and send.':'Write your inquiry below. While Crystal’s direct inbox is being confirmed, you can copy your message and contact her on LinkedIn.';
  field.value=inquiryDrafts.get(topic)||'';
  field.addEventListener('input',()=>inquiryDrafts.set(topic,field.value));
  document.querySelector('#inquiry-form').addEventListener('submit',event=>{
    event.preventDefault();
    const message=field.value.trim();
    if(!message){status.textContent='Please enter your message.';field.focus();return;}
    if(email){
      window.location.href='mailto:'+encodeURIComponent(email)+'?subject='+encodeURIComponent('Crystal Kizor — '+topic)+'&body='+encodeURIComponent(message);
      status.textContent='Your email draft is ready to open. Send it from your email app.';
      return;
    }
    status.textContent='Your message has not been sent. Copy it below, then send it to Crystal on LinkedIn.';
    const fallback=document.querySelector('#inquiry-fallback');fallback.replaceChildren();
    const copy=document.createElement('button');copy.type='button';copy.className='inquiry-copy';copy.textContent='Copy message';
    copy.onclick=async()=>{try{await navigator.clipboard.writeText(topic+'\n\n'+message);status.textContent='Message copied. Paste it into your LinkedIn conversation with Crystal.';}catch{field.focus();field.select();status.textContent='Select and copy your message, then paste it into LinkedIn.';}};
    const link=document.createElement('a');link.href='https://ng.linkedin.com/in/crystal-kizor';link.target='_blank';link.rel='noopener';link.textContent='Contact Crystal on LinkedIn';
    fallback.append(copy,link);
  });
  show();field.focus();
}
document.querySelectorAll('[data-detail]').forEach(b=>b.onclick=()=>{const key=b.dataset.detail;if(key==='credits'){label.textContent='CONCEPT NOTES';title.textContent='The visual world.';body.innerHTML='<p>This is a design concept. Stock models are not Crystal Kizor or affiliated team members. Interiors and furniture are visual references, not claimed brand projects.</p><p>Portrait: <a href="https://www.pexels.com/photo/joyful-black-woman-in-vibrant-orange-dress-28462500/" target="_blank" rel="noopener">Jamaal Hutchinson / Pexels</a>.</p><p>Studio editorial: <a href="https://www.pexels.com/photo/a-two-women-posing-together-8945201/" target="_blank" rel="noopener">MART PRODUCTION / Pexels</a>.</p><p>Architecture and chair: Unsplash reference photography. Replace with approved portfolio assets before a public brand launch.</p>';show();return}const d=data[key];label.textContent=d[0];title.textContent=d[1];body.replaceChildren();const p=document.createElement('p');p.textContent=d[2];const action=document.createElement('button');action.className='pill';action.textContent='Start a conversation ↗';action.onclick=()=>enquiry(d[3]);body.append(p,action);show()});document.querySelectorAll('[data-enquiry]').forEach(b=>b.onclick=()=>enquiry(b.dataset.enquiry));document.querySelector('.close').onclick=()=>dialog.close();dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});const menu=document.querySelector('.menu'),nav=document.querySelector('#main-navigation');menu.onclick=()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',open);menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');menu.textContent=open?'×':'☰'};nav.querySelectorAll('a').forEach(a=>a.onclick=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');menu.textContent='☰'});if('IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target)}}),{threshold:.08});document.querySelectorAll('.intro,.objects-row,.people-copy,.ideas-bottom').forEach(el=>{el.classList.add('reveal');observer.observe(el)})}addEventListener('scroll',()=>{const length=document.documentElement.scrollHeight-innerHeight;document.querySelector('.progress').style.width=(length?scrollY/length*100:0)+'%'},{passive:true});

const reduced=matchMedia('(prefers-reduced-motion: reduce)');

// Hero slideshow: 2.5-second cadence with explicit pause and reduced-motion support.
const founder=document.querySelector('.founder-carousel'),founderSlides=[...document.querySelectorAll('.founder-slide')],playButton=document.querySelector('.founder-play');
let founderIndex=0,founderTimer=null,founderUserPaused=reduced.matches;
const founderDelay=2500;
function showFounder(index){
 founderIndex=(index+founderSlides.length)%founderSlides.length;
 founderSlides.forEach((slide,i)=>{slide.classList.toggle('active',i===founderIndex);slide.setAttribute('aria-hidden',String(i!==founderIndex));});
 document.querySelector('.founder-count').textContent=String(founderIndex+1).padStart(2,'0')+' / 05';
}
function syncFounderButton(){playButton.textContent=founderUserPaused?'Play':'Pause';playButton.setAttribute('aria-pressed',String(!founderUserPaused));playButton.setAttribute('aria-label',founderUserPaused?'Play founder slideshow':'Pause founder slideshow');}
function stopFounder(){clearInterval(founderTimer);founderTimer=null;}
function startFounder(){stopFounder();if(founderUserPaused||document.hidden)return;founderTimer=setInterval(()=>showFounder(founderIndex+1),founderDelay);}
function manualFounder(direction){showFounder(founderIndex+direction);startFounder();}
document.querySelector('.founder-prev').onclick=()=>manualFounder(-1);
document.querySelector('.founder-next').onclick=()=>manualFounder(1);
playButton.onclick=()=>{founderUserPaused=!founderUserPaused;syncFounderButton();startFounder();};
founder.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();manualFounder(e.key==='ArrowRight'?1:-1);}});
let founderTouch=null;
founder.addEventListener('touchstart',e=>{stopFounder();founderTouch={x:e.changedTouches[0].clientX,y:e.changedTouches[0].clientY};},{passive:true});
founder.addEventListener('touchend',e=>{if(founderTouch){const dx=e.changedTouches[0].clientX-founderTouch.x,dy=e.changedTouches[0].clientY-founderTouch.y;if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy))showFounder(founderIndex+(dx<0?1:-1));}founderTouch=null;startFounder();},{passive:true});
founder.addEventListener('touchcancel',()=>{founderTouch=null;startFounder();},{passive:true});
founder.addEventListener('pointerenter',stopFounder);
founder.addEventListener('pointerleave',()=>{if(!founder.contains(document.activeElement))startFounder();});
founder.addEventListener('focusin',stopFounder);
founder.addEventListener('focusout',()=>{setTimeout(()=>{if(!founder.contains(document.activeElement))startFounder();},0);});
document.addEventListener('visibilitychange',()=>{if(document.hidden)stopFounder();else startFounder();});
reduced.addEventListener('change',()=>{founderUserPaused=reduced.matches;syncFounderButton();startFounder();});
syncFounderButton();startFounder();
const brandLinks={coka:['Explore Studio COKA','https://studiocoka.com/'],tea:['Explore the newsletter','https://lnkd.in/emqe3r9U'],speaking:['TEDxPortHarcourt speaker profile','https://www.tedxportharcourt.com/speakers/a01411ad-22eb-4e92-9f94-6867a1f1446b'],writing:['Read Crystal’s public writing','https://ng.linkedin.com/in/crystal-kizor'],ako:['View Crystal’s initiative profile','https://ng.linkedin.com/in/crystal-kizor'],alive:['View Crystal’s initiative profile','https://ng.linkedin.com/in/crystal-kizor']};
document.querySelectorAll('[data-detail]').forEach(button=>{if(button.dataset.detail==='credits')return;button.addEventListener('click',()=>{const key=button.dataset.detail,link=brandLinks[key];if(link){const a=document.createElement('a');a.href=link[1];a.target='_blank';a.rel='noopener';a.className='line-link';a.style.cssText='display:block;margin:20px 0;text-decoration:underline;font-size:14px';a.textContent=link[0];body.append(a)}if(['elevated','ako','alive'].includes(key)){const p=document.createElement('p');p.style.cssText='font-size:12px;margin-top:20px';p.textContent=key==='elevated'?'Official collection imagery and shop link are awaiting confirmation.':'Dedicated participation and support links are awaiting confirmation.';body.append(p)}})});
document.querySelector('[data-detail="credits"]').onclick=()=>{label.textContent='IMAGES & SOURCES';title.textContent='The visual world.';body.innerHTML='<p>Supplied founder portraits. Studio COKA project imagery and practice information: <a href="https://studiocoka.com/" target="_blank" rel="noopener">Studio COKA</a>. Speaking: <a href="https://www.tedxportharcourt.com/speakers/a01411ad-22eb-4e92-9f94-6867a1f1446b" target="_blank" rel="noopener">TEDxPortHarcourt</a>. Initiative roles and writing: <a href="https://ng.linkedin.com/in/crystal-kizor" target="_blank" rel="noopener">Crystal’s LinkedIn</a>.</p><p>Furniture and education gallery photographs are Pexels references, not ELEvated products or AKO Alliance programme documentation. Each gallery image links to its source. Supplied portraits do not establish event participation or project authorship. Positioning copy is proposed brand language. Contact links lead to Studio COKA or Crystal’s LinkedIn profile.</p>';show()};

// Keep navigation state consistent across keyboard, pointer and screen sizes.
function closeNavigation(returnFocus=false){
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded','false');
  menu.setAttribute('aria-label','Open navigation');
  menu.textContent='☰';
  if(returnFocus)menu.focus();
}
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'&&nav.classList.contains('open'))closeNavigation(true);
});
document.addEventListener('click',event=>{
  if(!event.target.closest('header'))closeNavigation();
});
matchMedia('(max-width:1100px)').addEventListener('change',()=>closeNavigation());
nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{
  if(getComputedStyle(menu).display==='none')return;
  const destination=document.querySelector(link.getAttribute('href'));
  if(destination){destination.setAttribute('tabindex','-1');destination.focus({preventScroll:true});}
}));
const navigationLinks=[...nav.querySelectorAll('a[href^="#"]')];
const navigationSections=navigationLinks.map(link=>document.querySelector(link.getAttribute('href')));
let navigationFrame=false;
function updateCurrentSection(){
  navigationFrame=false;
  let current=-1;
  navigationSections.forEach((section,index)=>{if(section.getBoundingClientRect().top<=150)current=index;});
  if(innerHeight+scrollY>=document.documentElement.scrollHeight-8)current=navigationSections.length-1;
  navigationLinks.forEach((link,index)=>{if(index===current)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});
}
addEventListener('scroll',()=>{if(!navigationFrame){navigationFrame=true;requestAnimationFrame(updateCurrentSection);}},{passive:true});
addEventListener('resize',updateCurrentSection);
updateCurrentSection();

// Education gallery: two native swipe slides with keyboard and button controls.
const educationTrack=document.querySelector('.education-track');
const educationPrev=document.querySelector('.education-prev');
const educationNext=document.querySelector('.education-next');
function updateEducation(){
  const index=Math.round(educationTrack.scrollLeft/educationTrack.clientWidth);
  educationPrev.disabled=index===0;
  educationNext.disabled=index===1;
  document.querySelector('.education-count').textContent=String(index+1).padStart(2,'0')+' / 02';
}
function moveEducation(direction){educationTrack.scrollBy({left:direction*educationTrack.clientWidth,behavior:reduced.matches?'instant':'smooth'});}
educationPrev.addEventListener('click',()=>moveEducation(-1));
educationNext.addEventListener('click',()=>moveEducation(1));
educationTrack.addEventListener('scroll',updateEducation,{passive:true});
educationTrack.addEventListener('keydown',event=>{
  if(event.key==='ArrowLeft'||event.key==='ArrowRight'){
    event.preventDefault();moveEducation(event.key==='ArrowRight'?1:-1);
  }
});
addEventListener('resize',updateEducation);
updateEducation();
