# Design Notes: What the Best Websites Do

Research from 2026-11-27. 52 well-known sites were screenshotted on desktop (1440 px), and 45 loaded. The other 7 blocked automated access (Dropbox, Mailchimp, Allbirds, Glossier, Patagonia, Rivian, Chipotle). Use these notes as a checklist when building any client site.

Categories covered:
- **Tech / SaaS:** Apple, Stripe, Linear, Vercel, Notion, Figma, Framer, Raycast, GitHub, Anthropic, Airbnb, Spotify, Slack, Shopify, Webflow, Loom, Arc, Duolingo
- **Brands / shops:** Nike, Aesop, Bang & Olufsen, Polestar, Tesla, Dyson, LEGO, Oatly
- **Restaurants / food:** Sweetgreen, Shake Shack, Nobu, Eleven Madison Park, Blue Bottle, Dishoom
- **Health:** One Medical, Hinge Health, Headspace, Sword Health (Calm, Zocdoc and Hims showed bot walls)
- **Creative / portfolio:** Chris Burkard, Awwwards, Pentagram, Squarespace, Behance, Dribbble

---

## 1. The hero (first screen) decides everything

- **One big promise in 3 to 8 words**, for example:
  - "Your shortcut to everything." (Raycast)
  - "A website makes it real." (Squarespace)
  - "Primary care designed for you." (One Medical)

  Benefit first, not company name.
- **One sentence underneath** explaining how. Never a paragraph.
- **Max two buttons:**
  - Primary, filled: *Get started*, *Book a table*, *Book an appointment*.
  - Secondary, outline or text: *Learn more*, *See the menu*.
- **One strong visual.** It can be:
  - the product itself (Linear, Notion and Slack show their real app UI);
  - a full-bleed photo (Nobu, Sweetgreen, Chris Burkard, Nike);
  - a bold graphic (Stripe's gradient wave, Vercel's glowing triangle).
- Restaurants and photographers go **image-first, text-last**. Sweetgreen is one giant food close-up with "Made From Scratch". Burkard is a photo with 4 menu words.

## 2. Trust right after the hero

- **Logo strip** of known clients directly under the hero: Stripe, Linear, Vercel, Figma, Framer, Webflow, Slack and Loom all do this.
  - For small businesses, use "As seen in", partner logos, or Google rating stars.
- **Big numbers:**
  - Squarespace: "14M+ / $36B+ / 200+".
  - GitHub: "225M+ developers".
  - Sword: "Join 1,000,000+ people".
  - Use 3 numbers max.
- **Health sites** lean on reassurance words like personalized, covered, no cost, licensed clinician.

## 3. Layout patterns that repeat everywhere

- **Bento grid:** cards of different sizes in one grid.
  - Used by Stripe, Sword, Apple and Linear's feature sections.
  - Good for "services" sections.
- **Horizontal card carousel** with arrows, as in Hinge Health "Pain relief from head to toe" and Airbnb rows. Good for services or menu categories on mobile.
- **Tabs or pills to switch content**, as on Headspace, Squarespace, Slack and Arc. This is the same idea as our restaurant menu tabs.
- **"Choose your path" cards:**
  - Headspace "What kind of headspace are you looking for?" (Stress less, Sleep soundly...).
  - Sword's 5 program cards.
  - Great for clinics: "Back pain / Sports injury / After surgery".
- **Alternating sections:** a light section, then a dark or coloured one, then light again (Slack purple band, Hinge dark green band). This creates rhythm and stops the page feeling long.

## 4. Typography

- **Huge, tight headlines**, often 60 to 100 px on desktop, with a slightly negative letter spacing. Linear, Vercel, Notion and Stripe are all like this.
- **Body text small and calm**, in a grey (not pure black) colour.
- **Serif for luxury and food:**
  - Anthropic, Eleven Madison Park and One Medical use serif headlines.
  - Nobu and Dishoom use elegant serif or small caps.
- **Sans for tech and health.**
- **Two-tone headline trick:** part of the sentence dark, the rest grey or a brand colour.
  - Stripe: "Financial infrastructure to grow your revenue. *Accept payments...*"
  - Shopify: "Sell everywhere people shop. *Online and in person.*"
  - Hinge: "Personalized care *for a life in motion*".

## 5. Colour

- **Mostly neutral** (white, off-white, black, or dark grey), plus **one accent colour** for buttons:
  - Stripe purple, Slack aubergine, One Medical teal, Hinge lime, Duolingo green.
- **Dark mode is the premium tech look:** Linear, Vercel, Raycast, Framer and Webflow.
- **Off-white / cream backgrounds** read as warm and calm: Anthropic, Sword and Aesop.
- **Brand colour as a whole section background** for emphasis: Headspace yellow card, Slack purple band.

### The 60-30-10 rule (Malek's rule, apply to every site)
- **60% dominant colour:** backgrounds and large areas, usually a neutral.
- **30% secondary colour:** sections, cards, header and footer, large text.
- **10% accent colour:** buttons, links, highlights and icons. This is the "jewellery" that pulls the eye to the action.

Examples from the research:
- Sweetgreen: cream / dark green / food photography.
- Hinge Health: white / deep green / lime accent.
- Stripe: white / navy text / purple buttons.

Our demo sites:
- Restaurant: cream 60 / dark brown 30 / terracotta 10.
- Physio: white 60 / navy and mint 30 / teal 10.
- Photographer: near-black 60 / dark grey 30 / gold 10.

Keep the accent rare. If it is everywhere, nothing stands out.

## 6. Navigation

- Logo on the left, 4 to 6 links, **one filled CTA button on the right** ("Get started", "Order", "Book a table").
- A sticky header on scroll is standard.
- Food and luxury use **centred logos** (Nobu, Eleven Madison Park, Aesop, Sweetgreen).
- An announcement bar at the very top is very common: Black Friday, "New: ...", free shipping (Headspace, Webflow, Loom, Aesop, Dribbble).

## 7. Per-industry lessons (for our clients)

| Client type | What the best do | Apply it like this |
|---|---|---|
| Restaurant / cafe | Full-screen food or interior photo, centred logo, "Book a table" or "Order" always visible, menu link up top (Nobu, Sweetgreen, Dishoom, Shake Shack) | Real food photos are 80% of the result. Keep the Book or Order button in the header. Include hours and location. |
| Clinic / health | Warm photo of a real person, reassuring headline, "Check eligibility" or "Book appointment" CTA, symptom or program cards, insurance and FAQ (Hinge, One Medical, Sword, Headspace) | Use "choose your problem" cards, a clear booking CTA, insurance information and FAQ. |
| Photographer / creative | The work is the site: full-bleed image, minimal menu, nothing competes with the photos (Burkard, Pentagram, Awwwards) | Show big images and little text, and keep the gallery near the top. |
| Shop / product | Product hero, category tiles with photos, product cards with price and an add-to-cart button, promo banner (Nike, LEGO, Dyson, Aesop) | Add category tiles under the hero and keep prices visible. |
| Service business / startup | Hero with a product screenshot, logo strip, features grid, testimonials, pricing, a final CTA (Stripe, Notion, Slack, Loom) | Follow this classic order. |

## 8. Things to avoid (seen even on big sites)

- **Too many popups.** Aesop, B&O, Blue Bottle and Eleven Madison Park cover the hero with cookie, region and newsletter popups on first load, which feels bad. Show one popup at most, late, and make it small.
- **Empty first screen.** Shake Shack and Duolingo rendered mostly blank space above the fold.
- **Text over busy photos without an overlay.** Always add a dark gradient behind the text.

## 9. Build checklist for every client site

1. A hero with a promise, one line of explanation, 1 or 2 CTAs and one strong visual.
2. A trust strip: logos, rating or numbers.
3. Services or products in a bento grid or cards.
4. One coloured or dark "band" section for rhythm.
5. Testimonials (real ones only).
6. FAQ where it fits (health, services).
7. A final CTA section, then a footer with hours, location and contact.
8. Mobile check at 390 px. Sticky header with the CTA. Fast images (compressed, lazy-loaded).
9. Accessibility: contrast, alt text, focus states.
10. At most one popup.
