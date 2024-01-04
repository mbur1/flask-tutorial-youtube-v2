from sqlalchemy import create_engine, text

db_connectionstring = "mysql+pymysql://cs-306092_primaryuser:Verhuxyz667?@localhost:3306/cs-306092_scammerscanner"

engine = create_engine(db_connectionstring, echo=True)

with engine.connect() as conn:
  result = conn.execute(text("select * from artikel_posts"))
