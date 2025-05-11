from .extensions import db
from datetime import datetime, timezone, timedelta
import string
from random import choices

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024))
    short_url = db.Column(db.String(6), unique=True)
    views = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    expiration_days = db.Column(db.Integer, default=30)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
