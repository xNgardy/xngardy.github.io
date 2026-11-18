(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  const updateToggle = () => {
    if (!toggle) return;
    const dark = root.dataset.theme !== 'light';
    toggle.textContent = dark ? 'Light mode' : 'Night mode';
    toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to night mode');
    toggle.setAttribute('aria-pressed', String(dark));
  };
  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#1c1d20' : '#f4f4f4');
    updateToggle();
  };
  if (toggle) {
    updateToggle();
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
      const theme = root.dataset.theme === 'light' ? 'dark' : 'light';
      applyTheme(theme);
      try { localStorage.setItem('portfolio-theme', theme); } catch (_) {}
    });
    window.addEventListener('storage', event => {
      if (event.key === 'portfolio-theme') {
        applyTheme(event.newValue === 'light' ? 'light' : 'dark');
      }
    });
  }
  document.querySelector('[data-print-cv]')?.addEventListener('click', () => window.print());
})();
