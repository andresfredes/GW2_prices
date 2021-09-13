from prices import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, TEXT, DATETIME

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    name = db.Column(VARCHAR(256), nullable=False)
    description = db.Column(TEXT)
    icon_url = db.Column(TEXT)
    coin_sell_to_vendor = db.Column(BOOLEAN, nullable=False, default=False)
    coin_price_to_vendor = db.Column(INTEGER)
    coin_buy_from_vendor = db.Column(BOOLEAN, nullable=False, default=False)
    coin_price_from_vendor = db.Column(INTEGER)
    coin_qty_from_vendor = db.Column(INTEGER)
    karma_buy_from_vendor = db.Column(BOOLEAN, nullable=False, default=False)
    karma_price_from_vendor = db.Column(INTEGER)
    karma_qty_from_vendor = db.Column(INTEGER)
    bound = db.Column(BOOLEAN, nullable=False, default=False)
    
    def __repr__(self):
        return f"<Item({self.id}, {self.name})>"

    def __str__(self):
        return f"<Item: id={self.id}, name={self.name}>"


class Favourite(db.Model):
    __tablename__ = 'faves'
    uid = db.Column(INTEGER, primary_key=True, nullable=False)
    is_item = db.Column(BOOLEAN, nullable=False)
    item_id = db.Column(INTEGER)
    recipe_id = db.Column(INTEGER)

    def get_type_typeid(self):
        if self.is_item:
            return "item", self.item_id
        else:
            return "recipe", self.recipe_id

    def __repr__(self):
        type, id = self.get_type_typeid()
        return f"<Favourite({self.uid}, {type}, {id})>"

    def __str__(self):
        type, id = self.get_type_typeid()
        return f"<Favourite: uid={self.uid}, {type}={id}>"


class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    output_qty = db.Column(INTEGER, nullable=False)
    output_item_id = db.Column(INTEGER, nullable=False)
    ingredient_1_qty = db.Column(INTEGER, nullable=False)
    ingredient_1_item_id = db.Column(INTEGER, nullable=False)
    ingredient_2_qty = db.Column(INTEGER, nullable=False)
    ingredient_2_item_id = db.Column(INTEGER, nullable=False)
    ingredient_3_qty = db.Column(INTEGER, nullable=False)
    ingredient_3_item_id = db.Column(INTEGER, nullable=False)
    ingredient_4_qty = db.Column(INTEGER, nullable=False)
    ingredient_4_item_id = db.Column(INTEGER, nullable=False)
    craft_artificer = db.Column(BOOLEAN, nullable=False, default=False)
    craft_armorsmith = db.Column(BOOLEAN, nullable=False, default=False)
    craft_chef = db.Column(BOOLEAN, nullable=False, default=False)
    craft_huntsman = db.Column(BOOLEAN, nullable=False, default=False)
    craft_jeweler = db.Column(BOOLEAN, nullable=False, default=False)
    craft_leatherworker = db.Column(BOOLEAN, nullable=False, default=False)
    craft_tailor = db.Column(BOOLEAN, nullable=False, default=False)
    craft_weaponsmith = db.Column(BOOLEAN, nullable=False, default=False)
    craft_scribe = db.Column(BOOLEAN, nullable=False, default=False)

    def __repr__(self):
        return f"<Recipe({self.id})>"

    def __str__(self):
        return f"<Recipe: id={self.id}>"


class Price_History(db.Model):
    __tablename__ = 'price_history'
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    item_id = db.Column(INTEGER, nullable=False)
    time = db.Column(DATETIME, nullable=False)
    price_buy = db.Column(INTEGER, nullable=False)
    price_sell = db.Column(INTEGER, nullable=False)

    def __repr__(self):
        return f"<Price_History({self.id})>"

    def __str__(self):
        return f"<Price_History: id={self.id}>"