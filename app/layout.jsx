import './globals.css';
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || process.env.URL;
export const metadata = {
  ...(siteUrl ? { metadataBase: new URL(siteUrl), alternates: { canonical: '/' } } : {}),
  title: 'Crystal Kizor | Architecture · Design · Ideas · Impact',
  description: 'Crystal Kizor — architect, designer, entrepreneur, researcher, and speaker. Architecture · Design · Ideas · Impact.',
  icons: { icon: '/favicon.svg' },
  openGraph: { type: 'website', siteName: 'Crystal Kizor', title: 'Crystal Kizor | Architecture & Design', description: 'Selected projects, design education, speaking and community initiatives.', ...(siteUrl ? { url: siteUrl, images: [{ url: '/assets/social-card.jpg', width: 1200, height: 630, alt: 'Crystal Kizor — Architecture, interiors and design' }] } : {}) },
  twitter: { card: 'summary_large_image', title: 'Crystal Kizor | Architecture & Design', ...(siteUrl ? { images: ['/assets/social-card.jpg'] } : {}) },
  ...(process.env.GOOGLE_SITE_VERIFICATION ? { verification: { google: process.env.GOOGLE_SITE_VERIFICATION } } : {})
};
export const viewport = { themeColor: '#ff572c' };
export default function RootLayout({ children }) { return <html lang="en"><body>{children}</body></html>; }
