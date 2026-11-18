# Pelinsu Kaleli — academic portfolio

Personal academic website for [Pelinsu Kaleli](https://xngardy.github.io), built with **Jekyll**, a custom academic theme, and **GitHub Pages**. No frontend framework, paid hosting, tracking, external fonts, or application server is required.

## Where to edit

| Content | File |
| --- | --- |
| Biography, research overview, experience, contact | `index.html` |
| CV page | `cv.md` |
| Downloadable CV | `assets/files/Pelinsu_Kaleli_CV.pdf` |
| Individual projects | `_projects/*.md` |
| Profile image | `assets/images/profile.png` |
| Appearance | `assets/style.css` |
| Shared layout, navigation, metadata | `_layouts/default.html` |
| Site URL and settings | `_config.yml` |
| Publishing workflow | `.github/workflows/pages.yml` |

To change text online, open the corresponding file in GitHub, choose **Edit**, and commit to `main`. GitHub Actions builds the site, checks internal links, and publishes it to GitHub Pages automatically.

## Local preview

Use a current Ruby installation (Ruby 3.2 or newer recommended) and Bundler:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Open the local address printed in the terminal. For a production build:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

## GitHub Pages configuration

The repository is named **`xngardy.github.io`**, under the **`xNgardy`** account. In **Settings → Pages**, the source is **GitHub Actions**. Every push to `main` runs the included workflow. The custom theme is implemented in this repository, so no remote theme or theme subscription is needed.

## Content notes

See `CONTENT_NOTES.md` for provenance and editorial decisions. Keep publication status, project status, and dates current. The project images show actual work; technical thumbnails without screenshots are typographic labels, not simulated outputs. The profile picture is the existing public GitHub avatar and can be replaced with a portrait at the same path.

The downloadable CV is a website edition assembled from the supplied CV and updated background. Its source text lives in `scripts/create_cv.py`; regenerate it with Python and ReportLab after editing. The website’s CV page is separately editable in `cv.md`.

## Credits

- Original portfolio layout and implementation created for Pelinsu Kaleli.
- RIDGE figures: Pelinsu Kaleli, Bulut Demir, Alper Keskin, Zeynep Sude İmdat, and Emre Sümer, from the graduation project report.
- PlayableSketch images: local development outputs from Pelinsu Kaleli’s project.
- Wrath of the Arcane Realms image: DEDICADE Studios, from the public Steam page.
- Radar image: an original schematic of the detection logic, labeled as a diagram rather than an application screenshot.
- Profile image: Pelinsu Kaleli’s public GitHub avatar.

Original website code is provided under the MIT license. Personal text, project images, documents, and third-party material retain their respective ownership and are not covered by that code license.
