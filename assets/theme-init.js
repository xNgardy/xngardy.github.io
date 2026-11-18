// Run before styles load so a saved light preference does not flash dark.
(() => {
  let theme = 'dark';
  try {
    const saved = localStorage.getItem('portfolio-theme');
    if (saved === 'light' || saved === 'dark') theme = saved;
  } catch (_) {
    // The page remains usable when browser storage is unavailable.
  }
  document.documentElement.dataset.theme = theme;
  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#1c1d20' : '#f4f4f4');
})();
