from datetime import datetime
import config.db as _database
import sqlalchemy as _sql


class User(_database.Base):
    __tablename__ = 'users'
    id = _sql.Column(_sql.Integer(), primary_key=True)
    first_name = _sql.Column(_sql.String(25), nullable=False)
    last_name = _sql.Column(_sql.String(25), nullable=False)
    username = _sql.Column(_sql.String(25), unique=True, nullable=False)
    email = _sql.Column(_sql.String(80), unique=True, nullable=False)
    password = _sql.Column(_sql.String(100), nullable=False)
    is_active = _sql.Column(_sql.BOOLEAN, default=False)
    date_created = _sql.Column(_sql.DateTime(), default=datetime.utcnow)
    date_modified = _sql.Column(_sql.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'<User username={self.username} email={self.email}>'
