import datetime

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import UserExtensionMixin
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class UserExtended(Model, UserExtensionMixin):
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=True)
    contact_group = relationship("ContactGroup")


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)


class Queue(Model):
    id = Column(Integer, primary_key=True)
    ip = Column(String(80), unique=True, nullable=False, primary_key=False)
    identity = Column(String(80), unique=False, nullable=True, primary_key=False)
    time = Column(String(80), unique=False, nullable=True, primary_key=False)

    def __repr__(self):
        return self.name


class Production(Model):
    id = Column(Integer, primary_key=True)
    ip = Column(String(80), unique=True, nullable=False, primary_key=False)
    identity = Column(String(80), unique=False, nullable=True, primary_key=False)
    time = Column(String(80), unique=False, nullable=True, primary_key=False)

    def __repr__(self):
        return self.name