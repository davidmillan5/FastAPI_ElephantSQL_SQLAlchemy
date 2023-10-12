from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://apkcwbew:uhemiwXFl9iJDFSfSDU-X1TwjyiL6Y_M@mahmud.db.elephantsql.com/apkcwbew',
                       echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
