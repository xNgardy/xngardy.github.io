(() => {
  const filters = document.querySelector('.project-filters');
  if (filters) {
    const rows = [...document.querySelectorAll('.project-row')];
    const buttons = [...filters.querySelectorAll('button')];
    const status = document.getElementById('filter-status');
    filters.hidden = false;
    buttons.forEach(button => button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      let visible = 0;
      rows.forEach(row => {
        row.hidden = filter !== 'all' && row.dataset.category !== filter;
        if (!row.hidden) visible++;
      });
      buttons.forEach(item => {
        const active = item === button;
        item.classList.toggle('active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      status.textContent = `${visible} project${visible === 1 ? '' : 's'} shown`;
    }));
  }
  document.querySelector('[data-print-cv]')?.addEventListener('click', () => window.print());
})();
