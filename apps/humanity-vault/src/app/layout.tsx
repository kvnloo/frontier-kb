import { Cormorant_Garamond, Manrope } from "next/font/google";
import type { Metadata, Viewport } from "next";
import { Shell } from "@/components/Shell";
import "./globals.css";

const serif = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["500", "600"],
  variable: "--font-serif",
  display: "swap",
});

const sans = Manrope({
  subsets: ["latin"],
  weight: ["400", "600"],
  variable: "--font-sans",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Humanity's Vault",
  description: "Open learning OS for frontier LLM knowledge. Encode, retrieve, rest, measure, prune.",
  manifest: "/manifest.webmanifest",
  icons: {
    icon: [{ url: "/art/icon-192.png", sizes: "192x192", type: "image/png" }],
    apple: "/art/icon-192.png",
  },
};

export const viewport: Viewport = {
  themeColor: "#050508",
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  viewportFit: "cover",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${serif.variable} ${sans.variable}`}>
      <body>
        <Shell>{children}</Shell>
      </body>
    </html>
  );
}
