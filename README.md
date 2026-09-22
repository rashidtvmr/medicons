# Hospital Clinical Icons

A hospital-specific vector library: **219 unique icons**, **18 categories**, **717 dedicated SVG files**.

The previously curated 234-entry scope is fully mapped in `CATALOG.md`. Fifteen repeated entries resolve to the same canonical icon instead of duplicating files. For example, baby incubator and neonatal incubator share one asset. Every canonical icon has its own SVG file in each static style.

## Start here

Open **`index.html`** in a browser after unzipping. The searchable gallery is self-contained: no build, server, network connection or external fonts are required. Search by name, anatomy, abbreviation or alias; filter by category and style; click an icon to see its source and download that SVG.

## What's included

| Style | Files | Notes |
| --- | ---: | --- |
| Outline | 219 | Rounded strokes, open shapes and clinical detail |
| Solid / filled | 219 | One-color filled geometry with transparent detail cut-outs |
| Duotone | 219 | Current-color tints at 14% and 30% opacity |
| Beam animated | 60 | Self-contained CSS path-travel animation on selected icons |
| **Total SVG files** | **717** | No sprites, raster traces, embedded fonts or externally referenced geometry |

`filled` means `solid`; a redundant fourth static SVG folder is intentionally not included. The React API accepts either name.

## Folder structure

```text
hospital-icons/
  index.html                    Searchable offline gallery
  README.md                     This usage guide
  CATALOG.md                    Canonical inventory and all 234 scope mappings
  LICENSE                       MIT license for the original assets and code
  svg/
    specialties/
      outline/cardiology.svg
      solid/cardiology.svg
      duotone/cardiology.svg
      beam/cardiology.svg
    critical-care-units/
    beds-and-patient-support/
    imaging-and-radiology/
    cardiac-diagnostics/
    laboratory-and-pathology/
    surgery-and-procedures/
    orthopaedics/
    womens-health-and-fertility/
    paediatrics-and-neonatal/
    anatomy/
    respiratory-and-sleep/
    emergency-and-trauma/
    rehabilitation/
    patient-journey/
    hospital-services/
    clinical-equipment/
    conditions/
  react/
    package.json                Local-installable ESM package
    src/                        Editable TypeScript sources
    dist/                       ESM JavaScript and TypeScript declarations
  metadata/
    manifest.json               Filenames, component names, aliases and beam support
    catalog-coverage.json       The original 234-entry scope mapping
    sha256sums.txt               SVG integrity checksums
    validation.json             Automated validation results
  sources/
    art.py                      Original vector recipes and shared anatomy geometry
    render.py                   SVG style renderer
    catalog.py                  Canonical catalog
    rebuild_svg.py              Standard-library SVG rebuild script
  preview/
    gallery.png                 Gallery screenshot
    contact-1.png ... contact-4.png
```

`beam/` is present only in categories that contain animated icons. An icon appears in one physical category. The gallery and manifest also cross-list it where relevant. For example, spine surgery is stored under specialties but is searchable in surgery and procedures.

## Design and color

Each SVG uses a **48 x 48 viewBox** and `currentColor`. Outline strokes use 2.1 design-grid units, with round caps and joins. These clinical symbols are intended primarily for service cards at 32-64 pixels and larger. Review the more detailed equipment and procedure symbols before using them at 16-24 pixels.

Inline SVG and React components can inherit the page's text color. Plain `<img>` references are independent image documents: the parent element's `color` and CSS variables do **not** recolor an external SVG. Use the React components or inline SVG when theme inheritance is needed; otherwise edit the SVG's root color explicitly.

```html
<!-- Plain file reference. Its default color is black. -->
<img
  src="/icons/svg/specialties/outline/cardiology.svg"
  width="48"
  height="48"
  alt="Cardiology"
/>
```

For icons adjacent to equivalent visible text, use `alt=""` on an image, or omit `title` and `ariaLabel` on the React component so it is decorative.

Solid icons use luminance masks for transparent cut-outs, not white-painted details. Keep the `<defs>` and `<mask>` elements when copying or optimizing a solid SVG. Some non-browser SVG-to-raster converters do not implement luminance masks correctly; validate the exported result rather than assuming renderer equivalence.

## Beam animation

Sixty icons have dedicated `beam/` SVGs. Their paths follow a meaningful part of the icon, such as a coronary vessel, waveform, scan arc or tubing. These are lightweight CSS stroke-travel effects, not medical simulations and not independent clinical illustrations.

The SVGs animate without JavaScript. Their defaults can be changed with CSS custom properties when the SVG is inline:

```css
.medical-icon {
  color: #173d49;
  --hmi-beam-color: #08b8bf;
  --hmi-duration: 3s;
}

.medical-icon.is-paused {
  --hmi-play-state: paused;
}
```

The root `<svg>` can receive the `medical-icon` class. When embedding a beam file as an external image, edit those variables inside the SVG rather than on the parent image element.

When the user requests reduced motion, the moving paths are hidden and the complete static base returns to full opacity. Avoid excessive concurrent animation on a hospital homepage. The static variants are available for every icon.

## React and TypeScript

The optional React folder is a **local package**, not a claim that the package is published to npm. It contains named components, per-category entrypoints and per-icon entrypoints. React is a peer dependency and is not bundled. The declared compatibility range is React 18-19.

From your existing application's directory, install the unpacked local package:

```bash
npm install /absolute/path/to/hospital-icons/react
```

Then:

```tsx
import { CardiologyIcon, MriScannerIcon } from "@frontendxlab/medicons";

export function Services() {
  return (
    <div>
      <CardiologyIcon
        size={48}
        variant="duotone"
        title="Cardiology"
        className="text-teal-700"
      />
      <MriScannerIcon
        size={56}
        variant="outline"
        animation="beam"
        duration={3}
        beamColor="#08b8bf"
        title="MRI scanning"
      />
    </div>
  );
}
```

Direct import, which avoids importing a category or full catalog entrypoint:

```tsx
import { CardiologyIcon } from "@frontendxlab/medicons/specialties/cardiology";
```

Import tiers, smallest first: single-icon path above, then category
(`@frontendxlab/medicons/specialties`), then full root. Prefer the single-icon
path for the smallest bundle. The package sets `"sideEffects": false` and
ships side-effect-free ESM, so named imports tree-shake cleanly; avoid
namespace imports (`import *`), which pull in all 219 icons (measured 3,176 B
single-icon vs 124,072 B namespace import with esbuild, minified, react
external). See `react/README.md` for the full table.

The component API accepts standard SVG props, a forwarded ref, and:

```ts
size?: number | string; // default 48
variant?: "outline" | "solid" | "filled" | "duotone";
strokeWidth?: number;   // design-grid units; default 2.1
animation?: "none" | "beam";
duration?: number;      // seconds; default 2.6, minimum 0.5
beamColor?: string;
title?: string;
ariaLabel?: string;
```

`animation="beam"` applies only to the 60 icons listed with `supportsBeam: true` in the manifest. It leaves unsupported icons static; it does not invent a generic scan animation for every icon.

The components use React `useId` to keep solid-mask IDs distinct across component instances. They include client-component directives for environments that separate server and client components. For zero component JavaScript on static pages, use the raw SVG files instead. The SVGs themselves do not require React, Next.js or an animation package.

## Validation and limitations

All 717 SVGs were parsed as XML and checked for internal mask references, file coverage, and the absence of raster images, fonts, scripts and external geometry. The 657 static variants were rendered in Chromium and checked for geometry outside the viewBox. All three styles were reviewed on contact sheets. The gallery's search, cross-category filtering, style switching, icon dialog, single-file download, dark theme, mobile layout and reduced-motion behavior were tested in Chromium.

The React TypeScript sources were transpiled to 239 ESM modules without syntax diagnostics. **A full React application, TypeScript checking against installed React type definitions, hydration, Safari, Firefox and screen-reader behavior were not tested in this environment.** Run your application's typecheck and integration tests before deployment.

These are schematic navigation assets, not diagnostic images, anatomical teaching plates, device specifications or treatment instructions. Several departments necessarily share visual motifs. Keep clear text labels, and obtain clinical review for the way icons are used on a public hospital website.

No Lucide or Ionicons SVG files were copied into the pack. No standalone arrows, menus, generic user avatars or social-brand logos are bundled. People, directional marks and familiar medical shapes appear only as part of the curated clinical compositions. A hospital-specific brand logo is not included because no hospital name or brand identity was supplied for this asset-generation phase.

## Editing the SVG recipes

The files in `sources/` preserve editable geometry. `rebuild_svg.py` uses only Python's standard library and regenerates SVG files, the catalog, manifest and checksums in the package root. The gallery and React exports are snapshots and must be updated separately after changing the underlying recipes. Make a copy before rebuilding.
