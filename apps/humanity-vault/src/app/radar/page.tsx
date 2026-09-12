import { Scene } from "@/components/Scene";
import { NoteStack } from "@/components/NoteStack";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function RadarPage() {
  const data = await gql<{ cluster: { notes: Note[] } }>(
    `query { cluster(id: HARNESS_RADAR) { notes { id title distilled type weight } } }`,
  );
  return (
    <main>
      <Scene src={ART.radar} kicker="SoL-Pi · host ports, not origin cores" title="Load the extension. Do not patch the host.">
        <p className="lede">
          Pi is the first-party host. OMP loads via the legacy shim. Hermes is a Python plugin port. ObservationPack is a
          projection.
        </p>
      </Scene>
      <div className="well">
        <NoteStack notes={data.cluster.notes} />
      </div>
    </main>
  );
}
