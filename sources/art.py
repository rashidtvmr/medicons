"""Original vector recipes. Coordinates are in a 48 x 48 design grid."""
from copy import deepcopy

def N(tag, role='body', **attrs): return {'tag':tag, 'role':role, 'attrs':attrs}
def P(d, role='body', **a): return N('path',role,d=d,**a)
def L(d, **a): return P(d,'line',**a)
def D(d, **a): return P(d,'cut',**a)
def R(x,y,w,h,r=2,role='body',**a): return N('rect',role,x=x,y=y,width=w,height=h,rx=r,**a)
def C(x,y,r,role='body',**a): return N('circle',role,cx=x,cy=y,r=r,**a)
def E(x,y,rx,ry,role='body',**a): return N('ellipse',role,cx=x,cy=y,rx=rx,ry=ry,**a)
def G(nodes, x=0,y=0,s=1,rotate=0):
    t=f'translate({x} {y}) scale({s})'
    if rotate: t+=f' rotate({rotate} 24 24)'
    return {'tag':'g','attrs':{'transform':t},'children':deepcopy(nodes)}
def shift(nodes,x=0,y=0,s=1,rotate=0): return [G(nodes,x,y,s,rotate)]

def heart():
    return [P('M23 12 C19 6 9 10 8 20 C6 31 17 40 26 42 C33 36 40 29 39 21 C39 15 35 11 29 12 L29 6 L24 6 L24 12 Z'),
            P('M17 12 L15 7 L19 5 L22 11','accent'),
            D('M25 15 C20 18 20 24 25 30 C27 33 29 35 29 38 M22 23 L15 24 M25 29 L33 26 M25 16 L32 17')]
def brain():
    return [P('M24 8 C19 3 12 7 12 12 C5 12 4 22 8 25 C4 30 9 37 14 37 C15 44 22 43 24 39 C27 44 34 42 35 37 C42 36 43 30 40 25 C45 19 41 12 36 12 C36 6 29 3 24 8 Z'),
            D('M24 9 L24 38 M12 13 C18 12 20 16 18 20 M8 25 C13 22 18 25 18 29 M14 37 C12 31 17 29 20 32 M36 13 C30 12 28 16 30 20 M40 25 C34 22 30 25 30 29 M34 37 C36 32 31 29 28 32')]
def lungs():
    return [P('M20 14 C16 11 11 17 8 25 C5 33 5 39 10 40 C15 41 21 36 21 32 L21 18 Z'),
            P('M28 14 C32 11 37 17 40 25 C43 33 43 39 38 40 C33 41 27 36 27 32 L27 18 Z'),
            L('M24 6 L24 22 M24 21 L16 29 M24 21 L32 29'),D('M17 27 L13 26 M31 27 L35 26 M16 29 L15 34 M32 29 L33 34')]
def kidney_one():
    return [P('M26 8 C17 3 8 11 8 24 C8 38 18 44 26 38 C32 34 27 29 23 29 C19 29 17 27 17 24 C17 20 19 18 23 18 C29 18 31 12 26 8 Z'),D('M23 12 C16 10 12 17 12 24 C12 32 16 37 22 35')]
def kidneys():
    return shift(kidney_one(),1,5,.72)+[G(kidney_one(),47,5,-.72)]+[L('M19 23 C22 25 20 31 21 37 M29 23 C26 25 28 31 27 37')]
# The mirrored right kidney needs a positive vertical scale.
def kidneys():
    return [G(kidney_one(),0,5,.73),{'tag':'g','attrs':{'transform':'translate(48 5) scale(-0.73 0.73)'},'children':kidney_one()},L('M18 23 C22 23 20 32 21 39 M30 23 C26 23 28 32 27 39')]
def liver():
    return [P('M7 17 C13 12 26 9 38 12 C44 13 43 21 39 23 L25 28 C19 30 12 39 8 35 C4 30 4 22 7 17 Z'),D('M27 12 L25 27 M9 22 C14 18 19 17 23 17'),P('M29 27 C34 28 34 35 29 36 C26 35 27 29 29 27 Z','accent')]
def stomach():
    return [P('M23 5 L23 15 C23 20 27 21 30 17 C35 11 43 15 42 25 C41 36 33 42 23 40 C18 39 16 34 12 34 L6 34 L6 28 L12 28 C15 28 16 32 20 30 C25 27 16 24 17 17 L17 5 Z'),D('M30 23 C37 19 38 29 31 33 C27 36 23 33 21 34')]
def colon():
    return [P('M12 39 L12 17 C8 14 11 8 16 10 C20 7 23 8 25 10 C29 7 32 8 34 11 C39 10 41 14 38 18 L38 29 C38 34 31 35 30 37 L30 43 L24 43 L24 36 C24 29 31 30 32 27 L32 18 L18 18 L18 39 Z'),D('M13 17 L17 18 M20 10 L20 16 M28 10 L28 16 M33 22 L37 22 M31 31 L34 34')]
def uterus():
    return [P('M18 17 C21 13 27 13 30 17 C33 23 28 28 27 32 L27 41 L21 41 L21 32 C20 28 15 23 18 17 Z'),
            L('M18 18 C13 8 5 10 6 18 M30 18 C35 8 43 10 42 18'),E(10,21,4,3,'accent'),E(38,21,4,3,'accent'),D('M23 20 C21 23 23 26 24 29 C25 26 27 23 25 20 M24 31 L24 39')]
def thyroid():
    return [P('M20 15 C15 8 8 9 8 18 C8 28 13 40 19 36 C21 34 21 28 24 28 C27 28 27 34 29 36 C35 40 40 28 40 18 C40 9 33 8 28 15 L27 21 L21 21 Z'),D('M24 6 L24 17 M21 10 L27 10 M21 14 L27 14 M22 24 L26 24')]
def eye():
    return [P('M5 24 C14 10 34 10 43 24 C34 38 14 38 5 24 Z'),C(24,24,8,'accent'),C(24,24,3,'cut')]
def bone():
    return [P('M17 7 C14 4 8 6 9 11 C4 14 7 20 12 19 L29 36 C28 42 35 44 38 40 C43 42 46 36 42 33 C45 28 39 25 35 28 L18 12 C20 10 20 8 17 7 Z'),D('M16 18 L30 32')]
def knee():
    return [P('M16 5 L29 5 L29 17 C35 23 31 28 26 25 C23 29 15 25 17 20 Z'),P('M16 31 C19 27 24 28 26 30 C29 27 33 29 32 33 L29 43 L19 43 Z'),E(35,23,3,5,'accent'),D('M20 9 L20 18 M22 34 L23 40 M32 32 L36 42')]
def hip():
    return [P('M8 6 C6 14 7 21 14 25 C19 28 22 24 24 20 C27 15 21 10 22 6 Z'),D('M11 10 C10 17 13 21 17 22'),P('M24 25 C18 27 19 20 23 19 C28 17 33 21 32 26 L37 32 L36 43 L27 43 L27 33 Z'),D('M24 23 L29 26 M31 33 L31 40')]
def spine(curved=False):
    nodes=[]
    offsets=[0,1,2,1,-1,-2] if curved else [0]*6
    for i,dx in enumerate(offsets):
        y=5+i*5.4
        nodes += [R(18+dx,y,12,4,1.5),L(f'M{18+dx} {y+2} L{13+dx} {y+2} M{30+dx} {y+2} L{35+dx} {y+2}')]
    nodes += [P('M18 38 L30 38 L24 44 Z')]
    return nodes

def fetus():
    return [P('M20 7 C32 5 41 13 40 25 C39 38 28 45 17 40 C7 37 5 27 8 17 C10 11 15 8 20 7 Z'),C(25,20,5,'accent'),D('M21 25 C16 25 15 34 22 35 C28 36 33 30 29 28 M19 30 L25 31 M25 24 L29 28 M33 15 C37 23 33 32 29 34')]
def newborn():
    return [P('M24 7 C17 7 13 13 14 20 L8 30 C8 39 16 44 24 43 C32 44 40 38 40 30 L34 20 C35 13 31 7 24 7 Z'),C(24,16,7,'accent'),D('M12 26 L31 37 M34 24 L15 35 M14 39 L34 30 M21 15 L21.2 15 M27 15 L27.2 15 M22 19 Q24 21 26 19')]
def ribbon():
    return [P('M24 6 C15 6 12 14 16 21 L29 43 L36 37 L23 16 C21 12 26 11 27 15 L12 37 L19 43 L32 21 C37 13 32 6 24 6 Z'),D('M17 14 C20 8 28 8 31 14 M19 24 L23 30')]
def cell(x=24,y=24,r=15):
    return [C(x,y,r),C(x-2,y+1,r*.32,'accent'),D(f'M{x-7} {y-7} l2 -1 M{x+6} {y-5} l2 2 M{x+5} {y+7} l-1 2')]
def vessel():
    return [P('M14 5 L22 5 L22 19 L33 8 L39 14 L25 28 L25 43 L16 43 L16 25 L6 15 L12 9 L17 14 Z'),D('M18 8 L18 19 L10 13 M20 38 L20 26 L34 12')]
def dna():
    return [L('M15 5 C38 17 10 31 33 43 M33 5 C10 17 38 31 15 43'),L('M18 8 L30 8 M19 15 L29 15 M20 22 L28 22 M20 28 L28 28 M19 35 L29 35 M18 40 L30 40')]
def scalpel():
    return [P('M31 7 L39 13 L23 30 L18 25 Z'),P('M17 26 L22 31 L10 43 C5 40 7 35 10 32 Z','accent'),D('M30 12 L33 15')]
def small_scalpel(): return shift(scalpel(),20,19,.54)
def suture(x=24,y=23):
    return [L(f'M{x-10} {y} L{x+10} {y} M{x-6} {y-3} L{x-6} {y+3} M{x} {y-3} L{x} {y+3} M{x+6} {y-3} L{x+6} {y+3}')]
def ecg(d='M5 25 H13 L17 18 L22 34 L27 14 L31 25 H43'): return [L(d)]
def monitor():
    return [R(6,6,36,27,3),D('M10 22 H17 L20 15 L25 27 L29 19 H38 M24 34 L24 40 M15 41 L33 41')]
def bed(patient=True):
    nodes=[R(5,26,38,7,2),L('M6 20 L6 39 M42 27 L42 39 M6 36 H42'),C(10,41,2),C(38,41,2)]
    if patient: nodes += [C(13,21,4,'accent'),P('M18 25 L18 19 L29 19 C34 19 37 22 38 26 Z')]
    return nodes

def mini_monitor(x=27,y=4,s=.45): return shift(monitor(),x,y,s)
def ward_frame(): return [L('M5 40 V10 Q5 6 9 6 H39 Q43 6 43 10 V40')]
def incubator():
    return [P('M9 24 V17 C9 8 39 8 39 17 V24 Z'),R(6,24,36,7,2),L('M12 32 V40 M36 32 V40 M10 40 H38'),C(12,42,2),C(36,42,2),C(18,20,3,'cut'),P('M22 23 L22 18 Q31 16 33 23 Z','cut'),D('M13 17 L15 14 M34 14 L36 17')]
def oxygen():
    return [R(15,12,18,31,5),R(19,6,10,6,1),L('M24 6 V3 M19 3 H29'),D('M20 19 L28 19 M20 36 H28')]
def iv():
    return [L('M26 6 V41 M18 42 H34 M15 8 H33'),R(9,11,13,17,2),D('M12 22 H19 M15.5 15 V18'),L('M15 28 V32 C15 39 7 34 7 41')]
def ventilator():
    return [R(8,7,27,24,3),D('M12 21 H16 L19 14 L23 25 L27 18 H31 M13 27 H17 M27 27 H30'),L('M21 32 V40 M11 42 H32 M35 14 C44 12 43 26 41 29 L37 31'),C(11,43,1.8),C(32,43,1.8)]
def dialysis_machine():
    return [R(12,5,25,34,3),R(17,10,15,10,1,'cut'),D('M18 16 H21 L24 12 L27 17 H30'),C(20,28,4,'cut'),C(30,28,3,'cut'),L('M17 40 V43 M32 40 V43 M12 13 C4 10 4 33 11 31 M37 24 C45 23 43 35 38 34')]
def ct():
    return [P('M7 29 V19 C7 2 39 2 39 19 V29 Z'),E(23,20,9,11,'cut'),P('M21 27 L30 27 L42 39 L13 39 Z','accent'),L('M15 39 V43 M39 39 V43'),D('M23 30 L31 36 M10 25 H12')]
def mri():
    return [P('M7 29 V19 C7 5 19 4 28 5 L37 9 C43 14 42 22 40 29 Z'),E(19,20,8,11,'cut'),P('M16 27 H24 L37 40 H7 Z','accent'),L('M10 40 V44 M34 40 V44'),D('M31 11 C36 14 37 21 35 25 M19 30 L26 37')]
def ultrasound():
    return [R(5,6,28,22,3),D('M11 12 L9 22 Q19 27 29 22 L26 12 M13 18 Q19 15 25 19'),P('M8 30 H31 L34 37 H5 Z','accent'),L('M10 37 V43 M28 37 V43 M33 15 C44 12 40 29 42 30'),R(37,29,7,9,2,'accent')]
def robot():
    return [P('M7 42 L11 35 H25 L29 42 Z'),R(13,25,10,10,2),C(18,23,4,'accent'),L('M18 19 L10 13 L18 7 L29 15 L37 7'),C(10,13,3),C(18,7,3),C(29,15,3),L('M37 7 L42 12 M40 10 L42 6 M40 10 L36 12'),D('M18 29 V32')]
def chair():
    return [P('M10 11 Q11 7 15 9 L23 25 H36 L42 32 H22 L11 18 Z'),L('M17 24 L12 38 M33 33 V41 M12 41 H39'),D('M16 15 L25 30 H36')]
def body_outline():
    return [C(24,8,4),P('M18 15 C15 15 14 19 13 29 L18 30 L19 24 L18 43 H23 L24 31 L25 43 H30 L29 24 L30 30 L35 29 C34 19 33 15 30 15 Z')]
def torso():
    return [P('M15 6 L20 9 H28 L33 6 L41 13 L35 20 L34 41 H14 L13 20 L7 13 Z'),D('M20 10 Q24 16 28 10')]
def home_frame(): return [L('M5 22 L24 6 L43 22 M9 22 V42 H39 V22')]
def clinician():
    return [C(17,11,5),P('M7 38 V26 C7 17 27 17 27 26 V38 Z'),D('M13 21 L17 29 L21 21 M17 29 V37'),L('M11 23 V29 Q11 34 16 34'),C(22,30,2,'cut')]
def vial():
    return [R(15,7,18,6,1),R(17,13,14,29,4),D('M20 29 H28 M20 25 H24 M20 34 H28'),P('M18 32 H30 V37 Q24 45 18 37 Z','accent')]
def petri():
    return [E(24,24,18,13),D('M7 23 C7 36 41 36 41 23'),C(17,21,3,'accent'),C(29,26,4,'accent'),C(30,18,2,'accent'),D('M17 20 L17 22 M27 26 H31')]
def rehab_person():
    return [C(22,8,4),L('M22 14 L20 26 L11 39 M20 26 L31 34 L36 42 M22 15 L33 19 L40 15 M22 15 L12 23 L6 23')]

ART={}
BEAMS={}
def add(slug,nodes,beam=None):
    if slug in ART: raise ValueError('duplicate recipe: '+slug)
    ART[slug]=nodes
    if beam: BEAMS[slug]=beam

# Core anatomy: purpose-built medical silhouettes, not generic UI hearts/bones.
add('anatomical-heart',heart(),'M24 8 V13 C16 17 19 25 25 30 L29 38')
add('coronary-arteries',heart()+[D('M21 18 L13 17 M22 24 L14 30 M25 29 L33 33 M27 16 L33 21')],'M13 17 L21 18 L22 24 L25 29 L33 33')
add('lungs',lungs(),'M24 6 V21 L16 29 L15 34')
add('bronchial-tree',[L('M24 5 V22 L13 32 M24 22 L35 32 M13 32 L6 30 M13 32 L11 40 M35 32 L42 30 M35 32 L37 40 M17 28 L13 21 M31 28 L35 21'),D('M21 9 H27 M21 14 H27 M21 19 H27')])
add('liver',liver())
add('pancreas',[P('M6 27 C7 22 12 20 16 22 C21 18 26 21 29 17 C36 13 44 18 41 24 C38 30 32 26 29 30 C23 33 17 29 14 33 C10 37 5 33 6 27 Z'),D('M11 28 C17 25 21 29 27 25 L36 21'),L('M10 17 C3 17 3 39 11 40')])
add('stomach',stomach())
add('gi-tract',shift(stomach(),8,1,.53)+[R(8,25,32,17,5),D('M14 30 H33 Q37 34 32 34 H17 Q12 38 18 38 H31'),L('M25 42 V45')])
add('colon',colon())
add('kidneys',kidneys(),'M18 20 C23 25 19 31 21 39')
add('bladder',[L('M10 6 C11 17 17 16 17 21 M38 6 C37 17 31 16 31 21'),P('M11 26 C11 15 37 15 37 26 C37 32 31 36 27 37 V43 H21 V37 C17 36 11 32 11 26 Z'),D('M16 26 C16 32 32 32 32 26')])
add('prostate',[P('M12 7 H36 V16 C36 24 12 24 12 16 Z'),P('M14 28 C16 23 21 25 24 27 C27 25 32 23 34 28 C39 38 28 42 24 37 C20 42 9 38 14 28 Z','accent'),D('M24 20 V43 M20 30 L20 33 M28 30 L28 33')])
add('thyroid',thyroid())
add('breast',[P('M18 6 C16 15 9 18 8 28 C7 39 22 44 31 36 C36 31 35 27 42 22 L38 7'),D('M21 12 C19 21 13 23 13 29 C13 35 22 38 27 34'),C(30,27,2,'accent')])

# Specialty navigation icons: clinical combinations retain the underlying organ.
add('cardiology',shift(heart(),2,0,.86)+ecg('M23 35 H28 L31 28 L35 40 L38 34 H44'),'M24 35 H28 L31 28 L35 40 L38 34 H44')
add('cardiothoracic-surgery',shift(heart(),3,5,.76)+[L('M37 7 V41 M33 13 H41 M33 21 H41 M33 29 H41 M33 37 H41')])
add('vascular-surgery',shift(vessel(),-1,0,.85)+small_scalpel(),'M14 8 V19 L21 27 V37')
add('neurology',brain()+[C(17,20,1.6,'dot'),C(31,30,1.6,'dot')],'M12 13 C18 12 20 16 18 20 L24 24 L30 29 L34 37')
add('neurosurgery',shift(brain(),0,0,.83)+small_scalpel())
add('orthopaedics',shift(knee(),-1,0,.92)+[L('M39 10 V20 M35 15 H43')])
add('spine-surgery',shift(spine(),-2,0,.84)+small_scalpel())
add('joint-replacement',shift(knee(),-1,0,.9)+[P('M15 26 H27 L29 29 H16 Z','accent'),D('M21 29 V36')])
add('sports-medicine',rehab_person()+[R(25,29,8,5,1,'accent',transform='rotate(35 29 31.5)')])
add('general-surgery',[P('M10 8 L17 11 H31 L38 8 L41 17 L34 22 L33 41 H13 L12 22 L5 17 Z'),D('M20 12 Q24 18 28 12')]+suture(24,29))
add('gastroenterology',shift(stomach(),1,-1,.78)+[L('M10 36 Q8 42 16 42 H34 Q40 39 34 36 H22')])
add('gi-surgery',shift(stomach(),-1,-1,.82)+small_scalpel())
add('hepatology',liver()+[C(35,36,5,'accent'),D('M32 36 H38 M35 33 V39')])
add('nephrology',kidneys()+[P('M24 29 C19 35 21 39 24 39 C28 39 29 35 24 29 Z','accent')])
add('urology',shift(kidneys(),5,-2,.8)+[P('M17 33 C17 28 31 28 31 33 Q31 39 26 40 V44 H22 V40 Q17 39 17 33 Z','accent')])
add('pulmonology',lungs()+[L('M8 8 Q4 12 5 16 M40 8 Q44 12 43 16')],'M24 6 V21 L32 29 L33 34')
add('endocrinology',shift(thyroid(),-1,2,.9)+[C(39,11,3,'accent'),C(40,34,2,'accent'),L('M34 18 L37 14 M34 30 L38 33')])
add('diabetology',[R(7,10,20,32,3),R(11,15,12,10,1,'cut'),C(17,33,3,'cut'),P('M35 6 C31 12 29 15 29 18 C29 26 42 26 42 18 C42 15 39 10 35 6 Z','accent'),D('M12 21 H16 L19 18 L22 21')])
add('rheumatology',shift(knee(),-3,0,.85)+[L('M34 16 L40 13 M35 22 H43 M34 28 L40 32')])
add('medical-oncology',shift(ribbon(),-2,0,.85)+[P('M31 30 C36 25 43 32 39 36 L33 42 C29 46 22 39 26 35 Z','accent'),D('M29 32 L36 39')])
add('surgical-oncology',shift(ribbon(),-3,0,.9)+small_scalpel())
add('radiation-oncology',[C(24,26,9),C(24,26,3,'accent'),P('M5 12 L10 5 L20 17 L16 20 Z','accent'),P('M38 6 L43 12 L31 20 L28 16 Z','accent'),P('M21 38 L27 38 L28 44 H20 Z','accent'),L('M12 15 L17 21 M37 15 L31 21 M24 35 V40')],'M9 8 L24 26 L40 10')
add('haematology',[E(15,17,10,8),E(15,17,4,3,'cut'),C(32,30,10,'accent'),D('M27 28 C27 24 32 26 32 28 C37 27 38 33 33 34 C32 37 26 34 28 31'),C(11,36,2,'dot'),C(39,10,2,'dot')])
add('obstetrics-gynaecology',shift(uterus(),-2,0,.88)+[C(37,34,7,'accent'),D('M37 28 Q31 34 37 39 M36 33 L39 35')])
add('fertility-ivf',[C(20,25,14),C(20,25,9,'cut'),C(18,24,3,'accent'),L('M29 18 L39 7 M35 8 L40 13 M39 6 L43 10')],'M41 7 L29 19 L22 25')
add('paediatrics',shift(newborn(),-1,2,.79)+[P('M31 31 C27 23 38 23 37 30 C43 27 46 35 38 40 Z','accent')])
add('neonatology',shift(incubator(),0,4,.94)+[L('M15 7 H20 L23 3 L26 10 L29 7 H34')])
add('ent',[P('M8 12 C8 3 22 3 23 13 C24 19 18 20 16 27 C14 31 8 29 9 24'),D('M12 13 C13 8 20 11 18 15 L14 18'),P('M31 7 L28 24 Q33 28 38 23 L35 17','accent'),L('M23 36 Q33 30 42 36 Q33 43 23 36 M27 36 H38')])
add('ophthalmology',eye()+[L('M8 10 L5 6 M24 9 V4 M40 10 L43 6')])
add('dermatology',[P('M6 22 C13 16 17 26 24 21 C31 16 36 22 42 18 V40 H6 Z'),D('M7 31 Q13 27 19 31 T31 31 T41 31 M13 35 V37 M25 35 V37 M37 35 V37'),L('M16 24 C14 17 18 11 15 6 M30 23 C28 15 32 11 31 5'),C(23,14,2,'accent')])

# Purpose-built rooms and high-acuity care environments.
add('icu',ward_frame()+shift(bed(),1,20,.48)+shift(bed(),24,20,.48)+mini_monitor(15,8,.38),'M19 17 H21 L22 14 L24 19 L25 16 H28')
add('micu',shift(bed(),0,7,.9)+shift(lungs(),21,-1,.5)+[L('M7 8 H16 V16')])
add('sicu',shift(bed(),0,7,.9)+suture(21,11)+[L('M39 6 V18 H32')])
add('ccu',shift(bed(),0,7,.9)+shift(heart(),23,1,.49)+ecg('M5 13 H10 L13 7 L17 18 L20 12 H24'),'M5 13 H10 L13 7 L17 18 L20 12 H24')
add('nicu',ward_frame()+shift(incubator(),3,14,.68)+mini_monitor(27,7,.36),'M31 15 H33 L34 12 L36 17 L37 14 H41')
add('picu',ward_frame()+shift(bed(False),2,9,.85)+[C(18,27,3,'accent'),P('M23 31 V25 Q31 23 34 31 Z','accent'),R(13,13,10,8,1),D('M16 17 H20'),L('M18 22 V26')])
add('hdu',ward_frame()+shift(chair(),1,16,.63)+mini_monitor(24,12,.4)+[L('M33 27 V38')])
add('emergency-department',[P('M5 43 V15 L24 5 L43 15 V43 Z'),R(10,22,28,16,1,'cut'),L('M24 23 V37'),P('M22 10 L18 18 H23 L21 23 L30 15 H25 L27 10 Z','accent')])
add('trauma-centre',ward_frame()+shift(bed(),0,5,.95)+[P('M18 11 H28 L26 22 H20 Z','accent'),D('M18 17 H28 M23 11 V22'),L('M9 12 V20 M5 16 H13 M38 12 V20 M34 16 H42')])
add('operation-theatre',[L('M24 4 V10'),P('M14 14 L18 9 H30 L34 14 L31 20 H17 Z'),D('M19 15 H29'),shift(bed(False),0,7,.9)[0],C(12,25,3,'accent'),P('M16 29 L18 23 H29 L35 29 Z','accent'),L('M43 24 V42 M39 25 H43')],'M18 14 H30')
add('pacu',shift(bed(),0,7,.9)+[L('M10 14 C17 2 33 5 38 15 M33 13 L39 16 L40 9'),C(37,27,4,'accent'),D('M37 24 V27 L39 29')])
add('labour-room',ward_frame()+shift(chair(),0,17,.7)+[C(21,22,3,'accent'),L('M22 26 L28 31 L34 27 M31 30 L35 35')]+shift(fetus(),30,9,.26))
add('dialysis-unit',ward_frame()+shift(chair(),0,14,.62)+shift(dialysis_machine(),24,13,.46)+[L('M25 29 C20 22 23 21 21 19')],'M29 23 C21 20 24 29 19 28')
add('isolation-unit',[R(7,5,34,39,3),L('M25 7 V42'),R(10,11,12,21,1,'cut'),C(31,25,1.8,'cut'),L('M13 17 H20 M13 23 H20 M15 29 H20'),P('M29 9 L35 9 L37 17 L27 17 Z','accent'),D('M32 11 V15')])

# Patient support: position, attachments and context differentiate these from a bed glyph.
add('icu-bed',shift(bed(),0,5,.89)+mini_monitor(23,0,.48)+[L('M10 26 V30 M14 26 V30 M18 26 V30 M10 27 H18')],'M28 11 H31 L32 7 L35 13 L37 9 H41')
add('ventilated-patient-bed',shift(bed(),-1,8,.87)+shift(ventilator(),28,1,.41)+[L('M34 14 C24 11 22 24 11 26')],'M40 14 C25 10 21 25 11 27')
add('monitored-bed',shift(bed(),0,7,.9)+mini_monitor(24,0,.43)+[L('M35 18 L28 25')])
add('iv-bed',shift(bed(),0,7,.88)+shift(iv(),27,0,.54))
add('oxygen-bed',shift(bed(),-1,8,.85)+shift(oxygen(),29,2,.45)+[L('M41 7 C32 5 30 18 27 21 L13 27')])
add('neonatal-incubator',incubator(),'M12 15 C15 9 33 9 37 15')
add('delivery-bed',[P('M7 15 Q8 11 12 12 L23 28 H32 L36 33 H22 L9 22 Z'),L('M18 29 V39 M13 40 H31 M33 28 L39 22 M31 32 L39 36 M39 18 V25 M39 33 V40'),R(36,17,7,4,1,'accent'),R(36,39,7,4,1,'accent'),D('M11 17 L24 30')])
add('dialysis-chair',shift(chair(),0,1,.97)+[L('M35 7 V22 M31 8 H41'),R(33,11,6,10,1,'accent'),L('M36 21 C36 26 29 25 26 26')])
add('recovery-bed',[P('M6 17 L12 16 L22 29 H39 L43 35 H21 L7 24 Z'),L('M14 30 V39 M38 36 V40'),C(14,42,2),C(38,42,2),C(14,15,4,'accent'),D('M15 22 L24 32 H36')])

# Imaging equipment is distinguished by the gantry, patient position and detector.
add('x-ray-machine',[L('M12 5 V42 M5 43 H20 M12 10 H32'),R(29,6,11,13,2),D('M32 15 H37'),L('M25 23 L20 30 M34 23 L39 30'),P('M22 34 H40 L43 39 H19 Z','accent'),L('M23 39 V44 M38 39 V44')],'M34 20 L25 32')
add('chest-x-ray',[R(5,4,38,40,3)]+shift(lungs(),7,9,.69)+[D('M24 13 V35 M9 9 H13 M35 39 H39')])
add('bone-x-ray',[R(5,4,38,40,3)]+shift(bone(),7,8,.67)+[D('M9 9 H13 M35 39 H39')])
add('ct-scanner',ct(),'M14 20 C14 5 32 5 32 20 C32 26 28 30 24 31')
add('mri-scanner',mri(),'M11 21 C11 7 27 7 27 21')
add('ultrasound',ultrasound(),'M19 12 L10 22 Q19 27 28 22 L19 12')
add('pregnancy-ultrasound',[R(5,5,38,30,3),P('M24 10 L12 27 Q24 34 36 27 Z','accent'),C(25,19,3,'cut'),D('M22 22 C17 24 21 29 26 27 L28 24 M18 40 H30 M24 36 V40')],'M24 11 L13 27 Q24 32 35 27')
add('mammography',[R(7,5,10,37,2),R(16,7,21,8,2,'accent'),L('M17 24 H35 M18 32 H38'),R(24,24,10,4,1),P('M41 10 C37 14 37 21 40 24 L43 24 L43 32 C38 33 36 36 36 43'),D('M10 12 V18')])
add('pet-ct',ct()+[C(22,19,4,'accent'),D('M22 15 V23 M18 19 H26'),L('M42 8 V15 M38 11 H45')],'M14 20 C14 5 32 5 32 20 C32 26 28 30 24 31')
add('c-arm',[P('M33 8 C16 2 5 14 10 27 C13 35 22 38 31 35 L29 29 C21 32 16 27 15 22 C13 14 21 10 29 14 Z'),R(28,5,11,10,2,'accent'),R(27,28,11,10,2,'accent'),L('M7 23 H3 V40 H18 M23 22 H44 M38 22 V43'),D('M33 8 V12 M30 32 H35')],'M30 11 C11 2 6 34 30 32')
add('fluoroscopy',[R(6,6,20,17,2),D('M10 10 H22 V19 H10 Z M15 11 L20 18'),L('M16 24 V37 M6 41 H25 M34 5 V19'),R(29,14,12,7,1,'accent'),P('M25 31 H39 L44 36 H22 Z'),L('M26 36 V43 M40 36 V43')])
add('interventional-radiology',[R(4,5,23,19,2),D('M8 10 L15 14 L10 20 M15 14 L23 11'),L('M16 25 V32 M7 34 H24'),P('M26 39 C27 28 40 27 42 38 L42 43 H25 Z','accent'),L('M25 17 C37 16 34 25 32 30'),C(32,29,2,'accent')])

# Cardiac tests and interventions.
add('twelve-lead-ecg',shift(torso(),-1,-2,.75)+[R(27,27,17,15,2),D('M30 36 H33 L35 31 L38 38 L40 34 H42'),L('M12 20 L28 31 M18 22 L28 34 M24 20 L28 28')]+[C(x,y,1.2,'accent') for x,y in [(12,20),(18,22),(24,20),(22,15),(17,14),(10,15)]],'M30 36 H33 L35 31 L38 38 L40 34 H42')
add('echocardiography',shift(heart(),-1,4,.8)+[R(31,9,10,15,2,'accent',transform='rotate(25 36 16)'),L('M38 10 C38 3 44 3 44 7 M32 24 L27 29'),D('M32 15 L39 18')],'M35 24 L24 30 L22 22')
add('holter-monitor',torso()+[R(19,24,13,14,2,'accent'),D('M23 28 H28 M23 33 H25'),L('M21 25 L17 19 M29 24 L32 18'),C(16,18,2,'cut'),C(32,17,2,'cut')])
add('treadmill-test',[C(25,7,4),L('M25 13 L20 24 L11 28 M20 24 L30 33 M23 16 L34 20 L40 16'),P('M6 37 H37 L43 43 H6 Z'),L('M39 17 V37 M34 17 H43'),D('M12 40 H34')])
add('coronary-angiography',heart()+[L('M40 39 C45 31 39 21 28 19'),D('M28 19 C23 17 19 24 25 31')],'M41 39 C45 31 39 21 28 19 C23 17 19 24 25 31')
add('cardiac-catheterisation',shift(torso(),-2,0,.86)+shift(heart(),15,10,.31)+[L('M43 41 C34 43 36 26 24 23'),D('M24 23 L22 18')],'M43 41 C34 43 36 26 24 23 L22 18')
add('pacemaker',[R(6,7,21,17,6),D('M12 13 H21 M13 18 H18'),L('M25 11 C40 8 45 20 38 31 M25 16 C34 16 29 23 30 29')]+shift(heart(),18,20,.52))
add('defibrillation',[R(5,18,26,24,3),R(10,23,16,9,1,'cut'),D('M13 28 H16 L18 25 L20 29 H23'),C(14,37,2,'cut'),L('M9 17 C3 5 17 3 18 12 M25 17 C28 10 37 12 38 21'),R(12,7,11,7,2,'accent'),R(33,21,10,10,2,'accent'),D('M35 25 H41')])

# Laboratory: sampling, handling and analysis, not a repeated test tube.
add('blood-sample-collection',[P('M5 32 L16 26 L26 28 L39 23 L43 30 L28 37 L17 34 L9 40 Z'),D('M17 30 L26 32'),R(18,8,7,13,1,'accent',transform='rotate(25 21.5 14.5)'),L('M17 10 L29 15 M22 21 L18 29'),C(18,29,1.3,'accent')])
add('vacutainer-set',[R(5,30,38,11,2),D('M10 35 H14 M22 35 H26 M34 35 H38')]+sum(([R(x,10,8,5,1,'accent'),P(f'M{x+1} 15 H{x+7} V29 Q{x+4} 34 {x+1} 29 Z'),D(f'M{x+2} 24 H{x+6}')] for x in [8,20,32]),[]))
add('blood-culture',[R(7,9,12,6,1),R(6,15,14,27,4),R(29,5,12,6,1),R(28,11,14,31,4),D('M9 24 H17 M31 20 H39 M10 32 L15 34 M32 29 L36 26 M33 35 L38 33')])
add('histopathology',[R(5,5,27,37,2),D('M10 10 H23 M10 36 H18'),P('M10 19 C16 13 27 16 27 24 C22 31 13 32 10 25 Z','accent'),C(19,23,3,'cut'),C(35,32,8),D('M32 29 L34 32 L38 29 M34 32 L34 36')])
add('biopsy-sample',[R(25,24,17,18,3),R(23,20,21,5,1,'accent'),P('M7 9 L12 5 L30 21 L26 25 Z'),D('M10 10 L25 23 M30 30 H37 M30 36 H34'),P('M31 31 Q38 26 38 33 Q34 38 31 35 Z','accent')])
add('cytology',[C(24,24,18),P('M12 22 C9 17 17 13 21 17 C26 14 32 18 30 23 C38 24 34 35 27 34 C21 39 14 34 16 29 C10 28 9 25 12 22 Z','accent'),C(23,25,4,'cut'),C(35,13,2,'dot')])
add('pcr',[R(5,21,38,22,3),D('M11 35 H19 M11 39 H16 M26 36 H36'),R(25,26,12,6,1,'cut')]+shift(dna(),11,1,.49)+[L('M11 26 L14 29 M17 26 L20 29')],'M19 3 C30 9 16 16 27 21')
add('blood-cell-analysis',[R(4,5,28,30,3),D('M9 11 H15 M9 17 H17 M9 23 H13 M9 29 H19'),C(33,31,10,'accent'),E(31,29,4,3,'cut'),C(37,35,2,'cut'),L('M30 41 L30 43 M36 41 V43')])
add('microbiology-culture',petri()+[L('M9 10 L12 13 M38 10 L35 13')])
add('blood-bank',[R(6,5,36,39,3),D('M24 7 V42 M10 11 H18 M28 11 H36 M9 35 H39'),P('M15 18 C9 25 10 30 15 30 C20 30 21 25 15 18 Z','accent'),P('M33 18 C27 25 28 30 33 30 C38 30 39 25 33 18 Z','accent')])
add('blood-transfusion',[R(9,5,21,25,4),D('M14 10 H25'),P('M20 13 C14 20 15 24 20 24 C25 24 26 20 20 13 Z','accent'),L('M20 31 V35 C20 42 40 43 40 34 V29'),R(36,23,8,7,1,'accent')],'M20 29 V35 C20 42 40 43 40 34 V29')
add('pathology-slide',[R(5,12,38,24,2),R(6,13,9,22,1,'accent'),D('M8 18 H12 M8 23 H12'),P('M23 18 Q31 14 35 22 Q39 29 29 31 Q20 29 23 18 Z','accent'),C(29,24,3,'cut')])

# Surgical procedures: each includes the organ or actual instrument context.
add('laparoscopic-surgery',[P('M13 5 L18 9 H30 L35 5 L39 14 L34 21 V42 H14 V21 L9 14 Z'),D('M20 11 Q24 17 28 11 M23 25 V36'),C(20,24,2,'cut'),C(28,28,2,'cut'),L('M6 7 L20 24 M42 10 L28 28'),R(3,4,9,4,1,'accent',transform='rotate(44 7 6)'),R(35,6,9,4,1,'accent',transform='rotate(-46 39 8)')])
add('robotic-surgery',shift(robot(),-1,0,.78)+shift(bed(),15,18,.61)+[L('M31 13 L36 22 M28 19 L26 27')],'M12 10 L19 6 L25 13 L29 7')
add('arthroscopy',shift(knee(),-2,0,.92)+[L('M41 9 L26 24'),R(34,5,10,6,1,'accent',transform='rotate(-40 39 8)'),D('M28 22 L23 26')])
add('endoscopy',shift(stomach(),6,4,.81)+[L('M5 7 C9 2 22 4 21 14'),D('M21 14 V21 C21 25 33 26 28 30')],'M5 7 C9 2 22 4 21 14 V21 C21 25 33 26 28 30')
add('colonoscopy',colon()+[D('M27 42 V36 C28 31 34 31 35 27 V17 Q35 12 30 14 H20'),L('M27 43 H38')],'M27 43 V36 C28 31 34 31 35 27 V17 Q35 12 30 14 H20')
add('bronchoscopy',lungs()+[L('M25 6 C36 1 43 5 40 10'),D('M25 8 V20 L31 28')],'M40 10 C43 5 36 1 25 6 V20 L31 28')
add('cardiac-surgery',[P('M16 6 L20 10 H28 L32 6 L41 12 L36 22 V41 H12 V22 L7 12 Z'),D('M24 13 V38 M17 18 H31 M17 25 H31 M17 32 H31')]+shift(heart(),16,12,.38))
add('fracture-fixation',[P('M15 5 H28 L28 18 L22 22 L26 26 L19 29 L16 22 Z'),P('M17 29 L23 27 L28 29 L29 43 H17 Z'),R(28,12,7,26,2,'accent'),L('M22 16 H39 M22 24 H39 M22 33 H39'),D('M31 14 V36')])
add('caesarean-section',[P('M14 5 C18 11 14 16 11 24 C6 40 15 44 24 43 C33 44 42 40 37 24 C34 16 30 11 34 5'),D('M24 19 V21 M13 34 Q24 29 35 34 M18 31 L17 36 M24 31 V35 M30 31 L31 36'),L('M13 9 L18 12 M35 9 L30 12')])
add('organ-transplant',shift(kidney_one(),12,-1,.76)+[P('M4 33 L10 28 L17 32 H31 L35 28 L44 32 L38 41 H13 Z'),D('M11 32 L18 36 H31 L37 32')])
add('angioplasty-stent',[P('M5 13 H17 L22 18 H28 L33 13 H43 V35 H33 L28 30 H22 L17 35 H5 Z'),R(14,20,24,8,4,'accent'),D('M19 21 L22 27 M25 21 L28 27 M31 21 L34 27'),L('M4 24 H14')],'M5 24 H42')
add('dialysis',shift(chair(),-1,10,.75)+shift(dialysis_machine(),23,0,.53)+[C(10,15,3,'accent'),L('M29 16 C20 13 26 31 20 28')],'M29 16 C20 13 26 31 20 28')
add('radiation-therapy',[P('M7 41 V14 L16 6 H30 L35 13 L29 18 L25 13 H20 L15 19 V41 Z'),R(27,17,11,7,1,'accent',transform='rotate(-35 32 20)'),P('M19 35 H42 V40 H19 Z','accent'),C(22,31,3,'accent'),L('M26 33 H38 M36 41 V44 M27 23 L30 31 M33 23 L32 31')],'M30 23 L32 32')

# Orthopaedic detail: deliberately different geometry for native and replaced joints.
add('shoulder-joint',[P('M7 7 L21 10 L19 21 L12 33 L7 25 Z'),P('M24 6 C25 13 34 10 36 18 C41 25 32 29 28 24 L28 43 H18 L19 27 C17 22 21 16 26 17 L28 16'),D('M23 22 C26 15 36 18 33 23 M24 29 V39'),L('M11 12 L19 14')])
add('shoulder-replacement',[P('M7 7 L19 10 L16 25 L10 33 L7 25 Z'),P('M20 28 L31 28 L31 43 H20 Z'),C(28,19,7,'accent'),P('M25 24 H30 L28 39 H25 Z','accent'),D('M23 17 Q29 13 32 19 M27 28 V36')])
add('elbow-joint',[P('M12 5 H24 L26 20 C29 27 22 29 19 25 C13 27 10 21 13 18 Z'),P('M28 23 L42 36 L36 43 L22 31 C15 33 12 27 18 24 L22 27 Z'),D('M18 9 V18 M25 31 L36 39'),P('M30 23 L42 32 L43 37 L32 30 Z','accent')])
add('wrist-joint',[P('M9 6 L20 5 L20 22 Q13 26 11 22 Z'),P('M25 5 L32 7 L29 22 L24 22 Z'),R(10,28,7,6,2,'accent'),R(20,27,7,6,2,'accent'),R(29,27,7,6,2,'accent'),L('M11 35 L8 43 M18 35 L17 44 M26 35 V44 M33 34 L37 42'),D('M14 10 L15 19 M28 11 L27 19')])
add('hip-joint',hip())
add('hip-replacement',[P('M8 6 C6 14 7 21 14 25 C18 28 21 25 23 20 C26 15 20 10 21 6 Z'),D('M11 10 C9 18 15 22 18 21'),C(24,23,5,'accent'),P('M28 25 L36 31 L33 43 H29 L29 34 L24 29 Z','accent'),D('M30 32 L31 39')])
add('knee-joint',knee())
add('knee-replacement',[P('M15 5 H30 L29 19 H16 Z'),P('M16 19 H30 L33 24 L28 28 L22 25 L17 28 L13 24 Z','accent'),P('M16 31 H32 L30 35 H18 Z','accent'),P('M19 35 H29 L28 43 H20 Z'),D('M23 7 V17 M24 33 V41')])
add('acl',[P('M12 5 H34 L32 14 C38 21 30 26 25 20 C19 25 11 23 14 16 Z'),P('M14 31 C18 27 29 27 33 31 L31 43 H17 Z'),P('M17 19 L22 18 L30 31 L26 33 Z','accent'),L('M29 20 L20 31'),D('M20 9 H29 M19 37 H29')])
add('meniscus',[P('M6 22 C6 7 22 7 23 17 C17 10 11 14 11 23 C11 31 18 35 23 28 C22 41 6 37 6 22 Z'),P('M42 22 C42 7 26 7 25 17 C31 10 37 14 37 23 C37 31 30 35 25 28 C26 41 42 37 42 22 Z'),L('M22 22 H26'),D('M9 21 Q8 31 17 32 M39 21 Q40 31 31 32')])
add('spine',spine())
add('scoliosis',spine(True)+[L('M8 6 C14 14 3 28 11 39')])
add('plate-screws',[P('M11 5 H37 V43 H11 Z'),R(20,8,8,32,3,'accent'),D('M24 10 V38 M14 23 L19 21 L21 26 L29 22 L34 24')]+[L(f'M16 {y} H32') for y in [13,19,29,35]])
add('intramedullary-nail',[P('M9 7 Q17 3 21 13 L32 19 V43 H21 L21 24 L12 17 Q5 17 9 7 Z'),P('M13 9 L17 10 L27 22 V40 H23 V24 L13 15 Z','accent'),L('M17 13 L28 7 M20 17 L32 11 M18 34 H33 M18 39 H33')])
add('external-fixator',[P('M20 5 H29 L28 21 L23 25 L28 29 L29 43 H20 L20 29 L24 26 L20 21 Z'),L('M7 8 V42 M39 8 V42 M7 13 H20 M29 13 H39 M7 34 H20 M29 34 H39'),R(4,11,6,6,1,'accent'),R(36,11,6,6,1,'accent'),R(4,31,6,6,1,'accent'),R(36,31,6,6,1,'accent'),D('M23 9 V19 M23 32 V39')])

# Women's health and reproductive medicine. Schematic, non-graphic anatomy.
add('uterus',uterus())
add('ovary',[P('M9 24 C8 11 25 7 35 14 C45 21 36 39 23 40 C15 41 8 33 9 24 Z'),C(18,22,4,'accent'),C(29,19,3,'accent'),C(29,30,5,'accent'),C(17,33,2,'dot'),D('M14 15 L11 10 M35 35 L40 39')])
add('female-reproductive-system',[P('M8 6 Q24 14 40 6 M8 6 L6 22 Q8 33 17 39 L20 44 M40 6 L42 22 Q40 33 31 39 L28 44')]+shift(uterus(),6,8,.75))
add('pregnancy-foetus',fetus())
add('foetal-medicine',shift(fetus(),-1,0,.84)+[R(32,19,10,16,2,'accent',transform='rotate(20 37 27)'),L('M39 20 C39 12 44 13 44 7'),D('M33 25 L41 28')],'M34 31 L20 27 L28 20')
add('normal-delivery',[P('M7 6 C3 16 8 24 17 24 L19 37 L24 43 L29 37 L31 24 C40 24 45 16 41 6'),C(24,29,6,'accent'),D('M19 34 L24 39 L29 34 M9 13 C7 18 12 21 16 20 M39 13 C41 18 36 21 32 20'),L('M24 8 V18 M20 14 L24 18 L28 14')])
add('breastfeeding',[C(23,9,5),P('M14 42 C10 36 9 23 15 18 C20 14 27 18 30 26 L40 33 L35 40 L26 34 L27 43 Z'),C(32,26,5,'accent'),D('M15 27 C15 35 23 38 33 36 M19 22 L25 27')])
add('ivf',[E(24,32,18,10),D('M7 32 C10 42 38 42 41 32'),C(22,30,5,'accent'),C(29,29,3,'accent'),P('M32 5 L38 9 L28 25 L24 23 Z'),D('M32 11 L34 12'),L('M26 25 L24 28')],'M35 8 L26 24 L24 28')
add('egg-retrieval',[E(16,25,11,15),C(15,18,3,'accent'),C(12,29,3,'accent'),C(21,28,3,'accent'),L('M21 28 L38 14'),R(34,6,9,12,2,'accent',transform='rotate(42 38.5 12)'),D('M36 10 L41 14')])
add('embryo',[C(24,24,18),C(18,18,6,'accent'),C(30,18,6,'accent'),C(18,30,6,'accent'),C(30,30,6,'accent'),C(24,24,4,'accent'),D('M16 18 H19 M28 18 H31 M16 30 H19 M28 30 H31')])
add('embryo-transfer',uterus()+[L('M43 41 H33 C28 41 24 36 24 29'),D('M24 29 V22'),C(24,21,1.5,'accent')],'M43 41 H33 C28 41 24 36 24 29 V22')

# Neonatal and paediatric care.
add('newborn',newborn())
add('premature-baby',shift(newborn(),5,10,.72)+[L('M9 11 H16 L19 6 L23 15 L27 10 H37'),L('M7 32 C5 18 13 20 17 24')],'M9 11 H16 L19 6 L23 15 L27 10 H37')
add('neonatal-ventilation',shift(incubator(),-1,13,.74)+shift(ventilator(),28,-1,.42)+[L('M32 11 C25 8 25 23 14 27')],'M32 11 C25 8 25 23 14 27')
add('mother-baby',[C(19,9,5),P('M9 41 V26 C9 15 25 15 28 24 L37 33 L32 41 H9 Z'),C(32,24,5,'accent'),D('M12 29 C15 39 31 39 35 32 M23 25 L30 31')])
add('child-development',[C(14,9,4),L('M14 15 V27 L8 40 M14 27 L20 39 M14 19 L6 24 M14 19 L25 17'),R(28,29,15,14,2,'accent'),D('M35 30 V42 M28 36 H43'),C(34,17,4,'accent'),L('M32 7 V10 M41 12 L44 10')])
add('paediatric-surgery',[C(18,10,6),P('M11 19 H25 L29 30 L24 32 L23 43 H13 L12 32 L7 30 Z'),D('M16 21 V24 M20 21 V24')]+small_scalpel())

# Respiratory medicine and sleep diagnostics.
add('pulmonary-function-test',shift(lungs(),-1,0,.76)+[R(25,27,19,16,2),D('M29 31 V39 H41 M29 38 C31 28 34 29 36 35 L40 38')],'M29 38 C31 28 34 29 36 35 L40 38')
add('spirometry',[P('M11 6 C25 5 28 19 24 22 L29 25 L24 28 V32 H18 V42 H5 V23 C2 15 4 9 11 6 Z'),D('M20 18 H22'),L('M25 28 H32 C38 28 37 12 42 12'),R(31,31,13,12,2,'accent'),D('M35 35 H40 M35 39 H38')])
add('nebulisation',[R(5,28,24,15,3),D('M10 34 H18 M10 38 H15'),C(23,36,2,'cut'),L('M28 34 C40 36 38 25 33 23'),P('M27 8 Q38 9 39 18 L34 26 L26 22 L23 15 Z','accent'),D('M28 13 L33 17 M27 17 L31 20'),L('M20 7 L17 4 M17 13 H12 M18 20 L14 23')])
add('oxygen-therapy',shift(oxygen(),-4,1,.87)+[P('M36 5 C44 6 45 15 41 19 L44 23 L40 25 V31 H34 V39'),D('M38 15 H40'),L('M19 10 C25 5 29 22 37 23 M34 21 L36 25 M38 21 V25')],'M18 10 C25 5 29 22 37 23')
add('mechanical-ventilation',shift(ventilator(),-2,-1,.87)+[P('M34 29 C37 25 44 28 44 34 C44 39 38 41 34 38 Z','accent'),D('M36 33 H40'),L('M31 21 C43 17 41 28 38 32 M34 39 L29 43')],'M31 21 C43 17 41 28 38 32')
add('cpap-bipap',[P('M13 6 C24 4 29 14 25 20 L28 24 L23 28 V35 H17 V43 H6 V23 C2 17 5 8 13 6 Z'),P('M20 20 L27 21 L30 30 L23 32 L19 28 Z','accent'),L('M9 12 L24 23 M6 31 L22 28 M29 28 C41 25 44 37 37 39'),R(29,36,15,8,2,'accent'),D('M33 40 H39')])
add('sleep-study',shift(bed(),-1,6,.92)+[R(26,5,18,14,2),D('M29 12 H31 L33 8 L35 15 L38 10 H41'),L('M30 18 C24 21 21 20 13 28'),C(13,27,1.5,'accent'),L('M8 8 H14 L8 15 H14')],'M29 12 H31 L33 8 L35 15 L38 10 H41')

# Emergency care and trauma services.
add('trauma-patient',[R(11,4,26,40,7),C(24,13,5,'accent'),P('M17 22 H31 L32 39 H16 Z','accent'),D('M13 22 H35 M13 32 H35 M21 10 H27 M24 23 V39'),L('M7 10 V17 M41 10 V17 M7 32 V39 M41 32 V39')])
add('resuscitation',shift(bed(),0,7,.89)+[R(27,4,17,16,2),D('M30 13 H33 L35 7 L37 16 L40 11 H42'),P('M8 8 L12 5 L21 15 L17 19 Z','accent'),L('M18 19 L22 28'),C(21,28,2,'accent')],'M30 13 H33 L35 7 L37 16 L40 11 H42')
add('cpr',[C(10,31,4),P('M15 36 L17 28 H33 L40 35 V40 H6 V36 Z'),P('M13 6 L20 6 L29 21 L23 26 L19 21 Z','accent'),P('M31 6 H38 L28 24 L22 24 L22 20 Z','accent'),D('M20 15 L25 22 L30 15 M22 29 H28'),L('M5 43 H43')])
add('emergency-ventilation',[P('M27 29 C28 18 43 19 43 29 C44 37 39 40 33 39 L27 43 H17 L22 36 Z'),P('M27 23 L35 27 L33 33 L23 30 Z','accent'),E(17,16,10,7,'accent',transform='rotate(25 17 16)'),L('M25 20 L29 25 M7 12 L4 10'),D('M12 12 L22 17 M33 33 L38 32')],'M8 12 L25 20 L30 27')
add('emergency-bed',shift(bed(),0,5,.93)+[L('M7 14 V21 M42 16 V22'),P('M24 4 L17 14 H23 L21 22 L32 10 H26 L28 4 Z','accent')])
add('trauma-surgery',shift(body_outline(),-2,0,.88)+[D('M17 24 L22 28 L17 30'),L('M8 19 L14 22')]+small_scalpel())
add('polytrauma',body_outline()+[D('M18 18 L24 23 L29 18 M19 37 L23 34 M27 30 L30 34'),L('M7 10 L11 14 M4 25 H9 M37 36 L43 39')])
add('emergency-triage',[R(6,6,36,37,3),D('M11 13 H15 M11 24 H15 M11 35 H15'),R(20,10,17,5,1,'accent'),R(20,21,12,5,1,'accent'),R(20,32,7,5,1,'accent'),L('M24 4 V8')])
add('code-blue',[R(5,5,38,28,3),D('M9 22 H15 L18 15 L23 27 L28 11 L32 22 H39'),L('M10 34 V43 M38 34 V43 M11 38 H37'),C(20,40,2,'accent'),C(28,40,2,'accent')],'M9 22 H15 L18 15 L23 27 L28 11 L32 22 H39')
add('air-ambulance',[P('M14 19 H28 C34 19 42 24 42 29 C42 35 22 36 17 31 L8 30 L4 20 H9 L15 24 Z'),P('M30 20 V27 H40','accent'),L('M23 11 V18 M8 10 H40 M13 39 H40 M19 34 V39 M34 34 V39'),D('M22 23 V30 M18.5 26.5 H25.5')])

# Rehabilitation: actions, assistive equipment and clinical context.
add('physiotherapy',[C(10,10,4),C(30,18,4),L('M10 16 L13 29 L7 42 M13 29 L19 40 M11 19 L23 23 M13 24 L22 28 M29 23 L25 31 L38 34 L41 41'),L('M21 35 H41 M23 35 V43 M39 35 V43')])
add('gait-training',[C(24,8,4),L('M24 14 L21 26 L14 40 M21 26 L30 33 L33 42 M23 17 L13 23 M24 17 L35 23 M6 21 H16 M32 21 H42 M8 22 V43 M40 22 V43'),P('M18 22 L23 23 L22 28 L17 27 Z','accent')])
add('joint-rehabilitation',shift(knee(),-2,4,.81)+[L('M28 6 C43 9 45 32 34 40 M34 34 L33 41 L41 40')])
add('sports-rehabilitation',rehab_person()+[L('M10 25 C18 33 28 26 33 21'),P('M5 39 H13 L14 44 H4 Z','accent'),D('M28 31 L31 29')])
add('neuro-rehabilitation',shift(brain(),-2,-1,.68)+[C(31,27,3,'accent'),L('M31 31 L29 37 L24 43 M29 37 L35 43 M31 33 L40 34 L43 30'),L('M15 34 L19 38 L22 34')])
add('pulmonary-rehabilitation',shift(lungs(),-1,-1,.86)+[L('M21 42 H35 C43 42 44 34 41 29 M37 31 L41 27 L45 31')],'M21 42 H35 C43 42 44 34 41 29')
add('cardiac-rehabilitation',shift(heart(),-1,-1,.81)+[L('M22 41 H34 C43 41 44 32 41 27 M37 28 L41 25 L44 30')])
add('occupational-therapy',[P('M6 42 V28 L9 24 L14 29 V13 C14 8 20 8 20 13 V23 L23 17 C26 14 29 18 28 21 L26 26 L30 23 C34 23 34 27 32 30 L23 42 Z'),R(32,5,11,12,2,'accent'),D('M37 7 V15 M34 11 H41 M15 30 L20 34')])
add('speech-therapy',[P('M12 6 C24 4 30 15 25 21 L30 25 L24 28 V33 H17 V42 H5 V23 C2 16 4 9 12 6 Z'),D('M21 18 H23 M20 28 H24'),L('M34 19 Q38 24 34 29 M39 14 Q46 24 39 34')],'M34 19 Q38 24 34 29')

# Patient journey icons are clinical composites, not generic users/calendars.
add('op-consultation',shift(clinician(),-1,0,.86)+[C(35,16,5),P('M28 42 V30 Q35 22 42 30 V42 Z'),L('M6 36 H27'),D('M31 32 L35 36 L39 32')])
add('inpatient-admission',[L('M6 42 V7 H42 V42'),R(29,10,9,16,1,'accent'),D('M32 14 H35 M32 19 H35')]+shift(bed(),-1,14,.71)+[L('M11 15 H23 M19 11 L23 15 L19 19')])
add('day-care-admission',shift(chair(),0,11,.82)+[C(33,13,8,'accent'),D('M33 8 V13 L37 16'),L('M31 2 H35 M44 11 V15')])
add('preoperative-assessment',[R(7,8,30,35,3),R(16,5,13,7,2,'accent'),D('M12 18 H22 M12 24 H19 M12 31 L15 34 L20 28')]+small_scalpel())
add('surgery-scheduled',[R(5,8,38,35,3),D('M6 18 H42 M12 13 V5 M36 13 V5 M11 24 H16 M11 31 H16 M22 24 H26')]+small_scalpel())
add('postoperative-care',shift(bed(),-1,6,.92)+suture(24,10)+[D('M22 30 H30 M25 27 V33')])
add('patient-transfer',shift(bed(),-1,6,.92)+[L('M6 9 H27 L23 5 M27 9 L23 13 M41 19 H24 L28 15 M24 19 L28 23')])
add('discharge',[L('M7 42 V6 H30 V18'),R(11,10,14,16,2,'accent'),D('M14 14 H21 M14 19 H19'),C(32,25,3),L('M32 29 L31 36 L27 43 M31 36 L37 42 M32 32 L39 33 L43 28 M11 36 H22 M18 32 L22 36 L18 40')])
add('follow-up-consultation',shift(clinician(),-1,3,.87)+[C(34,19,8,'accent'),D('M31 19 L34 22 L38 16'),L('M25 7 C39 2 46 13 43 26 M39 24 L43 28 L46 23')])
add('home-healthcare',home_frame()+shift(clinician(),11,17,.53)+[L('M30 27 H34 L36 23 L39 31')])

# Hospital service icons.
add('round-the-clock-emergency',[P('M11 5 H38 V40 H10 V30 H5 V17 H10 Z'),D('M15 15 C15 10 23 10 23 14 C23 17 15 18 15 22 H23 M33 11 L27 18 H35 M33 11 V23 M17 29 H26 L20 37'),P('M35 26 L29 34 H34 L31 43 L42 31 H37 L40 26 Z','accent')])
add('preventive-health-check',[P('M24 4 L41 11 V24 C41 34 32 40 24 44 C16 40 7 34 7 24 V11 Z'),D('M12 25 H18 L21 18 L26 32 L30 23 H36'),L('M17 11 L24 8 L31 11')])
add('master-health-check',[R(6,5,36,39,3),R(11,11,12,12,2,'accent'),D('M13 18 H16 L18 14 L20 20 M28 13 H37 M28 19 H34 M11 30 H23 M11 36 H20'),P('M33 27 C26 34 28 40 33 40 C38 40 40 34 33 27 Z','accent')])
add('executive-health-check',[R(5,14,38,29,3),P('M17 14 V8 Q17 5 21 5 H27 Q31 5 31 8 V14 Z'),D('M6 24 H17 M31 24 H42 M11 32 H16'),P('M24 18 C18 12 13 20 18 25 L24 31 L30 25 C35 20 30 12 24 18 Z','accent'),D('M19 23 H22 L24 19 L26 26 L28 23')])
add('home-sample-collection',home_frame()+shift(vial(),12,16,.54))
add('home-nursing',home_frame()+[C(24,26,5,'accent'),P('M17 24 L18 19 H30 L31 24 Z'),P('M14 42 V38 C14 30 34 30 34 38 V42 Z','accent'),D('M21 34 L24 38 L27 34')])
add('home-physiotherapy',home_frame()+[C(23,23,3,'accent'),L('M23 27 L21 34 L16 41 M21 34 L28 41 M23 29 L32 31 M23 29 L15 33 M32 30 V42')])
add('pharmacy-delivery',[P('M5 15 H28 V36 H5 Z'),P('M28 23 H36 L43 30 V36 H28 Z','accent'),C(13,39,4),C(35,39,4),P('M13 9 C16 5 22 10 19 14 L15 20 C12 24 6 19 9 15 Z','accent'),D('M11 12 L17 17 M32 27 H36 L39 31 H32 Z')])
add('international-patient-care',[C(24,24,19),E(24,24,9,19,'cut'),D('M7 16 H41 M7 32 H41')]+shift(heart(),15,16,.49))
add('medical-tourism',[P('M6 5 H30 V43 H6 Z'),D('M10 10 H24 M10 36 H21'),C(18,22,7,'cut'),D('M11 22 H25 M18 15 V29'),P('M29 23 L42 14 L44 17 L37 26 L41 32 L39 34 L33 30 L29 35 L26 34 L29 28 Z','accent')])
add('blood-donation',[P('M24 5 C14 18 13 22 13 26 C13 39 35 39 35 26 C35 22 32 17 24 5 Z'),D('M18 26 Q18 32 23 32'),L('M5 36 L12 42 H35 L43 36 M12 42 L12 44 M35 42 L35 44')],'M24 9 C18 18 16 23 18 28')
add('palliative-care',[P('M24 18 C17 9 6 16 12 24 L24 34 L36 24 C42 16 31 9 24 18 Z','accent'),P('M5 28 L12 32 L17 32 L24 38 L31 32 L36 32 L43 28 V37 L33 44 H15 L5 37 Z'),D('M12 33 L18 38 M36 33 L30 38')])
add('rehabilitation-program',[C(24,8,4,'accent'),L('M24 14 V28 L14 41 M24 28 L34 41 M24 18 L12 25 M24 18 L36 25'),P('M5 25 L12 22 L15 29 L11 33 L9 43 H5 Z','accent'),P('M43 25 L36 22 L33 29 L37 33 L39 43 H43 Z','accent')])

# Standalone specialist equipment.
add('ventilator',ventilator(),'M12 21 H16 L19 14 L23 25 L27 18 H31')
add('patient-monitor',monitor(),'M10 22 H17 L20 15 L25 27 L29 19 H38')
add('infusion-pump',[L('M13 4 V42 M5 43 H22 M8 6 H26'),R(15,9,10,12,2),D('M18 16 H22'),R(20,25,22,15,2,'accent'),D('M24 29 H33 V35 H24 Z M37 29 V33'),L('M20 21 V24 M33 40 C33 44 42 44 43 39')],'M20 20 V24 M33 40 C33 44 42 44 43 39')
add('syringe-pump',[R(5,18,38,23,3),D('M10 33 H19 M10 37 H16 M29 32 H38'),R(13,9,22,9,2,'accent'),L('M8 13 H13 M8 9 V17 M35 13 H43'),D('M19 10 V16 M25 10 V16 M31 10 V16')])
add('dialysis-machine',dialysis_machine(),'M12 13 C4 10 4 33 11 31')
add('anaesthesia-workstation',[R(6,7,28,18,2),D('M10 17 H15 L18 11 L22 21 L26 15 H30'),R(5,28,31,11,2),C(11,33,2,'cut'),C(19,33,2,'cut'),L('M9 40 V43 M32 40 V43 M34 12 C44 8 46 26 39 29'),P('M37 28 C31 35 38 44 43 35 C45 30 41 26 37 28 Z','accent')])
add('surgical-robot',robot(),'M18 19 L10 13 L18 7 L29 15 L37 7')
add('ecmo',[C(12,10,4),P('M6 19 Q12 14 18 19 V39 H6 Z'),R(30,7,12,17,3,'accent'),D('M33 10 L39 21 M39 10 L33 21'),C(34,36,7),D('M34 32 V36 L38 38'),L('M18 23 C25 23 20 7 30 10 M40 25 L39 30 M27 36 C22 36 25 30 18 30')],'M18 23 C25 23 20 7 30 10 M40 25 L39 30 M27 36 C22 36 25 30 18 30')
add('heart-lung-machine',[R(6,27,36,13,2),D('M10 36 H38'),C(14,26,6,'accent'),C(33,26,6,'accent'),D('M14 22 L14 27 L17 29 M33 22 L33 27 L36 29'),L('M10 41 V44 M38 41 V44 M8 22 C3 10 13 4 21 7 M39 22 C45 10 35 4 27 7'),R(19,5,10,12,2,'accent'),D('M22 8 L26 14 M26 8 L22 14')],'M8 22 C3 10 13 4 21 7 M27 7 C35 4 45 10 39 22')
add('cath-lab-system',[P('M7 4 H25 V10 H14 V17 H7 Z'),R(24,5,17,12,2,'accent'),D('M27 12 H31 L33 8 L36 14 L38 11'),R(7,17,11,7,2,'accent'),L('M12 25 V29 M33 18 V23'),P('M7 32 H40 L44 37 H7 Z'),C(14,28,3,'accent'),L('M19 30 H33 M11 38 V44 M39 38 V44')])

# Condition navigation. Deliberately schematic; not diagnostic illustrations.
add('heart-attack',heart()+[P('M33 25 L26 33 H31 L27 43 L41 30 H35 L39 25 Z','accent'),D('M15 20 L20 23')])
add('stroke',brain()+[D('M25 12 L31 17 L29 23 M31 17 L36 18'),C(29,23,3,'accent'),D('M27 21 L31 25')])
add('coronary-artery-disease',heart()+[P('M18 19 L23 18 L25 26 L20 27 Z','accent'),D('M19 21 L24 24 M24 29 L33 33')])
add('heart-failure',[P('M24 12 C17 4 6 14 7 25 C7 38 17 44 28 42 C43 39 45 17 33 12 L32 6 H26 V13 Z'),D('M16 16 C10 21 14 31 23 34 M30 17 C37 18 39 29 31 34'),L('M22 23 H25 L28 28 H34')])
add('diabetes',[P('M23 5 C13 18 8 23 8 30 C8 47 39 47 39 30 C39 23 33 17 23 5 Z'),P('M14 29 Q18 24 23 28 Q31 22 33 28 Q35 34 28 33 Q22 39 18 34 Q12 36 14 29 Z','accent'),D('M18 30 L28 29')])
add('kidney-disease',kidney_one()+[D('M12 18 L16 20 M11 26 L15 25 M17 34 L20 31'),L('M34 15 L39 12 M34 23 H42 M32 31 L39 35')])
add('kidney-stone',kidney_one()+[P('M30 21 L36 18 L41 23 L38 30 L32 29 L29 25 Z','accent'),D('M33 22 L36 26 L39 23'),L('M25 25 C25 32 31 33 30 43')])
add('cancer',[P('M21 6 L26 9 L32 7 L35 13 L41 16 L38 23 L42 29 L36 33 L34 40 L27 38 L21 43 L16 37 L9 36 L10 29 L5 24 L10 18 L9 11 L16 12 Z'),P('M20 17 C23 13 29 18 28 21 C33 25 27 31 23 28 C16 32 14 23 18 22 Z','accent'),D('M14 17 L16 19 M30 32 L32 34 M33 17 L35 16')])
add('arthritis',shift(knee(),-2,0,.95)+[D('M17 25 L20 22 L23 25 L26 22 M18 31 L21 33 L24 30 L27 33'),L('M6 21 L10 24 M5 30 H10 M37 31 L42 34 M39 23 H44')])
add('osteoporosis',bone()+[C(16,13,2,'cut'),C(20,20,1.7,'cut'),C(25,26,2.1,'cut'),C(31,31,1.7,'cut'),C(36,35,2.2,'cut')])
add('asthma',shift(lungs(),-2,0,.81)+[C(34,32,10,'accent'),C(34,32,6,'cut'),P('M31 27 Q36 30 31 35 L34 36 Q39 31 34 27 Z','accent'),L('M27 25 L24 22')])
add('copd',shift(lungs(),-2,0,.76)+[C(32,33,11,'accent'),D('M24 29 C29 26 32 29 29 33 C29 38 24 39 24 34 M34 26 C39 25 42 33 37 33 C40 37 34 41 32 37 M29 33 L33 34')])
add('liver-disease',liver()+[C(13,22,2,'cut'),C(20,17,2,'cut'),C(15,29,2,'cut'),C(32,18,2,'cut'),D('M34 20 L37 22')])
add('high-risk-pregnancy',shift(fetus(),-1,0,.83)+[P('M35 27 L44 43 H26 Z','accent'),D('M35 32 V36 M35 40 L35.1 40')])
add('cataract',eye()+[P('M19 20 Q22 15 26 19 Q32 18 30 23 Q34 27 29 29 Q25 33 21 28 Q16 28 18 24 Z','accent'),D('M20 24 L28 26')])
add('glaucoma',[C(22,24,17),P('M38 20 L44 17 V31 L38 28 Z','accent'),P('M8 17 Q16 24 8 31 L5 26 V22 Z','accent'),D('M30 16 Q40 24 30 32'),L('M19 15 L26 22 M19 33 L26 26 M22 22 H26 V18 M22 26 H26 V30')])

# Fine-tuning the solid variant: boundaries inside other filled shapes need cut-outs.
for slug, nodes in ART.items():
    def correct(items):
        for n in items:
            if n['tag']=='g':
                correct(n['children'])
            elif n['tag']=='path' and n['attrs'].get('d')=='M10 22 H17 L20 15 L25 27 L29 19 H38 M24 34 L24 40 M15 41 L33 41':
                n['attrs']['d']='M10 22 H17 L20 15 L25 27 L29 19 H38'
                items.append(L('M24 34 L24 40 M15 41 L33 41'))
    correct(nodes)

# Insets retain an explicit negative-space edge when placed inside a filled panel.
def _inset_tree(node):
    if node['tag']=='g':
        for child in node['children']: _inset_tree(child)
    elif node['role']=='body': node['role']='accent'
    elif node['role']=='line': node['role']='cut'
    elif node['role']=='dot': node['role']='accent'
for _slug,_index in [('chest-x-ray',1),('bone-x-ray',1),('cardiac-catheterisation',1),('cardiac-surgery',2),('female-reproductive-system',1),('international-patient-care',3)]:
    _inset_tree(ART[_slug][_index])
ART['general-surgery'][-1]['role']='cut'
for _slug in ['plate-screws','intramedullary-nail','fracture-fixation']:
    for _node in ART[_slug]:
        if _node.get('role')=='line': _node['role']='cut'
# Glaucoma's pressure-direction strokes must also read inside the cross-section.
ART['glaucoma'][-1]['role']='cut'
