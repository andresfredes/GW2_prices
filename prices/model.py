from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, TEXT, VARCHAR, BOOLEAN, DATETIME
from prices import db

class Recipe(db.Model):
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


class Item(db.Model):
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


class Price_History(db.Model):
    __tablename__ = "price_history"
    id = Column("id", INTEGER, primary_key=True, nullable=False)
    item_id = Column("item_id", INTEGER, nullable=False)
    time = Column("time", DATETIME, nullable=False)
    price_buy = Column("price_buy", INTEGER, nullable=False)
    price_sell = Column("price_sell", INTEGER, nullable=False)


class Favourite(db.Model):
    __tablename__ = "faves"
    uid = Column(
        "uid", INTEGER, primary_key=True, nullable=False, autoincrement=True
    )
    is_item = Column("is_item", BOOLEAN, nullable=False)
    item_id = Column("item_id", INTEGER)
    recipe_id = Column("recipe_id", INTEGER)

