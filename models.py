from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, engine


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    submenu = relationship("Submenu", back_populates="menu")


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    menu_id = Column(Integer, ForeignKey("menus.id"))
    menu = relationship("Menu", back_populates="submenu")
    dish = relationship("Dish", back_populates="submenu")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

    submenu_id = Column(Integer, ForeignKey("submenus.id"))
    submenu = relationship("Submenu", back_populates="dish")


