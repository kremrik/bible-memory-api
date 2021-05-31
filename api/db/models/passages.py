from enum import unique
from piccolo.table import Table
from piccolo.columns import UUID, Text


class Passages(Table):
    user_id = UUID()
    passage = Text(unique=True)
