"""

Pydantic models

"""

# Importing packes and modules
from pydantic import BaseModel
from typing import List

# Input model
class Input(BaseModel):
    dataset_id: int
    channel: str
    slice_start: int
    slice_end: int