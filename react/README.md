# @frontendxlab/medicons

Optional local React package for the Hospital Clinical Icons SVG pack.

Includes 219 named icon components, 18 category entrypoints, per-icon entrypoints,
TypeScript source, ESM JavaScript and declaration files. React 18-19 is declared
as a peer dependency; React is not bundled. This package has not been published
to npm as part of generating this archive.

Install from the extracted folder:

```bash
npm install /absolute/path/to/hospital-icons/react
```

```tsx
import { CardiologyIcon } from "@frontendxlab/medicons/specialties/cardiology";

<CardiologyIcon size={48} variant="duotone" title="Cardiology" />
<CardiologyIcon size={48} animation="beam" duration={3} title="Cardiology" />
```

## Import tiers and bundle size

Three tiers, smallest first. Prefer the single-icon path for the smallest bundle.

```tsx
// Tier 1 - single icon (smallest, one module + shared core)
import { CardiologyIcon } from "@frontendxlab/medicons/specialties/cardiology";

// Tier 2 - category entrypoint (only that category's icons)
import { CardiologyIcon } from "@frontendxlab/medicons/specialties";

// Tier 3 - full root (relies on bundler tree-shaking; avoid `import *`)
import { CardiologyIcon } from "@frontendxlab/medicons";
```

Bundler guidance: named imports (`import { X }`) tree-shake cleanly from any
tier because the package sets `"sideEffects": false`, ships ESM only, keeps
`index.ts` as pure re-exports with no side effects, and category files
re-export directly from per-icon files (no barrel chains). The shared `core.ts`
holds only a module-level `css` string constant plus pure functions, so it is
side-effect free. Never use namespace imports (`import * from
"@frontendxlab/medicons"`); they defeat tree-shaking and pull in all 219 icons.

Measured with esbuild (bundle, minify, react external, one icon):

| Entry | Size | Gzip | Modules |
|---|---|---|---|
| Single icon `.../specialties/cardiology` | 3,176 B | 1,549 B | 3 |
| Category `@frontendxlab/medicons/specialties` | 3,176 B | 1,549 B | 3 |
| Root named `import { CardiologyIcon }` | 3,176 B | 1,557 B | 3 |
| Root namespace `import *` | 124,072 B | 23,771 B | 222 |

Named imports cost the same at every tier (39x smaller than namespace import).
Single-icon and category paths are immune to bundlers with weak tree-shaking;
use them when bundle size is critical.

Static variants: outline, solid, duotone. `filled` is an alias for solid.
Beam is available for the 60 icons marked `supportsBeam` in the parent manifest.
Components without a beam path remain static when beam is requested.

The components forward SVG props and refs. They use `useId` for solid-mask
isolation and include client-component directives. Raw SVGs in the parent
package are the alternative for pages requiring no component JavaScript.

TypeScript-to-ESM transpilation was checked. A complete React application,
full typechecking against installed React definitions, and hydration were
not tested here. Run the application's normal integration and type checks.

See the parent README for styling, accessibility, animation, validation and
clinical-usage notes. The included MIT license applies to these original files.
