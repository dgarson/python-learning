from random import SystemRandom
from hmac import new, compare_digest
from hashlib import pbkdf2_hmac
from sqlalchemy import Column, String, Integer, VARCHAR, Boolean, Table, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship, mapper
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
from app.database import Base

key_binding_keys_table = Table('association', Base.metadata,
                               Column('key_binding_id', Integer, ForeignKey('key_binding.id')),
                               Column('key_id', Integer, ForeignKey('key_type.id')))

class Account(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, nullable=False)
    # hashed (never unencrypted)
    _password = Column(LargeBinary(120))
    _salt = Column(String(120))
    key_maps = relationship("KeyMap", backref="account")

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self._salt is None:
            self._salt = bytes(SystemRandom().getrandbits(128))
        self._password = self._hash_password(value)

    def is_valid_password(self, password):
        new_hash = self._hash_password(password)
        return compare_digest(new_hash, self._password)

    def _hash_password(self, password):
        pwd = password.encode("utf-8")
        salt = bytes(self._salt)
        buff = pbkdf2_hmac("sha512", pwd, salt, iterations=100000)
        return bytes(buff)

    def __repr__(self):
        return "<User #{:d}>".format(self.id)


class KeyMap(Base):
    __tablename__ = 'key_map'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('account.id'))
    name = Column(String(128), unique=False)
    bindings = relationship("KeyBinding", backref="key_map")

class KeyBinding(Base):
    __tablename__ = 'key_binding'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('key_map.id'))
    description = Column(String(128), unique=False)
    keys = relationship("Key", secondary=key_binding_keys_table)

class Key(Base):
    __tablename__ = 'key_type'
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(16), unique=True, nullable=True)
    modifier = Column(Boolean, default=False, nullable=False)
    special = Column(Boolean, default=False, nullable=False)

