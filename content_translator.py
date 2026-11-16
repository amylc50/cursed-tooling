#!/usr/bin/env python3
from __future__ import annotations

import base64 as _b64
def _dq(_s):
    return _b64.b64decode(_s.encode("ascii")).decode("utf-8")

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
_k_010 = {_dq('c2NyaXB0'), _dq('c3R5bGU='), _dq('bm9zY3JpcHQ='), _dq('c3Zn'), _dq('aWZyYW1l'), _dq('b2JqZWN0'), _dq('ZW1iZWQ='), _dq('bmF2'), _dq('Zm9vdGVy'), _dq('aGVhZGVy'), _dq('YXNpZGU='), _dq('Zm9ybQ=='), _dq('YnV0dG9u'), _dq('ZGlhbG9n')}
_k_009 = re.compile(_dq('KGNvb2tpZXxiYW5uZXJ8c2lkZWJhcnxhZHZlcnR8c3BvbnNvcnxwcm9tb3xuZXdzbGV0dGVyfHBvcHVwfG1vZGFsfG1lbnV8bmF2YmFyfGJyZWFkY3J1bWJ8c29jaWFsLXNoYXJlfGRpc2NsYWltZXJ8cGFnaW5hdGlvbnx3aWRnZXQp'), re.IGNORECASE)
_k_001 = {_dq('bWFpbg=='), _dq('YXJ0aWNsZQ==')}
_k_000 = re.compile(_dq('KGNvbnRlbnR8YXJ0aWNsZXxkb2N1bWVudHxwb3N0fG1hcmtkb3duLWJvZHl8ZG9jLWNvbnRlbnR8bWFpbi1jb250ZW50fHBhZ2UtY29udGVudCk='), re.IGNORECASE)

class _k_007(HTMLParser):

    def __init__(self, base_url: str='') -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.doc_title = ''
        self._title_buffer: list[str] = []
        self._in_title = False
        self._output_chunks: list[str] = []
        self._ignore_depth = 0
        self._tag_stack: list[str] = []
        self._in_pre = False
        self._in_code = False
        self._code_lang = ''
        self._in_table = False
        self._in_tr = False
        self._in_th = False
        self._in_td = False
        self._table_matrix: list[list[str]] = []
        self._current_row: list[str] = []
        self._current_cell: list[str] = []
        self._list_stack: list[tuple[str, int]] = []
        self._current_link: str | None = None
        self._link_text: list[str] = []

    def handle_starttag(self, _k_130: str, _k_016: list[tuple[str, str | None]]) -> None:
        _k_015 = {_k_061.lower(): _k_143 or '' for _k_061, _k_143 in _k_016}
        _k_131 = _k_130.lower()
        if _k_131 in _k_010:
            self._ignore_depth += 1
            return
        _k_026 = f"{_k_015.get('class', '')} {_k_015.get('id', '')}"
        if _k_131 not in (_dq('Ym9keQ=='), _dq('aHRtbA=='), _dq('bWFpbg=='), _dq('YXJ0aWNsZQ==')) and _k_009.search(_k_026):
            if not _k_000.search(_k_026):
                self._ignore_depth += 1
                return
        if self._ignore_depth > 0:
            self._ignore_depth += 1
            return
        self._tag_stack.append(_k_131)
        if _k_131 == _dq('dGl0bGU='):
            self._in_title = True
            self._title_buffer.clear()
        elif _k_131 in (_dq('aDE='), _dq('aDI='), _dq('aDM='), _dq('aDQ='), _dq('aDU='), _dq('aDY=')):
            _k_066 = int(_k_131[1])
            self._output_chunks.append(f"\n\n{'#' * _k_066} ")
        elif _k_131 == _dq('cA=='):
            self._output_chunks.append(_dq('Cgo='))
        elif _k_131 == _dq('YnI='):
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 == _dq('aHI='):
            self._output_chunks.append(_dq('CgotLS0KCg=='))
        elif _k_131 == _dq('YmxvY2txdW90ZQ=='):
            self._output_chunks.append(_dq('Cgo+IA=='))
        elif _k_131 == _dq('cHJl'):
            self._in_pre = True
            cls = _k_015.get(_dq('Y2xhc3M='), '')
            _k_064 = re.search(_dq('KD86bGFuZyg/OnVhZ2UpPy18aGlnaGxpZ2h0LSkoXHcrKQ=='), cls, re.I)
            self._code_lang = _k_064.group(1).lower() if _k_064 else ''
            self._output_chunks.append(f'\n\n```{self._code_lang}\n')
        elif _k_131 == _dq('Y29kZQ=='):
            self._in_code = True
            if not self._in_pre:
                cls = _k_015.get(_dq('Y2xhc3M='), '')
                _k_064 = re.search(_dq('KD86bGFuZyg/OnVhZ2UpPy0pKFx3Kyk='), cls, re.I)
                if _k_064:
                    self._code_lang = _k_064.group(1).lower()
                self._output_chunks.append(_dq('YA=='))
        elif _k_131 in (_dq('c3Ryb25n'), _dq('Yg==')):
            self._output_chunks.append(_dq('Kio='))
        elif _k_131 in (_dq('ZW0='), _dq('aQ==')):
            self._output_chunks.append(_dq('Kg=='))
        elif _k_131 == _dq('YQ=='):
            _k_053 = _k_015.get(_dq('aHJlZg=='), '')
            if _k_053 and (not _k_053.startswith(_dq('amF2YXNjcmlwdDo='))) and (not _k_053.startswith(_dq('Iw=='))):
                self._current_link = _k_053
                self._link_text = []
        elif _k_131 == _dq('dWw='):
            self._list_stack.append((_dq('dWw='), 0))
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 == _dq('b2w='):
            self._list_stack.append((_dq('b2w='), 0))
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 == _dq('bGk='):
            indent = _dq('ICA=') * max(0, len(self._list_stack) - 1)
            if self._list_stack and self._list_stack[-1][0] == _dq('b2w='):
                _k_070, _k_030 = self._list_stack.pop()
                _k_030 += 1
                self._list_stack.append((_k_070, _k_030))
                self._output_chunks.append(f'\n{indent}{_k_030}. ')
            else:
                self._output_chunks.append(f'\n{indent}- ')
        elif _k_131 == _dq('dGFibGU='):
            self._in_table = True
            self._table_matrix = []
        elif _k_131 == _dq('dHI='):
            self._in_tr = True
            self._current_row = []
        elif _k_131 in (_dq('dGg='), _dq('dGQ=')):
            self._in_th = _k_131 == _dq('dGg=')
            self._in_td = _k_131 == _dq('dGQ=')
            self._current_cell = []

    def handle_endtag(self, _k_130: str) -> None:
        _k_131 = _k_130.lower()
        if self._ignore_depth > 0:
            self._ignore_depth -= 1
            return
        if self._tag_stack and self._tag_stack[-1] == _k_131:
            self._tag_stack.pop()
        if _k_131 == _dq('dGl0bGU='):
            self._in_title = False
            self.doc_title = ''.join(self._title_buffer).strip()
        elif _k_131 in (_dq('aDE='), _dq('aDI='), _dq('aDM='), _dq('aDQ='), _dq('aDU='), _dq('aDY=')):
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 == _dq('cA=='):
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 == _dq('cHJl'):
            self._in_pre = False
            self._output_chunks.append(_dq('CmBgYAo='))
            self._code_lang = ''
        elif _k_131 == _dq('Y29kZQ=='):
            self._in_code = False
            if not self._in_pre:
                self._output_chunks.append(_dq('YA=='))
        elif _k_131 in (_dq('c3Ryb25n'), _dq('Yg==')):
            self._output_chunks.append(_dq('Kio='))
        elif _k_131 in (_dq('ZW0='), _dq('aQ==')):
            self._output_chunks.append(_dq('Kg=='))
        elif _k_131 == _dq('YQ=='):
            if self._current_link is not None:
                _k_134 = ''.join(self._link_text).strip()
                if _k_134:
                    self._output_chunks.append(f'[{_k_134}]({self._current_link})')
                self._current_link = None
                self._link_text = []
        elif _k_131 in (_dq('dWw='), _dq('b2w=')):
            if self._list_stack:
                self._list_stack.pop()
            self._output_chunks.append(_dq('Cg=='))
        elif _k_131 in (_dq('dGg='), _dq('dGQ=')):
            _k_018 = ''.join(self._current_cell).replace(_dq('Cg=='), _dq('IA==')).replace(_dq('fA=='), _dq('XHw=')).strip()
            self._current_row.append(_k_018)
            self._current_cell = []
            self._in_th = False
            self._in_td = False
        elif _k_131 == _dq('dHI='):
            if self._current_row:
                self._table_matrix.append(self._current_row)
            self._current_row = []
            self._in_tr = False
        elif _k_131 == _dq('dGFibGU='):
            self._in_table = False
            self._render_markdown_table()

    def handle_data(self, _k_034: str) -> None:
        if self._ignore_depth > 0:
            return
        if self._in_title:
            self._title_buffer.append(_k_034)
            return
        if self._in_table and (self._in_th or self._in_td):
            self._current_cell.append(_k_034)
            return
        if self._current_link is not None:
            self._link_text.append(_k_034)
            return
        if self._in_pre:
            self._output_chunks.append(_k_034)
        else:
            _k_024 = re.sub(_dq('WyBcdF0r'), _dq('IA=='), _k_034)
            self._output_chunks.append(_k_024)

    def _render_markdown_table(self) -> None:
        if not self._table_matrix:
            return
        _k_084 = max((len(_k_108) for _k_108 in self._table_matrix))
        if _k_084 == 0:
            return
        _k_079 = [_k_108 + [''] * (_k_084 - len(_k_108)) for _k_108 in self._table_matrix]
        _k_129 = [_dq('Cgo=')]
        _k_051 = _k_079[0]
        _k_129.append(_dq('fCA=') + _dq('IHwg').join(_k_051) + _dq('IHwK'))
        _k_129.append(_dq('fCA=') + _dq('IHwg').join([_dq('LS0t')] * _k_084) + _dq('IHwK'))
        for _k_108 in _k_079[1:]:
            _k_129.append(_dq('fCA=') + _dq('IHwg').join(_k_108) + _dq('IHwK'))
        _k_129.append(_dq('Cg=='))
        self._output_chunks.append(''.join(_k_129))

    def get_markdown(self) -> str:
        _k_097 = ''.join(self._output_chunks)
        _k_025 = re.sub(_dq('XG57Myx9'), _dq('Cgo='), _k_097)
        _k_025 = re.sub(_dq('ICtcbg=='), _dq('Cg=='), _k_025)
        return _k_025.strip()

@dataclass
class _k_005:
    title: str
    source_url: str
    content_hash: str
    word_count: int
    summary: str
    key_topics: list[str]
    code_snippets: list[dict[str, str]]
    markdown_body: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_markdown_note(self) -> str:
        _k_049 = [_dq('LS0t'), f'title: {json.dumps(self.title)}', f'source: {json.dumps(self.source_url)}', f'sha256: {json.dumps(self.content_hash)}', f'word_count: {self.word_count}', f'topics: {json.dumps(self.key_topics)}']
        for _k_061, _k_143 in self.metadata.items():
            _k_049.append(f'{_k_061}: {json.dumps(_k_143)}')
        _k_049.append(_dq('LS0t'))
        _k_114 = [_dq('Cg==').join(_k_049), f'\n# {self.title}\n']
        if self.summary:
            _k_114.append(f'## Key Summary & Takeaways\n\n{self.summary}\n')
        if self.key_topics:
            _k_138 = _dq('LCA=').join((f'`{_k_128}`' for _k_128 in self.key_topics))
            _k_114.append(f'**Key Concepts**: {_k_138}\n')
        _k_114.append(f'## Content\n\n{self.markdown_body}\n')
        if self.code_snippets:
            _k_114.append(_dq('IyMgRGlzY292ZXJlZCBDb2RlIFNuaXBwZXRzIEluZGV4Cg=='))
            for _k_057, _k_058 in enumerate(self.code_snippets, start=1):
                _k_063 = _k_058.get(_dq('bGFuZ3VhZ2U='), _dq('dGV4dA==')) or _dq('dGV4dA==')
                code = _k_058.get(_dq('Y29kZQ=='), '').strip()
                _k_114.append(f'### Snippet {_k_057} ({_k_063})\n```{_k_063}\n{code}\n```\n')
        return _dq('Cg==').join(_k_114)

    def to_jsonl_chunks(self, _k_020: int=400, _k_085: int=50) -> list[str]:
        _k_146 = self.markdown_body.split()
        _k_023 = []
        if not _k_146:
            _k_102 = {_dq('ZG9jX3RpdGxl'): self.title, _dq('c291cmNlX3VybA=='): self.source_url, _dq('Y2h1bmtfaW5kZXg='): 0, _dq('dG90YWxfY2h1bmtz'): 1, _dq('dG9waWNz'): self.key_topics, _dq('dGV4dA=='): f'# {self.title}\n\n{self.summary}'}
            return [json.dumps(_k_102)]
        _k_122 = max(1, _k_020 - _k_085)
        _k_019: list[str] = []
        for _k_055 in range(0, len(_k_146), _k_122):
            _k_022 = _k_146[_k_055:_k_055 + _k_020]
            _k_019.append(_dq('IA==').join(_k_022))
            if _k_055 + _k_020 >= len(_k_146):
                break
        _k_139 = len(_k_019)
        for _k_057, _k_021 in enumerate(_k_019):
            _k_102 = {_dq('ZG9jX3RpdGxl'): self.title, _dq('c291cmNlX3VybA=='): self.source_url, _dq('Y2h1bmtfaW5kZXg='): _k_057, _dq('dG90YWxfY2h1bmtz'): _k_139, _dq('dG9waWNz'): self.key_topics, _dq('dGV4dA=='): _k_021}
            _k_023.append(json.dumps(_k_102))
        return _k_023

class ContentTranslator:

    @staticmethod
    def extract_topics(_k_134: str, _k_136: int=8) -> list[str]:
        _k_027 = re.findall(_dq('YChbXmBcc1xuXXsyLDMwfSlg'), _k_134)
        _k_056 = re.findall(_dq('XGJbQS1aXVthLXpBLVowLTlfXC1cLl17Mix9XGJ8XGJbYS16XSsoPzpbQS1aXVthLXowLTldKykrXGJ8XGJbYS16MC05XSsoPzpfW2EtejAtOV0rKStcYg=='), _k_134)
        _k_146 = _k_027 + _k_056
        _k_123 = {_dq('VGhl'), _dq('VGhpcw=='), _dq('VGhhdA=='), _dq('VGhlc2U='), _dq('VGhvc2U='), _dq('VGhlcmU='), _dq('SGVyZQ=='), _dq('V2hlbg=='), _dq('V2hhdA=='), _dq('V2hlcmU='), _dq('V2hpY2g='), _dq('V2l0aA=='), _dq('RnJvbQ=='), _dq('SW50bw=='), _dq('QWJvdXQ='), _dq('QWZ0ZXI='), _dq('QmVmb3Jl'), _dq('VW5kZXI='), _dq('QWJvdmU='), _dq('UGFnZQ=='), _dq('U2VjdGlvbg=='), _dq('SW5kZXg='), _dq('T3ZlcnZpZXc='), _dq('RG9jdW1lbnRhdGlvbg=='), _dq('TWFudWFs'), _dq('R3VpZGU='), _dq('UmVmZXJlbmNl'), _dq('Q29weXJpZ2h0'), _dq('QWxs'), _dq('dHJ1ZQ=='), _dq('ZmFsc2U='), _dq('bm9uZQ=='), _dq('bnVsbA==')}
        _k_047 = [_k_145 for _k_145 in _k_146 if _k_145 not in _k_123 and len(_k_145) > 2]
        _k_031: dict[str, int] = {}
        for _k_145 in _k_047:
            _k_031[_k_145] = _k_031.get(_k_145, 0) + 1
        _k_120 = sorted(_k_031.items(), key=lambda _k_147: _k_147[1], reverse=True)
        return [_k_128[0] for _k_128 in _k_120[:_k_136]]

    @staticmethod
    def extract_summary(markdown_body: str, _k_075: int=3) -> str:
        _k_095 = re.sub(_dq('YGBgW1xzXFNdKj9gYGA='), '', markdown_body)
        _k_095 = re.sub(_dq('XiMrXHMrLiok'), '', _k_095, flags=re.MULTILINE)
        _k_095 = re.sub(_dq('XFsoW15cXV0rKVxdXChbXlwpXStcKQ=='), _dq('XDE='), _k_095)
        _k_095 = re.sub(_dq('W1wqXF9cYFw+XQ=='), '', _k_095)
        _k_091 = [_k_086.strip() for _k_086 in _k_095.split(_dq('Cgo=')) if _k_086.strip()]
        _k_028: list[str] = []
        for _k_090 in _k_091:
            _k_115 = re.split(_dq('KD88PVsuIT9dKVxzKw=='), _k_090)
            for _k_110 in _k_115:
                _k_111 = _k_110.strip()
                if len(_k_111) > 25:
                    _k_028.append(_k_111)
                if len(_k_028) >= _k_075:
                    break
            if len(_k_028) >= _k_075:
                break
        return _dq('IA==').join(_k_028) if _k_028 else _dq('Tm8gc3VtbWFyeSBhdmFpbGFibGUu')

    @staticmethod
    def extract_code_blocks(markdown_body: str) -> list[dict[str, str]]:
        _k_094 = re.compile(_dq('YGBgKFx3KilcbihbXHNcU10qPylgYGA='))
        _k_119 = []
        for _k_074 in _k_094.finditer(markdown_body):
            _k_063, code = _k_074.groups()
            if code.strip():
                _k_119.append({_dq('bGFuZ3VhZ2U='): _k_063.strip() or _dq('dGV4dA=='), _dq('Y29kZQ=='): code.strip()})
        return _k_119

    @classmethod
    def translate_html(cls, _k_054: str, source_url: str='', metadata: dict[str, Any] | None=None) -> _k_005:
        _k_093 = _k_007(base_url=source_url)
        _k_093.feed(_k_054)
        _k_093.close()
        markdown_body = _k_093.get_markdown()
        title = _k_093.doc_title or (metadata.get(_dq('dGl0bGU=')) if metadata else '') or _dq('VW50aXRsZWQgRG9jdW1lbnQ=')
        if title == _dq('VW50aXRsZWQgRG9jdW1lbnQ='):
            _k_050 = re.search(_dq('XiNccysoLispJA=='), markdown_body, re.MULTILINE)
            if _k_050:
                title = _k_050.group(1).strip()
        content_hash = hashlib.sha256(_k_054.encode(_dq('dXRmLTg='))).hexdigest()
        _k_146 = markdown_body.split()
        word_count = len(_k_146)
        summary = cls.extract_summary(markdown_body)
        _k_137 = cls.extract_topics(markdown_body)
        code_snippets = cls.extract_code_blocks(markdown_body)
        return _k_005(title=title, source_url=source_url, content_hash=content_hash, word_count=word_count, summary=summary, key_topics=_k_137, code_snippets=code_snippets, markdown_body=markdown_body, metadata=metadata or {})

    @classmethod
    def translate_plain_text(cls, _k_135: str, title: str=_dq('UGxhaW4gRG9jdW1lbnQ='), source_url: str='', metadata: dict[str, Any] | None=None) -> _k_005:
        content_hash = hashlib.sha256(_k_135.encode(_dq('dXRmLTg='))).hexdigest()
        _k_146 = _k_135.split()
        word_count = len(_k_146)
        summary = cls.extract_summary(_k_135)
        _k_137 = cls.extract_topics(_k_135)
        code_snippets = cls.extract_code_blocks(_k_135)
        return _k_005(title=title, source_url=source_url, content_hash=content_hash, word_count=word_count, summary=summary, key_topics=_k_137, code_snippets=code_snippets, markdown_body=_k_135, metadata=metadata or {})

def main() -> None:
    _k_093 = argparse.ArgumentParser(description=_dq('VHJhbnNsYXRlIG1lc3N5IEhUTUwgLyB3ZWIgZG9jdW1lbnRzIHRvIGNsZWFuLCBBSS1yZWFkeSBNYXJrZG93biBhbmQgSlNPTkwu'))
    _k_093.add_argument(_dq('LS1zcmM='), type=Path, required=True, help=_dq('U291cmNlIEhUTUwgb3IgdGV4dCBmaWxlLCBvciBkaXJlY3Rvcnk='))
    _k_093.add_argument(_dq('LS1kc3Q='), type=Path, default=Path(_dq('YWlfa25vd2xlZGdlX25vdGVz')), help=_dq('T3V0cHV0IGRpcmVjdG9yeSBmb3Igbm90ZXM='))
    _k_093.add_argument(_dq('LS1mb3JtYXQ='), choices=[_dq('bWFya2Rvd24='), _dq('anNvbmw='), _dq('Ym90aA==')], default=_dq('Ym90aA=='), help=_dq('T3V0cHV0IGZvcm1hdA=='))
    _k_093.add_argument(_dq('LS11cmw='), type=str, default='', help=_dq('T3JpZ2luYWwgc291cmNlIFVSTCBmb3IgYXR0cmlidXRpb24='))
    _k_014 = _k_093.parse_args()
    _k_037: Path = _k_014.dst
    _k_037.mkdir(parents=True, exist_ok=True)
    _k_121 = [_k_014.src] if _k_014.src.is_file() else list(_k_014.src.glob(_dq('KiovKi4q')))
    _k_140 = 0
    for _k_045 in _k_121:
        if _k_045.suffix.lower() not in (_dq('Lmh0bWw='), _dq('Lmh0bQ=='), _dq('LnR4dA=='), _dq('Lm1k'), _dq('Lmpzb24=')):
            continue
        _k_098 = _k_045.read_text(encoding=_dq('dXRmLTg='), errors=_dq('cmVwbGFjZQ=='))
        if _k_045.suffix.lower() in (_dq('Lmh0bWw='), _dq('Lmh0bQ==')):
            _k_062 = ContentTranslator.translate_html(_k_098, source_url=_k_014.url)
        else:
            _k_062 = ContentTranslator.translate_plain_text(_k_098, title=_k_045.stem.replace(_dq('Xw=='), _dq('IA==')).title(), source_url=_k_014.url)
        _k_112 = re.sub(_dq('W15cd1wtX1wuXQ=='), _dq('Xw=='), _k_062.title.lower())[:80] or _k_045.stem
        if _k_014.format in (_dq('bWFya2Rvd24='), _dq('Ym90aA==')):
            _k_076 = _k_037 / f'{_k_112}.md'
            _k_076.write_text(_k_062.to_markdown_note(), encoding=_dq('dXRmLTg='))
            print(f'[OK] Wrote Markdown note: {_k_076}')
        if _k_014.format in (_dq('anNvbmw='), _dq('Ym90aA==')):
            jsonl_path = _k_037 / f'{_k_112}.jsonl'
            _k_023 = _k_062.to_jsonl_chunks()
            jsonl_path.write_text(_dq('Cg==').join(_k_023) + _dq('Cg=='), encoding=_dq('dXRmLTg='))
            print(f'[OK] Wrote JSONL chunks: {jsonl_path} ({len(_k_023)} chunks)')
        _k_140 += 1
    print(f'\nSuccessfully translated {_k_140} document(s) to AI-ready knowledge.')
if __name__ == _dq('X19tYWluX18='):
    main()
