from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Todo(Base):
    __tablename__ = 'todos'

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(comment="Title of the Todo", nullable=False)
    description:Mapped[str] = mapped_column(comment="Detailed description of the ", nullable=True)

