import { BrainMap } from "@/components/BrainMap";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART, asset } from "@/lib/art";
import type { Note, Synapse } from "@/lib/cycle";

export default async function BrainPage() {
  const data = await gql<{
    brain: {
      neurons: number;
      synapses: number;
      meanWeight: number;
      pruneCandidates: number;
      nodes: Note[];
      edges: Synapse[];
    };
  }>(`query { brain { neurons synapses meanWeight pruneCandidates nodes { id title type weight } edges { src dst rel weight fires } } }`);
  return (
    <main>
      <Scene src={ART.synapses} kicker="Living graph" title="What fires together, wires.">
        <p className="lede">Gold is potentiation. Rose is dying. Nightly loop downscales idle weight.</p>
      </Scene>
      <div className="well">
        <div className="instrument">
          <div>
            <b>{data.brain.neurons}</b>
            neurons
          </div>
          <div>
            <b>{data.brain.synapses}</b>
            synapses
          </div>
          <div>
            <b>{data.brain.pruneCandidates}</b>
            pruned
          </div>
        </div>
      </div>
      <div className="brain" style={{ ["--syn" as string]: `url(${asset(ART.synapses)})` }}>
        <BrainMap nodes={data.brain.nodes} edges={data.brain.edges} />
      </div>
    </main>
  );
}
