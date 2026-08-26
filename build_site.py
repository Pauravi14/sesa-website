"""Generate static HTML pages for SESA KFZ-Sachverständigenbüro."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

from lucide_icons import lucide_svg

ROOT = Path(__file__).resolve().parent
LOGO_MONOGRAM = "assets/logo-monogram.png?v=6"
ABOUT_HERO = "assets/about/about-hero.jpg?v=1"
ABOUT_PORTRAIT = "assets/portrait-placeholder.png?v=1"

PHONE_DISPLAY = "+49 177 3145839"
PHONE_LINK = "+491773145839"
WHATSAPP_NUMBER = "491773145839"
EMAIL = "sesa-svb@outlook.de"
ADDRESS = "Pohlweg 76, 33098 Paderborn"
BUSINESS = "SESA KFZ-Sachverständigenbüro"
OWNER = "Selim Sabahoglu"

# Qualification copy — use exact certificate wording only after client confirmation
QUAL_TRUST_BLURB = (
    "Kfz-Meister und Sachverständiger für Kraftfahrzeuge. "
    "Detaillierte Qualifikationsnachweise stellen wir auf Anfrage zur Verfügung."
)

GUTACHTEN_TIMING = (
    "Gutachtenerstellung in der Regel innerhalb von 24–48 Stunden "
    "nach vollständiger Schadenaufnahme"
)
GUTACHTEN_TIMING_CARD = (
    "In der Regel innerhalb von 24–48 Stunden<br>nach vollständiger Schadenaufnahme"
)

HERO_IMG_VER = "4"
SERVICE_IMG_VER = "3"

HERO_SLIDES = [
    (f"assets/hero/slide-1.jpg?v={HERO_IMG_VER}", "Fahrzeugbegutachtung durch Kfz-Sachverständigen"),
    (f"assets/hero/slide-2.jpg?v={HERO_IMG_VER}", "Schadendokumentation am Fahrzeug"),
    (f"assets/hero/slide-3.jpg?v={HERO_IMG_VER}", "Wohnmobil-Begutachtung"),
    (f"assets/hero/slide-4.jpg?v={HERO_IMG_VER}", "Oldtimer und Youngtimer"),
    (f"assets/hero/slide-5.jpg?v={HERO_IMG_VER}", "Fachliche Fahrzeugbewertung"),
]

SERVICE_THUMBS = {
    "unfall": "assets/service/service-unfall.jpg?v=3",
    "bewertung": "assets/service/service-bewertung.jpg?v=3",
    "wohnmobile": "assets/service/service-wohnmobile.jpg?v=3",
    "oldtimer": "assets/service/service-oldtimer.jpg?v=3",
}

WHATSAPP_TEXT_BERATUNG = (
    "Guten Tag SESA,\n"
    "ich benötige eine Beratung.\n"
    "Bitte rufen Sie mich zurück."
)
WHATSAPP_TEXT_SCHADEN = (
    "Guten Tag SESA,\n"
    "ich möchte einen Schaden melden.\n"
    "Bitte rufen Sie mich zurück."
)

WHATSAPP_ICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="#ffffff" aria-hidden="true">'
    '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
    "</svg>"
)

PHONE_ICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24c1.12.37 2.33.57 3.58.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.46.57 3.58a1 1 0 01-.24 1.01l-2.2 2.2z"/>'
    "</svg>"
)


def whatsapp_url(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text, safe='')}"


def wa_float_widget() -> str:
    beratung = whatsapp_url(WHATSAPP_TEXT_BERATUNG)
    schaden = whatsapp_url(WHATSAPP_TEXT_SCHADEN)
    return f"""
    <div class="wa-float-wrap" data-wa-float>
      <button type="button" class="wa-float-trigger" aria-label="WhatsApp: Hilfe anfordern" aria-expanded="false" data-wa-toggle>
        <span class="wa-float-bubble">
          <span class="wa-float-bubble-small">Brauchen Sie Hilfe?</span>
          <span class="wa-float-bubble-strong">Jetzt kontaktieren</span>
        </span>
        <span class="wa-float-icon" aria-hidden="true">
          {WHATSAPP_ICON_SVG}
        </span>
      </button>
      <div class="wa-float-menu" hidden data-wa-menu>
        <p class="wa-float-greeting">Guten Tag SESA</p>
        <p class="wa-float-hint">Wie können wir Ihnen helfen?</p>
        <a class="wa-float-option" href="{beratung}" target="_blank" rel="noopener noreferrer">
          <span class="wa-float-option-title">Beratung</span>
          <span class="wa-float-preview">Guten Tag SESA, ich benötige eine Beratung. Bitte rufen Sie mich zurück.</span>
        </a>
        <a class="wa-float-option" href="{schaden}" target="_blank" rel="noopener noreferrer">
          <span class="wa-float-option-title">Schaden melden</span>
          <span class="wa-float-preview">Guten Tag SESA, ich möchte einen Schaden melden. Bitte rufen Sie mich zurück.</span>
        </a>
      </div>
    </div>"""


def mobile_action_bar() -> str:
    return ""


def hero_slides_html() -> str:
    parts = []
    for i, (src, _alt) in enumerate(HERO_SLIDES):
        active = " is-active" if i == 0 else ""
        fetch = " fetchpriority=\"high\"" if i == 0 else ""
        parts.append(
            f'        <img class="hero__slide{active}" src="{src}" alt="" '
            f'loading="eager" decoding="async"{fetch} />'
        )
    return "\n".join(parts)


PROCESS_FLOW_ORBIT = (
    '<span class="process-flow__orbit" data-process-orbit>'
    '<span class="process-flow__orbit-track"></span>'
    '<span class="process-flow__orbit-progress"></span>'
    '<span class="process-flow__orbit-chevron" data-orbit-chevron>&gt;</span>'
    '</span>'
)

PROCESS_FLOW_CONNECTOR_TRACK = (
    '<li class="process-flow__connector process-flow__connector--track" data-process-connector aria-hidden="true">'
    f'{PROCESS_FLOW_ORBIT}'
    '</li>'
)

PROCESS_FLOW_CONNECTOR_INLINE = (
    '<span class="process-flow__connector process-flow__connector--inline" data-process-connector aria-hidden="true">'
    f'{PROCESS_FLOW_ORBIT}'
    '</span>'
)


def process_flow_unit(number: str, title: str, body: str, with_connector: bool) -> str:
    inline = f"\n            {PROCESS_FLOW_CONNECTOR_INLINE}" if with_connector else ""
    track = f"\n{PROCESS_FLOW_CONNECTOR_TRACK}" if with_connector else ""
    return f"""
        <li class="process-flow__unit" data-flow-item>
          <div class="process-flow__unit-head">
            <span class="process-flow__marker" aria-hidden="true">{number}</span>{inline}
          </div>
          <article class="process-flow__card">
            <h3>{title}</h3>
            <p>{body}</p>
          </article>
        </li>{track}"""


SERVICE_ICON_SVG_OPEN = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
)

SERVICE_ICONS = {
    "unfall": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M3 17h18"/>'
        '<path d="M5 17v-5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v5"/>'
        '<circle cx="7.5" cy="17" r="1.5"/>'
        '<circle cx="16.5" cy="17" r="1.5"/>'
        '<path d="M8 12h8"/>'
        '<path d="M12 12V8"/>'
        '<path d="M9.5 8 12 5.5 14.5 8"/>'
        "</svg>"
    ),
    "bewertung": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M8 4h8v16H8z"/>'
        '<path d="M10 4V3h4v1"/>'
        '<path d="M10 9h4"/><path d="M10 12h4"/><path d="M10 15h2"/>'
        '<path d="M14.5 14.5 16 16l2.5-2.5"/>'
        "</svg>"
    ),
    "wohnmobile": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M3 16h18"/>'
        '<path d="M5 16V11h5l2-3h8v8"/>'
        '<rect x="11.5" y="11" width="2" height="1.8" rx=".25"/>'
        '<rect x="14.5" y="11" width="2" height="1.8" rx=".25"/>'
        '<circle cx="7" cy="16" r="1.5"/>'
        '<circle cx="17" cy="16" r="1.5"/>'
        "</svg>"
    ),
    "oldtimer": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M3 15h18"/>'
        '<path d="M5 15l2-4h6l2 2h4l1 2"/>'
        '<path d="M7 11V9"/>'
        '<circle cx="7" cy="15" r="1.5"/>'
        '<circle cx="17" cy="15" r="1.5"/>'
        '<path d="M10 13h4"/>'
        "</svg>"
    ),
    "beweissicherung": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M6 5h12v14H6z"/>'
        '<path d="M8 5V4h8v1"/>'
        '<path d="M9 10h6"/><path d="M9 13h4"/>'
        '<circle cx="16" cy="15" r="2"/>'
        '<path d="M16 13.5v3"/>'
        "</svg>"
    ),
    "privatgutachten": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<circle cx="9" cy="8" r="2.5"/>'
        '<path d="M5 18c0-2.5 1.8-4.5 4-4.5s4 2 4 4.5"/>'
        '<path d="M15 6h5v12h-5z"/>'
        '<path d="M17 9h2"/><path d="M17 12h2"/>'
        "</svg>"
    ),
    "kostenvoranschlag": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<rect x="6" y="4" width="12" height="16" rx="1"/>'
        '<path d="M9 8h2"/><path d="M13 8h2"/>'
        '<path d="M9 11h2"/><path d="M13 11h2"/>'
        '<path d="M9 14h2"/><path d="M13 14h2"/>'
        "</svg>"
    ),
    "versicherungsgutachten": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M12 3 5 6v5c0 4.5 3.5 7.5 7 9 3.5-1.5 7-4.5 7-9V6l-7-3z"/>'
        '<path d="M9.5 11.5h5"/>'
        '<path d="M12 9v5"/>'
        "</svg>"
    ),
    "beratung": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M5 9c0-2 1.8-3.5 4-3.5s4 1.5 4 3.5-1.8 3.5-4 3.5c-.5 0-1-.1-1.4-.3L7 16v-2.8"/>'
        '<path d="M14 10h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1l-1.5 2-1.5-2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2z"/>'
        "</svg>"
    ),
    "ortstermine": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M12 21s6-5 6-9a6 6 0 1 0-12 0c0 4 6 9 6 9z"/>'
        '<circle cx="12" cy="12" r="2"/>'
        "</svg>"
    ),
    "rechte": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<path d="M6 3h7l3 3v14H6z"/>'
        '<path d="M13 3v3h3"/>'
        '<path d="M9 10h4"/><path d="M9 13h3"/>'
        '<path d="M17 5.5 19 8.25 17 11"/>'
        '<path d="M15.25 8.25h3.5"/>'
        "</svg>"
    ),
    "faq": (
        f"{SERVICE_ICON_SVG_OPEN}"
        '<circle cx="12" cy="12" r="8"/>'
        '<path d="M9.5 9.5A2 2 0 0 1 12.5 11c0 1.2-1.5 1.5-1.5 2.5"/>'
        '<path d="M12 16.5v.5"/>'
        "</svg>"
    ),
}

SERVICE_STEP_ICONS: dict[str, list[str]] = {
    "unfallgutachten.html": ["file-text", "shield-check", "message-circle"],
    "fahrzeugbewertung.html": ["car", "clipboard-check"],
    "oldtimer-youngtimer.html": ["car", "file-text"],
    "wohnmobile.html": ["caravan", "droplets"],
    "beweissicherung.html": ["camera", "file-text"],
    "privatgutachten.html": ["scale", "circle-euro"],
    "kostenvoranschlag.html": ["calculator", "clipboard-list"],
    "versicherungsgutachten.html": ["shield", "circle-euro"],
    "beratung.html": ["messages-square", "phone"],
    "ortstermine.html": ["map-pin", "clock"],
}

LEISTUNGEN_SERVICES = [
    ("unfallgutachten.html", "Unfallgutachten / Haftpflicht", "Schadenaufnahme nach unverschuldetem Unfall.", "unfall", True),
    ("fahrzeugbewertung.html", "Fahrzeugbewertung", "Marktwert und Wiederbeschaffungswert.", "bewertung", False),
    ("oldtimer-youngtimer.html", "Oldtimer & Youngtimer", "Klassiker und Sammlerfahrzeuge.", "oldtimer", False),
    ("wohnmobile.html", "Wohnmobile & Wohnwagen", "Freizeitfahrzeuge.", "wohnmobile", False),
    ("beweissicherung.html", "Beweissicherung", "Dokumentation vor Reparatur oder Veränderung.", "beweissicherung", False),
    ("privatgutachten.html", "Privatgutachten", "Unabhängige Begutachtung im Privatauftrag.", "privatgutachten", False),
    ("kostenvoranschlag.html", "Kostenvoranschlag", "Vereinfachte Reparaturkostenermittlung.", "kostenvoranschlag", False),
    ("versicherungsgutachten.html", "Versicherungsgutachten / Kasko", "Begutachtung von Kaskoschäden.", "versicherungsgutachten", False),
    ("beratung.html", "Beratung", "Ersteinschätzung und Vorgehen.", "beratung", False),
    ("ortstermine.html", "Ortstermine", "Begutachtung am Fahrzeugstandort.", "ortstermine", False),
]


def service_icon_svg(key: str) -> str:
    return SERVICE_ICONS[key]


def service_card_icon(key: str, wrapper_class: str = "service-card__icon") -> str:
    return f'<span class="{wrapper_class}">{service_icon_svg(key)}</span>'


def leistungen_service_card(slug: str, title: str, description: str, icon_key: str, featured: bool = False) -> str:
    featured_class = " leistungen-card--featured" if featured else ""
    heading = "h2" if featured else "h3"
    return f"""
        <article class="leistungen-card{featured_class}">
          <a class="leistungen-card__link" href="{slug}">
            {service_card_icon(icon_key, "leistungen-card__icon")}
            <div class="leistungen-card__copy">
              <{heading} class="leistungen-card__title">{title}</{heading}>
              <p class="leistungen-card__desc">{description}</p>
            </div>
          </a>
        </article>"""


def leistungen_page_body() -> str:
    cards = "".join(
        leistungen_service_card(slug, title, description, icon_key, featured)
        for slug, title, description, icon_key, featured in LEISTUNGEN_SERVICES
    )
    return f"""
    <div class="services-page">
      <section class="services-hero" aria-labelledby="services-title">
        <div class="services-hero__inner">
          <header class="services-hero__copy">
            <p class="services-hero__kicker">SESA · Kfz-Sachverständigenbüro</p>
            <h1 id="services-title">Leistungen</h1>
            <span class="services-hero__rule" aria-hidden="true"></span>
            <p class="services-hero__lead">Alle fachlichen Angebote im Überblick — von Unfallgutachten bis Ortstermin.</p>
          </header>
          <div class="services-hero__media" aria-hidden="true">
            <img src="../assets/workshop-tools.png" alt="" width="640" height="420" loading="eager" decoding="async" />
          </div>
        </div>
      </section>

      <section class="services-grid" aria-label="Leistungen">
        <div class="services-page__inner services-grid__inner">
          <div class="services-grid__cards">
{cards}
          </div>
        </div>
      </section>

      <section class="services-cta" aria-label="Kontakt">
        <div class="services-page__inner services-cta__inner">
          <p class="services-cta__text">Fragen oder Gutachten nötig? Ich bin persönlich für Sie da.</p>
          <div class="services-cta__actions">
            <a class="btn btn-primary" href="tel:{PHONE_LINK}">Jetzt anrufen</a>
            <a class="btn btn-outline-copper" href="../schaden-melden.html">Schaden melden</a>
          </div>
        </div>
      </section>
    </div>"""


def about_page_body(depth: int = 0) -> str:
    p = prefix(depth)
    kontakt = f"{p}kontakt.html"
    portrait_img = f"{p}{ABOUT_PORTRAIT}"
    return f"""
    <div class="about-page">
      <section class="about-hero" aria-labelledby="about-title">
        <div class="about-hero__inner">
          <header class="about-hero__copy">
            <p class="about-hero__kicker">SESA · Kfz-Sachverständigenbüro</p>
            <h1 id="about-title">Über uns</h1>
            <span class="about-hero__rule" aria-hidden="true"></span>
            <p class="about-hero__lead">{OWNER} — unabhängiger Kfz-Sachverständiger in Paderborn.</p>
          </header>
          <div class="about-hero__media" aria-hidden="true">
            <img src="{portrait_img}" alt="" width="480" height="600" decoding="async" />
          </div>
        </div>
      </section>

      <section class="about-main">
        <div class="about-page__inner about-main__grid">
          <aside class="about-profile">
            <div class="about-profile__photo">
              <img src="{portrait_img}" alt="" width="480" height="600" decoding="async" />
            </div>
            <div class="about-profile__body">
              <h2>{OWNER}</h2>
              <p class="about-profile__role">Inhaber · {BUSINESS}</p>
              <ul class="about-profile__contact">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.6 10.8a13 13 0 0 0 5.7 5.7l2.1-2.1a1 1 0 0 1 1-.24c1.1.37 2.2.57 3.4.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A16 16 0 0 1 3 4a1 1 0 0 1 1-1h3.4a1 1 0 0 1 1 1c0 1.2.2 2.4.6 3.5a1 1 0 0 1-.24 1Z"/></svg><a href="tel:+491773145839">{PHONE_DISPLAY}</a></li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="5.5" width="17" height="13" rx="1.5"/><path d="m4 7 8 6 8-6"/></svg><a href="mailto:{EMAIL}">{EMAIL}</a></li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s6-5.2 6-10a6 6 0 1 0-12 0c0 4.8 6 10 6 10Z"/><circle cx="12" cy="11" r="2.2"/></svg><span>{ADDRESS}</span></li>
            </ul>
            </div>
          </aside>

          <div class="about-editorial">
            <blockquote class="about-bio">
              <span class="about-bio__mark" aria-hidden="true">„</span>
              Schon als Kind interessierte mich die Fahrzeugtechnik – von neuen Modellen bis zu Klassikern.
              Nach meiner Ausbildung im VAG-Konzern bei einem VW- und Audi-Autohaus und dem Kfz-Meister folgte
              die Tätigkeit bei TÜV NORD als Fahrzeugbewerter und Unfallschadengutachter. Heute steht eine
              persönliche, unabhängige und gründliche Beratung im Mittelpunkt.
            </blockquote>

            <div class="about-details">
              <div class="about-detail">
                <div class="about-detail__head">
                  <span class="about-detail__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="8" width="17" height="12" rx="1.5"/><path d="M8 8V6.5A1.5 1.5 0 0 1 9.5 5h5A1.5 1.5 0 0 1 16 6.5V8"/><path d="M3.5 13h17"/></svg></span>
                  <h3>Beruflicher Werdegang (Auszug)</h3>
                </div>
                <ul>
                  <li>TÜV NORD Autoservice, Paderborn — Kfz-Sachverständiger / Fahrzeugbewerter und Unfallschadengutachter (frühere Tätigkeit, keine aktuelle Partnerschaft mit TÜV NORD)</li>
                  <li>Grafschafter Autozentrale VW/Audi Partner, Nordhorn — Ausbildung Kfz-Mechatroniker</li>
                </ul>
              </div>

              <div class="about-detail">
                <div class="about-detail__head">
                  <span class="about-detail__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8.5" r="4.5"/><path d="M8.2 13 7 20l5-2.5L17 20l-1.2-7"/><path d="M9 18.5h6"/></svg></span>
                  <h3>Qualifikationen</h3>
                </div>
                <ul>
                  <li>Kfz-Meister</li>
                  <li>Sachverständiger für Kraftfahrzeuge</li>
                  <li>Mitglied im Verband freier Kraftfahrzeug-Sachverständiger e. V. (VfK)</li>
                </ul>
              </div>
            </div>

            <div class="about-note">
              <span class="about-note__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 5 6v6c0 4.2 3 7.5 7 9 4-1.5 7-4.8 7-9V6l-7-3Z"/><path d="m9.5 12 1.8 1.8L15 10.1"/></svg></span>
              <p>Kfz-Meister und Sachverständiger für Kraftfahrzeuge. Genaue Bezeichnungen und Nachweise gemäß Originalunterlagen stellen wir auf Anfrage zur Verfügung. Ein Gutachten schafft Klarheit, wenn Sachverhalte komplex sind. Unabhängigkeit, fachliche Sorgfalt und transparente Dokumentation stehen im Mittelpunkt unserer Arbeit.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="about-values about-values--band" aria-labelledby="about-values-title">
        <div class="about-page__inner about-values__inner">
          <header class="about-values__header">
            <h2 class="about-values__title" id="about-values-title">Wofür SESA steht</h2>
            <span class="about-values__rule" aria-hidden="true"></span>
          </header>
          <div class="about-values__grid">
            <article class="about-value">
              <span class="about-value__icon" aria-hidden="true">{lucide_svg("scale")}</span>
              <div class="about-value__copy">
                <h3>Unabhängig</h3>
                <p>Objektive Bewertungen ohne Hersteller- oder Werkstattbindung.</p>
              </div>
            </article>
            <article class="about-value">
              <span class="about-value__icon" aria-hidden="true">{lucide_svg("file-check")}</span>
              <div class="about-value__copy">
                <h3>Gründlich</h3>
                <p>Detaillierte Analyse und transparente Dokumentation.</p>
              </div>
            </article>
            <article class="about-value">
              <span class="about-value__icon" aria-hidden="true">{lucide_svg("user-round")}</span>
              <div class="about-value__copy">
                <h3>Persönlich</h3>
                <p>Direkter Kontakt und individuelle Betreuung Ihrer Anliegen.</p>
              </div>
            </article>
          </div>
          <aside class="about-values__cta">
            <div class="about-values__cta-copy">
              <span class="about-values__cta-icon" aria-hidden="true">{lucide_svg("phone")}</span>
              <p>Fragen oder Gutachten nötig? Ich bin persönlich für Sie da.</p>
            </div>
            <a class="btn btn-primary" href="{kontakt}">Kontakt aufnehmen</a>
          </aside>
        </div>
      </section>
    </div>"""


def hero_preload_head() -> str:
    return "\n".join(
        f'    <link rel="preload" as="image" href="{src.split("?")[0]}" />' for src, _ in HERO_SLIDES
    )


def home_page_body() -> str:
    beratung = whatsapp_url(WHATSAPP_TEXT_BERATUNG)
    slides = hero_slides_html()
    return f"""
    <section class="hero hero--home hero--slideshow hero--centered" data-section="hero" data-hero-slider aria-label="SESA Kfz-Sachverständigenbüro">
      <div class="hero__slides" aria-hidden="true">
{slides}
      </div>
      <div class="hero__overlay" aria-hidden="true"></div>
      <div class="hero__inner hero__inner--centered">
        <div class="hero__content hero__content--centered">
          <p class="hero__eyebrow">Unabhängiger Kfz-Sachverständiger</p>
          <h1 class="hero__title">Kfz-Gutachter für Unfall, Bewertung &amp; Begutachtung</h1>
          <p class="hero__region">Nordrhein-Westfalen · Niedersachsen · Hessen · Hamburg · Bremen</p>
          <p class="hero__services">Unfallgutachten · Fahrzeugbewertung · Wohnmobile · Oldtimer.</p>
          <p class="hero__description">Unverschuldeter Unfall? Wir dokumentieren Schäden fachgerecht und schaffen eine belastbare Grundlage für die weitere Schadenregulierung.</p>
          <ul class="hero-trust hero-trust--centered" role="list">
            <li class="hero-trust__item">
              <span class="hero-trust__icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9.5 12 1.8 1.8L15 10.1"/></svg>
              </span>
              <div class="hero-trust__copy">
                <strong>Unabhängig</strong>
                <span>Eigenes Sachverständigenbüro ohne Weisungsbindung</span>
              </div>
            </li>
            <li class="hero-trust__item">
              <span class="hero-trust__icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 17h14l-1.2-5.5a2 2 0 0 0-2-1.5H8.2a2 2 0 0 0-2 1.5L5 17Z"/><path d="M7 17v2M17 17v2"/><circle cx="7.5" cy="19.5" r="1.5"/><circle cx="16.5" cy="19.5" r="1.5"/><path d="M5 11h14l1-4H4l1 4Z"/></svg>
              </span>
              <div class="hero-trust__copy">
                <strong>Mobil vor Ort</strong>
                <span>Bei Ihnen, in der Werkstatt oder am Fahrzeugstandort</span>
              </div>
            </li>
            <li class="hero-trust__item">
              <span class="hero-trust__icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>
              </span>
              <div class="hero-trust__copy">
                <strong>24–48 Std.</strong>
                <span>{GUTACHTEN_TIMING}</span>
              </div>
            </li>
          </ul>
          <div class="hero-actions hero-actions--centered">
            <div class="hero-actions__row">
              <a class="btn btn-primary hero-cta-primary" href="tel:{PHONE_LINK}">Jetzt anrufen</a>
              <a class="btn btn-secondary btn-wa hero-cta-secondary" href="{beratung}" target="_blank" rel="noopener noreferrer">Per WhatsApp schreiben</a>
            </div>
            <a class="btn btn-tertiary hero-cta-tertiary" href="schaden-melden.html">Schaden online melden</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section home-section home-expert" data-section="expert" id="expertise">
      <div class="expert-spotlight expert-spotlight--premium expert-spotlight--composed">
        <div class="expert-spotlight__media">
          <img class="expert-spotlight__photo" src="assets/portrait-placeholder.png" alt="Porträtfoto — {OWNER}" loading="lazy" />
        </div>
        <div class="expert-spotlight__content">
          <h2 class="expert-spotlight__title">
            <span class="kicker">Qualifikation &amp; Erfahrung</span>
            <span class="expert-spotlight__name">{OWNER}</span>
          </h2>
          <p class="expert-spotlight__role">Inhaber · {BUSINESS}</p>
          <ul class="expert-credentials">
            <li>Kfz-Meister</li>
            <li>Sachverständiger für Kraftfahrzeuge</li>
            <li>Erfahrung als Fahrzeugbewerter und Unfallschadengutachter</li>
            <li>Frühere Tätigkeit bei TÜV NORD — keine aktuelle Partnerschaft</li>
          </ul>
          <a class="btn btn-outline-copper" href="ueber-uns.html">Mehr über SESA</a>
        </div>
      </div>
    </section>

    <section class="section content-light home-section home-services" data-section="services" id="leistungen">
      <header class="section-header section-header--center">
        <h2>Leistungen im Überblick</h2>
        <p class="section-intro">Von der Schadenaufnahme bis zur Wertermittlung — fachlich fundiert und persönlich betreut.</p>
      </header>
      <div class="service-grid">
        <article class="service-card">
          <div class="service-card__media"><img src="{SERVICE_THUMBS["unfall"]}" alt="Schadendetail am Fahrzeug" loading="lazy" /></div>
          <div class="service-card__body">
            {service_card_icon("unfall")}
            <h3>Unfallgutachten</h3>
            <p>Unabhängige Schadenaufnahme als technische Grundlage für die Regulierung.</p>
            <a class="service-card__link" href="leistungen/unfallgutachten.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="{SERVICE_THUMBS["bewertung"]}" alt="Werkzeug und Dokumentation zur Fahrzeugbewertung" loading="lazy" /></div>
          <div class="service-card__body">
            {service_card_icon("bewertung")}
            <h3>Fahrzeugbewertung</h3>
            <p>Marktwert, Wiederbeschaffungswert oder Fahrzeugwert je nach Anlass.</p>
            <a class="service-card__link" href="leistungen/fahrzeugbewertung.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="{SERVICE_THUMBS["wohnmobile"]}" alt="Wohnmobil auf einer Landstraße" loading="lazy" /></div>
          <div class="service-card__body">
            {service_card_icon("wohnmobile")}
            <h3>Wohnmobile &amp; Wohnwagen</h3>
            <p>Begutachtung und Bewertung von Freizeitfahrzeugen.</p>
            <a class="service-card__link" href="leistungen/wohnmobile.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="{SERVICE_THUMBS["oldtimer"]}" alt="Oldtimer in der Werkstatt" loading="lazy" /></div>
          <div class="service-card__body">
            {service_card_icon("oldtimer")}
            <h3>Oldtimer &amp; Youngtimer</h3>
            <p>Zustand, Originalität und Wertermittlung für Klassiker.</p>
            <a class="service-card__link" href="leistungen/oldtimer-youngtimer.html">Mehr erfahren</a>
          </div>
        </article>
      </div>
      <p class="section-footer-link"><a href="leistungen/index.html">Alle Leistungen ansehen</a></p>
    </section>

    <section class="section home-section home-process" data-section="process" id="ablauf">
      <header class="section-header section-header--center">
        <h2>In vier Schritten zum Gutachten</h2>
      </header>
      <div class="process-flow" data-process-flow>
        <ol class="process-flow__track" role="list">
{process_flow_unit("01", "Kontakt", "Kontaktaufnahme und Erstberatung", True)}
{process_flow_unit("02", "Begutachtung", "Schadenaufnahme am Fahrzeugstandort", True)}
{process_flow_unit("03", "Dokumentation", GUTACHTEN_TIMING_CARD, True)}
{process_flow_unit("04", "Besprechung", "Persönliche Betreuung bei Rückfragen", False)}
        </ol>
      </div>
    </section>

    <section class="section content-light home-section home-trust" data-section="trust" id="warum-sesa">
      <header class="section-header section-header--center">
        <h2 class="home-trust__title">Warum SESA?</h2>
        <p class="section-intro">Ihr Vorteil auf einen Blick</p>
      </header>
      <div class="grid-3 trust-grid">
        <article class="panel trust-panel">
          <h3>Qualifikation</h3>
          <p class="muted">{QUAL_TRUST_BLURB}</p>
        </article>
        <article class="panel trust-panel">
          <h3>Erfahrung</h3>
          <p class="muted">Berufliche Tätigkeit u. a. als Fahrzeugbewerter und Unfallschadengutachter — frühere Tätigkeit bei TÜV NORD, keine aktuelle Partnerschaft.</p>
        </article>
        <article class="panel trust-panel">
          <h3>Persönliche Betreuung</h3>
          <p class="muted">Ein Ansprechpartner von der ersten Kontaktaufnahme bis zur Besprechung des Gutachtens.</p>
        </article>
      </div>
    </section>"""

NAV = [
    ("Startseite", "index.html"),
    ("Leistungen", "leistungen/index.html"),
    ("Über uns", "ueber-uns.html"),
    ("Ratgeber", "ratgeber/index.html"),
    ("Kontakt", "kontakt.html"),
]

SERVICE_LINKS = [
    ("Alle Leistungen", "leistungen/index.html"),
    ("Unfallgutachten", "leistungen/unfallgutachten.html"),
    ("Fahrzeugbewertung", "leistungen/fahrzeugbewertung.html"),
    ("Oldtimer & Youngtimer", "leistungen/oldtimer-youngtimer.html"),
    ("Wohnmobile & Wohnwagen", "leistungen/wohnmobile.html"),
    ("Beweissicherung", "leistungen/beweissicherung.html"),
    ("Privatgutachten", "leistungen/privatgutachten.html"),
    ("Kostenvoranschlag", "leistungen/kostenvoranschlag.html"),
    ("Versicherungsgutachten", "leistungen/versicherungsgutachten.html"),
    ("Beratung", "leistungen/beratung.html"),
    ("Ortstermine", "leistungen/ortstermine.html"),
]


def prefix(depth: int) -> str:
    return "../" * depth if depth else "./"


def services_dropdown(depth: int, active: str) -> str:
    p = prefix(depth)
    items = []
    for label, href in SERVICE_LINKS:
        full = p + href
        items.append(f"<li><a href=\"{full}\">{label}</a></li>")
    submenu = "\n".join(items)
    return f"""<li class="menu-item menu-item--services">
      <details class="menu-accordion">
        <summary class="menu-accordion__summary" aria-expanded="false">
          <span class="menu-accordion__label">Leistungen</span>
          <span class="menu-caret" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 12" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" d="M2.5 4.5 6 8 9.5 4.5"/></svg></span>
        </summary>
        <ul class="menu-dropdown">
{submenu}
        </ul>
      </details>
    </li>"""


def nav_links(depth: int, active: str) -> str:
    targets = [
        ("HOME", "index.html", False),
        ("Über uns", "ueber-uns.html", False),
        (None, None, True),
        ("GUTACHTEN", "ratgeber/index.html", False),
        ("Kontakt", "kontakt.html", False),
    ]
    parts = []
    for label, href, is_services in targets:
        if is_services:
            parts.append(services_dropdown(depth, active))
            continue
        full = prefix(depth) + href
        cur = " aria-current=\"page\"" if active == label else ""
        parts.append(f"<li><a href=\"{full}\"{cur}>{label}</a></li>")
    return "\n".join(parts)


def header_contact(depth: int) -> str:
    p = prefix(depth)
    return f"""
    <div class="header-contact">
      <a class="header-phone" href="tel:{PHONE_LINK}">
        {PHONE_ICON_SVG}
        <span>{PHONE_DISPLAY}</span>
      </a>
      <a class="btn btn-inquiry" href="{p}kontakt.html">Anfrage</a>
    </div>"""


def consent_banner(depth: int) -> str:
    p = prefix(depth)
    return f"""
    <div class="consent-backdrop" data-consent-backdrop hidden>
      <div class="consent-modal" role="dialog" aria-labelledby="consent-title" aria-modal="true">
        <div class="consent-panel" data-consent-main>
          <h2 id="consent-title">Datenschutzeinstellungen</h2>
          <div class="consent-text consent-text--compact">
            <p>Wir verwenden Cookies, um die Website bereitzustellen und Ihre Einwilligung zu speichern. Optional können Google Maps auf der Kontaktseite eingebunden werden. Details in der <a href="{p}datenschutz.html">Datenschutzerklärung</a>.</p>
          </div>
          <div class="consent-actions">
            <button type="button" class="consent-btn consent-btn-primary" data-consent-accept-all>Alle akzeptieren</button>
            <button type="button" class="consent-btn consent-btn-secondary" data-consent-decline>Ohne Einwilligung fortfahren</button>
          </div>
          <button type="button" class="consent-customize-link" data-consent-customize>Einstellungen anpassen</button>
        </div>
        <div class="consent-panel" data-consent-detail hidden>
          <h2>Einstellungen anpassen</h2>
          <div class="consent-text consent-text--detail">
            <p>Im Detail können Sie festlegen, welche optionalen Dienste wir einbinden dürfen:</p>
            <ul>
              <li>Speichern Ihrer Einwilligung (technisch erforderlich)</li>
              <li>Google Maps auf der Kontaktseite (optional)</li>
            </ul>
          </div>
          <div class="consent-option">
            <div>
              <strong>Technisch erforderlich</strong>
              <p class="muted">Speichert Ihre Auswahl (Einwilligung). Kann nicht deaktiviert werden.</p>
            </div>
            <span class="consent-badge">Immer aktiv</span>
          </div>
          <div class="consent-option">
            <div>
              <strong>Google Maps</strong>
              <p class="muted">Kartenansicht auf der Kontaktseite. Anbieter: Google Ireland Limited.</p>
            </div>
            <label class="consent-switch">
              <input type="checkbox" data-consent-maps />
              <span class="consent-switch-ui"></span>
            </label>
          </div>
          <div class="consent-actions">
            <button type="button" class="consent-btn consent-btn-primary" data-consent-save>Auswahl speichern</button>
            <button type="button" class="consent-btn consent-btn-secondary" data-consent-back>Zurück</button>
          </div>
        </div>
      </div>
    </div>"""


def shell(
    depth: int,
    active: str,
    title: str,
    description: str,
    body: str,
    extra_head: str = "",
) -> str:
    p = prefix(depth)
    return f"""<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} — {BUSINESS}</title>
    <meta name="description" content="{description}" />
    <link rel="icon" href="{p}assets/favicon.png" type="image/png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="{p}css/styles.css?v=164" />
    {extra_head}
  </head>
  <body>
    <a class="skip" href="#main">Zum Hauptinhalt springen</a>
    <header class="header">
      <div class="nav">
        <a class="brand" href="{p}index.html">
          <span class="brand-mark-slot">
            <img class="brand-mark" src="{p}{LOGO_MONOGRAM}" width="290" height="280" alt="" />
          </span>
          <span class="brand-text">
            <span class="brand-name">SESA</span>
            <span class="brand-sub">KFZ - SACHVERSTÄNDIGENBÜRO</span>
          </span>
        </a>
        <div class="nav-divider" aria-hidden="true"></div>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Menü">
          <span class="menu-toggle__icon" aria-hidden="true"></span>
          <span class="menu-toggle__label">Menü</span>
        </button>
        <ul class="menu">{nav_links(depth, active)}</ul>
        <div class="nav-divider nav-divider-end" aria-hidden="true"></div>
        {header_contact(depth)}
      </div>
    </header>
    <main id="main">{body}</main>
    <footer class="footer">
      <div>
        <strong>{BUSINESS}</strong><br />
        Inhaber: {OWNER}<br />
        {ADDRESS}
      </div>
      <nav>
        <a href="{p}impressum.html">Impressum</a>
        <a href="{p}datenschutz.html">Datenschutz</a>
        <a href="{p}widerruf.html">Widerrufsbelehrung</a>
        <a href="{p}kontakt.html">Kontakt</a>
        <a href="#" data-consent-reopen>Cookie-Einstellungen</a>
      </nav>
      <p class="muted">Keine Rechtsberatung. Inhalte dienen der sachlichen Information.</p>
    </footer>
    {consent_banner(depth)}
    {mobile_action_bar()}
    {wa_float_widget()}
    <script src="{p}js/main.js?v=44" defer></script>
  </body>
</html>"""


def write(
    path: Path,
    depth: int,
    active: str,
    title: str,
    desc: str,
    body: str,
    extra_head: str = "",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(shell(depth, active, title, desc, body, extra_head), encoding="utf-8")
    print("wrote", path)


def page_hero(
    title: str,
    lead: str,
    img: str,
    depth: int,
    editorial: bool = False,
    extra_class: str = "",
) -> str:
    p = prefix(depth)
    if editorial:
        modifier = f" {extra_class}" if extra_class else ""
        return f"""
    <section class="page-hero page-hero--editorial{modifier}">
      <div class="page-hero__inner">
        <div class="page-hero__copy">
          <p class="kicker">SESA · Kfz-Sachverständigenbüro</p>
          <h1>{title}</h1>
          <p class="lead">{lead}</p>
        </div>
        <div class="page-hero__media">
          <img src="{p}{img}" alt="" loading="lazy" />
        </div>
      </div>
    </section>"""
    return f"""
    <section class="page-hero">
      <div>
        <p class="kicker">SESA · Kfz-Sachverständigenbüro</p>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
      </div>
      <img src="{p}{img}" alt="" loading="lazy" />
    </section>"""


def counselor_card(slug: str, title: str, description: str, icon_name: str) -> str:
    return f"""
        <article class="counselor-card">
          <a class="counselor-card__link" href="{slug}">
            <span class="counselor-card__icon" aria-hidden="true">{lucide_svg(icon_name)}</span>
            <h3 class="counselor-card__title">{title}</h3>
            <p class="counselor-card__desc">{description}</p>
            <span class="counselor-card__more">Mehr erfahren</span>
          </a>
        </article>"""


def ratgeber_index_body() -> str:
    cards = [
        (
            "nach-einem-unfall.html",
            "Was tun nach einem Unfall?",
            "Erste Schritte an der Unfallstelle.",
            "car-front",
        ),
        (
            "rechte.html",
            "Ihre Rechte nach einem unverschuldeten Unfall",
            "Informationen nach einem unverschuldeten Verkehrsunfall.",
            "shield-check",
        ),
        (
            "faq.html",
            "FAQ",
            "Häufige Fragen zum Gutachten.",
            "circle-question-mark",
        ),
    ]
    card_html = "".join(counselor_card(slug, title, description, icon_name) for slug, title, description, icon_name in cards)
    hero = page_hero(
        "Ratgeber",
        "Sachliche Informationen — keine Rechtsberatung.",
        "assets/nrw-road.png",
        1,
        editorial=True,
        extra_class="page-hero--counselor",
    )
    return f"""
    <div class="guide-index">
      {hero}
      <section class="guide-index__cards" aria-label="Ratgeber">
        <div class="guide-index__inner">
          <div class="counselor-cards">
            {card_html}
          </div>
        </div>
      </section>
    </div>"""


UNFALL_STEPS = [
    "Ruhe bewahren und Unfallstelle sichern.",
    "Bei Bedarf Polizei rufen und Beteiligte dokumentieren.",
    "Unfallort, Uhrzeit und Schäden fotografieren.",
    "Keine vorschnellen Erklärungen zur Schuld oder Schadenhöhe abgeben.",
    "Schadenfotos und Informationen an SESA senden (WhatsApp oder Telefon).",
    "Weiteres Vorgehen im persönlichen Gespräch klären.",
]


def guide_unfall_step(number: int, text: str) -> str:
    return f"""
            <li class="guide-unfall__step-item">
              <span class="guide-unfall__step-marker" aria-hidden="true">{number:02d}</span>
              <p class="guide-unfall__step-text">{text}</p>
            </li>"""


def unfall_page_body() -> str:
    left_steps = "".join(
        guide_unfall_step(index, text) for index, text in enumerate(UNFALL_STEPS[:3], start=1)
    )
    right_steps = "".join(
        guide_unfall_step(index, text) for index, text in enumerate(UNFALL_STEPS[3:], start=4)
    )
    p = prefix(1)
    return f"""
    <div class="guide-unfall">
      <section class="page-hero page-hero--editorial page-hero--unfall" aria-labelledby="unfall-title">
        <div class="page-hero__inner">
          <div class="page-hero__copy">
            <p class="kicker">SESA · Kfz-Sachverständigenbüro</p>
            <h1 id="unfall-title">Was tun nach einem Unfall?</h1>
            <span class="page-hero__rule" aria-hidden="true"></span>
            <p class="lead">Erste Schritte an der Unfallstelle.</p>
          </div>
          <div class="page-hero__media">
            <img src="{p}assets/damage-detail.png" alt="" loading="eager" decoding="async" />
          </div>
        </div>
      </section>
      <section class="guide-unfall__article" aria-label="Erste Schritte nach einem Unfall">
        <div class="guide-unfall__inner">
          <div class="guide-unfall__panel">
            <div class="guide-unfall__panel-grid">
              <ol class="guide-unfall__col guide-unfall__col--left" role="list">
                {left_steps}
              </ol>
              <div class="guide-unfall__divider" aria-hidden="true">
                <span class="guide-unfall__divider-track"></span>
              </div>
              <ol class="guide-unfall__col guide-unfall__col--right" role="list">
                {right_steps}
              </ol>
            </div>
          </div>
          <p class="guide-unfall__disclaimer"><em>Keine Rechtsberatung. Bei rechtlichen Fragen wenden Sie sich an einen Rechtsanwalt.</em></p>
        </div>
      </section>
    </div>"""


RECHTE_ROWS = [
    (
        "Freie Sachverständigenwahl",
        "Bei einem unverschuldeten Haftpflichtschaden kann grundsätzlich das Recht bestehen, einen eigenen unabhängigen Sachverständigen zu beauftragen. Ob Kosten erstattungsfähig sind, hängt vom Einzelfall ab.",
    ),
    (
        "Reparaturkosten",
        "Das Gutachten dokumentiert technisch erforderliche Reparaturmaßnahmen und voraussichtliche Kosten.",
    ),
    (
        "Wertminderung",
        "Ob eine merkantile Wertminderung vorliegt, wird im Einzelfall beurteilt.",
    ),
    (
        "Totalschaden",
        "Wiederbeschaffungswert, Restwert und Reparaturkosten werden gegenübergestellt.",
    ),
    (
        "Teilschuld",
        "Bei Mithaftung können Kosten nur anteilig erstattet werden. Die Haftungsquote sollte rechtlich geprüft werden.",
    ),
]


def guide_rechte_row(number: int, title: str, description: str) -> str:
    return f"""
              <tr>
                <td class="guide-rechte__num"><span aria-hidden="true">{number:02d}</span></td>
                <th scope="row" class="guide-rechte__title">{title}</th>
                <td class="guide-rechte__desc">{description}</td>
              </tr>"""


def rechte_page_body() -> str:
    rows = "".join(
        guide_rechte_row(index, title, description)
        for index, (title, description) in enumerate(RECHTE_ROWS, start=1)
    )
    p = prefix(1)
    return f"""
    <div class="guide-rechte">
      <section class="page-hero page-hero--editorial page-hero--rechte" aria-labelledby="rechte-title">
        <div class="page-hero__inner">
          <div class="page-hero__copy">
            <p class="kicker">SESA · Kfz-Sachverständigenbüro</p>
            <h1 id="rechte-title">Ihre Rechte nach einem unverschuldeten Unfall</h1>
            <p class="lead">Informationen nach einem unverschuldeten Verkehrsunfall.</p>
            <span class="page-hero__rule" aria-hidden="true"></span>
          </div>
          <div class="page-hero__media">
            <img src="{p}assets/workshop-tools.png" alt="" loading="eager" decoding="async" />
          </div>
        </div>
      </section>
      <section class="guide-rechte__article" aria-label="Ihre Rechte im Überblick">
        <div class="guide-rechte__inner">
          <p class="guide-rechte__intro">Die folgenden Hinweise dienen der sachlichen Information und ersetzen keine individuelle Rechtsberatung.</p>
          <div class="guide-rechte__table-wrap">
            <table class="guide-rechte__table">
              <caption class="guide-rechte__caption">Ihre Rechte nach einem unverschuldeten Unfall</caption>
              <colgroup>
                <col class="guide-rechte__col-num" />
                <col class="guide-rechte__col-title" />
                <col class="guide-rechte__col-desc" />
              </colgroup>
              <tbody>
                {rows}
              </tbody>
            </table>
          </div>
          <p class="guide-rechte__disclaimer"><em>Keine Rechtsberatung. Bei rechtlichen Fragen wenden Sie sich an einen Rechtsanwalt.</em></p>
        </div>
      </section>
    </div>"""


def service_step_item(number: int, text: str, icon_name: str) -> str:
    return f"""
            <li class="service-steps__item">
              <span class="service-steps__icon" aria-hidden="true">{lucide_svg(icon_name)}</span>
              <span class="service-steps__number">{number:02d}</span>
              <p class="service-steps__text">{text}</p>
            </li>"""


def service_steps_column(steps: list[tuple[int, str, str]]) -> str:
    items = "".join(service_step_item(number, text, icon_name) for number, text, icon_name in steps)
    return f"""
          <ol class="service-steps__col" role="list">
            {items}
          </ol>"""


def service_page_content(paragraphs: list[str], icon_names: list[str]) -> str:
    """Shared service-detail body — Editorial Steps card (all Leistungen pages)."""
    if len(icon_names) != len(paragraphs):
        raise ValueError("Each service paragraph needs a matching step icon.")

    steps = [
        (index, paragraph, icon_name)
        for index, (paragraph, icon_name) in enumerate(zip(paragraphs, icon_names), start=1)
    ]
    split_at = (len(steps) + 1) // 2
    left_col = service_steps_column(steps[:split_at])
    right_col = service_steps_column(steps[split_at:]) if split_at < len(steps) else ""
    single_col_class = " service-steps-card__grid--single" if not right_col else ""

    return f"""
    <section class="section content-light service-detail service-detail--steps" aria-label="Leistungsbeschreibung">
      <div class="service-detail__inner">
        <article class="service-steps-card">
          <div class="service-steps-card__grid{single_col_class}">
            {left_col}
            {right_col}
          </div>
          <p class="service-steps-card__note"><em>Hinweis: Diese Information ersetzt keine individuelle Rechtsberatung.</em></p>
        </article>
        <div class="service-detail__cta">
          <a class="btn btn-primary" href="../schaden-melden.html">Schaden melden</a>
          <a class="btn btn-secondary-navy" href="tel:+491773145839">Jetzt anrufen</a>
        </div>
      </div>
    </section>"""


def service_page(slug: str, title: str, lead: str, paragraphs: list[str], img: str) -> None:
    body = page_hero(title, lead, img, 1, editorial=True)
    body += service_page_content(paragraphs, SERVICE_STEP_ICONS[slug])
    write(ROOT / "leistungen" / slug, 1, "Leistungen", title, lead, body)


def main() -> None:
  # --- Startseite ---
    write(
        ROOT / "index.html",
        0,
        "HOME",
        "Kfz-Gutachter",
        "Unabhängiges Kfz-Sachverständigenbüro — Schadengutachten und Fahrzeugbewertung.",
        home_page_body(),
        hero_preload_head(),
    )

    # Leistungen overview
    write(
        ROOT / "leistungen" / "index.html",
        1,
        "Leistungen",
        "Leistungen",
        "Gutachten und Bewertungen.",
        leistungen_page_body(),
    )

    services = {
        "unfallgutachten.html": (
            "Unfallgutachten / Haftpflichtgutachten",
            "Unabhängige Schadenaufnahme nach einem Verkehrsunfall.",
            [
                "Ein Haftpflicht-Schadengutachten dokumentiert die festgestellten Schäden und kann unter anderem Reparaturkosten sowie weitere technisch und wirtschaftlich relevante Positionen erfassen.",
                "Es schafft eine fachliche Grundlage für die weitere Schadenregulierung. Bei einem unverschuldeten Haftpflichtschaden können erforderliche Sachverständigenkosten grundsätzlich zu den ersatzfähigen Schadenpositionen gehören — im Einzelfall können Abweichungen bestehen.",
                "Benötigte Unterlagen und der genaue Ablauf werden im persönlichen Gespräch besprochen.",
            ],
            "assets/damage-detail.png",
        ),
        "fahrzeugbewertung.html": (
            "Fahrzeugbewertung / Wertgutachten",
            "Ermittlung von Marktwert oder Wiederbeschaffungswert.",
            [
                "Relevant beim An- und Verkauf, für besondere Bewertungsanlässe sowie bei hochwertigen oder spezialisierten Fahrzeugen.",
                "Die Bewertung erfolgt nach dem vereinbarten Anlass und den anerkannten fachlichen Grundsätzen.",
            ],
            "assets/workshop-tools.png",
        ),
        "oldtimer-youngtimer.html": (
            "Oldtimer & Youngtimer",
            "Bewertung von Klassikern und Sammlerfahrzeugen.",
            [
                "Zustand, Originalität und Wertermittlung für Versicherung, An- und Verkauf.",
                "Es werden nur tatsächlich angewendete Bewertungsstandards genannt und dokumentiert.",
            ],
            "assets/hero-inspection.png",
        ),
        "wohnmobile.html": (
            "Wohnmobile & Wohnwagen",
            "Begutachtung von Freizeitfahrzeugen.",
            [
                "Bewertung von Fahrzeug und Aufbau, soweit im Auftrag vereinbart und fachlich abgedeckt.",
                "Feuchtigkeits- oder Dichtigkeitsmessungen nur bei entsprechender Qualifikation und Auftrag.",
            ],
            SERVICE_THUMBS["wohnmobile"],
        ),
        "beweissicherung.html": (
            "Beweissicherung",
            "Dokumentation von Spuren, Schäden oder Mängeln.",
            [
                "Sinnvoll bevor das Fahrzeug repariert, verändert oder weiter genutzt wird.",
                "Die Dokumentation dient der technischen Beweissicherung und kann als Grundlage in außergerichtlichen und gerichtlichen Auseinandersetzungen dienen.",
            ],
            "assets/damage-detail.png",
        ),
        "privatgutachten.html": (
            "Privatgutachten",
            "Unabhängige Begutachtung im Privatauftrag.",
            [
                "Etwa bei Streitigkeiten nach Reparaturen oder Mängeln nach einem Fahrzeugkauf.",
                "Kosten trägt grundsätzlich der Auftraggeber.",
            ],
            "assets/workshop-tools.png",
        ),
        "kostenvoranschlag.html": (
            "Kostenvoranschlag",
            "Vereinfachte Ermittlung voraussichtlicher Reparaturkosten.",
            [
                "Wenn ein vollständiges Gutachten im konkreten Fall nicht erforderlich ist.",
                "Ein Kostenvoranschlag konzentriert sich hauptsächlich auf Reparaturkosten; ein Schadengutachten dokumentiert darüber hinaus weitere relevante Positionen.",
            ],
            "assets/workshop-tools.png",
        ),
        "versicherungsgutachten.html": (
            "Versicherungsgutachten / Kaskoschäden",
            "Begutachtung von Kaskoschäden.",
            [
                "Soweit diese Leistung im konkreten Auftrag angeboten und vereinbart wird.",
                "Bei Kaskoschäden entscheidet die eigene Versicherung über die Kostenübernahme.",
            ],
            "assets/damage-detail.png",
        ),
        "beratung.html": (
            "Beratung",
            "Fachliche Ersteinschätzung und Orientierung.",
            [
                "Unterstützung bei der Wahl des sinnvollen Vorgehens sowie Beratung rund um Kraftfahrzeuge.",
                "Erste Orientierung per Telefon, E-Mail oder WhatsApp — ersetzt keine vollständige Begutachtung.",
            ],
            "assets/hero-inspection.png",
        ),
        "ortstermine.html": (
            "Ortstermine",
            "Begutachtung am Fahrzeugstandort.",
            [
                "Zu Hause, in der Werkstatt, auf dem Abschlepphof oder an einem anderen geeigneten Ort.",
                "Kurzfristige Termine sind je nach Standort, Auslastung und Art des Auftrags möglich.",
            ],
            "assets/nrw-road.png",
        ),
    }
    for slug, (title, lead, paras, img) in services.items():
        service_page(slug, title, lead, paras, img)

    # Über uns
    write(
        ROOT / "ueber-uns.html",
        0,
        "Über uns",
        "Über uns",
        f"{OWNER} — unabhängiger Kfz-Sachverständiger in Paderborn.",
        about_page_body(0),
    )

    # Ratgeber
    write(
        ROOT / "ratgeber" / "index.html",
        1,
        "GUTACHTEN",
        "Ratgeber",
        "Unfallhilfe und FAQ.",
        ratgeber_index_body(),
    )

    write(
        ROOT / "ratgeber" / "nach-einem-unfall.html",
        1,
        "GUTACHTEN",
        "Nach einem Unfall",
        "Erste Schritte.",
        unfall_page_body(),
    )

    write(
        ROOT / "ratgeber" / "rechte.html",
        1,
        "GUTACHTEN",
        "Ihre Rechte",
        "Informationen nach Unfall.",
        rechte_page_body(),
    )

    faq_items = [
        ("Was kostet ein Gutachten?", "Bei einem unverschuldeten Haftpflichtschaden können erforderliche Sachverständigenkosten grundsätzlich zu den ersatzfähigen Schadenpositionen gehören. Bei Bagatellschäden oder Mithaftung können Abweichungen bestehen. Andere Gutachten werden je nach Auftrag berechnet."),
        ("Wer bezahlt das Gutachten?", "Bei unverschuldetem Haftpflichtschaden können Kosten grundsätzlich vom Schädiger bzw. dessen Haftpflichtversicherung zu erstatten sein. Bei Kaskoschäden entscheidet die eigene Versicherung."),
        ("Wie schnell bekomme ich einen Termin?", "Kurzfristige Termine sind je nach Standort, Auslastung und Auftrag möglich."),
        ("Wie lange dauert die Erstellung?", f"{GUTACHTEN_TIMING} — abhängig vom Schadenumfang."),
        ("Darf ich den Gutachter selbst wählen?", "Bei unverschuldetem Haftpflichtschaden besteht grundsätzlich die Möglichkeit zur freien Wahl. Bei kleinen Schäden und Kaskoschäden gelten Besonderheiten."),
        ("Kann ich Fotos per WhatsApp schicken?", "Ja, für eine erste Orientierung. Je nach Schaden ersetzt dies keine vollständige Begutachtung."),
    ]
    faq_body = page_hero("FAQ", "Häufige Fragen zum Gutachten.", "assets/workshop-tools.png", 1)
    faq_body += "<section class=\"section content-light faq\">"
    for q, a in faq_items:
        faq_body += f"<details><summary>{q}</summary><p class=\"muted\">{a}</p></details>"
    faq_body += "</section>"
    write(ROOT / "ratgeber" / "faq.html", 1, "GUTACHTEN", "FAQ", "Häufige Fragen.", faq_body)

    # Kontakt
    kontakt = page_hero("Kontakt", "Telefon, E-Mail, Anschrift und Kartenansicht.", "assets/hero-inspection.png", 0)
    kontakt += """
    <section class="section content-light split">
      <div>
        <div class="portrait-card">
          <img class="portrait" src="assets/portrait-placeholder.png" alt="Porträtfoto Platzhalter" />
          <h2>""" + OWNER + """</h2>
          <ul class="contact-list">
            <li>Telefon: <a href="tel:+491773145839">""" + PHONE_DISPLAY + """</a></li>
            <li>E-Mail: <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></li>
            <li>WhatsApp: <a href="schaden-melden.html">Schaden melden</a></li>
            <li>""" + ADDRESS + """</li>
          </ul>
          <p class="muted">Öffnungszeiten: nach Vereinbarung</p>
        </div>
      </div>
      <div>
        <h2>Standort</h2>
        <div class="map-wrap" data-map>
          <p class="muted">Karte wird nach Zustimmung geladen.<br /><button class="btn" type="button" data-load-map>Karte anzeigen</button></p>
        </div>
        <p class="muted"><a href="https://www.google.com/maps?q=Pohlweg+76,+33098+Paderborn" rel="noopener noreferrer" target="_blank">Route in Google Maps öffnen</a></p>
      </div>
    </section>"""
    write(ROOT / "kontakt.html", 0, "Kontakt", "Kontakt", "Kontakt und Anfahrt.", kontakt)

    # Schaden melden
    schaden = page_hero("Schaden melden", "Kurze Angaben — Weiterleitung an WhatsApp.", "assets/damage-detail.png", 0)
    schaden += """
    <section class="section content-light">
      <form id="schaden-form" class="panel">
        <label for="unfallort">Unfallort / Standort des Fahrzeugs (Pflichtfeld)</label>
        <input id="unfallort" name="unfallort" required placeholder="Adresse, PLZ/Ort oder Werkstatt" />
        <button class="btn" type="button" data-geo>Standort übernehmen (Browser)</button>
        <p class="muted">Standortübernahme nur mit Ihrer Einwilligung — siehe Datenschutzerklärung.</p>
        <fieldset class="choice">
          <legend>Wer hat den Unfall verursacht?</legend>
          <label><input type="radio" name="verursacher" value="Ich" required /> Ich</label>
          <label><input type="radio" name="verursacher" value="Jemand anderes" /> Jemand anderes</label>
        </fieldset>
        <label for="hinweis">Kurze Hinweise (optional)</label>
        <textarea id="hinweis" rows="4" placeholder="z. B. Kennzeichen, Kurzbeschreibung"></textarea>
        <button class="btn btn-solid" type="submit">Weiter zu WhatsApp</button>
        <p class="muted">Fotos können Sie direkt in WhatsApp senden. Kein Datei-Upload auf dieser Website.</p>
      </form>
    </section>"""
    write(ROOT / "schaden-melden.html", 0, "Kontakt", "Schaden melden", "Schaden per WhatsApp melden.", schaden)

    # Legal pages - Impressum
    impressum = """
    <section class="section content-light legal">
      <h1>Impressum</h1>
      <p>Angaben gemäß § 5 TMG</p>
      <p><strong>""" + BUSINESS + """</strong><br />
      Inhaber: """ + OWNER + """<br />
      """ + ADDRESS + """</p>
      <p><strong>Kontakt</strong><br />
      Telefon: <a href="tel:+491773145839">""" + PHONE_DISPLAY + """</a><br />
      E-Mail: <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
      <p><strong>Berufsbezeichnung</strong><br />
      Kfz-Sachverständiger / Kraftfahrzeugsachverständiger (Deutschland)</p>
      <p><strong>Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV</strong><br />
      """ + OWNER + """, """ + ADDRESS + """</p>
      <p class="muted">Umsatzsteuer-Identifikationsnummer und weitere registerrechtliche Angaben werden ergänzt, sobald vorhanden.</p>
      <h2>Haftung für Inhalte</h2>
      <p>Als Diensteanbieter sind wir gemäß § 7 Abs. 1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.</p>
      <h2>Haftung für Links</h2>
      <p>Unser Angebot enthält Links zu externen Websites Dritter. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter verantwortlich.</p>
      <h2>Urheberrecht</h2>
      <p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht.</p>
    </section>"""
    write(ROOT / "impressum.html", 0, "Kontakt", "Impressum", "Impressum.", impressum)

    # Datenschutz — vollständig gemäß bereitgestelltem PDF + Web-Ergänzungen
    datenschutz = """
    <section class="section content-light legal">
      <h1>Datenschutzerklärung</h1>
      <p>Informationen über die Verarbeitung personenbezogener Daten gemäß Art. 13, 14 und 21 DSGVO</p>
      <h2>1. Name und Kontaktdaten des Verantwortlichen</h2>
      <p>Verantwortlicher: """ + BUSINESS + """<br />
      Inhaber: """ + OWNER + """<br />
      Anschrift: """ + ADDRESS + """<br />
      Telefon: """ + PHONE_DISPLAY + """<br />
      E-Mail: <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
      <h2>2. Allgemeine Hinweise zur Datenverarbeitung</h2>
      <p>Wir nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung. Wenn Sie unsere Website nutzen oder uns mit der Erstellung eines KFZ-Schadengutachtens beauftragen, werden verschiedene personenbezogene Daten erhoben. Personenbezogene Daten sind Daten, mit denen Sie persönlich identifiziert werden können.</p>
      <h2>3. Datenerfassung auf unserer Website (Server-Log-Dateien)</h2>
      <p>Der Provider der Seiten erhebt und speichert automatisch Informationen in sogenannten Server-Log-Dateien, die Ihr Browser automatisch an uns übermittelt. Dies sind:</p>
      <ul>
        <li>Browsertyp und Browserversion sowie verwendetes Betriebssystem</li>
        <li>Referrer URL (die zuvor besuchte Seite) und Hostname des zugreifenden Rechners (IP-Adresse)</li>
        <li>Uhrzeit der Serveranfrage</li>
      </ul>
      <p>Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen. Die Erfassung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Der Websitebetreiber hat ein berechtigtes Interesse an der technisch fehlerfreien Darstellung und der Optimierung seiner Website.</p>
      <h2>4. Kontaktaufnahme per E-Mail, Telefon oder Anfragen</h2>
      <p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, wird Ihre Anfrage inklusive aller daraus hervorgehenden personenbezogenen Daten (z. B. Name, Telefonnummer, E-Mail-Adresse, Anliegen) zum Zwecke der Bearbeitung Ihres Anliegens bei uns gespeichert und verarbeitet.</p>
      <p>Die Verarbeitung dieser Daten erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Erfüllung eines Vertrags zusammenhängt oder zur Durchführung vorvertraglicher Maßnahmen erforderlich ist. In allen übrigen Fällen beruht die Verarbeitung auf unserem berechtigten Interesse an der effektiven Bearbeitung der an uns gerichteten Anfragen (Art. 6 Abs. 1 lit. f DSGVO) oder auf Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
      <h2>5. Datenverarbeitung im Rahmen der Erstellung von Schadengutachten</h2>
      <p>Im Rahmen der Beauftragung zur Erstellung eines KFZ-Schadengutachtens erheben und verarbeiten wir personenbezogene Daten des Auftraggebers, Fahrzeughalters, Fahrers sowie ggf. von Unfallgegnern und Zeugen. Hierzu gehören insbesondere:</p>
      <ul>
        <li>Stammdaten (Name, Anschrift, Kontaktdaten)</li>
        <li>Fahrzeug- und Auftragsdaten (Amtliches Kennzeichen, Fahrgestellnummer, Vorsteuerabzugsberechtigung)</li>
        <li>Schadensdaten (Schadentag, Schadensort, Schadennummer, Hergang)</li>
        <li>Versicherungs- und Geschäftsdaten (Versicherungsgesellschaft, Versicherungsnummer, Aktenzeichen)</li>
      </ul>
      <h3>Weitergabe von Daten zur Schadenregulierung</h3>
      <p>Zum Zwecke der ordnungsgemäßen Erstellung des Schadengutachtens sowie zur zügigen Abwicklung und Regulierung des Schadensfalls übermitteln wir die erforderlichen personenbezogenen Daten an folgende Beteiligte:</p>
      <ul>
        <li>Die von Ihnen beauftragte Reparaturwerkstatt</li>
        <li>Die von Ihnen beauftragte Anwaltskanzlei</li>
        <li>Die für den Schadenfall zuständige und regulierungspflichtige Versicherung</li>
      </ul>
      <p>Rechtsgrundlagen der Datenweitergabe: Die Übermittlung erfolgt zur Erfüllung des Vertragsverhältnisses bzw. Durchführung vorvertraglicher Maßnahmen gem. Art. 6 Abs. 1 lit. b DSGVO sowie auf Grundlage Ihrer ausdrücklich erteilten schriftlichen Datenschutz-Einwilligung gem. Art. 6 Abs. 1 lit. a DSGVO.</p>
      <h2>6. Speicherdauer</h2>
      <p>Soweit innerhalb dieser Datenschutzerklärung keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck für die Datenverarbeitung entfällt. Wenn Sie ein berechtigtes Löschersuchen geltend machen oder eine Einwilligung zur Datenverarbeitung widerrufen, werden Ihre Daten gelöscht, sofern wir keine anderen rechtlich zulässigen Gründe für die Speicherung Ihrer personenbezogenen Daten haben (z. B. steuer- oder handelsrechtliche Aufbewahrungsfristen nach § 147 AO oder § 257 HGB von bis zu 10 Jahren).</p>
      <h2>7. Rechte der betroffenen Personen</h2>
      <p>Sie haben im Rahmen der geltenden gesetzlichen Bestimmungen jederzeit folgende Rechte:</p>
      <ul>
        <li><strong>Auskunftsrecht (Art. 15 DSGVO):</strong> Sie haben das Recht, jederzeit unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten.</li>
        <li><strong>Recht auf Berichtigung (Art. 16 DSGVO):</strong> Sie haben das Recht, die Berichtigung unrichtiger oder Vervollständigung Ihrer bei uns gespeicherten Daten zu verlangen.</li>
        <li><strong>Recht auf Löschung (Art. 17 DSGVO):</strong> Sie haben das Recht, die Löschung Ihrer personenbezogenen Daten zu verlangen, soweit nicht gesetzliche Pflichten oder berechtigte Interessen dem entgegenstehen.</li>
        <li><strong>Recht auf Einschränkung der Verarbeitung (Art. 18 DSGVO):</strong> Sie haben das Recht, die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen.</li>
        <li><strong>Recht auf Datenübertragbarkeit (Art. 20 DSGVO):</strong> Sie haben das Recht, Daten, die wir auf Grundlage Ihrer Einwilligung oder in Erfüllung eines Vertrags automatisiert verarbeiten, an sich oder an einen Dritten in einem gängigen, maschinenlesbaren Format aushändigen zu lassen.</li>
        <li><strong>Widerruf Ihrer Einwilligung (Art. 7 Abs. 3 DSGVO):</strong> Sie können eine erteilte Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen (per E-Mail an """ + EMAIL + """). Die Rechtmäßigkeit der bis zum Widerruf erfolgten Datenverarbeitung bleibt unberührt.</li>
        <li><strong>Beschwerderecht bei der Aufsichtsbehörde (Art. 77 DSGVO):</strong> Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW), Kavalleriestr. 2-4, 40213 Düsseldorf.</li>
      </ul>
      <h2>8. Datensicherheit</h2>
      <p>Diese Seite nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte eine SSL- bzw. TLS-Verschlüsselung. Zudem setzen wir geeignete technische und organisatorische Sicherheitsmaßnahmen (TOM) ein, um Ihre Daten gegen unbefugten Zugriff Dritter, Verlust oder Manipulation zu schützen.</p>
      <h2>9. WhatsApp-Kontakt (Ergänzung für diese Website)</h2>
      <p>Über den WhatsApp-Button auf allen Seiten sowie auf der Seite „Schaden melden“ können Sie per Link zu WhatsApp (Meta Platforms Ireland Ltd.) eine vorbefüllte Nachricht senden (z. B. Beratung oder Schadenmeldung). Dabei werden Sie auf die Dienste von WhatsApp umgeleitet. Es gelten die Datenschutzbestimmungen von WhatsApp/Meta. Übermitteln Sie nur die für die Erstinformation erforderlichen Daten. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO (Anbahnung/Erfüllung) bzw. Art. 6 Abs. 1 lit. a DSGVO (Einwilligung durch Nutzung des Links).</p>
      <h2>10. Google Maps (Ergänzung für diese Website)</h2>
      <p>Auf der Kontaktseite kann nach Ihrer Einwilligung eine Kartenansicht von Google Maps eingebunden werden. Anbieter: Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Beim Laden der Karte können personenbezogene Daten (insbesondere IP-Adresse) an Google übermittelt werden. Rechtsgrundlage: Art. 6 Abs. 1 lit. a DSGVO. Sie können die Einwilligung jederzeit widerrufen, indem Sie die Karte nicht laden oder gespeicherte Einwilligungen in Ihrem Browser löschen.</p>
      <h2>11. Standortübernahme im Browser (Ergänzung für diese Website)</h2>
      <p>Wenn Sie auf „Standort übernehmen“ klicken, fragt Ihr Browser einmalig Ihren Standort ab. Die Koordinaten werden nur in das Formularfeld auf Ihrem Gerät eingetragen und nicht auf unseren Server übertragen. Rechtsgrundlage: Art. 6 Abs. 1 lit. a DSGVO.</p>
      <p class="muted">Stand der Datenschutzerklärung: August 2026</p>
    </section>"""
    write(ROOT / "datenschutz.html", 0, "Kontakt", "Datenschutz", "Datenschutzerklärung.", datenschutz)

    widerruf = """
    <section class="section content-light legal">
      <h1>Widerrufsbelehrung</h1>
      <p>Rechtssichere Widerrufsbelehrung für Kfz-Gutachten — konform mit BGB und EGBGB Fernabsatzrecht</p>
      <p><strong>Diensteanbieter:</strong> """ + BUSINESS + """ (Inh. """ + OWNER + """)<br />
      <strong>Anschrift:</strong> """ + ADDRESS + """<br />
      <strong>Kontakt:</strong> Telefon: """ + PHONE_DISPLAY + """ · E-Mail: <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
      <h2>1. Gesetzliche Widerrufsbelehrung (Dienstleistungen)</h2>
      <h3>Widerrufsrecht</h3>
      <p>Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gründen diesen Vertrag zu widerrufen. Die Widerrufsfrist beträgt vierzehn Tage ab dem Tag des Vertragsabschlusses.</p>
      <p>Um Ihr Widerrufsrecht auszuüben, müssen Sie uns (""" + BUSINESS + """, Inh. """ + OWNER + """, """ + ADDRESS + """, Tel.: """ + PHONE_DISPLAY + """, E-Mail: """ + EMAIL + """) mittels einer eindeutigen Erklärung (z. B. ein mit der Post versandter Brief oder eine E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen, informieren. Sie können dafür das beigefügte Muster-Widerrufsformular verwenden, das jedoch nicht vorgeschrieben ist.</p>
      <p>Zur Wahrung der Widerrufsfrist reicht es aus, dass Sie die Mitteilung über die Ausübung des Widerrufsrechts vor Ablauf der Widerrufsfrist absenden.</p>
      <h3>Folgen des Widerrufs</h3>
      <p>Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, einschließlich der Lieferkosten (mit Ausnahme der zusätzlichen Kosten, die sich daraus ergeben, dass Sie eine andere Art der Lieferung als die von uns angebotene, günstigste Standardlieferung gewählt haben), unverzüglich und spätestens binnen vierzehn Tagen ab dem Tag zurückzuzahlen, an dem die Mitteilung über Ihren Widerruf dieses Vertrags bei uns eingegangen ist. Für diese Rückzahlung verwenden wir dasselbe Zahlungsmittel, das Sie bei der ursprünglichen Transaktion eingesetzt haben, es sei denn, mit Ihnen wurde ausdrücklich etwas anderes vereinbart; in keinem Fall werden Ihnen wegen dieser Rückzahlung Entgelte berechnet.</p>
      <p>Haben Sie verlangt, dass die Dienstleistungen während der Widerrufsfrist beginnen sollen, so haben Sie uns einen angemessenen Betrag zu zahlen, der dem Anteil der bis zu dem Zeitpunkt, zu dem Sie uns von der Ausübung des Widerrufsrechts hinsichtlich dieses Vertrags unterrichten, bereits erbrachten Dienstleistungen im Verhältnis zum Gesamtumfang der im Vertrag vorgesehenen Dienstleistungen entspricht.</p>
      <h3>Besonderer Hinweis zum vorzeitigen Erlöschen des Widerrufsrechts (§ 356 Abs. 4 BGB)</h3>
      <p>Das Widerrufsrecht erlischt bei einem Vertrag zur Erbringung von Dienstleistungen auch dann, wenn der Unternehmer die Dienstleistung vollständig erbracht hat und mit der Ausführung der Dienstleistung erst begonnen hat, nachdem der Verbraucher dazu seine ausdrückliche Zustimmung erteilt hat und gleichzeitig seine Kenntnis davon bestätigt hat, dass er sein Widerrufsrecht bei vollständiger Vertragserfüllung durch den Unternehmer verliert.</p>
      <h2>2. Muster-Widerrufsformular</h2>
      <p>(Wenn Sie den Vertrag widerrufen wollen, dann füllen Sie bitte dieses Formular aus und senden Sie es zurück.)</p>
      <p>An: """ + BUSINESS + """, Inhaber: """ + OWNER + """, """ + ADDRESS + """, E-Mail: """ + EMAIL + """</p>
      <p>Hiermit widerrufe(n) ich/wir (*) den von mir/uns (*) abgeschlossenen Vertrag über die Erbringung der folgenden Dienstleistung (z. B. Kfz-Gutachten / Wertermittlung):</p>
      <p>Bestellt am (*) / beauftragt am (*): ___________________<br />
      Erhalten am (*): ___________________<br />
      Name des/der Verbraucher(s):<br />
      Anschrift des/der Verbraucher(s):<br />
      __________________________________________________<br />
      Unterschrift des/der Verbraucher(s) (nur bei Mitteilung auf Papier) · Datum: __________________<br />
      (*) Unzutreffendes streichen.</p>
      <h2>3. Hinweis zur Online-Beauftragung</h2>
      <p>Für eine spätere kostenpflichtige Online-Beauftragung auf dieser Website sind vor dem Absende-Button folgende Pflicht-Checkboxen vorgesehen (nicht vorausgewählt):</p>
      <ul>
        <li>„Ich habe die AGB und die Widerrufsbelehrung zur Kenntnis genommen und erkläre mich mit deren Geltung einverstanden.“</li>
        <li>„Ich verlangt ausdrücklich und stimme zu, dass das """ + BUSINESS + """ mit der Dienstleistung (Gutachtenerstellung) vor Ablauf der 14-tägigen Widerrufsfrist beginnt. Mir ist bekannt, dass ich mein Widerrufsrecht bei vollständiger Vertragserfüllung verliere.“</li>
      </ul>
      <p>Der Absendebutton muss eindeutig beschriftet sein (z. B. „Kostenpflichtig beauftragen“, § 312j BGB). Nach Eingang einer Online-Beauftragung ist eine Bestätigungs-E-Mail inkl. Widerrufsbelehrung als dauerhafter Datenträger erforderlich.</p>
      <p class="muted">Stand: August 2026</p>
    </section>"""
    write(ROOT / "widerruf.html", 0, "Kontakt", "Widerruf", "Widerrufsbelehrung.", widerruf)

    print("done")


if __name__ == "__main__":
    main()
