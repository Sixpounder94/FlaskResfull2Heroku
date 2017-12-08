from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel



class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank"
                        )


    @jwt_required()
    def get(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            return  item.json()

        return {'message':'item do not exists'},404


    def post(self,name):
        if ItemModel.find_by_name(name):
             return {'message':"An item with name'{}'already exists".format(name)}, 400

        data = Item.parser.parse_args()
        print(data)
        item = ItemModel(name,**data)

        try:
            ItemModel.save_to_db(item)
        except:
            return {'message': 'An error occured'},500

        return {'message': 'item created'}, 201


    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item :
             item.delete_from_db()
        return {'message':'Item deleted!11'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):

        itm = ItemModel.query.all()

        print(itm)
        return {'items': [item.json() for item in itm]}

