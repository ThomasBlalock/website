/* /shared/shell.js
   Loads the shared top nav from /shared/nav.html into the empty
   <header id="site-nav"></header> slot every tab includes, then
   marks the current tab active.

   Tabs only need this in <head>:
     <link rel="stylesheet" href="/shared/styles.css">
     <script src="/shared/shell.js" defer></script>
   …and in <body>:
     <header id="site-nav"></header>
   …and at the bottom:
     <footer class="site-foot">…</footer>     (optional, plain HTML — no JS needed)
*/

(async function mountNav() {
  const slot = document.getElementById("site-nav");
  if (!slot) return;
  try {
    const r = await fetch("/shared/nav.html", { credentials: "same-origin" });
    if (!r.ok) return;
    slot.innerHTML = await r.text();
  } catch (_) {
    return;
  }
  // Mark the current tab active.
  const here = window.location.pathname.replace(/\/+$/, "/") || "/";
  for (const a of slot.querySelectorAll("a[data-path]")) {
    const path = a.dataset.path;
    const exact = a.dataset.match === "exact";
    const hit = exact ? (here === path) : here.startsWith(path);
    if (hit) a.classList.add("active");
  }
})();
