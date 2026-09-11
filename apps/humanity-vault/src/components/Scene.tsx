import { asset } from "@/lib/art";

export function Scene({
  src,
  kicker,
  title,
  children,
}: {
  src: string;
  kicker: string;
  title: string;
  children?: React.ReactNode;
}) {
  return (
    <header className="scene">
      <img src={asset(src)} alt="" />
      <div className="scene-copy">
        <p className="kicker">{kicker}</p>
        <h2 className="claim">{title}</h2>
        {children}
      </div>
    </header>
  );
}
