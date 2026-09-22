"use client";

import { createElement as h, forwardRef, useId } from "react";
import type { ForwardRefExoticComponent, RefAttributes, SVGProps } from "react";

export type IconVariant = "outline" | "solid" | "filled" | "duotone";
export type IconAnimation = "none" | "beam";
export type ClinicalIconProps = Omit<SVGProps<SVGSVGElement>, "children" | "title" | "strokeWidth"> & {
  size?: number | string;
  variant?: IconVariant;
  strokeWidth?: number;
  title?: string;
  ariaLabel?: string;
  animation?: IconAnimation;
  /** Beam duration in seconds. A minimum of 0.5 seconds is enforced. */
  duration?: number;
  beamColor?: string;
};
export type ClinicalIconComponent = ForwardRefExoticComponent<ClinicalIconProps & RefAttributes<SVGSVGElement>>;
type Attributes = Record<string, string | number>;
type Shape = { tag: "path" | "circle" | "rect" | "ellipse"; role: "body" | "accent" | "line" | "cut" | "dot"; attrs: Attributes };
type Group = { tag: "g"; attrs: Attributes; children: Node[] };
type Node = Shape | Group;
type PaintVariant = Exclude<IconVariant, "filled">;

const css = "@keyframes hmi-flow{to{stroke-dashoffset:-100}}.hmi-beam-tail,.hmi-beam-head{animation:hmi-flow var(--hmi-duration,2.6s) linear infinite;animation-play-state:var(--hmi-play-state,running)}.hmi-beam-tail{stroke-dasharray:20 80;opacity:.22}.hmi-beam-head{stroke-dasharray:7 93}@media(prefers-reduced-motion:reduce){.hmi-beam-tail,.hmi-beam-head{animation:none;display:none}.hmi-beam-base{opacity:1}}";

function paint(nodes: Node[], variant: PaintVariant, mode: "paint" | "mask", strokeWidth: number): ReturnType<typeof h>[] {
  const result: ReturnType<typeof h>[] = [];
  nodes.forEach((node, index) => {
    if (node.tag === "g") {
      const children = paint(node.children, variant, mode, strokeWidth);
      if (children.length) result.push(h("g", { ...node.attrs, key: index }, ...children));
      return;
    }
    const attributes: Record<string, unknown> = { ...node.attrs, key: index };
    if (mode === "mask") {
      if (node.role !== "cut" && node.role !== "accent") return;
      Object.assign(attributes, { fill: "none", stroke: "black", strokeWidth: strokeWidth * (1.75 / 2.1) });
    } else {
      if (variant === "solid" && node.role === "cut") return;
      Object.assign(attributes, { fill: "none", stroke: "currentColor", strokeWidth: variant === "solid" ? strokeWidth * (1.6 / 2.1) : strokeWidth });
      if (node.role === "body" || node.role === "accent") {
        if (variant === "solid") attributes.fill = "currentColor";
        if (variant === "duotone") Object.assign(attributes, { fill: "currentColor", fillOpacity: node.role === "body" ? 0.14 : 0.30 });
      }
      if (node.role === "line" && variant === "solid") attributes.strokeWidth = strokeWidth;
      if (node.role === "dot") Object.assign(attributes, { fill: "currentColor", stroke: "none" });
    }
    result.push(h(node.tag, attributes));
  });
  return result;
}

/** Original geometry, shared rendering, and collision-safe mask IDs. */
export function createClinicalIcon(slug: string, displayName: string, nodes: Node[], beamPath?: string): ClinicalIconComponent {
  const Icon = forwardRef<SVGSVGElement, ClinicalIconProps>(function ClinicalIcon(props, ref) {
    const {
      size = 48, width, height, variant = "outline", strokeWidth = 2.1,
      animation = "none", duration = 2.6, beamColor, title, ariaLabel,
      "aria-label": explicitLabel, "aria-hidden": explicitHidden, style, ...rest
    } = props;
    const instanceId = useId();
    const maskId = "hci-" + slug + "-" + instanceId;
    const activeVariant: PaintVariant = variant === "filled" ? "solid" : variant;
    const label = explicitLabel ?? ariaLabel ?? title;
    const isBeam = animation === "beam" && Boolean(beamPath);
    const actualStroke = Number.isFinite(strokeWidth) && strokeWidth > 0 ? strokeWidth : 2.1;
    const actualDuration = Number.isFinite(duration) ? Math.max(0.5, duration) : 2.6;
    let art = paint(nodes, activeVariant, "paint", actualStroke);
    if (activeVariant === "solid") {
      const cutouts = paint(nodes, activeVariant, "mask", actualStroke);
      if (cutouts.length) {
        art = [
          h("defs", { key: "defs" }, h("mask", { id: maskId, maskUnits: "userSpaceOnUse", x: 0, y: 0, width: 48, height: 48, style: { maskType: "luminance" } },
            h("rect", { width: 48, height: 48, fill: "white" }), ...cutouts)),
          h("g", { key: "art", mask: `url(#${maskId})` }, ...art),
        ];
      }
    }
    if (isBeam) {
      art = [
        h("style", { key: "style" }, css),
        h("g", { key: "base", className: "hmi-beam-base", opacity: 0.48 }, ...art),
        h("g", { key: "beam", fill: "none", stroke: beamColor ?? "var(--hmi-beam-color, currentColor)" },
          h("path", { className: "hmi-beam-tail", d: beamPath, pathLength: 100, strokeWidth: actualStroke * (3.8 / 2.1) }),
          h("path", { className: "hmi-beam-head", d: beamPath, pathLength: 100, strokeWidth: actualStroke * (2.3 / 2.1) })),
      ];
    }
    const rootStyle = isBeam ? { "--hmi-duration": actualDuration + "s", ...style } : style;
    return h("svg", {
      ...rest, ref, xmlns: "http://www.w3.org/2000/svg", width: width ?? size, height: height ?? size,
      viewBox: "0 0 48 48", fill: "none", strokeLinecap: "round", strokeLinejoin: "round",
      role: label ? "img" : rest.role, "aria-label": label,
      "aria-hidden": explicitHidden ?? (label ? undefined : true), style: rootStyle,
      "data-clinical-icon": slug,
    }, title ? h("title", { key: "title" }, title) : null, ...art);
  });
  Icon.displayName = displayName;
  return Icon;
}
