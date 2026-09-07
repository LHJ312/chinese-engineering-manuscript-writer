"""Read selected runtime assets only; never load source papers or development logs."""
from pathlib import Path
import argparse,csv,json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def checked(path):
    p=(ROOT/path).resolve()
    if not p.is_relative_to(ROOT.resolve()):raise ValueError('Asset must remain inside skill root')
    return p
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='mode',required=True)
    p=sub.add_parser('rules');p.add_argument('--ids',required=True)
    p=sub.add_parser('list');p.add_argument('--kind',choices=['case','style'],required=True);p.add_argument('--section');p.add_argument('--function')
    p=sub.add_parser('read');p.add_argument('--kind',choices=['case','style'],required=True);p.add_argument('--id',required=True)
    args=ap.parse_args()
    if args.mode=='rules':
        ids=[x.strip() for x in args.ids.split(',') if x.strip()]
        index=load('criteria/rule_index_v2.json')
        aliases={r['old_id']:r['canonical_id'] for r in csv.DictReader((ROOT/'criteria/rule_aliases_v2.csv').open(encoding='utf-8-sig'))}
        aliases['原Methods候选M01']='METHODS-IMPL-01'
        ids=list(dict.fromkeys(aliases.get(x,x) for x in ids))
        if not ids or any(x not in index and x!='METHODS-IMPL-01' for x in ids):raise ValueError('Unknown rule ID; numeric M-01 differs from METHODS-IMPL-01')
        source=ROOT/'criteria/writing_criteria_v2.md'
        freeze=load('criteria/writing_criteria_v2_freeze.json')
        if hashlib.sha256(source.read_bytes()).hexdigest()!=freeze['approved_sha256']:raise ValueError('Approved rule source changed; resolve version before use')
        lines=source.read_text(encoding='utf-8').splitlines()
        print('LEVEL_1_HARD: identify material semantic/basis error; LEVEL_2_STRONG: check exceptions; LEVEL_3_HEURISTIC: optional, never automatic rewrite. Missing context is CONTEXT_REQUIRED, not automatic FAIL.')
        for rid in ids:
            if rid=='METHODS-IMPL-01':print((ROOT/'criteria/methods_impl_01.md').read_text(encoding='utf-8'));continue
            r=index[rid];print('\n'+'\n'.join(lines[r['line_start']-1:r['line_end']]))
        return
    index=load('examples/case_index.json' if args.kind=='case' else 'examples/style_cards/style_index.json')
    if args.mode=='list':
        if args.section:index=[r for r in index if r.get('section','').casefold()==args.section.casefold()]
        if args.function:index=[r for r in index if args.function.casefold() in str(r.get('function',r.get('writing_function',''))).casefold()]
        print(json.dumps(index,ensure_ascii=False,indent=2))
    else:
        key='case_id' if args.kind=='case' else 'style_id';hits=[r for r in index if r[key]==args.id]
        if len(hits)!=1:raise ValueError('Unknown asset ID')
        print(checked(hits[0]['path']).read_text(encoding='utf-8'))
if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    try:main()
    except (ValueError,KeyError) as e:print(str(e),file=sys.stderr);sys.exit(2)
