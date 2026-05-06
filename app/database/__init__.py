from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


def _getDBFilePath()->str:
    from pathlib import Path
    current_dir = Path(__file__).parent
    instance_dir = current_dir.parent.parent / "instance"
    db_path = instance_dir / "todo.db"
    instance_dir.mkdir(parents=True, exist_ok=True)
    return f'sqlite:///{db_path.absolute()}'


SQLALCHEMY_DATABASE_URL = _getDBFilePath()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create a base Derclarative Class to inherit the models
class Base(DeclarativeBase):
    pass


