#!/usr/bin/env python3
from __future__ import annotations

import base64 as _b64
def _dq(_s):
    return _b64.b64decode(_s.encode("ascii")).decode("utf-8")

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlparse
_s2_003 = _dq('RG9jc1Jlc2VhcmNoQm90LzEuMCAobG9jYWwgcmVmZXJlbmNlIGNhY2hpbmc7IG5vIGRpcmVjdCBjb250YWN0KQ==')
_s2_001 = 8 * 1024 * 1024
_s2_002 = 1.5
_s2_000 = [(_dq('cHl0aG9u'), _dq('aHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy9saWJyYXJ5L2luZGV4Lmh0bWw='), _dq('c3RkbGliIGluZGV4')), (_dq('amF2YXNjcmlwdA=='), _dq('aHR0cHM6Ly9kZXZlbG9wZXIubW96aWxsYS5vcmcvZW4tVVMvZG9jcy9XZWIvSmF2YVNjcmlwdC9SZWZlcmVuY2U='), _dq('SlMgcmVmZXJlbmNlIGluZGV4')), (_dq('bm9kZWpz'), _dq('aHR0cHM6Ly9ub2RlanMub3JnL2RvY3MvbGF0ZXN0L2FwaS9hbGwuaHRtbA=='), _dq('ZnVsbCBBUEkgZG9jIChvZmZpY2lhbCBzaW5nbGUtZmlsZSBkdW1wKQ==')), (_dq('dHlwZXNjcmlwdA=='), _dq('aHR0cHM6Ly93d3cudHlwZXNjcmlwdGxhbmcub3JnL2RvY3MvaGFuZGJvb2svaW50cm8uaHRtbA=='), _dq('aGFuZGJvb2sgaW50cm8=')), (_dq('amF2YQ=='), _dq('aHR0cHM6Ly9kb2NzLm9yYWNsZS5jb20vZW4vamF2YS9qYXZhc2UvMjEvZG9jcy9hcGkvaW5kZXguaHRtbA=='), _dq('SmF2YSBTRSBBUEkgaW5kZXg=')), (_dq('Y3Bw'), _dq('aHR0cHM6Ly9lbi5jcHByZWZlcmVuY2UuY29tL3cvY3BwL3N0YW5kYXJkX2xpYnJhcnk='), _dq('c3RkIGxpYnJhcnkgaW5kZXg=')), (_dq('Y3NoYXJw'), _dq('aHR0cHM6Ly9sZWFybi5taWNyb3NvZnQuY29tL2VuLXVzL2RvdG5ldC9jc2hhcnAvdG91ci1vZi1jc2hhcnAv'), _dq('QyMgdG91ci9yZWZlcmVuY2U=')), (_dq('Z28='), _dq('aHR0cHM6Ly9nby5kZXYvcmVmL3NwZWM='), _dq('bGFuZ3VhZ2Ugc3BlYw==')), (_dq('Z28='), _dq('aHR0cHM6Ly9wa2cuZ28uZGV2L3N0ZA=='), _dq('c3RkbGliIGluZGV4')), (_dq('cnVzdA=='), _dq('aHR0cHM6Ly9kb2MucnVzdC1sYW5nLm9yZy9zdGQvaW5kZXguaHRtbA=='), _dq('c3RkIGRvY3MgaW5kZXg=')), (_dq('cnVzdA=='), _dq('aHR0cHM6Ly9kb2MucnVzdC1sYW5nLm9yZy9ib29rL2luZGV4Lmh0bWw='), _dq('Ym9vayBpbmRleA==')), (_dq('cGhw'), _dq('aHR0cHM6Ly93d3cucGhwLm5ldC9tYW51YWwvZW4vaW5kZXhlcy5mdW5jdGlvbnMucGhw'), _dq('ZnVuY3Rpb24gaW5kZXg=')), (_dq('cnVieQ=='), _dq('aHR0cHM6Ly9kb2NzLnJ1YnktbGFuZy5vcmcvZW4vMy4zL2luZGV4Lmh0bWw='), _dq('Y29yZSBBUEkgaW5kZXg=')), (_dq('c3dpZnQ='), _dq('aHR0cHM6Ly93d3cuc3dpZnQub3JnL2RvY3VtZW50YXRpb24v'), _dq('ZG9jdW1lbnRhdGlvbiBpbmRleA==')), (_dq('a290bGlu'), _dq('aHR0cHM6Ly9rb3RsaW5sYW5nLm9yZy9kb2NzL2hvbWUuaHRtbA=='), _dq('ZG9jcyBob21l')), (_dq('a290bGlu'), _dq('aHR0cHM6Ly9rb3RsaW5sYW5nLm9yZy9hcGkvbGF0ZXN0L2p2bS9zdGRsaWIv'), _dq('c3RkbGliIEFQSSBpbmRleA==')), (_dq('cg=='), _dq('aHR0cHM6Ly9jcmFuLnItcHJvamVjdC5vcmcvZG9jL21hbnVhbHMvci1yZWxlYXNlL1ItbGFuZy5odG1s'), _dq('UiBsYW5ndWFnZSBkZWZpbml0aW9u')), (_dq('cG9zdGdyZXNxbA=='), _dq('aHR0cHM6Ly93d3cucG9zdGdyZXNxbC5vcmcvZG9jcy9jdXJyZW50L2luZGV4Lmh0bWw='), _dq('ZG9jcyBpbmRleA==')), (_dq('bXlzcWw='), _dq('aHR0cHM6Ly9kZXYubXlzcWwuY29tL2RvYy9yZWZtYW4vOC40L2VuLw=='), _dq('cmVmZXJlbmNlIG1hbnVhbCBpbmRleA==')), (_dq('YmFzaA=='), _dq('aHR0cHM6Ly93d3cuZ251Lm9yZy9zb2Z0d2FyZS9iYXNoL21hbnVhbC9iYXNoLmh0bWw='), _dq('ZnVsbCBtYW51YWwgKHNpbmdsZSBwYWdlKQ==')), (_dq('cG9zaXgtc2hlbGw='), _dq('aHR0cHM6Ly9wdWJzLm9wZW5ncm91cC5vcmcvb25saW5lcHVicy85Njk5OTE5Nzk5L3V0aWxpdGllcy9WM19jaGFwMDIuaHRtbA=='), _dq('c2hlbGwgY29tbWFuZCBsYW5ndWFnZQ==')), (_dq('bWF0bGFi'), _dq('aHR0cHM6Ly93d3cubWF0aHdvcmtzLmNvbS9oZWxwL21hdGxhYi9yZWZlcmVuY2VsaXN0Lmh0bWw='), _dq('ZnVuY3Rpb24gcmVmZXJlbmNlIGluZGV4')), (_dq('c2NhbGE='), _dq('aHR0cHM6Ly9kb2NzLnNjYWxhLWxhbmcub3JnL292ZXJ2aWV3cy9pbmRleC5odG1s'), _dq('b3ZlcnZpZXdzIGluZGV4')), (_dq('c2NhbGE='), _dq('aHR0cHM6Ly93d3cuc2NhbGEtbGFuZy5vcmcvYXBpL2N1cnJlbnQv'), _dq('c3RkbGliIEFQSSBpbmRleA==')), (_dq('ZGFydA=='), _dq('aHR0cHM6Ly9kYXJ0LmRldi9sYW5ndWFnZQ=='), _dq('bGFuZ3VhZ2UgdG91ciAoY29yZSBBUEkgaW5kZXggcmV0dXJuZWQgNDA0KQ==')), (_dq('Zmx1dHRlcg=='), _dq('aHR0cHM6Ly9hcGkuZmx1dHRlci5kZXYvaW5kZXguaHRtbA=='), _dq('Rmx1dHRlciBBUEkgaW5kZXg=')), (_dq('cGVybA=='), _dq('aHR0cHM6Ly9wZXJsZG9jLnBlcmwub3JnL3BlcmxmdW5j'), _dq('YnVpbHRpbiBmdW5jdGlvbnM=')), (_dq('cGVybA=='), _dq('aHR0cHM6Ly9wZXJsZG9jLnBlcmwub3JnL3BlcmxpbnRybw=='), _dq('bGFuZ3VhZ2UgaW50cm8=')), (_dq('b2JqZWN0aXZlLWM='), _dq('aHR0cHM6Ly9kZXZlbG9wZXIuYXBwbGUuY29tL2RvY3VtZW50YXRpb24vb2JqZWN0aXZlYw=='), _dq('Rm91bmRhdGlvbi9Db2NvYSBpbmRleA==')), (_dq('bHVh'), _dq('aHR0cHM6Ly93d3cubHVhLm9yZy9tYW51YWwvNS40L21hbnVhbC5odG1s'), _dq('ZnVsbCBtYW51YWwgKHNpbmdsZSBwYWdlKQ==')), (_dq('aGFza2VsbA=='), _dq('aHR0cHM6Ly93d3cuaGFza2VsbC5vcmcvZG9jdW1lbnRhdGlvbi8='), _dq('ZG9jdW1lbnRhdGlvbiBpbmRleA==')), (_dq('aGFza2VsbA=='), _dq('aHR0cHM6Ly9oYWNrYWdlLmhhc2tlbGwub3JnL3BhY2thZ2UvYmFzZQ=='), _dq('YmFzZSBsaWJyYXJ5IGluZGV4')), (_dq('anVsaWE='), _dq('aHR0cHM6Ly9kb2NzLmp1bGlhbGFuZy5vcmcvZW4vdjEvYmFzZS9iYXNlLw=='), _dq('QmFzZSBsaWJyYXJ5IGluZGV4')), (_dq('ZWxpeGly'), _dq('aHR0cHM6Ly9lbGl4aXItbGFuZy5vcmcvZG9jcy5odG1s'), _dq('ZG9jdW1lbnRhdGlvbiBpbmRleA==')), (_dq('ZXJsYW5n'), _dq('aHR0cHM6Ly93d3cuZXJsYW5nLm9yZy9kb2Mv'), _dq('T1RQIGRvY3MgaW5kZXg='))]
_s2_004: dict[str, urllib.robotparser.RobotFileParser] = {}

def _s2_026(_s2_032: str) -> bool:
    _s2_022 = urlparse(_s2_032)
    _s2_012 = f'{_s2_022.scheme}://{_s2_022.netloc}'
    _s2_027 = _s2_004.get(_s2_012)
    if _s2_027 is None:
        _s2_027 = urllib.robotparser.RobotFileParser()
        _s2_027.set_url(_s2_012 + _dq('L3JvYm90cy50eHQ='))
        try:
            _s2_027.read()
        except Exception:
            _s2_027 = None
        _s2_004[_s2_012] = _s2_027
    if _s2_027 is None:
        return True
    return _s2_027.can_fetch(_s2_003, _s2_032)

def _s2_011(_s2_032: str, max_bytes: int) -> tuple[int, bytes | None, str]:
    _s2_024 = urllib.request.Request(_s2_032, headers={_dq('VXNlci1BZ2VudA=='): _s2_003})
    try:
        with urllib.request.urlopen(_s2_024, timeout=40) as _s2_025:
            _s2_006 = _s2_025.read(max_bytes + 1)
            if len(_s2_006) > max_bytes:
                return (_s2_025.status, None, _dq('c2tpcHBlZDogZXhjZWVkcyBtYXgtYnl0ZXMgY2Fw'))
            return (_s2_025.status, _s2_006, _s2_025.headers.get(_dq('Q29udGVudC1UeXBl'), ''))
    except urllib.error.HTTPError as e:
        return (_s2_008.code, None, f'http error: {_s2_008.reason}')
    except Exception as e:
        return (0, None, f'error: {_s2_008}')

def _s2_030(_s2_032: str) -> str:
    _s2_022 = urlparse(_s2_032)
    path = _s2_022.path.strip(_dq('Lw==')).replace(_dq('Lw=='), _dq('Xw==')) or _dq('aW5kZXg=')
    if not path.endswith((_dq('Lmh0bWw='), _dq('Lmh0bQ=='), _dq('LnBkZg=='), _dq('LnR4dA=='))):
        path += _dq('Lmh0bWw=')
    return path

def main() -> None:
    _s2_023 = argparse.ArgumentParser(description=__doc__)
    _s2_023.add_argument(_dq('LS1kc3Q='), type=Path, default=Path(_dq('L2RhdGEvY29ycHVzL2xhbmctZG9jcw==')))
    _s2_023.add_argument(_dq('LS1kZWxheQ=='), type=float, default=_s2_002)
    _s2_023.add_argument(_dq('LS1tYXgtYnl0ZXM='), type=int, default=_s2_001)
    _s2_005 = _s2_023.parse_args()
    _s2_005.dst.mkdir(parents=True, exist_ok=True)
    _s2_018 = []
    _s2_017: dict[str, float] = {}
    _s2_028 = _s2_029 = _s2_010 = 0
    _s2_031 = 0
    for _s2_014, _s2_032, _s2_020 in _s2_000:
        _s2_012 = urlparse(_s2_032).netloc
        _s2_016 = _s2_017.get(_s2_012, 0.0)
        _s2_033 = _s2_005.delay - (time.time() - _s2_016)
        if _s2_033 > 0:
            time.sleep(_s2_033)
        _s2_017[_s2_012] = time.time()
        _s2_009 = {_dq('bGFuZw=='): _s2_014, _dq('dXJs'): _s2_032, _dq('bm90ZQ=='): _s2_020, _dq('dGltZQ=='): time.strftime(_dq('JVktJW0tJWRUJUg6JU06JVNa'), time.gmtime())}
        if not _s2_026(_s2_032):
            _s2_009.update(status=_dq('c2tpcHBlZA=='), reason=_dq('cm9ib3RzLnR4dCBkaXNhbGxvd3M='))
            _s2_029 += 1
            _s2_018.append(_s2_009)
            print(f'[skip:robots] {_s2_014}: {_s2_032}')
            continue
        status, _s2_006, _s2_013 = _s2_011(_s2_032, _s2_005.max_bytes)
        if _s2_006 is None:
            _s2_009.update(status=_dq('ZmFpbGVk'), http_status=status, reason=_s2_013)
            _s2_010 += 1
            _s2_018.append(_s2_009)
            print(f'[fail] {_s2_014}: {_s2_032} ({_s2_013})')
            continue
        _s2_015 = _s2_005.dst / _s2_014
        _s2_015.mkdir(parents=True, exist_ok=True)
        _s2_021 = _s2_015 / _s2_030(_s2_032)
        _s2_021.write_bytes(_s2_006)
        _s2_007 = hashlib.sha256(_s2_006).hexdigest()
        _s2_031 += len(_s2_006)
        _s2_028 += 1
        _s2_009.update(status=_dq('c2F2ZWQ='), http_status=status, bytes=len(_s2_006), sha256=_s2_007, content_type=_s2_013, file=str(_s2_021))
        _s2_018.append(_s2_009)
        print(f'[ok] {_s2_014}: {_s2_032} -> {_s2_021} ({len(_s2_006)} bytes)')
    _s2_019 = _s2_005.dst / _dq('bWFuaWZlc3QuanNvbg==')
    _s2_019.write_text(json.dumps(_s2_018, indent=2), encoding=_dq('dXRmLTg='))
    print(f'\ndone: {_s2_028} saved, {_s2_029} skipped, {_s2_010} failed, {_s2_031 / 1024:.1f} KiB written')
    print(f'manifest: {_s2_019}')
if __name__ == _dq('X19tYWluX18='):
    main()
