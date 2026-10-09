Crystal Kizor — portfolio refinement (9 October 2026)

Open index.html or serve this folder with python3 -m http.server 4173.

Changes
- Preserved headline and visual system; primary CTA is View selected projects.
- Three permanent project profiles with location, type, scope, challenge, approach and role disclosure. Sources linked directly from each profile.
- Copy outside project profiles reduced from 915 to 775 words (15.3%). Total page copy grows to accommodate substantive project information.
- Project WebP images total 734,536 bytes versus 1,483,391 bytes for originals (50% reduction). Originals retained for full-image links.
- Project images retain their full aspect ratio; mobile founder portraits use contain. Carousel controls have 44px minimum tap targets. Founder slideshow starts paused. Existing mobile navigation, keyboard controls and reduced-motion behavior retained.
- Descriptive title and description, Open Graph/Twitter tags, 1200x630 social card, existing SVG favicon, image alt text and robots.txt.

Required before launch
No confirmed public URL/custom domain or Search Console token was supplied. Do not assume the studio domain is the personal portfolio domain.
Run: python3 scripts/configure_site.py --url https://YOUR-CONFIRMED-DOMAIN --google-token YOUR-HTML-VERIFICATION-TOKEN
Use only the content value from Google's HTML verification tag. The token is optional.
This generates sitemap.xml, updates robots.txt, and adds canonical, og:url and absolute social-image URLs. It adds the verification tag when provided. Deploy the files to the confirmed host, finish Verify in Search Console, and submit sitemap.xml. DNS/domain connection and Search Console verification have not been performed.

Editorial items still needed
Approved completed-project photos and individual project responsibilities for Crystal. Existing project imagery is labelled as studio portfolio imagery, not completed photography. Studio Design Director is verified, but project-specific responsibilities are not. ELEvated furniture remains a labelled stock reference.

Checks performed
JavaScript syntax; all local assets exist; all nonempty internal anchors resolve; IDs unique; all images have alt attributes; configuration generator tested in an isolated temporary fixture.

Verification limits
No browser was available through the connected browser tools. Preview binding was denied by the sandbox. Actual mobile navigation, wrapping, cropping, swipe interactions, tap targets and throttled-network loading remain unverified in-browser. Check 320/375/390/768px widths, keyboard/Escape navigation, both remaining carousels, full-image links, reduced motion, and a cold-cache mobile connection before launch. No deployment or Lighthouse score claimed.

Brand gallery update
- Studio COKA, ELEvated and AKO Alliance have individual introductory text and freely flowing image galleries (4 / 3 / 3 images).
- Brand navigation jumps to each introduction. Images preserve their proportions and open larger in a new tab. Source links accompany every image.
- Studio COKA briefs remain beneath the gallery as native expandable details, available without JavaScript.
- Studio imagery comes from studiocoka.com. The new Garden Home view is https://studiocoka.com/projects/2/2.jpeg.
- ELEvated references: Pexels photos 7193628, 7188522, 15392676.
- AKO education references: Pexels photos 14554004, 28593054, 34162714.
- Stock photographs are clearly labelled as references, not the brands’ work or programme participants. Exact source-page URLs are linked in the visible captions.
- Downloaded images are stored locally; WebP versions are used on the page, with lazy loading and explicit intrinsic dimensions.
- Verified HTML nesting, unique IDs, internal anchor destinations, local image readability, dimensions and alt attributes, gallery counts and JavaScript syntax. Browser/mobile visual verification remains outstanding.
