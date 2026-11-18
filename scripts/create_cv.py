"""Generate the public website CV. Requires ReportLab; no source PDFs needed."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/files/Pelinsu_Kaleli_CV.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
mac = Path('/System/Library/Fonts/Supplemental')
linux = Path('/usr/share/fonts/truetype/dejavu')
fonts = [('Body', 'Arial.ttf', 'DejaVuSans.ttf'), ('BodyBold', 'Arial Bold.ttf', 'DejaVuSans-Bold.ttf'), ('BodyItalic', 'Arial Italic.ttf', 'DejaVuSans-Oblique.ttf'), ('Display', 'Georgia.ttf', 'DejaVuSerif.ttf')]
for name, apple, fallback in fonts:
    pdfmetrics.registerFont(TTFont(name, str(mac / apple if (mac / apple).exists() else linux / fallback)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='BodyItalic', boldItalic='BodyBold')
ink, muted, accent = [HexColor(x) for x in ['#29272c', '#6d6874', '#6e4a87']]
styles = {
    'name': ParagraphStyle('name', fontName='Display', fontSize=27, leading=32, textColor=ink, spaceAfter=8),
    'subtitle': ParagraphStyle('subtitle', fontName='Body', fontSize=10, leading=15, textColor=accent, spaceAfter=7),
    'body': ParagraphStyle('body', fontName='Body', fontSize=9, leading=12, textColor=ink, spaceAfter=4),
    'small': ParagraphStyle('small', fontName='Body', fontSize=8.2, leading=11.5, textColor=muted, spaceAfter=3),
    'section': ParagraphStyle('section', fontName='Display', fontSize=15, leading=20, textColor=accent, spaceBefore=8, spaceAfter=5, keepWithNext=True),
    'heading': ParagraphStyle('heading', fontName='BodyBold', fontSize=9.3, leading=13.2, textColor=ink, spaceBefore=5, spaceAfter=2, keepWithNext=True),
    'bullet': ParagraphStyle('bullet', fontName='Body', fontSize=9, leading=12, textColor=ink, leftIndent=10, firstLineIndent=-8, spaceAfter=3),
}
story=[]
def p(text, kind='body'):
    story.append(Paragraph(text, styles[kind]))
def section(text): p(text, 'section')
def heading(text, detail=None):
    p(text,'heading')
    if detail: p(detail,'small')
def bullet(text): p('• '+text,'bullet')
def link(url, label): return f'<a href="{url}" color="#6e4a87">{label}</a>'

p('Pelinsu Kaleli','name')
p('Computer graphics · Procedural environments · Creative tools','subtitle')
p('Ankara, Türkiye · '+link('mailto:pelinsu.kaleli@gmail.com','pelinsu.kaleli@gmail.com')+'<br/>'+link('https://xngardy.github.io','xngardy.github.io')+' · '+link('https://github.com/xNgardy','GitHub / xNgardy')+' · '+link('https://www.linkedin.com/in/pelinsukaleli/','LinkedIn')+' · '+link('https://ngardy.itch.io','itch.io')+' · '+link('https://orcid.org/0009-0008-4366-2115','ORCID'),'small')
section('Education')
heading('Başkent University — BEng, Computer Engineering','September 2022–June 2026 · GPA 3.83/4.00 · English-medium program')
p('Graduated <b>first across the English- and Turkish-medium Computer Engineering programs</b> and <b>second in the Faculty of Engineering</b>. High honors every semester; merit scholarship recipient.')
heading('TED University — Industrial Design studies','September 2020–June 2022 · GPA 3.88/4.00 · Full scholarship')
p('Studied industrial design before transitioning to computer engineering; no degree awarded.')
section('Research &amp; manuscript')
heading('An automated spatial-data integration framework for satellite imagery, elevation data, and simulator-ready 3D terrain')
p('<b>Pelinsu Kaleli</b>, Bulut Demir, Alper Keskin, Zeynep Sude İmdat, and Emre Sümer.<br/><i>Submitted to the Journal of Spatial Science.</i>')
p('<b>RIDGE, graduation project (2025–2026).</b> Supervised by Assoc. Prof. Emre Sümer; supported by HAVELSAN SUIT and IMPROSAT. '+link('https://xngardy.github.io/projects/ridge/','Project')+' · '+link('https://github.com/xNgardy/RIDGE','Code'))
bullet('Developed vegetation detection using NDVI, Python, Rasterio, and NumPy; produced masks for procedural placement.')
bullet('Designed the Unity pipeline architecture and Unity C# integration, including terrain material classification and vegetation placement. Team framework also supports X-Plane scenery export.')
section('Selected projects')
heading(link('https://github.com/xNgardy/PlayableSketch','PlayableSketch')+' — ongoing personal project')
p('Sketch-to-level authoring with U-Net wall segmentation, YOLO11n door detection, editable browser geometry, and Unreal Engine C++ export. The user reviews inferred layouts before generating geometry or a playable level.')
heading(link('https://store.steampowered.com/app/4363570/Wrath_of_the_Arcane_Realms/','Wrath of the Arcane Realms')+' — DEDICADE Studios')
p('Co-founder, artist, and game developer on a Unity hex-based roguelike strategy game. Showcased at GG Convention in 2026. Collaborative project; currently on hiatus after the team disbanded.')
heading(link('https://github.com/xNgardy/Radar_Target_Detection_UE5','Radar Target Detection')+' — Unreal Engine / C++')
p('Directional radar sweep, moving targets, classification, tracking states, threat evaluation, warning audio, and visual detection feedback.')
heading(link('https://github.com/xNgardy/OBSS_AI_Image_Captioning_Challenge','OBSS AI Image Captioning Challenge')+' — 2nd of 280 participants')
p('Fine-tuned Qwen2.5-VL-7B with LoRA and 4-bit quantization for detailed captions under memory constraints; iterated on training and inference.')
heading(link('https://github.com/xNgardy/YZUP_Parallel_Programming_on_PostgreSQL_Servers','PostgreSQL performance &amp; concurrency study'))
p('Benchmarked server configuration and sequential, threaded, and asynchronous execution on 10 million rows; observed up to 4.08× threaded speedup in the tested setup.')
story.append(PageBreak())
p('Pelinsu Kaleli','name')
p('Experience, training &amp; distinctions','subtitle')
section('Experience')
heading('Beyond Technologies — Unreal Engine Developer','July–September 2026 · Ankara, Türkiye')
bullet('Built satellite-data preparation and editor tooling with Python, Rasterio, NumPy, and Unreal Engine 5.5 for aerial simulation environments.')
bullet('Worked on heightmaps, landscape layers, vegetation masks, road generation, and material optimization. Implemented the terrain workflow excluding the building component.')
heading('TaleWorlds Entertainment — Software Developer Intern','August–September 2025 · Ankara, Türkiye')
bullet('Co-developed a three-stage treasure-hunt quest mod for Mount &amp; Blade II: Bannerlord in C#, including clue generation, quest progression, and disguise checks.')
bullet('Fixed Unity bugs and worked on optimization for an unannounced project, with QA reproduction and regression checks; used Plastic SCM.')
heading('ATOM, ODTÜ Teknokent — DEDICADE co-founder / Pre-incubation member','November 2023–September 2025 · Ankara, Türkiye')
bullet('Worked as an artist and game developer on Wrath of the Arcane Realms, with mentorship in Unity development, marketing, and publishing.')
bullet('Participated in game jams, hackathons, and ideathons; qualified to present the team’s project to investors at Girişim23. Shared the team’s story at Karabük University’s Department of Architecture.')
heading('Fdn SOFT — Game Developer Intern','July–August 2024 · Ankara, Türkiye')
bullet('Developed Bullet Run, a Geometry Dash-inspired mobile runner, in Unity and C#: alternating player forms, obstacle spawning, parallax scrolling, and survival-based scoring.')
section('Training &amp; certifications')
heading('AI Specialization — National Technology Academy / Ministry of Industry and Technology','2024–2025')
p('Selected for the specialization cohort of 120 from the initial 1,000 trainees. Training and projects in machine learning, PyTorch, Spark, data science, stock-sector classification, and database benchmarking.')
heading('Google Game and Application Academy')
p('Selected among 2,000 participants from 35,000 applicants. Approximately eight months of training in Unity, design, marketing, and entrepreneurship.')
heading('Google Project Management Certificate — Coursera','2023 · '+link('https://coursera.org/share/452be4653382c80136254663cb7e0606','Credential'))
section('Honors &amp; awards')
bullet('<b>1st place — Kargakarga &amp; Infinia Hackathon, 2023.</b> Technical art and level design for Mazeship, built by a four-person team in 30 hours.')
bullet('<b>3rd place — Bilkent CYBERPARK Digital Culture Ideathon, 2022.</b> Game development and art in a four-person team over 24 hours.')
section('Technical skills')
p('<b>Languages:</b> C#, C++, Python.<br/><b>Engines &amp; workflow:</b> Unity, Unreal Engine, Blueprints, Git, Plastic SCM.<br/><b>Spatial data &amp; machine learning:</b> Rasterio, NumPy, PyTorch, OpenCV, U-Net, YOLO, LoRA.<br/><b>Data:</b> PostgreSQL, pandas, scikit-learn, Spark.')

def footer(canvas, doc):
    canvas.saveState()
    w,h=A4
    canvas.setStrokeColor(HexColor('#e5e1e5'));canvas.setLineWidth(.5);canvas.line(44,37,w-44,37)
    canvas.setFont('Body',7);canvas.setFillColor(muted)
    canvas.drawString(44,24,'Pelinsu Kaleli · '+ 'xngardy.github.io')
    canvas.drawRightString(w-44,24,str(doc.page))
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=35,bottomMargin=47,title='Pelinsu Kaleli — Curriculum Vitae',author='Pelinsu Kaleli')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
