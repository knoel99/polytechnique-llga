(function () {
  var KEY = "llga-theme";
  var root = document.documentElement;

  function systemDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function current() {
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) {}
    if (stored === "dark" || stored === "light") return stored;
    return systemDark() ? "dark" : "light";
  }

  function apply(theme, persist) {
    root.setAttribute("data-theme", theme);
    if (persist) {
      try { localStorage.setItem(KEY, theme); } catch (e) {}
    }
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      var dark = theme === "dark";
      btn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
      btn.setAttribute("title", dark ? "Light mode" : "Dark mode");
      btn.textContent = dark ? "☀" : "☾";
    }
  }

  // Apply early to avoid a flash (if the script is deferred, data-theme may
  // also be set by an inline snippet — we re-apply anyway).
  apply(current(), false);

  function mount() {
    if (document.getElementById("theme-toggle")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.id = "theme-toggle";
    btn.className = "theme-toggle";
    btn.addEventListener("click", function () {
      apply(current() === "dark" ? "light" : "dark", true);
    });
    document.body.appendChild(btn);
    apply(current(), false);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }

  if (window.matchMedia) {
    try {
      window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () {
        var stored = null;
        try { stored = localStorage.getItem(KEY); } catch (e) {}
        if (stored !== "dark" && stored !== "light") apply(current(), false);
      });
    } catch (e) {}
  }
})();
