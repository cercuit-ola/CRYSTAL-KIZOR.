export const dynamic = 'force-static';
export default function sitemap() {
 const url = process.env.NEXT_PUBLIC_SITE_URL || process.env.URL;
 return url ? [{ url: `${url.replace(/\/$/, '')}/` }] : [];
}
