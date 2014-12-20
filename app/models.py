from random import SystemRandom
from hmac import compare_digest
from crypt import METHOD_SHA512, mksalt, crypt
from sqlalchemy import Column, String, Integer, VARCHAR, Boolean, Table, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship, mapper
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
from app.database import Base, db, metadata, engine

randomizer = SystemRandom()

class Account(UserMixin, db.Model):
    # __table__ = Table('accounts', metadata, autoload=True)
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, nullable=False)
    # hashed (never unencrypted)
    _password = Column(LargeBinary(120))
    _salt = Column(String(120))
    key_maps = relationship("KeyMap")

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self._hash_password(value)

    def is_valid_password(self, password):
        new_hash = self._hash_password(password)
        return compare_digest(new_hash, self._password)

    def _hash_password(self, password):
        if self._salt is None:
            self._salt = mksalt(method = METHOD_SHA512)
        encrypted = crypt(password, self._salt)
        return bytes(encrypted, encoding="utf-8")

    def __repr__(self):
        return "<User #{:d}>".format(self.id)


class Key(db.Model):
    # __table__ = Table('key_type', metadata, autoload=True)
    __tablename__ = 'key_types'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(16), unique=True, nullable=True)
    modifier = Column(Boolean, default=False, nullable=False)
    special = Column(Boolean, default=False, nullable=False)

class KeyMap(db.Model):
    # __table__ = Table('key_maps', metadata, autoload=True)
    __tablename__ = 'key_maps'
    id = Column(Integer, primary_key=True)
    account = Column(Integer, ForeignKey('accounts.id'))
    name = Column(String(128), unique=False)
    bindings = relationship("KeyBinding")

class KeyBinding(db.Model):
    # __table__ = Table('key_bindings', metadata, autoload=True)
    __tablename__ = 'key_bindings'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('key_maps.id'))
    description = Column(String(128), unique=False)
    keys = relationship("Key", secondary=Table('association', metadata,
                                                Column('key_binding_id', Integer, ForeignKey('key_bindings.id')),
                                                Column('key_type_id', Integer, ForeignKey('key_types.id'))))
