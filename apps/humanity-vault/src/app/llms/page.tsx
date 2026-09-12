import { Scene } from "@/components/Scene";
import { NoteStack } from "@/components/NoteStack";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function LlmsPage() {
  const data = await gql<{ llmFrontier: Note[] }>(
    `query { llmFrontier { id title distilled weight type } }`,
  );
  return (
    <main>
      <Scene src={ART.llms} kicker="LLM frontier · 2026 invariants" title="Learn the invariants. Model names are examples.">
        <p className="lede">
          Post-training in the harness. Tool shape. Specialist routing. Note-ledger vs conversation memory. Context triad.
        </p>
      </Scene>
      <div className="well">
        <NoteStack notes={data.llmFrontier} />
      </div>
    </main>
  );
}
