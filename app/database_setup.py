from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy import create_engine

Base = declarative_base()


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name=Column(String(250))
    category = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,


        }


class Mcq(Base):
    __tablename__ = 'mcq'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)
    question_body = Column(String(250))
    Answer1=Column(String(250))
    Answer2=Column(String(250))
    Answer3=Column(String(250))
    AnswerTrue=Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'game_id': self.game_id,
            'question_body': self.question_body,
            'Answer1': self.Answer1,
            'Answer2': self.Answer2,
            'Answer3': self.Answer3,
            'AnswerTrue': self.AnswerTrue



        }


engine = create_engine('sqlite:///Games.db')


Base.metadata.create_all(engine)
