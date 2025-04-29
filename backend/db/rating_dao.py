from sqlalchemy.orm import Session
from backend.db.dao import DAO
from sqlalchemy import select
from sqlalchemy import text
from datetime import datetime

from backend.db.entities import Rating

class RatingDAO(DAO):
    def insert_rating(self, user_email, stars, comment, dish_id):
        with Session(self.engine) as session:
            rating = Rating(timestamp = datetime.now, user_email = user_email, stars = stars, comment = comment, dish_id = dish_id)
            session.add(rating)
            session.commit()


    def delete_rating(self, dish_id, user_email, timestamp):
        with Session(self.engine) as session:
            rating = self.get_rating(dish_id, user_email, timestamp)
            session.delete(rating)
            session.commit()

    def get_rating(self, dish_id, user_email, timestamp):
        with Session(self.engine) as session:
            stmt = select(Rating).where(Rating.dish_id == dish_id and Rating.user_email == user_email and Rating.timestamp == timestamp)
            rating = session.scalars(stmt).one()

            return rating
        
    def alter_rating(self, dish_id, user_email, timestamp, attribute, value):
        with Session(self.engine) as session:
            rating = self.get_rating(dish_id, user_email, timestamp)
            match attribute:
                case "stars":
                    rating.stars = value
                    timestamp = datetime.now

                case "comment":
                    rating.comment = value
                    timestamp = datetime.now
        
          session.commit()

