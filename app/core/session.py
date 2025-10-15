from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

from app.core.base import Base

load_dotenv()
# database_file = os.getenv("DATABASE_FILE")
database_url = os.getenv("DATABASE_URL")

# engine = create_engine("sqlite:///" + database_file, echo=False)
engine = create_engine(
    database_url,
    echo=False,
    pool_pre_ping=True,      # ★これが最重要
    pool_recycle=3600,       # 1時間でリサイクル
    pool_size=5,
    max_overflow=10,
    connect_args={
        "connect_timeout": 60
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
