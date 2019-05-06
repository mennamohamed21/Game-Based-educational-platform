from flask import Flask, request
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, Game, Mcq

app = Flask(__name__)

# DB Connection
engine = create_engine('sqlite:///Games.db')
Base.metadata.bind = engine


# Select all games
@app.route('/games/')
def games():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    games = session.query(Game).all()
    return jsonify(game=[r.serialize for r in games])


# Add new game
@app.route('/game/new', methods=['POST'])
def addgame():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    data = request.get_json()
    game = Game(
        name=data['name'],
        category=data['category'])
    session.add(game)
    session.commit()
    return jsonify({'message': 'new game Added'})


# sleect questons of mcq game
@app.route('/game/<int:id>/mcq', methods=['GET'])
def Mcqestions(id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    game = session.query(Game).filter_by(id=id).all()
    if not game:
        return jsonify({'message': 'nNo '})
    mcq = session.query(Mcq).filter_by(
        game_id=id).all()
    return jsonify(questions=[r.serialize for r in mcq])


# edit question
@app.route('/game/<int:game_id>/mcq/<int:que_id>/edit', methods=['PUT'])
def editquestion(game_id, que_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    data = request.get_json()
    editedquestion = session.query(Mcq).filter_by(id=que_id).one()
    editedquestion.question_body = data['question_body']
    editedquestion.Answer1 = data['Answer1']
    editedquestion.Answer2 = data['Answer2']
    editedquestion.Answer3 = data['Answer3']
    editedquestion.AnswerTrue = data['AnswerTrue']

    session.commit()
    return jsonify({'message': 'question promoted'})


# delete question if you are authorized
@app.route('/game/<int:game_id>/mcq/<int:que_id>/delete', methods=['DELETE'])
def delete_qustion(game_id, que_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    questionTodelete = session.query(Mcq).filter_by(id=que_id).one()

    session.delete(questionTodelete)
    session.commit()
    return jsonify({'message': 'question deleted '})


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
