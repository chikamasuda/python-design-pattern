a: int = 1
b: float
c: str
d: bool

e:list[int] = [1, 2]
f:dict[str, bool] = {"Flag: True"}

from typing import Literal
g: Literal["OK", "NG"] = "OK"

def sample(x: str) -> bool:
  return True