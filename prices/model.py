from sqlalchemy import Column, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, TEXT, VARCHAR, BOOLEAN, DATETIME
from sqlalchemy.ext.declarative import declarative_base

# in-memory db used during development and testing. Final form will be:
# "mariadb+mariadbconnector://<username>:<password>@<host>:<port>/<dbname>"
engine = create_engine(
    "mariadb+mariadbconnector:///:memory:",
    echo=True,
    future=True
)
Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column("id", INTEGER, primary_key=True, nullable=False)
    output_qty = Column("output_qty", INTEGER, nullable=False)
    output_item = Column("output_item", INTEGER, nullable=False)
    ingredient_1_qty = Column("ingredient_1_qty", INTEGER, nullable=False)
    ingredient_1_item_id = Column(
        "ingredient_1_item_id", INTEGER, nullable=False
    )
    ingredient_2_qty = Column("ingredient_1_qty", INTEGER, nullable=False)
    ingredient_2_item_id = Column("ingredient_1_item_id", INTEGER)
    ingredient_3_qty = Column("ingredient_1_qty", INTEGER)
    ingredient_3_item_id = Column("ingredient_1_item_id", INTEGER)
    ingredient_4_qty = Column("ingredient_1_qty", INTEGER)
    ingredient_4_item_id = Column("ingredient_1_item_id", INTEGER)
    craft_artificer = Column(
        "craft_artificer", BOOLEAN, default=False, nullable=False
    )
    craft_armoursmith = Column(
        "craft_armoursmith", BOOLEAN, default=False, nullable=False
    )
    craft_chef = Column("craft_chef", BOOLEAN, default=False, nullable=False)
    craft_huntsman= Column(
        "craft_huntsman", BOOLEAN, default=False, nullable=False
    )
    craft_jeweler = Column(
        "craft_jeweler", BOOLEAN, default=False, nullable=False
    )
    craft_leatherworker = Column(
        "craft_leatherworker", BOOLEAN, default=False, nullable=False
    )
    craft_tailor = Column(
        "craft_tailor", BOOLEAN, default=False, nullable=False
    )
    craft_weaponsmith = Column(
        "craft_weaponsmith", BOOLEAN, default=False, nullable=False
    )
    craft_scribe = Column(
        "craft_scribe", BOOLEAN, default=False, nullable=False
    )

    ingredients = relationship("Item", back_populates="recipes")
    favourites = relationship("Favourite", back_populates="recipes")


class Item(Base):
    __tablename__ = "items"
    id = Column("id", INTEGER, primary_key=True, nullable=False)
    name = Column("name", VARCHAR, nullable=False)
    description = Column("description", TEXT)
    icon_url = Column("icon_url", TEXT)
    vendor_sellable = Column(
        "vendor_sellable", BOOLEAN, default=False, nullable=False
    )
    vendor_sell_price = Column("vendor_sell_price", INTEGER)
    vendor_sell_qty = Column("vendor_sell_qty", INTEGER)
    vendor_buyable = Column(
        "vendor_buyable", BOOLEAN, default=False, nullable=False
    )
    vendor_buy_price = Column("vendor_buy_price", INTEGER)
    karma_buyable = Column(
        "karma_buyable", BOOLEAN, default=False, nullable=False
    )
    karma_sell_price = Column("karma_sell_price", INTEGER)
    karma_sell_qty = Column("karma_sell_qty", INTEGER)
    bound = Column("bound", BOOLEAN, default=False, nullable=False)

    recipes = relationship("Recipe", back_populates="ingredients")
    price_histories = relationship("Price_History", back_populates="items")
    favourites = relationship("Favourite", back_populates="items")

class Price_History(Base):
    __tablename__ = "price_history"
    id = Column("id", INTEGER, primary_key=True, nullable=False)
    item_id = Column("item_id", INTEGER, nullable=False)
    time = Column("time", DATETIME, nullable=False)
    price_buy = Column("price_buy", INTEGER, nullable=False)
    price_sell = Column("price_sell", INTEGER, nullable=False)

    items = relationship("Item", back_populates="price_histories")

class Favourite(Base):
    __tablename__ = "faves"
    uid = Column(
        "uid", INTEGER, primary_key=True, nullable=False, autoincrement=True
    )
    is_item = Column("is_item", BOOLEAN, nullable=False)
    item_id = Column("item_id", INTEGER)
    recipe_id = Column("recipe_id", INTEGER)

    items = relationship("Item", back_populates="favourites")
    recipes = relationship("Recipe", back_populates="favourites")
    
