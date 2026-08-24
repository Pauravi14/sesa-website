(function () {
  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".menu-toggle");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      if (!open) {
        nav.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (item) {
          item.classList.remove("is-open");
          const btn = item.querySelector("[data-nav-dropdown-toggle]");
          if (btn) btn.setAttribute("aria-expanded", "false");
        });
      }
    });
  }

  document.querySelectorAll("[data-nav-dropdown]").forEach(function (item) {
    const btn = item.querySelector("[data-nav-dropdown-toggle]");
    const parentLink = item.querySelector(".menu-parent-link");
    if (!btn) return;

    function setDropdownOpen(open) {
      document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (other) {
        if (other === item) return;
        other.classList.remove("is-open");
        const otherBtn = other.querySelector("[data-nav-dropdown-toggle]");
        if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
      });
      item.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", String(open));
    }

    function toggleDropdown() {
      setDropdownOpen(!item.classList.contains("is-open"));
    }

    btn.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      toggleDropdown();
    });

    parentLink?.addEventListener("click", function (event) {
      if (!window.matchMedia("(max-width: 760px)").matches) return;
      if (!nav?.classList.contains("is-open")) return;
      event.preventDefault();
      toggleDropdown();
    });
  });

  document.querySelectorAll(".menu-dropdown a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (!window.matchMedia("(max-width: 760px)").matches || !nav) return;
      nav.classList.remove("is-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
      nav.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (item) {
        item.classList.remove("is-open");
        const btn = item.querySelector("[data-nav-dropdown-toggle]");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    });
  });

  document.addEventListener("click", function (event) {
    if (window.matchMedia("(min-width: 761px)").matches) return;
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (item) {
      if (!item.contains(event.target)) {
        item.classList.remove("is-open");
        const btn = item.querySelector("[data-nav-dropdown-toggle]");
        if (btn) btn.setAttribute("aria-expanded", "false");
      }
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (item) {
      item.classList.remove("is-open");
      const btn = item.querySelector("[data-nav-dropdown-toggle]");
      if (btn) {
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    });
  });

  const CONSENT_KEY = "sesa-consent";
  const LEGACY_KEY = "sesa-maps-consent";
  const backdrop = document.querySelector("[data-consent-backdrop]");
  const mainPanel = document.querySelector("[data-consent-main]");
  const detailPanel = document.querySelector("[data-consent-detail]");
  const mapsToggle = document.querySelector("[data-consent-maps]");
  const mapsHost = document.querySelector("[data-map]");

  function readConsent() {
    try {
      const raw = localStorage.getItem(CONSENT_KEY);
      if (raw) return JSON.parse(raw);
    } catch (_) {
      /* ignore */
    }
    const legacy = localStorage.getItem(LEGACY_KEY);
    if (legacy === "1") return { decided: true, maps: true };
    if (legacy === "0") return { decided: true, maps: false };
    return null;
  }

  function saveConsent(consent) {
    localStorage.setItem(CONSENT_KEY, JSON.stringify(consent));
    localStorage.removeItem(LEGACY_KEY);
  }

  function loadMap() {
    if (!mapsHost || mapsHost.dataset.loaded === "1") return;
    const iframe = document.createElement("iframe");
    iframe.title = "Karte: SESA KFZ-Sachverständigenbüro in Paderborn";
    iframe.loading = "lazy";
    iframe.referrerPolicy = "no-referrer-when-downgrade";
    iframe.src =
      "https://www.google.com/maps?q=Pohlweg+76,+33098+Paderborn&output=embed";
    mapsHost.innerHTML = "";
    mapsHost.appendChild(iframe);
    mapsHost.dataset.loaded = "1";
  }

  function showMainPanel() {
    if (mainPanel) mainPanel.hidden = false;
    if (detailPanel) detailPanel.hidden = true;
  }

  function showDetailPanel() {
    const consent = readConsent();
    if (mapsToggle) mapsToggle.checked = consent?.maps === true;
    if (mainPanel) mainPanel.hidden = true;
    if (detailPanel) detailPanel.hidden = false;
  }

  function showModal() {
    if (!backdrop) return;
    showMainPanel();
    backdrop.hidden = false;
    document.body.classList.add("consent-open");
  }

  function hideModal() {
    if (!backdrop) return;
    backdrop.hidden = true;
    document.body.classList.remove("consent-open");
    showMainPanel();
  }

  function applyConsent(consent) {
    saveConsent(consent);
    if (consent.maps) {
      loadMap();
    } else if (mapsHost) {
      mapsHost.dataset.loaded = "0";
      mapsHost.innerHTML =
        "<p class=\"muted\">Karte nur nach Einwilligung. <button class=\"btn\" type=\"button\" data-load-map>Karte laden</button></p>";
    }
    hideModal();
  }

  const stored = readConsent();
  if (!stored || !stored.decided) {
    showModal();
  } else if (stored.maps) {
    loadMap();
  }

  document.querySelector("[data-consent-accept-all]")?.addEventListener("click", function () {
    applyConsent({ decided: true, maps: true });
  });

  document.querySelector("[data-consent-decline]")?.addEventListener("click", function () {
    applyConsent({ decided: true, maps: false });
  });

  document.querySelector("[data-consent-customize]")?.addEventListener("click", function () {
    showDetailPanel();
  });

  document.querySelector("[data-consent-back]")?.addEventListener("click", function () {
    showMainPanel();
  });

  document.querySelector("[data-consent-save]")?.addEventListener("click", function () {
    applyConsent({ decided: true, maps: mapsToggle?.checked === true });
  });

  document.querySelectorAll("[data-consent-reopen]").forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      showModal();
    });
  });

  document.querySelector("[data-load-map]")?.addEventListener("click", function () {
    applyConsent({ decided: true, maps: true });
  });

  const geoBtn = document.querySelector("[data-geo]");
  const locationInput = document.querySelector("#unfallort");
  geoBtn?.addEventListener("click", function () {
    if (!navigator.geolocation) {
      alert("Standort ist in diesem Browser nicht verfügbar.");
      return;
    }
    geoBtn.disabled = true;
    navigator.geolocation.getCurrentPosition(
      function (pos) {
        const lat = pos.coords.latitude.toFixed(5);
        const lng = pos.coords.longitude.toFixed(6);
        if (locationInput) {
          locationInput.value = "Standort ca. " + lat + ", " + lng;
        }
        geoBtn.disabled = false;
      },
      function () {
        alert("Standort konnte nicht ermittelt werden.");
        geoBtn.disabled = false;
      }
    );
  });

  document.querySelector("#schaden-form")?.addEventListener("submit", function (event) {
    event.preventDefault();
    const ort = document.querySelector("#unfallort")?.value.trim();
    const wer = document.querySelector("input[name='verursacher']:checked")?.value;
    const note = document.querySelector("#hinweis")?.value.trim();
    if (!ort || !wer) {
      alert("Bitte Unfallort und Verursacher angeben.");
      return;
    }
    const lines = [
      "Guten Tag SESA,",
      "ich möchte einen Schaden melden.",
      "Unfallort: " + ort,
      "Verursacher: " + wer + ".",
    ];
    if (note) lines.push("Hinweis: " + note);
    lines.push("Bitte rufen Sie mich zurück.");
    const url = "https://wa.me/491773145839?text=" + encodeURIComponent(lines.join("\n"));
    window.location.href = url;
  });

  const waWrap = document.querySelector("[data-wa-float]");
  const waToggle = document.querySelector("[data-wa-toggle]");
  const waMenu = document.querySelector("[data-wa-menu]");

  function closeWaMenu() {
    if (!waMenu || !waToggle) return;
    waMenu.hidden = true;
    waToggle.setAttribute("aria-expanded", "false");
  }

  function openWaMenu() {
    if (!waMenu || !waToggle) return;
    waMenu.hidden = false;
    waToggle.setAttribute("aria-expanded", "true");
  }

  waToggle?.addEventListener("click", function () {
    if (waMenu?.hidden) {
      openWaMenu();
    } else {
      closeWaMenu();
    }
  });

  document.addEventListener("click", function (event) {
    if (!waWrap || waMenu?.hidden) return;
    if (!waWrap.contains(event.target)) {
      closeWaMenu();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeWaMenu();
      if (backdrop && !backdrop.hidden && detailPanel && !detailPanel.hidden) {
        showMainPanel();
      }
    }
  });

  const processFlow = document.querySelector("[data-process-flow]");
  if (processFlow) {
    const flowItems = processFlow.querySelectorAll("[data-flow-item]");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function revealFlowItem(index) {
      const item = flowItems[index];
      if (!item) return;
      item.classList.add("is-visible");
      if (index < flowItems.length - 1) {
        window.setTimeout(function () {
          revealFlowItem(index + 1);
        }, reducedMotion ? 0 : 520);
      }
    }

    if (reducedMotion || !flowItems.length) {
      flowItems.forEach(function (item) {
        item.classList.add("is-visible");
      });
    } else {
      const flowObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            flowObserver.disconnect();
            revealFlowItem(0);
          });
        },
        { threshold: 0.2, rootMargin: "0px 0px -8% 0px" }
      );
      flowObserver.observe(processFlow);
    }
  }

  const heroSlider = document.querySelector("[data-hero-slider]");
  if (heroSlider) {
    const slides = heroSlider.querySelectorAll(".hero__slide");
    if (slides.length > 1) {
      slides.forEach(function (slide) {
        slide.loading = "eager";
        if (slide.decode) {
          slide.decode().catch(function () {
            /* ignore decode errors */
          });
        }
      });

      if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        const fadeMs = 3000;
        const holdMs = 6500;
        let active = 0;

        window.setInterval(function () {
          const next = (active + 1) % slides.length;
          slides[active].classList.remove("is-active");
          slides[next].classList.add("is-active");
          active = next;
        }, holdMs + fadeMs);
      }
    }
  }
})();
