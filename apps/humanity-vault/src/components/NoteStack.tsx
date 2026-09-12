import Link from "next/link";
import type { Note } from "@/lib/cycle";

export function NoteStack({ notes }: { notes: Note[] }) {
  return (
    <div className="stack">
      {notes.map((n) => (
        <Link key={n.id} href={`/note/${n.id}`} className="card">
          <h3>{n.title}</h3>
          <p>{n.distilled}</p>
          <div className="meta">
            <span>{n.type}</span>
            <span>w {n.weight.toFixed(2)}</span>
          </div>
        </Link>
      ))}
    </div>
  );
}
