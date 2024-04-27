from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

# from app.configs.config import dbSettings
# from app.models.auth import Base, User

SQLALCHEMY_DATABASE_URL = URL.create(
  f"postgresql",
    # username=dbSettings.CLINIC_APPOINTMENT_SYSTEM_DB_USER,
    # password=dbSettings.CLINIC_APPOINTMENT_SYSTEM_DB_PASSWORD,
    # host=dbSettings.POSTGRES_HOSTNAME,
    # database=dbSettings.CLINIC_APPOINTMENT_SYSTEM_DB_NAME
    username="backend",
    password="backend",
    host="127.0.0.1",
    database="clinic_appointment_system"
    )

Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args = {"client_encoding": "utf8"},
)

Session = sessionmaker(bind=Engine)
session = Session()

# test_command = text("CREATE TABLE IF NOT EXISTS testtttt (id SERIAL, PRIMARY KEY (id))")
test_command = text("SELECT * FROM patients")
result = session.execute(test_command)
print(result)
for item in result:
    print(item)
session.commit()

def get_conn():
    
    db = session
    
    try:
        yield db
    
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()