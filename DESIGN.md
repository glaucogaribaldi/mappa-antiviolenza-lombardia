---
name: Mappa Antiviolenza Lombardia
description: Brand identity and design system for the Lombardy Anti-violence and Emergency Support Map.
version: alpha
colors:
  primary: "#ec008c"      # 1522 Magenta Brand (Pari Opportunità)
  secondary: "#1976d2"    # Institutional Blue (Safety & Security)
  tertiary: "#e60000"     # Emergency Red (NUE 112 Official Color)
  neutral: "#ffffff"      # Core White Backgrounds
  neutral-light: "#f5f5f5" # Soft Neutral/Backgrounds (Off-white)
  neutral-dark: "#212121"  # Deep Charcoal for High-Contrast Text
  border: "#eee"          # Light borders
  success: "#4CAF50"      # Geolocalize Green
typography:
  brand:
    fontFamily: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
    fontSize: 1.15rem
    fontWeight: 800
  h1:
    fontFamily: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
    fontSize: 1.25rem
    fontWeight: 850
  body-md:
    fontFamily: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
    fontSize: 0.85rem
    fontWeight: 500
  label-caps:
    fontFamily: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
    fontSize: 0.75rem
    fontWeight: 800
    textTransform: uppercase
  emergency-title:
    fontFamily: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
    fontSize: 1.0rem
    fontWeight: 900
    fontStyle: italic
rounded:
  sm: 12px
  md: 20px
  lg: 24px
  pill: 30px
spacing:
  xs: 6px
  sm: 10px
  md: 15px
  lg: 20px
components:
  top-brand-card:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  button-quick-exit:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  filter-pill-cav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm}"
  filter-pill-ps:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm}"
  filter-pill-police:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm}"
  btn-112:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  btn-1522:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  bottom-sheet:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.neutral-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

## Overview

High-Contrast Accessibility meets Critical Emergency Usability. 

Designed for Giacomo's "Mappa Antiviolenza Lombardia", this UI takes inspiration from a modern, App-like map interface (e.g., Apple Maps) specifically optimized for high-stress mobile scenarios. It features absolute structural clarity, rapid gesture-friendly click targets, bold institutional color markers, and an instantaneous safety exit mechanism.

## Colors

The system uses three high-contrast brand keys to distinguish the support levels instantly:

- **Primary (#ec008c):** "1522 Magenta" representing Equal Opportunities and CAV (Centri Antiviolenza) support.
- **Secondary (#1976d2):** "Institutional Blue" representing police stations and safety presidiums.
- **Tertiary (#e60000):** "Emergency Red" representing medical Pronto Soccorso and the official NUE 112 hotline.
- **Neutral (#ffffff) & Light (#f5f5f5):** Form the clean, glass-like background layers.
- **Neutral-Dark (#212121):** Premium charcoal, ensuring perfect text-contrast and readability.

## Typography

Font scales are optimized for extreme readability in low-light and high-stress situations:

- **Brand Title:** Bold and authoritative to anchor the app's purpose.
- **H1 (Headings):** Compact yet heavy-weight (850+) headings to frame locations and cards.
- **Body-MD:** High-contrast text spacing for telephone numbers, opening hours, and support instructions.
- **Emergency Titles:** Set in bold italicized uppercase, replicating the urgent institutional typography of emergency services.

## Layout

A fully responsive, Mobile-First structure that eliminates all unnecessary clutter:

- **Full-Screen Canvas:** The Google Maps layer occupies 100% of the viewport.
- **Floating Upper Console:** Integrates a compact search bar and dropdown filter selectors.
- **Unified Bottom Bar:** Houses two giant, unmissable emergency calling buttons.
- **Segmented Categories:** Displays the 3 filters (CAV, P. Soccorso, Police) as side-by-side equal segments above the footer, completely avoiding horizontal scrolling.

## Elevation & Depth

Visual hierarchy is maintained through high-blur translucent overlays:

- **Glassmorphism Backdrop Filter:** Panels use `backdrop-filter: blur(15px)` with a very fine border `1px solid rgba(255, 255, 255, 0.25)` to stand out dynamically against the map underneath.
- **Drop Shadows:** Components use lightweight, soft shadows (`box-shadow: 0 8px 32px rgba(0,0,0,0.15)`) to emphasize interactive floating surfaces and drawers.

## Shapes

Organic and high-contrast shapes ensure touch targets feel approachable and ergonomic:

- **High Rounded Edges (20px to 24px):** Applied to cards, sheets, and headers to create a protective, modern, app-like feeling.
- **Pill Shapes (30px):** Applied to filters and action items to guarantee high-tactility button surfaces.

## Components

The critical user touchpoints are modeled as strict components:

- **NUE 112 Button:** A prominent red container featuring a circular white badge with a red phone receiver and the text "112" on the left, followed by the bold italic "EMERGENZA" on the right.
- **1522 Button:** A magenta button with pulsating aura animations to immediately draw attention for domestic violence support.
- **Quick Exit FAB:** An isolated red button in the top right that redirects instantly to google.it on tap or upon pressing the "Esc" key.
- **Details Drawer (Bottom Sheet):** Slides up gracefully from the bottom, showing large direct-dialing phone numbers, verified badges, and structured bullet points of available support services.

## Do's and Don'ts

### Do's:
- **Do** make all buttons and phone numbers large enough to be easily tapped with one thumb under stress.
- **Do** keep a clear visual separation between the Brand Title and the Quick Exit button.
- **Do** use the official red, magenta, and blue colors for their respective categories.

### Don'ts:
- **Don't** allow categories or filters to overflow horizontally and require a side-scroll on narrow screens.
- **Don't** hide critical information behind menus or multiple click layers.
- **Don't** use low-contrast text that compromises readability.
