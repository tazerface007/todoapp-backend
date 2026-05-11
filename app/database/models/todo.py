from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    is_archived: Mapped[bool] = mapped_column(default=False)
    # Automatically sets the time when a row is created
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
