"""Generate static HTML pages for SESA KFZ-Sachverständigenbüro."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
LOGO_MONOGRAM = "assets/logo-monogram.png?v=5"

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

HERO_SLIDES = [
    ("assets/hero-inspection.png", "Fahrzeugbegutachtung durch Kfz-Sachverständigen"),
    ("assets/damage-detail.png", "Schadendokumentation am Fahrzeug"),
    ("assets/workshop-tools.png", "Fachliche Begutachtung in der Werkstatt"),
    ("assets/nrw-road.png", "Mobiler Kfz-Gutachter in Nordrhein-Westfalen"),
    ("assets/portrait-placeholder.png", "Kfz-Sachverständiger bei der Schadenaufnahme"),
]

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
    beratung = whatsapp_url(WHATSAPP_TEXT_BERATUNG)
    return f"""
    <nav class="mobile-action-bar" aria-label="Schnellkontakt">
      <a class="mobile-action-bar__btn mobile-action-bar__btn--call" href="tel:{PHONE_LINK}">Anrufen</a>
      <a class="mobile-action-bar__btn mobile-action-bar__btn--wa" href="{beratung}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </nav>"""


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


def hero_preload_head() -> str:
    return "\n".join(
        f'    <link rel="preload" as="image" href="{src}" />' for src, _ in HERO_SLIDES
    )


def home_page_body() -> str:
    beratung = whatsapp_url(WHATSAPP_TEXT_BERATUNG)
    slides = hero_slides_html()
    return f"""
    <section class="hero hero--home hero--slideshow" data-section="hero" data-hero-slider aria-label="SESA Kfz-Sachverständigenbüro">
      <div class="hero__slides" aria-hidden="true">
{slides}
      </div>
      <div class="hero__overlay" aria-hidden="true"></div>
      <div class="hero__inner">
      <div class="hero__content">
        <p class="kicker">Unabhängiger Kfz-Sachverständiger</p>
        <h1>Kfz-Gutachter für Nordrhein-Westfalen, Niedersachsen, Hessen, Hamburg und Bremen</h1>
        <p class="lead hero__lead">Unfallgutachten · Fahrzeugbewertung · Wohnmobile · Oldtimer. Unverschuldeter Unfall? Wir dokumentieren Schäden fachgerecht und schaffen eine belastbare Grundlage für die weitere Schadenregulierung.</p>
        <ul class="hero-trust" role="list">
          <li>
            <strong>Unabhängig</strong>
            <span>Eigenes Sachverständigenbüro ohne Weisungsbindung</span>
          </li>
          <li>
            <strong>Mobil vor Ort</strong>
            <span>Bei Ihnen, in der Werkstatt oder am Fahrzeugstandort</span>
          </li>
          <li>
            <strong>24–48 Std.</strong>
            <span>Gutachtenerstellung nach vollständiger Schadenaufnahme</span>
          </li>
        </ul>
        <div class="hero-actions hero-actions--tiered">
          <a class="btn btn-primary hero-cta-primary" href="tel:{PHONE_LINK}">Jetzt anrufen</a>
          <a class="btn btn-secondary btn-wa hero-cta-secondary" href="{beratung}" target="_blank" rel="noopener noreferrer">Per WhatsApp schreiben</a>
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
      <header class="section-header">
        <p class="kicker">Leistungen</p>
        <h2>Leistungen im Überblick</h2>
        <p class="section-intro">Von der Schadenaufnahme bis zur Wertermittlung — fachlich fundiert und persönlich betreut.</p>
      </header>
      <div class="service-grid">
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-unfall.jpg" alt="" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Unfallgutachten</h3>
            <p>Unabhängige Schadenaufnahme als technische Grundlage für die Regulierung.</p>
            <a class="service-card__link" href="leistungen/unfallgutachten.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-bewertung.jpg" alt="" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Fahrzeugbewertung</h3>
            <p>Marktwert, Wiederbeschaffungswert oder Fahrzeugwert je nach Anlass.</p>
            <a class="service-card__link" href="leistungen/fahrzeugbewertung.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-wohnmobile.jpg" alt="" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Wohnmobile &amp; Wohnwagen</h3>
            <p>Begutachtung und Bewertung von Freizeitfahrzeugen.</p>
            <a class="service-card__link" href="leistungen/wohnmobile.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-oldtimer.jpg" alt="" loading="lazy" /></div>
          <div class="service-card__body">
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
        <p class="kicker">Ablauf</p>
        <h2>In vier Schritten zum Gutachten</h2>
      </header>
      <ol class="process-timeline" role="list">
        <li class="process-timeline__step">
          <span class="process-timeline__marker" aria-hidden="true">01</span>
          <article class="process-timeline__card">
            <h3>Kontakt</h3>
            <p>Kontaktaufnahme und Erstberatung</p>
          </article>
        </li>
        <li class="process-timeline__step">
          <span class="process-timeline__marker" aria-hidden="true">02</span>
          <article class="process-timeline__card">
            <h3>Begutachtung</h3>
            <p>Schadenaufnahme am Fahrzeugstandort</p>
          </article>
        </li>
        <li class="process-timeline__step">
          <span class="process-timeline__marker" aria-hidden="true">03</span>
          <article class="process-timeline__card">
            <h3>Dokumentation</h3>
            <p>Gutachtenerstellung in der Regel innerhalb von 24–48 Stunden</p>
          </article>
        </li>
        <li class="process-timeline__step">
          <span class="process-timeline__marker" aria-hidden="true">04</span>
          <article class="process-timeline__card">
            <h3>Besprechung</h3>
            <p>Persönliche Betreuung bei Rückfragen</p>
          </article>
        </li>
      </ol>
    </section>

    <section class="section content-light home-section home-trust" data-section="trust" id="warum-sesa">
      <header class="section-header">
        <p class="kicker">Warum SESA?</p>
        <h2>Ihr Vorteil auf einen Blick</h2>
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
    parent_href = p + "leistungen/index.html"
    parent_cur = " aria-current=\"page\"" if active == "Leistungen" else ""
    items = []
    for label, href in SERVICE_LINKS:
        full = p + href
        items.append(f"<li><a href=\"{full}\">{label}</a></li>")
    submenu = "\n".join(items)
    return f"""<li class="menu-item menu-item--dropdown" data-nav-dropdown>
      <span class="menu-item-row">
        <a href="{parent_href}" class="menu-parent-link"{parent_cur}>Leistungen</a>
        <button type="button" class="menu-submenu-toggle" aria-expanded="false" aria-label="Leistungen Untermenü anzeigen" data-nav-dropdown-toggle>
          <span class="menu-caret" aria-hidden="true"></span>
        </button>
      </span>
      <ul class="menu-dropdown" data-nav-dropdown-menu>
{submenu}
      </ul>
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
          <div class="consent-text">
            <p>Wir verwenden auf dieser Website Cookies und ähnliche Technologien, um die Website bereitzustellen und — nur mit Ihrer Einwilligung — Dienste von Drittanbietern einzubinden.</p>
            <p>Dabei können personenbezogene Daten (z. B. IP-Adresse) verarbeitet werden. Einwilligung ist freiwillig und kann jederzeit widerrufen werden. Details in der <a href="{p}datenschutz.html">Datenschutzerklärung</a>.</p>
            <ul>
              <li>Speichern Ihrer Einwilligung (technisch erforderlich)</li>
              <li>Google Maps auf der Kontaktseite (optional)</li>
            </ul>
          </div>
          <div class="consent-actions">
            <button type="button" class="consent-btn consent-btn-primary" data-consent-accept-all>Alle akzeptieren</button>
            <button type="button" class="consent-btn consent-btn-secondary" data-consent-decline>Ohne Einwilligung fortfahren</button>
          </div>
          <button type="button" class="consent-customize-link" data-consent-customize>Einstellungen anpassen</button>
        </div>
        <div class="consent-panel" data-consent-detail hidden>
          <h2>Einstellungen anpassen</h2>
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
    <link rel="stylesheet" href="{p}css/styles.css?v=28" />
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
        <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Menü">Menü</button>
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
    <script src="{p}js/main.js?v=2" defer></script>
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


def page_hero(title: str, lead: str, img: str, depth: int) -> str:
    p = prefix(depth)
    return f"""
    <section class="page-hero">
      <div>
        <p class="kicker">SESA · Kfz-Sachverständigenbüro</p>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
      </div>
      <img src="{p}{img}" alt="" loading="lazy" />
    </section>"""


def service_page(slug: str, title: str, lead: str, paragraphs: list[str], img: str) -> None:
    body = page_hero(title, lead, img, 1)
    body += "<section class=\"section content-light\"><div class=\"legal\">"
    for para in paragraphs:
        body += f"<p>{para}</p>"
    body += """
    <p class="muted"><em>Hinweis: Diese Information ersetzt keine individuelle Rechtsberatung.</em></p>
    <div class="cta-row">
      <a class="btn btn-solid" href="../schaden-melden.html">Schaden melden</a>
      <a class="btn" href="tel:+491773145839">Jetzt anrufen</a>
    </div>
    </div></section>"""
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
    leistungen_body = page_hero(
        "Leistungen",
        "Alle fachlichen Angebote im Überblick — von Unfallgutachten bis Ortstermin.",
        "assets/workshop-tools.png",
        1,
    )
    leistungen_body += """
    <section class="section content-light"><div class="grid-3">
      <article class="card"><h3><a href="unfallgutachten.html">Unfallgutachten / Haftpflicht</a></h3><p class="muted">Schadenaufnahme nach unverschuldetem Unfall.</p></article>
      <article class="card"><h3><a href="fahrzeugbewertung.html">Fahrzeugbewertung</a></h3><p class="muted">Marktwert und Wiederbeschaffungswert.</p></article>
      <article class="card"><h3><a href="oldtimer-youngtimer.html">Oldtimer & Youngtimer</a></h3><p class="muted">Klassiker und Sammlerfahrzeuge.</p></article>
      <article class="card"><h3><a href="wohnmobile.html">Wohnmobile & Wohnwagen</a></h3><p class="muted">Freizeitfahrzeuge.</p></article>
      <article class="card"><h3><a href="beweissicherung.html">Beweissicherung</a></h3><p class="muted">Dokumentation vor Reparatur oder Veränderung.</p></article>
      <article class="card"><h3><a href="privatgutachten.html">Privatgutachten</a></h3><p class="muted">Unabhängige Begutachtung im Privatauftrag.</p></article>
      <article class="card"><h3><a href="kostenvoranschlag.html">Kostenvoranschlag</a></h3><p class="muted">Vereinfachte Reparaturkostenermittlung.</p></article>
      <article class="card"><h3><a href="versicherungsgutachten.html">Versicherungsgutachten / Kasko</a></h3><p class="muted">Begutachtung von Kaskoschäden.</p></article>
      <article class="card"><h3><a href="beratung.html">Beratung</a></h3><p class="muted">Ersteinschätzung und Vorgehen.</p></article>
      <article class="card"><h3><a href="ortstermine.html">Ortstermine</a></h3><p class="muted">Begutachtung am Fahrzeugstandort.</p></article>
    </div></section>"""
    write(ROOT / "leistungen" / "index.html", 1, "Leistungen", "Leistungen", "Gutachten und Bewertungen.", leistungen_body)

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
            "assets/nrw-road.png",
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
    ueber = page_hero(
        "Über uns",
        "Selim Sabahoglu — unabhängiger Kfz-Sachverständiger in Paderborn.",
        "assets/portrait-placeholder.png",
        0,
    )
    ueber += """
    <section class="section content-light split">
      <div class="portrait-card">
        <img class="portrait" src="assets/portrait-placeholder.png" alt="Porträtfoto — Platzhalter bis Foto vom Inhaber eingereicht wird" />
        <h2>""" + OWNER + """</h2>
        <p>Inhaber · """ + BUSINESS + """</p>
        <ul class="contact-list">
          <li><a href="tel:+491773145839">""" + PHONE_DISPLAY + """</a></li>
          <li><a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></li>
          <li>""" + ADDRESS + """</li>
        </ul>
      </div>
      <div class="legal">
        <p>Schon als Kind interessierte mich die Fahrzeugtechnik — von neuen Modellen bis zu Klassikern. Nach der Ausbildung im VAG-Konzern bei einem VW- und Audi-Autohaus und dem Kfz-Meister folgte die Tätigkeit bei TÜV NORD als Fahrzeugbewerter und Unfallschadengutachter. Heute steht eine persönliche, unabhängige und gründliche Beratung im Mittelpunkt.</p>
        <p><strong>Beruflicher Werdegang (Auszug):</strong></p>
        <ul>
          <li>TÜV NORD Autoservice, Paderborn — Kfz-Sachverständiger / Fahrzeugbewerter und Unfallschadengutachter (frühere Tätigkeit, keine aktuelle Partnerschaft mit TÜV NORD)</li>
          <li>Grafschafter Autozentrale VW/Audi Partner, Nordhorn — Ausbildung Kfz-Mechatroniker</li>
        </ul>
        <p><strong>Qualifikationen</strong></p>
        <p class="muted">Kfz-Meister und Sachverständiger für Kraftfahrzeuge. Genaue Bezeichnungen und Nachweise gemäß Originalunterlagen stellen wir auf Anfrage zur Verfügung.</p>
        <ul>
          <li>Kfz-Meister</li>
          <li>Sachverständiger für Kraftfahrzeuge</li>
          <li>Mitglied im Verband freier Kraftfahrzeug-Sachverständiger e. V. (VFK)</li>
        </ul>
        <p>Ein Gutachten schafft Klarheit, wenn Sachverhalte komplex sind. Unabhängigkeit, fachliche Sorgfalt und transparente Dokumentation stehen im Mittelpunkt unserer Arbeit.</p>
      </div>
    </section>"""
    write(ROOT / "ueber-uns.html", 0, "Über uns", "Über uns", "Selim Sabahoglu — Kfz-Sachverständiger.", ueber)

    # Ratgeber
    rat_index = page_hero("Ratgeber", "Sachliche Informationen — keine Rechtsberatung.", "assets/nrw-road.png", 1)
    rat_index += """
    <section class="section content-light"><div class="grid-3">
      <article class="card"><h3><a href="nach-einem-unfall.html">Was tun nach einem Unfall?</a></h3></article>
      <article class="card"><h3><a href="rechte.html">Ihre Rechte nach einem unverschuldeten Unfall</a></h3></article>
      <article class="card"><h3><a href="faq.html">FAQ</a></h3></article>
    </div></section>"""
    write(ROOT / "ratgeber" / "index.html", 1, "GUTACHTEN", "Ratgeber", "Unfallhilfe und FAQ.", rat_index)

    unfall_rat = page_hero("Was tun nach einem Unfall?", "Erste Schritte an der Unfallstelle.", "assets/damage-detail.png", 1)
    unfall_rat += """
    <section class="section content-light legal">
      <ol>
        <li>Ruhe bewahren und Unfallstelle sichern.</li>
        <li>Bei Bedarf Polizei rufen und Beteiligte dokumentieren.</li>
        <li>Unfallort, Uhrzeit und Schäden fotografieren.</li>
        <li>Keine vorschnellen Erklärungen zur Schuld oder Schadenhöhe abgeben.</li>
        <li>Schadenfotos und Informationen an SESA senden (WhatsApp oder Telefon).</li>
        <li>Weiteres Vorgehen im persönlichen Gespräch klären.</li>
      </ol>
      <p class="muted"><em>Keine Rechtsberatung. Bei rechtlichen Fragen wenden Sie sich an einen Rechtsanwalt.</em></p>
    </section>"""
    write(ROOT / "ratgeber" / "nach-einem-unfall.html", 1, "GUTACHTEN", "Nach einem Unfall", "Erste Schritte.", unfall_rat)

    rechte = page_hero("Ihre Rechte", "Informationen nach einem unverschuldeten Verkehrsunfall.", "assets/workshop-tools.png", 1)
    rechte += """
    <section class="section content-light legal">
      <p>Die folgenden Hinweise dienen der sachlichen Information und ersetzen keine individuelle Rechtsberatung.</p>
      <table class="legal-table">
        <tr><th>Freie Sachverständigenwahl</th><td>Bei einem unverschuldeten Haftpflichtschaden kann grundsätzlich das Recht bestehen, einen eigenen unabhängigen Sachverständigen zu beauftragen. Ob Kosten erstattungsfähig sind, hängt vom Einzelfall ab.</td></tr>
        <tr><th>Reparaturkosten</th><td>Das Gutachten dokumentiert technisch erforderliche Reparaturmaßnahmen und voraussichtliche Kosten.</td></tr>
        <tr><th>Wertminderung</th><td>Ob eine merkantile Wertminderung vorliegt, wird im Einzelfall beurteilt.</td></tr>
        <tr><th>Totalschaden</th><td>Wiederbeschaffungswert, Restwert und Reparaturkosten werden gegenübergestellt.</td></tr>
        <tr><th>Teilschuld</th><td>Bei Mithaftung können Kosten nur anteilig erstattet werden. Die Haftungsquote sollte rechtlich geprüft werden.</td></tr>
      </table>
    </section>"""
    write(ROOT / "ratgeber" / "rechte.html", 1, "GUTACHTEN", "Ihre Rechte", "Informationen nach Unfall.", rechte)

    faq_items = [
        ("Was kostet ein Gutachten?", "Bei einem unverschuldeten Haftpflichtschaden können erforderliche Sachverständigenkosten grundsätzlich zu den ersatzfähigen Schadenpositionen gehören. Bei Bagatellschäden oder Mithaftung können Abweichungen bestehen. Andere Gutachten werden je nach Auftrag berechnet."),
        ("Wer bezahlt das Gutachten?", "Bei unverschuldetem Haftpflichtschaden können Kosten grundsätzlich vom Schädiger bzw. dessen Haftpflichtversicherung zu erstatten sein. Bei Kaskoschäden entscheidet die eigene Versicherung."),
        ("Wie schnell bekomme ich einen Termin?", "Kurzfristige Termine sind je nach Standort, Auslastung und Auftrag möglich."),
        ("Wie lange dauert die Erstellung?", "In der Regel innerhalb von 24–48 Stunden nach vollständiger Schadenaufnahme — abhängig vom Schadenumfang."),
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
