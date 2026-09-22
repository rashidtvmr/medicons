from pathlib import Path
import sys,json,hashlib,collections
from catalog import ICONS,CATALOG,GROUPS
from art import ART,BEAMS
from render import svg

ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
ROOT.mkdir(parents=True,exist_ok=True)
VARIANTS=['outline','solid','duotone']
FRIENDLY={
'specialties':'Specialties & departments', 'critical-care-units':'Critical care & hospital units',
'beds-and-patient-support':'Beds & patient support', 'imaging-and-radiology':'Imaging & radiology',
'cardiac-diagnostics':'Cardiac diagnostics', 'laboratory-and-pathology':'Laboratory & pathology',
'surgery-and-procedures':'Surgery & procedures', 'orthopaedics':'Orthopaedics',
'womens-health-and-fertility':"Women's health & fertility", 'paediatrics-and-neonatal':'Paediatrics & neonatal',
'anatomy':'Anatomy', 'respiratory-and-sleep':'Respiratory medicine & sleep',
'emergency-and-trauma':'Emergency & trauma', 'rehabilitation':'Rehabilitation',
'patient-journey':'Patient journey', 'hospital-services':'Hospital services',
'clinical-equipment':'Clinical equipment', 'conditions':'Conditions'
}
EXTRA={
'icu':['intensive care unit'],'micu':['medical intensive care unit'],'sicu':['surgical intensive care unit'],
'ccu':['coronary care unit','cardiac care unit'],'nicu':['neonatal intensive care unit'],
'picu':['paediatric intensive care unit','pediatric intensive care unit'],'hdu':['high dependency unit'],
'pacu':['post anaesthesia care unit','post anesthesia care unit','recovery'],
'ent':['ear nose throat','otolaryngology'],'pcr':['polymerase chain reaction','molecular diagnostics'],
'ecmo':['extracorporeal membrane oxygenation'],'acl':['anterior cruciate ligament'],
'copd':['chronic obstructive pulmonary disease'],'ivf':['in vitro fertilisation','in vitro fertilization'],
'twelve-lead-ecg':['electrocardiography','ekg','ecg'],'mri-scanner':['magnetic resonance imaging'],
'ct-scanner':['computed tomography'],'pet-ct':['positron emission tomography'],
'cpap-bipap':['continuous positive airway pressure','bilevel positive airway pressure'],
'orthopaedics':['orthopedics'],'op-consultation':['outpatient','opd'],'treadmill-test':['tmt','exercise stress test'],
'c-arm':['c arm','mobile fluoroscopy'],'anaesthesia-workstation':['anesthesia machine']
}
def component_name(slug): return ''.join(x.title() for x in slug.split('-'))+'Icon'

assert set(ART)==set(ICONS)
manifest={'name':'Hospital Clinical Icons','version':'1.0.0','viewBox':'0 0 48 48',
    'catalogEntries':234,'uniqueIcons':219,'staticVariants':VARIANTS,'variantAliases':{'filled':'solid'},
    'beamIcons':len(BEAMS),'svgCount':len(ICONS)*3+len(BEAMS),
    'categories':[{'id':cat,'name':FRIENDLY[cat],'uniqueIcons':sum(v['category']==cat for v in ICONS.values())} for cat in GROUPS],
    'icons':[]}
gallery=[]
checksums=[]
for slug, record in ICONS.items():
    item=dict(record)
    item['component']=component_name(slug)
    item['keywords']=sorted(set([slug.replace('-',' '),item['name'],*item['aliases'],*EXTRA.get(slug,[])]))
    item['supportsBeam']=slug in BEAMS
    item['paths']={}
    item['viewBox']='0 0 48 48'
    contents={}
    for v in VARIANTS+(['beam'] if slug in BEAMS else []):
        file=ROOT/'svg'/item['category']/v/(slug+'.svg')
        file.parent.mkdir(parents=True,exist_ok=True)
        val=svg(ART[slug],'outline' if v=='beam' else v,slug,item['name'],BEAMS.get(slug) if v=='beam' else None)
        file.write_text(val,encoding='utf-8')
        contents[v]=val
        rel=file.relative_to(ROOT).as_posix()
        item['paths'][v]=rel
        checksums.append(hashlib.sha256(val.encode()).hexdigest()+'  '+rel)
    manifest['icons'].append(item)
    gallery.append({**item,'svg':contents})
(ROOT/'metadata').mkdir(exist_ok=True)
(ROOT/'metadata'/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
(ROOT/'metadata'/'catalog-coverage.json').write_text(json.dumps(CATALOG,indent=2,ensure_ascii=False)+'\n')
(ROOT/'metadata'/'sha256sums.txt').write_text('\n'.join(checksums)+'\n')
# Gallery and React exports are independent snapshots; see README before rebuilding.
lines=['# Hospital Clinical Icons - catalog','','219 unique drawings cover the 234 entries in the curated scope. All have outline, solid and duotone SVGs. Filled is an alias for solid, not a fourth duplicate file. There are 60 additional self-contained beam-animated SVGs.','','## Canonical files','']
for cat in GROUPS:
    lines+=['### '+FRIENDLY[cat],'','| Icon | Filename | Beam |','| --- | --- | --- |']
    for it in manifest['icons']:
        if it['category']==cat:
            lines.append(f"| {it['name']} | `{it['slug']}.svg` | {'Yes' if it['supportsBeam'] else '-'} |")
    lines+=['']
lines+=['## Full scope mapping (including repeated entries)','','Each number below corresponds to the previously curated 234-entry list. Repeated concepts resolve to one canonical SVG; they are not missing files.','','| # | Requested concept | Canonical category / filename |','| --- | --- | --- |']
for it in CATALOG:
    primary=ICONS[it['slug']]['category']
    lines.append(f"| {it['catalogNumber']} | {it['name']} | `{primary}/{it['slug']}.svg` |")
(ROOT/'CATALOG.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:manifest[k] for k in ['uniqueIcons','catalogEntries','beamIcons','svgCount']},indent=2))
