# Crystal Kizor — Next.js portfolio

## Local development
Use Node 22 (`nvm use` if available), then:

```sh
npm ci
npm run dev
```
Open http://localhost:3000.

## Deploy on Netlify
1. Push this folder to your Git repository and import that repository in Netlify.
2. The included `netlify.toml` sets build command `npm run build`, publish directory `out`, and Node 22.
3. Set `NEXT_PUBLIC_SITE_URL` to your public HTTPS Netlify URL or custom domain. Netlify's `URL` is used as a fallback. This enables canonical/social URLs and the sitemap.
4. Optionally set `NEXT_PUBLIC_CONTACT_EMAIL` to the approved recipient inbox and `GOOGLE_SITE_VERIFICATION` to the Google HTML-verification token.
5. Deploy. Changes to environment variables require a rebuild.

For manual deployment: run `npm run build`, then upload the contents of `out/` through Netlify's deploy interface. Set the site URL before building to include correct SEO URLs.

## Files to edit
- `app/page.jsx`: page content and sections, rendered with Next.js App Router.
- `app/globals.css`: responsive styles.
- `public/portfolio.js`: existing browser interactions, loaded after hydration through Next Script.
- `public/assets/`: local images.
- `app/layout.jsx`: metadata, favicon, root layout.
- `app/robots.js` and `app/sitemap.js`: static SEO files.

Original `index.html`, `style.css`, `script.js`, and `assets/` remain as the previous static version. They are not the Next.js source; changes there will not update the Next.js site. The old `scripts/configure_site.py` only configures that legacy version. Use environment variables for Next.js.

## Behavior and limits
Hero slideshow retains its 2.5-second cadence, mobile portrait-first order, pause and reduced-motion support. Education retains the two-photo slider. Contact cards retain topic-specific dialogs. With a contact email configured, Send inquiry opens an email draft; it does not deliver mail from a server. Without one, it offers the existing copy/LinkedIn fallback.

The site exports static files and needs no Netlify server runtime. `npm run preview` serves the production `out/` directory at http://127.0.0.1:4174. `npm start` is not used for static exports.

No Netlify account deployment or domain connection is performed by this conversion. Browser visual/interaction verification remains separate from production build checks.
