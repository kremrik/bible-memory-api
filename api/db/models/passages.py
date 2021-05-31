from piccolo.table import Table
from piccolo.columns import UUID, Varchar


class Passages(Table):
    user_id = Varchar(36)
    passage = UUID()
