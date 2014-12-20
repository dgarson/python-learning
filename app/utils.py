from xml.etree import ElementTree
from app.database import db, engine
from app.models import Account
from sqlalchemy.orm import sessionmaker

__author__ = 'dgarson'

class UserFile(object):

    def __init__(self, filename):
        print("processing default user file", filename)
        self._tree = ElementTree.parse(filename)
        self.defaultUsers = []

    def process(self):
        assert self._tree

        root = self._tree.getroot()
        for user in root.iter("user"):
            email = user.get('email')
            print("processing default user", email)
            plainTextPassword = user.get("password")
            self._persistUser(email, plainTextPassword)

    def _persistUser(self, email, password):
        acct = Account()
        acct.email = email
        acct.password = password
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(acct)
        session.commit()
        print("persisted default user with email", email, " and id ", acct.id)

