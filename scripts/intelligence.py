#!/usr/bin/env python3
"""Source routing and evidence-backed report rendering; Python stdlib only."""
import argparse
import csv
import html
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def catalog():
    return json.loads((ROOT / 'data/sources.json').read_text(encoding='utf-8'))['sources']


def select_sources(sources, topic=None, region=None, platform=None):
    return [s for s in sources
            if (not topic or topic in s['topics'])
            and (not region or region in s['regions'] or 'global' in s['regions'])
            and (not platform or platform in s['platforms'] or 'all' in s['platforms'])]


def validate(data, sources=None):
    errors = []
    if not isinstance(data, dict):
        return ['report must be an object']
    for key in ['id', 'title', 'question', 'scope', 'claims', 'recommendation', 'unknowns']:
        if key not in data:
            errors.append(f'missing {key}')
    claims = data.get('claims', [])
    if not isinstance(claims, list):
        return errors + ['claims must be a list']
    known = {s['id'] for s in (sources if sources is not None else catalog())}
    seen = set()
    for c in claims:
        if not isinstance(c, dict):
            errors.append('claim must be an object'); continue
        cid = c.get('id')
        if not isinstance(cid, str) or not cid or cid in seen:
            errors.append('missing or duplicate claim ID')
        seen.add(str(cid))
        for key in ['statement', 'kind', 'value', 'unit', 'period', 'scope', 'source_ids', 'evidence']:
            if key not in c:
                errors.append(f'{cid}: missing {key}')
        if c.get('kind') not in ['observed', 'estimate', 'assumption', 'inference']:
            errors.append(f'{cid}: invalid kind')
        if c.get('value') is None and not c.get('unknown_reason'):
            errors.append(f'{cid}: unknown value needs a reason')
        refs = c.get('source_ids', [])
        if not isinstance(refs, list):
            errors.append(f'{cid}: source_ids must be a list'); refs = []
        for sid in refs:
            if sid not in known:
                errors.append(f'{cid}: unknown source {sid}; register the source first')
        if c.get('value') is not None and c.get('kind') != 'assumption' and (not refs or not c.get('evidence')):
            errors.append(f'{cid}: stated observation/estimate/inference needs specific evidence')
    recommendation = data.get('recommendation', {})
    if not isinstance(recommendation, dict):
        return errors + ['recommendation must be an object']
    if recommendation.get('status') not in ['proposed', 'confirmed']:
        errors.append('recommendation status must be proposed or confirmed')
    if recommendation.get('status') == 'confirmed' and not recommendation.get('authority_reference'):
        errors.append('confirmed decision needs an authority reference')
    comparison = data.get('comparison')
    if comparison is not None:
        if not isinstance(comparison, dict):
            return errors + ['comparison must be an object']
        axes = comparison.get('axes', [])
        if not isinstance(axes, list) or not axes or any(not isinstance(a, dict) or not isinstance(a.get('id'), str) or not a.get('id') or not a.get('label') for a in axes):
            return errors + ['comparison axes need unique IDs and labels']
        axis_ids = {a['id'] for a in axes}
        if len(axis_ids) != len(axes): errors.append('duplicate comparison axis')
        products = comparison.get('products', [])
        if not isinstance(products, list) or not products:
            return errors + ['comparison products must be a nonempty list']
        product_ids = set()
        for product in products:
            if not isinstance(product, dict) or not isinstance(product.get('id'), str) or not product.get('id') or not product.get('name'):
                errors.append('comparison product needs ID and name'); continue
            if product['id'] in product_ids: errors.append('duplicate comparison product')
            product_ids.add(product['id'])
            cells = product.get('cells')
            if not isinstance(cells, dict) or set(cells) != axis_ids:
                errors.append(product['id'] + ': include every axis; record unknowns explicitly'); continue
            for axis, cell in cells.items():
                if not isinstance(cell, dict) or not isinstance(cell.get('text'), str) or not cell['text'].strip():
                    errors.append(f"{product['id']}/{axis}: missing cell text"); continue
                refs = cell.get('claim_ids')
                if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in seen for ref in refs):
                    errors.append(f"{product['id']}/{axis}: cell requires valid evidence claim IDs")
    return errors


def render(data, out, language='zh'):
    if language not in ('zh', 'en'):
        raise ValueError('language must be zh or en')
    labels = {'Scope': '范围', 'Recommendation': '建议', 'Evidence and findings': '证据与结论',
              'Unknown: ': '未知：', 'Evidence': '依据', 'Open validation': '待验证',
              'Product / lens': '产品 / 比较维度', 'Cross-lens comparison': '多视角比较',
              'Finding': '结论', 'Kind': '性质', 'Value / gap': '值 / 缺口',
              'Business period': '业务期间', 'Evidence location': '具体证据',
              'This report renders the supplied evidence. Missing metrics are not invented. Use browser print to save a PDF.':
              '本报告仅呈现输入底稿；未取得的指标未自动补齐。可通过浏览器打印保存 PDF。'}
    t = lambda label: labels.get(label, label) if language == 'zh' else label
    errors = validate(data)
    if errors:
        raise ValueError('; '.join(errors))
    out.mkdir(parents=True, exist_ok=False)
    esc = lambda value: html.escape(str(value), quote=True)
    rows = []
    md = [f"# {data['title']}", '', data['question'], '',
          f"**{t('Scope')}:** " + json.dumps(data['scope'], ensure_ascii=False), '',
          f"**{t('Recommendation')} (" + data['recommendation']['status'] + '):** ' + data['recommendation'].get('text', ''), '',
          '## ' + t('Evidence and findings'), '']
    for c in data['claims']:
        value = t('Unknown: ') + c['unknown_reason'] if c['value'] is None else str(c['value']) + ' ' + str(c['unit'])
        evidence = json.dumps(c['evidence'], ensure_ascii=False)
        links=[]
        for entry in c['evidence'] if isinstance(c['evidence'], list) else []:
            if isinstance(entry, dict) and isinstance(entry.get('url'),str) and urlsplit(entry['url']).scheme in ('http','https'):
                links.append('<a href="'+esc(entry['url'])+'">'+esc(urlsplit(entry['url']).netloc)+'</a><br><small>'+esc(entry.get('locator',''))+'</small>')
        citation='<br>'.join(links) if links else esc(evidence)
        rows.append('<tr>' + ''.join(f'<td>{esc(v)}</td>' for v in [c['id'], c['statement'], c['kind'], value, c['period']]) + '<td>'+citation+'</td></tr>')
        md += [f"- **{c['id']} · {c['statement']}**：{value}（{c['kind']}，{c['period']}）", f"  {t('Evidence')}: {evidence}", '']
    md += ['## ' + t('Open validation'), ''] + ['- ' + str(u) for u in data['unknowns']]
    matrix = ''
    if data.get('comparison'):
        comparison = data['comparison']
        axes = comparison['axes']
        header = '<th>' + t('Product / lens') + '</th>' + ''.join('<th>' + esc(a['label']) + '</th>' for a in axes)
        matrix_rows = []
        with (out / 'comparison.csv').open('w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product_id', 'product', 'axis', 'value', 'value_en', 'claim_ids'])
            md += ['', '## ' + t('Cross-lens comparison'), '']
            for product in comparison['products']:
                cells = []
                md += ['### ' + product['name'], '']
                for axis in axes:
                    cell = product['cells'][axis['id']]
                    refs = ', '.join(cell['claim_ids'])
                    cells.append('<td>' + esc(cell['text']) + '<br><small>' + esc(refs) + '</small></td>')
                    writer.writerow([product['id'], product['name'], axis['id'], cell['text'], cell.get('text_en', ''), refs])
                    md.append(f"- **{axis['label']}**：{cell['text']} · {refs}")
                matrix_rows.append('<tr><th>' + esc(product['name']) + '</th>' + ''.join(cells) + '</tr>')
        matrix = '<h2>' + t('Cross-lens comparison') + '</h2><div class="scroll"><table><thead><tr>' + header + '</tr></thead><tbody>' + ''.join(matrix_rows) + '</tbody></table></div>'
    page = f'''<!doctype html><html lang="{'zh-CN' if language == 'zh' else 'en'}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(data['title'])}</title><style>body{{max-width:1160px;margin:40px auto;padding:0 24px;font:16px/1.75 system-ui;color:#14374b;background:#f5f9fb}}h1{{line-height:1.2;background:#001f3f;color:#f5f9fb;padding:32px;margin:0 -24px 28px;letter-spacing:-1px}}a{{color:#007d86;text-underline-offset:4px}}h2{{color:#007d86}}small{{font-size:12px;color:#486674}}table{{border-collapse:collapse;width:100%;background:white}}th,td{{padding:12px;border:0;border-bottom:1px solid #c6d7dc;text-align:left;vertical-align:top;overflow-wrap:anywhere}}.scroll{{overflow:auto}}.note{{background:#dfeded;border-left:3px solid #007d86;padding:18px}}@media print{{body{{margin:0;background:white;font-size:11pt}}tr{{break-inside:avoid}}}}</style>
<h1>{esc(data['title'])}</h1><p>{esc(data['question'])}</p><p>{t('Scope')}: {esc(json.dumps(data['scope'],ensure_ascii=False))}</p>
<div class="note"><b>{t('Recommendation')} · {esc(data['recommendation']['status'])}</b><p>{esc(data['recommendation'].get('text',''))}</p></div>
{matrix}<h2>{t('Evidence and findings')}</h2><div class="scroll"><table><thead><tr><th>ID</th><th>{t('Finding')}</th><th>{t('Kind')}</th><th>{t('Value / gap')}</th><th>{t('Business period')}</th><th>{t('Evidence location')}</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<h2>{t('Open validation')}</h2><ul>{''.join('<li>'+esc(u)+'</li>' for u in data['unknowns'])}</ul>
<p>{t('This report renders the supplied evidence. Missing metrics are not invented. Use browser print to save a PDF.')}</p></html>'''
    (out / 'report.html').write_text(page, encoding='utf-8')
    (out / 'report.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    (out / 'report.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    q = commands.add_parser('sources')
    q.add_argument('--topic'); q.add_argument('--region'); q.add_argument('--platform')
    for name in ['validate', 'report']:
        p = commands.add_parser(name); p.add_argument('input', type=Path)
        if name == 'report':
            p.add_argument('--out', type=Path, required=True)
            p.add_argument('--lang', choices=['zh', 'en'], default='zh', help='Report labels; input narrative is preserved (default: zh)')
    args = parser.parse_args()
    try:
        if args.command == 'sources':
            result = select_sources(catalog(), args.topic, args.region, args.platform)
            print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
        data = json.loads(args.input.read_text(encoding='utf-8-sig'))
        errors = validate(data)
        if errors:
            print(json.dumps({'valid': False, 'errors': errors}, ensure_ascii=False)); return 1
        if args.command == 'report': render(data, args.out, args.lang)
        print(json.dumps({'valid': True, 'output': str(args.out) if args.command == 'report' else None}, ensure_ascii=False)); return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    raise SystemExit(main())
