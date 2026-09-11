import { Scene } from "@/components/Scene";
import { ART } from "@/lib/art";

export default function NotFound() {
  return (
    <main>
      <Scene src={ART.prune} kicker="404" title="This neuron is not in the vault yet.">
        <p className="lede">Pruned notes stay queryable after restore. New knowledge arrives through frontier-kb.</p>
      </Scene>
    </main>
  );
}
