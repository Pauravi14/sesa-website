(function () {
  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".menu-toggle");
  const mobileNav = window.matchMedia("(max-width: 760px)");

  function closeMobileNav() {
    if (!nav) return;
    nav.classList.remove("is-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
    nav.querySelectorAll(".menu-accordion[open]").forEach(function (details) {
      details.removeAttribute("open");
    });
  }

  function closeDesktopServicesMenu() {
    document.querySelectorAll(".menu-item--services.is-services-open").forEach(function (item) {
      item.classList.remove("is-services-open");
      const details = item.querySelector(".menu-accordion");
      const summary = item.querySelector(".menu-accordion__summary");
      details?.removeAttribute("open");
      summary?.setAttribute("aria-expanded", "false");
    });
  }

  function syncServicesMenuMode() {
    document.querySelectorAll(".menu-accordion").forEach(function (details) {
      const item = details.closest(".menu-item--services");
      if (mobileNav.matches) {
        item?.classList.remove("is-services-open");
        details.removeAttribute("open");
      } else {
        item?.classList.remove("is-services-open");
        details.removeAttribute("open");
        details.querySelector(".menu-accordion__summary")?.setAttribute("aria-expanded", "false");
      }
    });
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      if (!open) {
        nav.querySelectorAll(".menu-accordion[open]").forEach(function (details) {
          details.removeAttribute("open");
        });
      }
    });
  }

  document.querySelectorAll(".menu-accordion").forEach(function (details) {
    details.addEventListener("toggle", function () {
      if (!mobileNav.matches || !nav?.classList.contains("is-open")) return;
      const summary = details.querySelector(".menu-accordion__summary");
      if (details.open && summary) {
        window.requestAnimationFrame(function () {
          summary.scrollIntoView({ block: "nearest", behavior: "auto" });
        });
      }
    });
  });

  document.querySelectorAll(".menu-accordion__summary").forEach(function (summary) {
    summary.addEventListener("click", function (event) {
      if (mobileNav.matches) return;
      event.preventDefault();
      const item = summary.closest(".menu-item--services");
      const details = summary.closest(".menu-accordion");
      if (!item || !details) return;
      const willOpen = !item.classList.contains("is-services-open");
      closeDesktopServicesMenu();
      if (willOpen) {
        item.classList.add("is-services-open");
        details.setAttribute("open", "");
        summary.setAttribute("aria-expanded", "true");
      }
    });
  });

  document.querySelectorAll(".menu > li > a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (!mobileNav.matches) closeDesktopServicesMenu();
    });
  });

  document.querySelectorAll(".menu-accordion .menu-dropdown a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (!mobileNav.matches) return;
      closeMobileNav();
    });
  });

  syncServicesMenuMode();
  if (typeof mobileNav.addEventListener === "function") {
    mobileNav.addEventListener("change", syncServicesMenuMode);
  } else if (typeof mobileNav.addListener === "function") {
    mobileNav.addListener(syncServicesMenuMode);
  }

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    closeDesktopServicesMenu();
    nav?.querySelectorAll(".menu-accordion[open]").forEach(function (details) {
      details.removeAttribute("open");
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
    const units = Array.prototype.slice.call(processFlow.querySelectorAll(".process-flow__unit"));
    const connectors = Array.prototype.slice.call(
      processFlow.querySelectorAll("[data-process-connector]")
    );
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const TIMING = {
      initialDelay: 250,
      travel: 1000,
      arrivalPause: 250,
      markerReveal: 280,
      cardReveal: 350,
      betweenSegments: 180,
      finalHold: 2200,
      resetFade: 250
    };

    let running = false;
    let sequenceFinished = false;
    let sequenceGeneration = 0;
    let timers = [];
    let rafIds = [];
    let flowObserver = null;

    function clearTimers() {
      timers.forEach(function (id) {
        window.clearTimeout(id);
      });
      timers = [];
      rafIds.forEach(function (id) {
        window.cancelAnimationFrame(id);
      });
      rafIds = [];
    }

    function wait(ms) {
      return new Promise(function (resolve) {
        const id = window.setTimeout(resolve, ms);
        timers.push(id);
      });
    }

    function easeInOut(t) {
      return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    }

    function setConnectorProgress(orbit, value) {
      orbit.style.setProperty("--connector-progress", String(value));
    }

    function travelConnector(connector, duration, generation) {
      return new Promise(function (resolve) {
        if (generation !== sequenceGeneration) {
          resolve();
          return;
        }

        const orbit = connector.querySelector("[data-process-orbit]");
        if (!orbit) {
          resolve();
          return;
        }

        connector.classList.add("is-connector-live");
        setConnectorProgress(orbit, 0);

        let start = null;
        function frame(now) {
          if (generation !== sequenceGeneration) {
            resolve();
            return;
          }

          if (start === null) start = now;
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          setConnectorProgress(orbit, easeInOut(progress));

          if (progress < 1) {
            const rafId = window.requestAnimationFrame(frame);
            rafIds.push(rafId);
          } else {
            resolve();
          }
        }

        const rafId = window.requestAnimationFrame(frame);
        rafIds.push(rafId);
      });
    }

    function revealStep(unit, generation) {
      return new Promise(function (resolve) {
        if (generation !== sequenceGeneration) {
          resolve();
          return;
        }

        unit.classList.add("is-step-live");
        wait(TIMING.markerReveal).then(function () {
          if (generation !== sequenceGeneration) {
            resolve();
            return;
          }
          unit.classList.add("is-step-open");
          return wait(TIMING.cardReveal);
        }).then(resolve);
      });
    }

    function finishSequence(generation) {
      if (generation !== sequenceGeneration || sequenceFinished) {
        return Promise.resolve();
      }

      running = false;
      sequenceFinished = true;
      clearTimers();

      units.forEach(function (unit) {
        unit.classList.add("is-step-live", "is-step-open");
      });

      connectors.forEach(function (connector) {
        connector.classList.add("is-connector-live");
        const orbit = connector.querySelector("[data-process-orbit]");
        if (orbit) setConnectorProgress(orbit, 1);
      });

      processFlow.classList.remove("is-sequencing");
      processFlow.classList.add("is-sequence-complete");

      if (flowObserver) {
        flowObserver.disconnect();
        flowObserver = null;
      }

      return Promise.resolve();
    }

    function runSequence(generation) {
      units[0].classList.add("is-step-live", "is-step-open");

      return wait(TIMING.initialDelay)
        .then(function () {
          if (generation !== sequenceGeneration) return;
          return connectors.reduce(function (chain, connector, index) {
            return chain
              .then(function () {
                if (generation !== sequenceGeneration) return;
                return travelConnector(connector, TIMING.travel, generation);
              })
              .then(function () {
                if (generation !== sequenceGeneration) return;
                return wait(TIMING.arrivalPause);
              })
              .then(function () {
                if (generation !== sequenceGeneration) return;
                return revealStep(units[index + 1], generation);
              })
              .then(function () {
                if (generation !== sequenceGeneration) return;
                return wait(TIMING.betweenSegments);
              });
          }, Promise.resolve());
        })
        .then(function () {
          if (generation !== sequenceGeneration) return;
          return wait(TIMING.finalHold);
        })
        .then(function () {
          if (generation !== sequenceGeneration) return;
          return finishSequence(generation);
        });
    }

    function startSequence() {
      if (running || sequenceFinished) return;
      running = true;
      sequenceGeneration += 1;
      const generation = sequenceGeneration;
      clearTimers();
      processFlow.classList.add("is-sequencing");
      runSequence(generation);

      if (flowObserver) {
        flowObserver.disconnect();
        flowObserver = null;
      }

      window.setTimeout(function () {
        finishSequence(generation);
      }, 14000);
    }

    function isProcessFlowInView() {
      const rect = processFlow.getBoundingClientRect();
      return rect.top < window.innerHeight * 0.92 && rect.bottom > 0;
    }

    if (reduceMotion || !units.length) {
      processFlow.classList.add("is-static");
      units.forEach(function (unit) {
        unit.classList.add("is-step-live", "is-step-open");
      });
      connectors.forEach(function (connector) {
        connector.classList.add("is-connector-live");
        const orbit = connector.querySelector("[data-process-orbit]");
        if (orbit) setConnectorProgress(orbit, 1);
      });
    } else {
      flowObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              startSequence();
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px 0px 0px" }
      );
      flowObserver.observe(processFlow);

      if (isProcessFlowInView()) {
        startSequence();
      }
    }
  }

  const heroScrollCue = document.querySelector(".hero__scroll-cue");
  if (heroScrollCue) {
    function updateHeroScrollCue() {
      if (window.scrollY > 72) {
        heroScrollCue.classList.add("is-hidden");
      } else {
        heroScrollCue.classList.remove("is-hidden");
      }
    }

    window.addEventListener("scroll", updateHeroScrollCue, { passive: true });
    updateHeroScrollCue();
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
