from html import escape
import re

SW=2.1

def attrs(d):
    return ' '.join(f'{k}="{escape(str(v),quote=True)}"' for k,v in d.items())

def draw_nodes(nodes,variant='outline',mode='paint'):
    result=[]
    for n in nodes:
        tag=n['tag']
        if tag=='g':
            children=draw_nodes(n['children'],variant,mode)
            if children: result.append(f'<g {attrs(n["attrs"])}>{children}</g>')
            continue
        role=n['role']
        a=n['attrs'].copy()
        if mode=='mask':
            if role not in ('cut','accent'): continue
            a.update(fill='none',stroke='black',**{'stroke-width':1.75})
        else:
            if variant=='solid' and role=='cut': continue
            a.update(fill='none',stroke='currentColor',**{'stroke-width':SW if variant!='solid' else 1.6})
            if role in ('body','accent'):
                if variant=='solid': a.update(fill='currentColor')
                elif variant=='duotone': a.update(fill='currentColor',**{'fill-opacity':.14 if role=='body' else .30})
            if role=='line' and variant=='solid': a['stroke-width']=SW
            if role=='dot': a.update(fill='currentColor',stroke='none')
        result.append(f'<{tag} {attrs(a)}/>')
    return ''.join(result)

def content(nodes, variant, slug, mask_id=None):
    markup=draw_nodes(nodes,variant)
    if variant=='solid':
        holes=draw_nodes(nodes,variant,'mask')
        if holes:
            mid=mask_id or 'hmi-'+slug+'-solid'
            markup=f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48" style="mask-type:luminance"><rect width="48" height="48" fill="white"/>{holes}</mask></defs><g mask="url(#{mid})">{markup}</g>'
    return markup

BEAM_CSS='''@keyframes hmi-flow{to{stroke-dashoffset:-100}}.hmi-beam-tail,.hmi-beam-head{animation:hmi-flow var(--hmi-duration,2.6s) linear infinite;animation-play-state:var(--hmi-play-state,running)}.hmi-beam-tail{stroke-dasharray:20 80;opacity:.22}.hmi-beam-head{stroke-dasharray:7 93}@media(prefers-reduced-motion:reduce){.hmi-beam-tail,.hmi-beam-head{animation:none;display:none}.hmi-beam-base{opacity:1}}'''

def svg(nodes,variant,slug,name,beam=None):
    root={'xmlns':'http://www.w3.org/2000/svg','width':48,'height':48,'viewBox':'0 0 48 48','fill':'none','stroke-linecap':'round','stroke-linejoin':'round','role':'img','aria-label':name}
    inner=content(nodes,variant,slug)
    if beam:
        inner='<style>'+BEAM_CSS+'</style><g class="hmi-beam-base" opacity="0.48">'+inner+'</g>'+f'<g fill="none" stroke="var(--hmi-beam-color, currentColor)"><path class="hmi-beam-tail" d="{beam}" pathLength="100" stroke-width="3.8"/><path class="hmi-beam-head" d="{beam}" pathLength="100" stroke-width="2.3"/></g>'
    return '<svg '+attrs(root)+'><title>'+escape(name)+'</title>'+inner+'</svg>\n'
