#!/usr/bin/env python3
from __future__ import annotations

import base64 as _b64
def _dq(_s):
    return _b64.b64decode(_s.encode("ascii")).decode("utf-8")

import argparse
import re
from collections import defaultdict
from pathlib import Path
_s1_002 = re.compile(_dq('XihzdGF0dXMgb2YgdGhpcyBtZW1vfGFic3RyYWN0fHRhYmxlIG9mIGNvbnRlbnRzfGNvcHlyaWdodCBub3RpY2V8ZnVsbCBjb3B5cmlnaHQgc3RhdGVtZW50KVxzKiQ='), re.I)
_s1_000 = re.compile(_dq('XlxzKkF1dGhvcnM/OlxzKiguKz8pXHMqJA=='), re.I)
_s1_003 = re.compile(_dq('XGIoPzpbQS1aXVtBLVphLXonXC1dKlwuXHMqKXsxLDN9W0EtWl1bQS1aYS16J1wtXSsoPzosXHMqKD86RWRcLj98RWRpdG9yKSk/XGI='))
_s1_006 = re.compile(_dq('LD9ccyooPzpFZFwuP3xFZGl0b3IpXHMqJA=='), re.I)
_s1_001 = {_dq('bHRk'), _dq('aW5j'), _dq('Y29ycA=='), _dq('bGxj'), _dq('Y28='), _dq('Z3JvdXA='), _dq('bGFicw=='), _dq('c3lzdGVtcw=='), _dq('bmV0d29ya3M='), _dq('Z21iaA=='), _dq('c2E='), _dq('c3Js'), _dq('cGxj')}
_s1_005 = re.compile(_dq('XnJmYyhcZCtbYS16XT8pXC50eHQk'), re.I)
_s1_004 = re.compile(_dq('XlxzKihUaXRsZXxBdXRob3JzP3xEYXRlfEluc3RhbGxhdGlvbilccyo6'), re.I)

def _s1_025(_s1_032: list[str], _s1_034: int=30) -> list[str]:
    _s1_056: list[str] = []
    _s1_035 = min(len(_s1_032), _s1_034)
    _s1_012 = 0
    _s1_048 = False
    _s1_026 = 0
    while _s1_026 < _s1_035:
        _s1_031 = _s1_032[_s1_026]
        _s1_052 = _s1_031.strip()
        if _s1_002.match(_s1_052):
            break
        if not _s1_052:
            if not _s1_048:
                _s1_026 += 1
                continue
            _s1_012 += 1
            if _s1_012 >= 2:
                _s1_028 = _s1_026 + 1
                while _s1_028 < _s1_035 and (not _s1_032[_s1_028].strip()):
                    _s1_028 += 1
                if _s1_028 < _s1_035 and _s1_004.match(_s1_032[_s1_028]):
                    _s1_012 = 0
                    _s1_056.append(_s1_031)
                    _s1_026 += 1
                    continue
                break
            _s1_056.append(_s1_031)
            _s1_026 += 1
            continue
        _s1_012 = 0
        _s1_048 = True
        _s1_056.append(_s1_031)
        _s1_026 += 1
    return _s1_056

def _s1_024(_s1_056: list[str]) -> list[str]:
    _s1_037: list[str] = []
    for _s1_031 in _s1_056:
        _s1_033 = _s1_000.match(_s1_031)
        if _s1_033:
            for _s1_040 in re.split(_dq('LHwgYW5kIA=='), _s1_033.group(1)):
                _s1_040 = _s1_040.strip().rstrip(_dq('Lg=='))
                if _s1_040 and re.match(_dq('XltBLVpdW2EtekEtWidcLV0rKFxzK1tBLVpdW2EtekEtWidcLV0rKXswLDN9JA=='), _s1_040):
                    _s1_037.append(_s1_040)
            continue
        if _s1_031.strip().isupper():
            continue
        _s1_037.extend((_s1_033.group(0) for _s1_033 in _s1_003.finditer(_s1_031)))
    return [_s1_035 for _s1_035 in _s1_037 if _s1_020(_s1_035).split()[-1].lower() not in _s1_001]

def _s1_038(name: str) -> str:
    _s1_011 = _s1_006.sub('', name)
    _s1_011 = re.sub(_dq('Wy5cLSdd'), '', _s1_011)
    _s1_011 = re.sub(_dq('XHMr'), _dq('IA=='), _s1_011).strip().lower()
    return _s1_011

def _s1_020(name: str) -> str:
    _s1_016 = _s1_006.sub('', name).strip()
    return re.sub(_dq('XHMr'), _dq('IA=='), _s1_016)

def _s1_051(name: str) -> str:
    _s1_050 = re.sub(_dq('W15BLVphLXowLTldKw=='), _dq('LQ=='), name).strip(_dq('LQ=='))
    return _s1_050 or _dq('dW5rbm93bg==')

def _s1_008(name: str) -> str:
    _s1_053 = re.sub(_dq('W15BLVphLXpd'), '', name.split()[-1]) if name.split() else ''
    return _s1_053[0].upper() if _s1_053 else _dq('Xw==')

def _s1_046(stem: str) -> str:
    _s1_033 = re.match(_dq('cmZjKFxkK1thLXpdPyk='), stem, re.I)
    return f'RFC {_s1_033.group(1)}' if _s1_033 else stem

def _s1_017(src: Path, limit: int | None) -> dict[str, dict]:
    _s1_009: dict[str, dict] = defaultdict(lambda: {_dq('ZGlzcGxheQ=='): None, _dq('cmZjcw=='): set()})
    _s1_018 = 0
    for _s1_041 in sorted(src.glob(_dq('Ki50eHQ='))):
        _s1_033 = _s1_005.match(_s1_041.name)
        if not _s1_033:
            continue
        if limit and _s1_018 >= limit:
            break
        _s1_018 += 1
        _s1_043 = _s1_041.read_text(encoding=_dq('dXRmLTg='), errors=_dq('cmVwbGFjZQ==')).lstrip(_dq('77u/'))
        _s1_032 = _s1_043.replace(_dq('DQo='), _dq('Cg==')).replace(_dq('DQ=='), _dq('Cg==')).split(_dq('Cg=='))
        _s1_056 = _s1_025(_s1_032)
        for _s1_044 in _s1_024(_s1_056):
            key = _s1_038(_s1_044)
            if not key or len(key) < 3:
                continue
            _s1_023 = _s1_009[key]
            _s1_019 = _s1_020(_s1_044)
            if _s1_023[_dq('ZGlzcGxheQ==')] is None or len(_s1_019) > len(_s1_023[_dq('ZGlzcGxheQ==')]):
                _s1_023[_dq('ZGlzcGxheQ==')] = _s1_019
            _s1_023[_dq('cmZjcw==')].add(_s1_041.stem)
    print(f'scanned {_s1_018} RFC files, found {len(_s1_009)} distinct authors')
    return _s1_009

def _s1_057(_s1_009: dict[str, dict], dst: Path) -> None:
    _s1_010 = dst / _dq('YXV0aG9ycw==')
    _s1_010.mkdir(parents=True, exist_ok=True)
    _s1_022 = sorted(_s1_009.values(), key=lambda _s1_021: _s1_021[_dq('ZGlzcGxheQ==')].lower())
    _s1_049: dict[str, int] = {}
    _s1_015: dict[str, list[tuple[str, str, int]]] = defaultdict(list)
    for _s1_023 in _s1_022:
        name = _s1_023[_dq('ZGlzcGxheQ==')]
        _s1_050 = _s1_051(name)
        if _s1_050 in _s1_049:
            _s1_049[_s1_050] += 1
            _s1_050 = f'{_s1_050}-{_s1_049[_s1_050]}'
        else:
            _s1_049[_s1_050] = 0
        _s1_045 = sorted(_s1_023[_dq('cmZjcw==')], key=lambda _s1_047: (len(_s1_047), _s1_047))
        _s1_013 = _s1_008(name)
        _s1_055 = f'chunk-author-{_s1_013}'
        _s1_032 = [_dq('LS0t'), _dq('dHlwZTogcGVyc29u'), f'tags: [codebase-map, rfc-editor, author, {_s1_055}]', f'name: {name}', _dq('LS0t'), '', f'# {name}', '', _dq('IyMgUkZDcw=='), '']
        for stem in _s1_045:
            _s1_032.append(f'- [[{stem}]] ({_s1_046(stem)})')
        _s1_032.append('')
        _s1_014 = _s1_010 / _s1_013
        _s1_014.mkdir(parents=True, exist_ok=True)
        (_s1_014 / f'{_s1_050}.md').write_text(_dq('Cg==').join(_s1_032), encoding=_dq('dXRmLTg='))
        _s1_015[_s1_013].append((_s1_050, name, len(_s1_045)))
    _s1_030 = sorted(_s1_015)
    for _s1_042, _s1_029 in enumerate(_s1_030):
        _s1_055 = f'chunk-author-{_s1_029}'
        _s1_032 = [_dq('LS0t'), _dq('dHlwZTogaW5kZXg='), f'tags: [chunk-index, {_s1_055}]', _dq('LS0t'), '', f'# Authors: {_s1_029}', '']
        if _s1_042 > 0:
            _s1_032.append(f'Prev: [[_chunk-author-{_s1_030[_s1_042 - 1]}]]')
        if _s1_042 < len(_s1_030) - 1:
            _s1_032.append(f'Next: [[_chunk-author-{_s1_030[_s1_042 + 1]}]]')
        _s1_032.append(_dq('VXA6IFtbYXV0aG9ycy1pbmRleF1d'))
        _s1_032.append('')
        _s1_032.append(f'## Members ({len(_s1_015[_s1_029])})')
        _s1_032.append('')
        for _s1_050, name, _s1_036 in sorted(_s1_015[_s1_029], key=lambda _s1_054: _s1_054[1].lower()):
            _s1_032.append(f'- [[{_s1_050}|{name}]] ({_s1_036} RFC(s))')
        _s1_032.append('')
        (_s1_010 / _s1_029 / f'_chunk-author-{_s1_029}.md').write_text(_dq('Cg==').join(_s1_032), encoding=_dq('dXRmLTg='))
    _s1_027 = [_dq('LS0t'), _dq('dHlwZTogaW5kZXg='), _dq('dGFnczogW2NvZGViYXNlLW1hcCwgcmZjLWVkaXRvciwgYXV0aG9ycywgY2h1bmstaW5kZXhd'), _dq('LS0t'), '', _dq('IyBSRkMgQXV0aG9ycyBJbmRleA=='), '', _dq('QnJhaWRlZCBwZXItbGV0dGVyIGNodW5rIGNoYWluIOKAlCBmaWx0ZXIgdGhlIGdyYXBoIHZpZXcgYnkgYSBgY2h1bmstYXV0aG9yLTxMZXR0ZXI+YCB0YWcgb3Igb3BlbiBhIGxldHRlcidzIGxvY2FsIGdyYXBoIHRvIGJyb3dzZSBhdXRob3JzIHdpdGhvdXQgbG9hZGluZyBhbGwgb2YgdGhlbSBhdCBvbmNlLg=='), '']
    for _s1_029 in _s1_030:
        _s1_027.append(f'- [[_chunk-author-{_s1_029}]] ({len(_s1_015[_s1_029])} authors)')
    _s1_027.append('')
    (dst / _dq('YXV0aG9ycy1pbmRleC5tZA==')).write_text(_dq('Cg==').join(_s1_027), encoding=_dq('dXRmLTg='))
    print(f'wrote {len(_s1_022)} author notes to {_s1_010}')
    print(f'wrote {len(_s1_030)} letter chunk indexes + authors-index.md')

def main() -> None:
    _s1_039 = argparse.ArgumentParser(description=__doc__)
    _s1_039.add_argument(_dq('LS1zcmM='), type=Path, default=Path(_dq('L2RhdGEvY29ycHVzL3JmYy1lZGl0b3I=')))
    _s1_039.add_argument(_dq('LS1kc3Q='), type=Path, default=Path(_dq('L2RhdGEvdmF1bHQvcmZjLWVkaXRvcg==')))
    _s1_039.add_argument(_dq('LS1saW1pdA=='), type=int, default=None, help=_dq('c2NhbiBhdCBtb3N0IE4gUkZDIGZpbGVz'))
    _s1_007 = _s1_039.parse_args()
    _s1_009 = _s1_017(_s1_007.src, _s1_007.limit)
    _s1_057(_s1_009, _s1_007.dst)
if __name__ == _dq('X19tYWluX18='):
    main()
