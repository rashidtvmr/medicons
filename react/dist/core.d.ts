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
