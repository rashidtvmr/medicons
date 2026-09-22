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
