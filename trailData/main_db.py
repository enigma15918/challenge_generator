from sqlalchemy import Column,Integer,String,create_engine,Sequence,ForeignKey

from sqlalchemy.orm import sessionmaker,declarative_base,relationship

engine=create_engine("sqlite:///cwd.db")

Session=sessionmaker(bind=engine)

session=Session()

Base=declarative_base()


class User(Base):

    __tablename__ = "users"

    id=Column(Integer,Sequence("user_id_seq"),primary_key=True)

    name=Column(String(50))

    email=Column(String(50))

Base.metadata.create_all(engine)

user1=User(name="Salem",email="salem@gmail.com")

user2=User(name="jana",email="jana@gmail.com")


# session.add_all([user1,user2])

# session.commit()


user= session.query(User).filter_by(name="Salem").first()

# print(user)

session.delete(user)
session.commit()