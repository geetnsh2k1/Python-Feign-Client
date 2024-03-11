from dataclasses import dataclass
from typing import Optional


@dataclass
class Post:
    id: int
    userId: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None


@dataclass
class Posts:
    posts: list[Post]
