from .extensions import db
from datetime import datetime, timezone, timedelta
import string
from random import choices

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024), nullable=False)
    short_url = db.Column(db.String(20), nullable=False,unique=True)
    views = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    expiration_days = db.Column(db.Integer, default=30)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

         # If no custom id is provided, generate one
        if not self.short_url:
            self.short_url = self.generate_short_link()


    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.generate_short_link()
    
        return short_url
    
    def is_expired(self):
        if not self.date_created or self.expiration_days:
            return False
        return datetime.utcnow() > self.date_created + timedelta(days=self.expiration_days)
