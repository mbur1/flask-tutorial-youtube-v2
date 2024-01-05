from sqlalchemy import create_engine, text
import os

db_connectionstring = os.environ['DB_CONNECTION']

engine = create_engine(db_connectionstring, echo=True)



def load_artikel_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from artikel_posts"))
    print(engine, "Hergestellt")
    artikel = []
    for row in result.all():
      artikel.append(row)
    return artikel

'''
def load_singleart_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from artikel_posts where id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
      '''