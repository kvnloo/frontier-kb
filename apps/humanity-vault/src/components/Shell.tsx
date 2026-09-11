"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ART, asset } from "@/lib/art";

const LINKS = [
  { href: "/", label: "Cycle", icon: ART.nav.cycle },
  { href: "/encode", label: "Encode", icon: ART.nav.encode },
  { href: "/retrieve", label: "Retrieve", icon: ART.nav.retrieve },
  { href: "/brain", label: "Brain", icon: ART.nav.brain },
  { href: "/measure", label: "Measure", icon: ART.nav.measure },
] as const;

export function Shell({ children }: { children: React.ReactNode }) {
  const path = usePathname();
  const home = path === "/" || path === "";
  return (
    <div className={`shell${home ? " shell-home" : ""}`}>
      <div className="grain" style={{ backgroundImage: `url(${asset(ART.grain)})` }} aria-hidden="true" />
      <header className="brand">
        <Link href="/" className="mark">
          <img src={asset(ART.icon)} alt="" width={30} height={30} />
          <span>Humanity&rsquo;s Vault</span>
        </Link>
        <small>open brain</small>
      </header>
      {children}
      <nav className="nav" aria-label="Learning cycle">
        {LINKS.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            aria-current={path === link.href || (link.href !== "/" && path.startsWith(link.href)) ? "page" : undefined}
          >
            <img src={asset(link.icon)} alt="" width={28} height={28} />
            {link.label}
          </Link>
        ))}
      </nav>
    </div>
  );
}
