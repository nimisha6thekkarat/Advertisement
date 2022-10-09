from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, inputs

app = Flask(__name__)
api = Api(app)

advert_put_args = reqparse.RequestParser()
advert_put_args.add_argument("customer_id", type=int, help="12 digit ID for the Sky Customer the TV is registered to is required", required=True)
advert_put_args.add_argument("opt_in", type=inputs.boolean, help="indicating if the Customer has opted in to targeted advertising is required", required=True)
advert_put_args.add_argument("inactivity_timer", type=int, help="number of seconds since the Customer last used the remote is required", required=True)

advertisements = {}
advertisement_stats={}
def abort_if_add_id_doesnt_exist(advert_id):
    if advert_id not in advertisements:
        abort(404,message="could not found advertiment ID..")
        
    
class Advertising(Resource):
    def get(self, advert_id):
        abort_if_add_id_doesnt_exist(advert_id)
        return advertisements[advert_id]
    def put(self, advert_id):
        args = advert_put_args.parse_args()
        if not args['opt_in']:
            advertisement_stats[advert_id]=False
            return advertisement_stats[advert_id]
        if args['inactivity_timer'] > 2:
            advertisement_stats[advert_id]=False
            return advertisement_stats[advert_id]
        if args['customer_id']%7 == 0:
            advertisement_stats[advert_id]=False
            return advertisement_stats[advert_id]
        advertisements[advert_id] = args
        advertisement_stats[advert_id]=True
        return advertisement_stats[advert_id]
api.add_resource(Advertising, "/advertising/<int:advert_id>") 

if __name__ == '__main__':
    app.run(debug=True) # dont run debug=True in production env

