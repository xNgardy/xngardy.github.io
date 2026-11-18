# Pelinsu Kaleli

My [portfolio](https://xngardy.github.io), with research, projects, internship experience, and CV. Built with Jekyll and hosted on GitHub Pages.

## Editing

- `index.html`: homepage
- `_projects/`: project pages
- `experience/`: internship and studio pages
- `cv.md`: CV page
- `scripts/create_cv.py`: downloadable CV source (requires ReportLab)
- `assets/`: images, files, styles, and JavaScript
- `_layouts/`: shared page layouts

## Local development

With Ruby and Bundler installed:

```sh
BUNDLE_PATH=vendor/bundle bundle install
npm run dev
```

To build and check links:

```sh
npm run build
python3 scripts/check_site.py _site
```

Pushing to `main` builds and deploys the site through GitHub Actions.

## Credits and license

RIDGE figures are from our graduation project report. Bannerlord artwork belongs to TaleWorlds Entertainment; Wrath of the Arcane Realms artwork belongs to DEDICADE Studios.

Website code is licensed under MIT. Personal content, project materials, and third-party images retain their respective ownership.
