from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


DATABASE_URL = "postgresql://postgres:goit@localhost:5432/postgres"

# Створення з'єднання з базою даних
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Виконання запиту
# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print(result.fetchone())  # Це виведе (1,)
# except Exception as e:
#     print("Error connecting to database:", e)
