from collections import OrderedDict
GROUPS = OrderedDict([
('specialties', '''Cardiology|cardiology
Cardiothoracic Surgery|cardiothoracic-surgery
Vascular Surgery|vascular-surgery
Neurology|neurology
Neurosurgery|neurosurgery
Orthopaedics|orthopaedics
Spine Surgery|spine-surgery
Joint Replacement|joint-replacement
Sports Medicine|sports-medicine
General Surgery|general-surgery
Gastroenterology|gastroenterology
GI Surgery|gi-surgery
Hepatology|hepatology
Nephrology|nephrology
Urology|urology
Pulmonology|pulmonology
Endocrinology|endocrinology
Diabetology|diabetology
Rheumatology|rheumatology
Medical Oncology|medical-oncology
Surgical Oncology|surgical-oncology
Radiation Oncology|radiation-oncology
Haematology|haematology
Obstetrics & Gynaecology|obstetrics-gynaecology
Fertility / IVF|fertility-ivf
Paediatrics|paediatrics
Neonatology|neonatology
ENT|ent
Ophthalmology|ophthalmology
Dermatology|dermatology'''),
('critical-care-units', '''ICU|icu
MICU|micu
SICU|sicu
CCU|ccu
NICU|nicu
PICU|picu
HDU|hdu
Emergency Department|emergency-department
Trauma Centre|trauma-centre
Operation Theatre|operation-theatre
Recovery / PACU|pacu
Labour Room|labour-room
Dialysis Unit|dialysis-unit
Isolation Unit|isolation-unit'''),
('beds-and-patient-support', '''ICU Bed|icu-bed
Ventilated Patient Bed|ventilated-patient-bed
Bed with Patient Monitor|monitored-bed
Bed with IV|iv-bed
Bed with Oxygen|oxygen-bed
Neonatal Incubator|neonatal-incubator
Labour / Delivery Bed|delivery-bed
Dialysis Chair|dialysis-chair
Recovery Bed|recovery-bed'''),
('imaging-and-radiology', '''X-Ray Machine|x-ray-machine
Chest X-Ray|chest-x-ray
Bone X-Ray|bone-x-ray
CT Scanner|ct-scanner
MRI Scanner|mri-scanner
Ultrasound|ultrasound
Pregnancy Ultrasound|pregnancy-ultrasound
Mammography|mammography
PET-CT|pet-ct
C-Arm|c-arm
Fluoroscopy|fluoroscopy
Interventional Radiology|interventional-radiology'''),
('cardiac-diagnostics', '''12-Lead ECG|twelve-lead-ecg
Echocardiography|echocardiography
Holter Monitor|holter-monitor
Treadmill Test / TMT|treadmill-test
Coronary Angiography|coronary-angiography
Cardiac Catheterisation|cardiac-catheterisation
Pacemaker|pacemaker
Defibrillation|defibrillation'''),
('laboratory-and-pathology', '''Blood Sample Collection|blood-sample-collection
Vacutainer Set|vacutainer-set
Blood Culture|blood-culture
Histopathology|histopathology
Biopsy Sample|biopsy-sample
Cytology|cytology
PCR / Molecular Diagnostics|pcr
Blood Cell Analysis|blood-cell-analysis
Microbiology Culture|microbiology-culture
Blood Bank|blood-bank
Blood Transfusion|blood-transfusion
Pathology Slide|pathology-slide'''),
('surgery-and-procedures', '''Laparoscopic Surgery|laparoscopic-surgery
Robotic Surgery|robotic-surgery
Arthroscopy|arthroscopy
Endoscopy|endoscopy
Colonoscopy|colonoscopy
Bronchoscopy|bronchoscopy
Cardiac Surgery|cardiac-surgery
Neurosurgery|neurosurgery
Joint Replacement Surgery|joint-replacement
Spine Surgery|spine-surgery
Fracture Fixation|fracture-fixation
Caesarean Section|caesarean-section
Organ Transplant|organ-transplant
Angioplasty / Stent|angioplasty-stent
Dialysis|dialysis
Radiation Therapy|radiation-therapy'''),
('orthopaedics', '''Shoulder Joint|shoulder-joint
Shoulder Replacement|shoulder-replacement
Elbow Joint|elbow-joint
Wrist Joint|wrist-joint
Hip Joint|hip-joint
Hip Replacement|hip-replacement
Knee Joint|knee-joint
Knee Replacement|knee-replacement
ACL|acl
Meniscus|meniscus
Spine|spine
Scoliosis|scoliosis
Fracture Fixation|fracture-fixation
Plate and Screws|plate-screws
Intramedullary Nail|intramedullary-nail
External Fixator|external-fixator'''),
('womens-health-and-fertility', '''Uterus|uterus
Ovary|ovary
Female Reproductive System|female-reproductive-system
Pregnancy / Foetus|pregnancy-foetus
Foetal Medicine|foetal-medicine
Normal Delivery|normal-delivery
Caesarean Delivery|caesarean-section
Breastfeeding|breastfeeding
IVF|ivf
Egg Retrieval|egg-retrieval
Embryo|embryo
Embryo Transfer|embryo-transfer'''),
('paediatrics-and-neonatal', '''Newborn|newborn
Premature Baby|premature-baby
Baby Incubator|neonatal-incubator
Neonatal Ventilation|neonatal-ventilation
Mother and Baby|mother-baby
Paediatric Care|paediatrics
Child Development|child-development
Paediatric Surgery|paediatric-surgery'''),
('anatomy', '''Anatomical Heart|anatomical-heart
Coronary Arteries|coronary-arteries
Lungs|lungs
Bronchial Tree|bronchial-tree
Liver|liver
Pancreas|pancreas
Stomach|stomach
Intestine / GI Tract|gi-tract
Colon|colon
Kidneys|kidneys
Bladder|bladder
Prostate|prostate
Thyroid|thyroid
Uterus|uterus
Breast|breast
Spinal Column|spine
Knee Anatomy|knee-joint
Hip Anatomy|hip-joint'''),
('respiratory-and-sleep', '''Pulmonary Function Test|pulmonary-function-test
Spirometry|spirometry
Bronchoscopy|bronchoscopy
Nebulisation|nebulisation
Oxygen Therapy|oxygen-therapy
Mechanical Ventilation|mechanical-ventilation
CPAP / BiPAP|cpap-bipap
Sleep Study|sleep-study'''),
('emergency-and-trauma', '''Trauma Patient|trauma-patient
Resuscitation|resuscitation
CPR|cpr
Emergency Ventilation|emergency-ventilation
Emergency Bed|emergency-bed
Trauma Surgery|trauma-surgery
Polytrauma|polytrauma
Emergency Triage|emergency-triage
Code Blue|code-blue
Air Ambulance|air-ambulance'''),
('rehabilitation', '''Physiotherapy|physiotherapy
Gait Training|gait-training
Joint Rehabilitation|joint-rehabilitation
Sports Rehabilitation|sports-rehabilitation
Neuro Rehabilitation|neuro-rehabilitation
Pulmonary Rehabilitation|pulmonary-rehabilitation
Cardiac Rehabilitation|cardiac-rehabilitation
Occupational Therapy|occupational-therapy
Speech Therapy|speech-therapy'''),
('patient-journey', '''OP Consultation|op-consultation
Inpatient Admission|inpatient-admission
Day Care Admission|day-care-admission
Preoperative Assessment|preoperative-assessment
Surgery Scheduled|surgery-scheduled
Postoperative Care|postoperative-care
Patient Transfer|patient-transfer
Discharge|discharge
Follow-up Consultation|follow-up-consultation
Home Healthcare|home-healthcare'''),
('hospital-services', '''24/7 Emergency|round-the-clock-emergency
Preventive Health Check|preventive-health-check
Master Health Check|master-health-check
Executive Health Check|executive-health-check
Home Sample Collection|home-sample-collection
Home Nursing|home-nursing
Home Physiotherapy|home-physiotherapy
Pharmacy Delivery|pharmacy-delivery
International Patient Care|international-patient-care
Medical Tourism|medical-tourism
Organ Transplant Program|organ-transplant
Blood Donation|blood-donation
Palliative Care|palliative-care
Rehabilitation Program|rehabilitation-program'''),
('clinical-equipment', '''Ventilator|ventilator
Patient Monitor|patient-monitor
Infusion Pump|infusion-pump
Syringe Pump|syringe-pump
Dialysis Machine|dialysis-machine
Anaesthesia Workstation|anaesthesia-workstation
Surgical Robot|surgical-robot
C-Arm|c-arm
Incubator|neonatal-incubator
ECMO|ecmo
Heart-Lung Machine|heart-lung-machine
Cath Lab System|cath-lab-system'''),
('conditions', '''Heart Attack|heart-attack
Stroke|stroke
Coronary Artery Disease|coronary-artery-disease
Heart Failure|heart-failure
Diabetes|diabetes
Kidney Disease|kidney-disease
Kidney Stone|kidney-stone
Cancer|cancer
Arthritis|arthritis
Osteoporosis|osteoporosis
Asthma|asthma
COPD|copd
Liver Disease|liver-disease
High-Risk Pregnancy|high-risk-pregnancy
Cataract|cataract
Glaucoma|glaucoma''')
])
CATALOG=[]
ICONS=OrderedDict()
for cat, text in GROUPS.items():
    for row in text.splitlines():
        name, slug = row.split('|')
        entry={'catalogNumber':len(CATALOG)+1, 'name':name,'slug':slug,'category':cat}
        CATALOG.append(entry)
        if slug not in ICONS:
            ICONS[slug]={'slug':slug,'name':name,'category':cat,'categories':[cat],'aliases':[], 'catalogNumbers':[]}
        icon=ICONS[slug]
        if cat not in icon['categories']: icon['categories'].append(cat)
        if name != icon['name'] and name not in icon['aliases']: icon['aliases'].append(name)
        icon['catalogNumbers'].append(entry['catalogNumber'])
assert len(CATALOG)==234,len(CATALOG)
assert len(ICONS)==219,len(ICONS)
if __name__=='__main__':
    print(len(CATALOG),'catalog entries;',len(ICONS),'unique icons')
    for cat in GROUPS:
        print(cat, sum(i['category']==cat for i in ICONS.values()))
