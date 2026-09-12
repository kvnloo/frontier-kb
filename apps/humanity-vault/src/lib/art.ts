export function asset(path: string): string {
  const base = process.env.NEXT_PUBLIC_BASE_PATH || "";
  return `${base}${path.startsWith("/") ? path : `/${path}`}`;
}

export const ART = {
  heroPortrait: "/art/hero-portrait.webp",
  heroWide: "/art/hero-wide.webp",
  encode: "/art/encode.webp",
  retrieve: "/art/retrieve.webp",
  measure: "/art/measure.webp",
  rest: "/art/rest.webp",
  prune: "/art/prune.webp",
  synapses: "/art/synapses.webp",
  llms: "/art/llms.webp",
  aodl: "/art/aodl.webp",
  radar: "/art/radar.webp",
  grain: "/art/grain.webp",
  icon: "/art/icon-192.png",
  nav: {
    cycle: "/art/nav-cycle.webp",
    encode: "/art/nav-encode.webp",
    retrieve: "/art/nav-retrieve.webp",
    brain: "/art/nav-brain.webp",
    measure: "/art/nav-measure.webp",
  },
} as const;

export function noteArt(type: string): string {
  if (type === "literature") return ART.measure;
  if (type === "permanent") return ART.encode;
  if (type === "harness") return ART.radar;
  if (type === "inbox") return ART.aodl;
  return ART.retrieve;
}
