#!/usr/bin/env python3
from __future__ import annotations

import base64 as _b64
def _dq(_s):
    return _b64.b64decode(_s.encode("ascii")).decode("utf-8")

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
_s0_003 = _dq('DA==')
_s0_007 = _dq('SmFudWFyeXxGZWJydWFyeXxNYXJjaHxBcHJpbHxNYXl8SnVuZXxKdWx5fEF1Z3VzdHxTZXB0ZW1iZXJ8T2N0b2JlcnxOb3ZlbWJlcnxEZWNlbWJlcg==')
_s0_004 = re.compile(f'^\\s*\\S.*\\b(?:{_s0_007})\\s+\\d{{4}}\\s*$')
_s0_009 = re.compile(_dq('XlxzKlxTPy4qXFtccypbUHBdYWdlXHMrW2l2eGxjZG0wLTldK1xzKlxdXHMqJA=='))
_s0_006 = {_dq('cmZjX251bWJlcg=='): re.compile(_dq('UmVxdWVzdCBmb3IgQ29tbWVudHM6XHMqKFxkKyk='), re.I), _dq('c3RkX251bWJlcg=='): re.compile(_dq('XlNURDpccyooXFMuKj8pKD86XHN7Mix9XFN8JCk='), re.I | re.M), _dq('Y2F0ZWdvcnk='): re.compile(_dq('XkNhdGVnb3J5OlxzKihcUy4qPykoPzpcc3syLH1cU3wkKQ=='), re.I | re.M), _dq('aXNzbg=='): re.compile(_dq('XklTU046XHMqKFxTLio/KSg/OlxzezIsfVxTfCQp'), re.I | re.M), _dq('b2Jzb2xldGVz'): re.compile(_dq('Xk9ic29sZXRlczpccyooXFMuKj8pKD86XHN7Mix9XFN8JCk='), re.I | re.M), _dq('dXBkYXRlcw=='): re.compile(_dq('XlVwZGF0ZXM6XHMqKFxTLio/KSg/OlxzezIsfVxTfCQp'), re.I | re.M)}
_s0_005 = re.compile(_dq('Xig/OlJlcXVlc3QgZm9yIENvbW1lbnRzfFJGQ3xCQ1B8U1REfEZZSXxJRU58Q2F0ZWdvcnl8SVNTTnxPYnNvbGV0ZXN8VXBkYXRlc3xJbnRlcm5ldC1EcmFmdClccyo6fF4oPzpOZXR3b3JrIFdvcmtpbmcgR3JvdXB8SW50ZXJuZXQgRW5naW5lZXJpbmcgVGFzayBGb3JjZSkoPzpccysuKik/JA=='), re.I)
_s0_010 = re.compile(_dq('XihcZCsoPzpcLlxkKykqKVwuP1xzKyhcUy4qKSQ='))
_s0_000 = re.compile(_dq('XkFwcGVuZGl4XHMrKFtBLVowLTldKylcLj9ccyooLiopJA=='), re.I)
_s0_012 = re.compile(_dq('XC57Mix9XHMqW2l2eGxjZG0wLTldK1xzKiQ='), re.I)
_s0_008 = {_dq('YWJzdHJhY3Q='), _dq('c3RhdHVzIG9mIHRoaXMgbWVtbw=='), _dq('Y29weXJpZ2h0IG5vdGljZQ=='), _dq('dGFibGUgb2YgY29udGVudHM='), _dq('YWNrbm93bGVkZ2VtZW50cw=='), _dq('YWNrbm93bGVkZ21lbnRz'), _dq('YXV0aG9yJ3MgYWRkcmVzcw=='), _dq('YXV0aG9ycycgYWRkcmVzc2Vz'), _dq('ZnVsbCBjb3B5cmlnaHQgc3RhdGVtZW50'), _dq('c2VjdXJpdHkgY29uc2lkZXJhdGlvbnM='), _dq('aWFuYSBjb25zaWRlcmF0aW9ucw=='), _dq('cmVmZXJlbmNlcw=='), _dq('aW50cm9kdWN0aW9u'), _dq('cHJlZmFjZQ=='), _dq('Z2xvc3Nhcnk=')}
_s0_002 = {_dq('cmZj'): _dq('UkZD'), _dq('YmNw'): _dq('QkNQ'), _dq('c3Rk'): _dq('U1RE'), _dq('Znlp'): _dq('RllJ'), _dq('aWVu'): _dq('SUVO')}
_s0_013 = re.compile(_dq('XnJmYyhcZCspW2Etel0/XC50eHQk'), re.I)
_s0_001 = 1000

def _s0_018(_s0_052: int) -> str:
    _s0_044 = _s0_052 // _s0_001 * _s0_001
    _s0_035 = _s0_044 + _s0_001 - 1
    return f'{_s0_044:04d}-{_s0_035:04d}'

def _s0_019(_s0_071: Path, _s0_072: Path, _s0_029: Path) -> Path:
    _s0_064 = _s0_071.relative_to(_s0_072)
    if len(_s0_064.parts) > 1:
        return _s0_029 / _s0_064.with_suffix(_dq('Lm1k'))
    _s0_045 = _s0_013.match(_s0_071.name)
    if _s0_045:
        return _s0_029 / _dq('cmZj') / _s0_018(int(_s0_045.group(1))) / _s0_064.with_suffix(_dq('Lm1k')).name
    return _s0_029 / _dq('cmVmZXJlbmNl') / _s0_064.with_suffix(_dq('Lm1k')).name

def _s0_022(_s0_071: Path, _s0_072: Path) -> str:
    _s0_064 = _s0_071.relative_to(_s0_072)
    if len(_s0_064.parts) > 1:
        return f'chunk-{_s0_064.parts[0]}'
    _s0_045 = _s0_013.match(_s0_071.name)
    if _s0_045:
        return f'chunk-rfc-{_s0_018(int(_s0_045.group(1)))}'
    return _dq('Y2h1bmstcmVmZXJlbmNl')

def _s0_021(_s0_075: str) -> tuple[int, str]:
    _s0_045 = re.match(_dq('Y2h1bmstcmZjLShcZCspLVxkKyQ='), _s0_075)
    if _s0_045:
        return (0, f'{int(_s0_045.group(1)):08d}')
    _s0_062 = {_dq('Y2h1bmstYmNw'): 1, _dq('Y2h1bmstZnlp'): 2, _dq('Y2h1bmstaWVu'): 3, _dq('Y2h1bmstc3Rk'): 4, _dq('Y2h1bmstcmVmZXJlbmNl'): 5}
    return (_s0_062.get(_s0_075, 9), _s0_075)

def _s0_079(_s0_023: dict[str, dict], _s0_029: Path) -> Path:
    _s0_055 = sorted(_s0_023, key=_s0_021)
    for _s0_061, _s0_075 in enumerate(_s0_055):
        _s0_037 = _s0_023[_s0_075]
        _s0_043 = [_dq('LS0t'), _dq('dHlwZTogaW5kZXg='), f'tags: [chunk-index, {_s0_075}]', _dq('LS0t'), '', f'# Chunk: {_s0_075}', '']
        if _s0_061 > 0:
            _s0_043.append(f'Prev: [[_{_s0_055[_s0_061 - 1]}]]')
        if _s0_061 < len(_s0_055) - 1:
            _s0_043.append(f'Next: [[_{_s0_055[_s0_061 + 1]}]]')
        _s0_043.append(_dq('VXA6IFtbX2NodW5rLXZhdWx0XV0='))
        _s0_043.append('')
        _s0_043.append(f"## Members ({len(_s0_037['stems'])})")
        _s0_043.append('')
        for stem in sorted(_s0_037[_dq('c3RlbXM=')], key=lambda _s0_066: (len(_s0_066), _s0_066)):
            _s0_043.append(f'- [[{stem}]]')
        _s0_043.append('')
        (_s0_037[_dq('ZGly')] / f'_{_s0_075}.md').write_text(_dq('Cg==').join(_s0_043), encoding=_dq('dXRmLTg='))
    _s0_048 = [_dq('LS0t'), _dq('dHlwZTogaW5kZXg='), _dq('dGFnczogW2NodW5rLWluZGV4LCBjaHVuay12YXVsdF0='), _dq('LS0t'), '', _dq('IyBSRkMgVmF1bHQgTWFw'), '', _dq('QnJhaWRlZCBjaHVuayBjaGFpbiDigJQgb3BlbiBvbmUgY2h1bmsncyBsb2NhbCBncmFwaCBvciBmaWx0ZXIgdGhlIGdyYXBoIHZpZXcgYnkgaXRzIHRhZyB0byBleHBsb3JlIHRoYXQgc2xpY2Ugd2l0aG91dCBsb2FkaW5nIHRoZSB3aG9sZSB2YXVsdC4='), '']
    for _s0_075 in _s0_055:
        _s0_048.append(f"- [[_{_s0_075}]] ({len(_s0_023[_s0_075]['stems'])} notes)")
    _s0_048.append(_dq('LSBbW2F1dGhvcnMtaW5kZXhdXSAoYXV0aG9yIGNodW5rIGNoYWluKQ=='))
    _s0_048.append('')
    _s0_049 = _s0_029 / _dq('X2NodW5rLXZhdWx0Lm1k')
    _s0_049.write_text(_dq('Cg==').join(_s0_048), encoding=_dq('dXRmLTg='))
    return _s0_049

def _s0_032(stem: str) -> str:
    _s0_045 = re.match(_dq('KFthLXpdKykoXGQrW2Etel0/KSQ='), stem)
    if _s0_045 and _s0_045.group(1) in _s0_002:
        return f'{_s0_002[_s0_045.group(1)]} {_s0_045.group(2)}'
    return stem

def _s0_073(_s0_043: list[str]) -> list[str]:
    _s0_036 = 0
    while _s0_036 < len(_s0_043) and (not _s0_043[_s0_036].strip()):
        _s0_036 += 1
    if _s0_036 < len(_s0_043) and _s0_004.match(_s0_043[_s0_036]):
        _s0_036 += 1
        _s0_039 = _s0_036
        while _s0_039 < len(_s0_043) and (not _s0_043[_s0_039].strip()):
            _s0_039 += 1
        if _s0_039 < len(_s0_043) and 0 < len(_s0_043[_s0_039].strip()) <= 78:
            _s0_036 = _s0_039 + 1
    _s0_043 = _s0_043[_s0_036:]
    _s0_039 = len(_s0_043)
    while _s0_039 > 0 and (not _s0_043[_s0_039 - 1].strip()):
        _s0_039 -= 1
    if _s0_039 > 0 and _s0_009.match(_s0_043[_s0_039 - 1]):
        _s0_039 -= 1
    _s0_043 = _s0_043[:_s0_039]
    return _s0_043

def _s0_024(_s0_063: str) -> str:
    _s0_063 = _s0_063.replace(_dq('DQo='), _dq('Cg==')).replace(_dq('DQ=='), _dq('Cg=='))
    _s0_058 = _s0_063.split(_s0_003) if _s0_003 in _s0_063 else [_s0_063]
    _s0_026 = [_s0_073(_s0_057.split(_dq('Cg=='))) for _s0_057 in _s0_058]
    _s0_076 = _dq('Cgo=').join((_dq('Cg==').join(_s0_043) for _s0_043 in _s0_026))
    _s0_076 = _dq('Cg==').join((_s0_040 for _s0_040 in _s0_076.split(_dq('Cg==')) if not _s0_009.match(_s0_040)))
    _s0_076 = re.sub(_dq('XG57Myx9'), _dq('Cgo='), _s0_076)
    return _s0_076.strip(_dq('Cg=='))

def _s0_030(_s0_076: str) -> dict[str, str]:
    _s0_050: dict[str, str] = {}
    for key, _s0_060 in _s0_006.items():
        _s0_045 = _s0_060.search(_s0_076)
        if _s0_045:
            _s0_050[key] = re.sub(_dq('XHMr'), _dq('IA=='), _s0_045.group(1)).strip()
    return _s0_050

def _s0_031(_s0_043: list[str], stem: str) -> tuple[str, int]:
    _s0_036 = 0
    limit = min(len(_s0_043), 60)
    _s0_067 = False
    while _s0_036 < limit:
        _s0_042 = _s0_043[_s0_036]
        if not _s0_042.strip():
            _s0_036 += 1
            continue
        if _s0_005.match(_s0_042.strip()):
            _s0_067 = True
            _s0_036 += 1
            continue
        if _s0_067:
            _s0_077 = _s0_042.strip()
            _s0_039 = _s0_036 + 1
            while _s0_039 < limit and _s0_043[_s0_039].strip() and (len(_s0_043[_s0_039].strip()) < 60):
                _s0_054 = _s0_043[_s0_039].strip()
                if _s0_054.lower() in _s0_008:
                    break
                _s0_077 += _dq('IA==') + _s0_054
                _s0_039 += 1
            return (_s0_077, _s0_039)
        break
    return (_s0_032(stem), 0)

def _s0_034(_s0_053: str) -> int:
    return min(2 + _s0_053.count(_dq('Lg==')), 6)

@dataclass
class _s0_011:
    heading: str | None = None
    level: int = 2
    body: list[str] = field(default_factory=list)

def _s0_020(_s0_043: list[str]) -> list[_s0_011]:
    _s0_069: list[_s0_011] = [_s0_011(heading=None, level=1, body=[])]
    for _s0_042 in _s0_043:
        _s0_074 = _s0_042.strip()
        _s0_038 = bool(_s0_012.search(_s0_042))
        _s0_016 = _s0_042 == _s0_074 and (not _s0_038)
        _s0_045 = _s0_010.match(_s0_042) if _s0_016 else None
        _s0_014 = _s0_000.match(_s0_042) if _s0_016 else None
        _s0_051 = _s0_074.lower() in _s0_008 if _s0_016 else False
        if _s0_045:
            _s0_069.append(_s0_011(heading=f'{_s0_045.group(1)}. {_s0_045.group(2)}', level=_s0_034(_s0_045.group(1))))
        elif _s0_014:
            _s0_041 = f'Appendix {_s0_014.group(1)}' + (f'. {_s0_014.group(2)}' if _s0_014.group(2) else '')
            _s0_069.append(_s0_011(heading=_s0_041, level=2))
        elif _s0_051:
            _s0_069.append(_s0_011(heading=_s0_074, level=2))
        else:
            _s0_069[-1].body.append(_s0_042)
    return _s0_069

def _s0_065(_s0_071: Path, _s0_072: Path, _s0_063: str, _s0_075: str) -> str:
    stem = _s0_071.stem
    _s0_025 = _s0_024(_s0_063)
    _s0_050 = _s0_030(_s0_025)
    _s0_043 = _s0_025.split(_dq('Cg=='))
    _s0_077, _s0_078 = _s0_031(_s0_043, stem)
    _s0_017 = _s0_043[_s0_078:] if _s0_078 else _s0_043
    _s0_069 = _s0_020(_s0_017)
    _s0_064 = _s0_071.relative_to(_s0_072.parent)
    _s0_033 = [_dq('LS0t'), _dq('dHlwZTogcmVmZXJlbmNl'), _dq('bGFuZ3VhZ2U6IE1hcmtkb3du'), f'file: {_s0_064}', _dq('c291cmNlOiByZmMtZWRpdG9yIHJmY3MtdGV4dC1vbmx5IG1pcnJvcg=='), f'tags: [reference-cache, rfc-editor, ietf, {_s0_075}]']
    if _dq('cmZjX251bWJlcg==') in _s0_050:
        _s0_033.append(f"rfc: {_s0_050['rfc_number']}")
    if _dq('c3RkX251bWJlcg==') in _s0_050:
        _s0_033.append(f"std: {_s0_050['std_number']}")
    for key in (_dq('Y2F0ZWdvcnk='), _dq('aXNzbg=='), _dq('b2Jzb2xldGVz'), _dq('dXBkYXRlcw==')):
        if key in _s0_050:
            _s0_033.append(f'{key}: "{_s0_050[key]}"')
    _s0_033.append(_dq('LS0t'))
    _s0_056 = [_dq('Cg==').join(_s0_033), '', f'# {_s0_077}', '']
    for _s0_068 in _s0_069:
        if _s0_068.heading:
            _s0_056.append(f"{'#' * _s0_068.level} {_s0_068.heading}")
            _s0_056.append('')
        body = _dq('Cg==').join(_s0_068.body).strip(_dq('Cg=='))
        if body.strip():
            _s0_056.append(_dq('YGBgdGV4dA=='))
            _s0_056.append(body)
            _s0_056.append(_dq('YGBg'))
            _s0_056.append('')
    return _dq('Cg==').join(_s0_056).rstrip() + _dq('Cg==')

def _s0_027(_s0_072: Path, _s0_029: Path, only: str | None, limit: int | None) -> None:
    count = 0
    _s0_070 = 0
    _s0_023: dict[str, dict] = {}
    for _s0_071 in sorted(_s0_072.rglob(only or _dq('Ki50eHQ='))):
        if not _s0_071.is_file():
            _s0_070 += 1
            continue
        if limit and count >= limit:
            break
        _s0_075 = _s0_022(_s0_071, _s0_072)
        _s0_063 = _s0_071.read_text(encoding=_dq('dXRmLTg='), errors=_dq('cmVwbGFjZQ=='))
        _s0_046 = _s0_065(_s0_071, _s0_072, _s0_063, _s0_075)
        _s0_028 = _s0_019(_s0_071, _s0_072, _s0_029)
        _s0_028.parent.mkdir(parents=True, exist_ok=True)
        _s0_028.write_text(_s0_046, encoding=_dq('dXRmLTg='))
        _s0_023.setdefault(_s0_075, {_dq('ZGly'): _s0_028.parent, _dq('c3RlbXM='): []})[_dq('c3RlbXM=')].append(_s0_028.stem)
        count += 1
        if count % 1000 == 0:
            print(f'converted {count} files...')
    print(f'done: {count} files converted, {_s0_070} skipped')
    if _s0_023:
        _s0_047 = _s0_079(_s0_023, _s0_029)
        print(f'wrote {len(_s0_023)} chunk indexes + master braid index: {_s0_047}')

def main() -> None:
    _s0_059 = argparse.ArgumentParser(description=__doc__)
    _s0_059.add_argument(_dq('LS1zcmM='), type=Path, default=Path(_dq('L2RhdGEvY29ycHVzL3JmYy1lZGl0b3I=')))
    _s0_059.add_argument(_dq('LS1kc3Q='), type=Path, default=Path(_dq('L2RhdGEvdmF1bHQvcmZjLWVkaXRvcg==')))
    _s0_059.add_argument(_dq('LS1vbmx5'), default=None, help=_dq('Z2xvYiBwYXR0ZXJuLCBkZWZhdWx0ICoudHh0'))
    _s0_059.add_argument(_dq('LS1saW1pdA=='), type=int, default=None, help=_dq('Y29udmVydCBhdCBtb3N0IE4gZmlsZXM='))
    _s0_015 = _s0_059.parse_args()
    _s0_027(_s0_015.src, _s0_015.dst, _s0_015.only, _s0_015.limit)
if __name__ == _dq('X19tYWluX18='):
    main()
