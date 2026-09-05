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
      btn.setAttribute("aria-label", dark ? "Passer en mode clair" : "Passer en mode sombre");
      btn.setAttribute("title", dark ? "Mode clair" : "Mode sombre");
      btn.textContent = dark ? "☀" : "☾";
    }
  }

  // Appliquer tôt pour éviter un flash (si le script est en defer, data-theme
  // peut aussi être posé par un snippet inline — on réapplique quand même).
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
