from backend.db.dao import DAO
from backend.db.entities import Suggestion, User
from sqlalchemy.orm import Session
from backend.db.dao import DAO
from sqlalchemy import select
from datetime import datetime

class UserDAO(DAO):
    def insert_user(self, email, name, password):
        with Session(self.engine) as session:
            user = User(email=email, name=name, password=password)
            session.add(user)
            session.commit()

    def delete_user(self, email):
        with Session(self.engine) as session:
            user = self.get_user(email)
            session.delete(user)
            session.commit()
    
    def get_user(self, email):
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            
            try:
                user = session.scalars(stmt).one()
                return user
            except:
                return None
        
    def alter_user(self, email, attribute, value):
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            user = session.scalars(stmt).one()
            match attribute:
                case "name":
                    user.name = value

                case "password":
                    user.password = value

            session.commit()
        
    def insert_suggestion(self, email, description):
        with Session(self.engine) as session:
            suggestion = Suggestion(description=description, timestamp=datetime.now(), user_email=email)
            user = self.get_user(email)
            user = session.merge(user)
            user.suggestions.append(suggestion)
            session.commit()

    def vote_suggestion(self, email, suggestionID):
        with Session(self.engine) as session:
            stmt = select(Suggestion).where(Suggestion.suggestionID == suggestionID)
            suggestion = session.scalars(stmt).one()
            user = self.get_user(email)
            user.suggestions_voted.append(suggestion)
            session.commit()

    def check_password(self, email, password):
        with Session(self.engine) as session:
            user = self.get_user(email)
            if user.password == password:
                return True
            else:
                return False
    def password_complexity(self, password):
        return True
