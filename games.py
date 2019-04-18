from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Game, Base, Mcq

engine = create_engine('sqlite:///Games.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()



game1 = Game(id=1, name="mcq11",category="MCQ")
session.add(game1)
session.commit()

game2 = Game(id=2, name="mcq12",category="MCQ")
session.add(game2)
session.commit()


game1questions1=Mcq(id=1,game_id=1,question_body="ASD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game1questions1)
session.commit()
game1questions2=Mcq(id=2,game_id=1,question_body="BAD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game1questions2)
session.commit()
game1questions3=Mcq(id=3,game_id=1,question_body="CSD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game1questions3)
session.commit()



game2questions1=Mcq(id=4,game_id=2,question_body="ASD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game2questions1)
session.commit()
game2questions2=Mcq(id=5,game_id=2,question_body="BAD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game2questions2)
session.commit()
game2questions3=Mcq(id=6,game_id=3,question_body="CSD",Answer1="2",Answer2="2",Answer3="1",AnswerTrue="1")
session.add(game2questions3)
session.commit()

print("Added order")




print("Added order")