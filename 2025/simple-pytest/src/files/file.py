import re
from dataclasses import dataclass, field

from src.languages import Languages
from src.srt.srt_part import SRTPart


@dataclass
class File:
    name: str
    language: Languages
    source_path: str = ""
    target_path: str = ""
    contents: str = ""
    translated_content: str = ""
    SRTParts: list[SRTPart] = field(default_factory=list[SRTPart])
    breakpoints: list[int] = field(default_factory=list[int])

    @property
    def number_of_tokens(self) -> int:
        words = re.findall(r"\w+|[^\w\s]", self.contents, re.UNICODE)
        return len(words) + self.contents.count(" ")
