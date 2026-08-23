(function () {
  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".menu-toggle");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const cookie = document.querySelector("[data-cookie]");
  const mapsHost = document.querySelector("[data-map]");
  const consentKey = "sesa-maps-consent";

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

  if (localStorage.getItem(consentKey) === "1") {
    loadMap();
  } else if (cookie) {
    cookie.classList.add("is-on");
  }

  document.querySelector("[data-cookie-accept]")?.addEventListener("click", function () {
    localStorage.setItem(consentKey, "1");
    cookie?.classList.remove("is-on");
    loadMap();
  });

  document.querySelector("[data-cookie-decline]")?.addEventListener("click", function () {
    localStorage.setItem(consentKey, "0");
    cookie?.classList.remove("is-on");
  });

  document.querySelector("[data-load-map]")?.addEventListener("click", function () {
    localStorage.setItem(consentKey, "1");
    cookie?.classList.remove("is-on");
    loadMap();
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
    }
  });
})();
