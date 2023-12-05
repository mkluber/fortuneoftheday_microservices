import boto3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

application = Flask(__name__)
api = Api(application)
CORS(application, origins=["https://static.outworldindustries.com"])

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('Fortunes')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ScanFortune(Resource):
    def get(self):
        response = table.scan()
        items = response['Items']
        print(items)
        return jsonify(items)

class ReadFortune(Resource):
    def get(self):
        fortune_key = request.args.get('readfortune')
        origin_key = request.args.get('readorigin')
        response = table.get_item(
            Key={
                'FortuneName': fortune_key,
                'FortuneOrigin': origin_key
            }
        )
        item = response['Item']
        return jsonify(item)

class AddFortune(Resource):
    def post(self):
        fortune = request.form['addfortune']
        origin = request.form['addorigin']
        table.put_item(
            Item={
            'FortuneName': fortune,
            'FortuneOrigin': origin
            }
        )

class UpdateFortune(Resource):
    def post(self):
        fortune_key = request.form['updatefortune']
        origin_key = request.form['updateorigin']
        author = request.form['updateattribute1']
        color = request.form['updateattribute2']
        response = table.update_item(
            Key={
                'FortuneName': fortune_key,
                'FortuneOrigin': origin_key
            },
            AttributeUpdates={
                'FortuneAuthor': {
                    'Value'  : author,
                    'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
                },
                'FortuneColor': {
                    'Value'  : color,
                    'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
                }
            }
        )

class DeleteFortune(Resource):
    def post(self):
        fortune_key = request.form['deletefortune']
        origin_key = request.form['deleteorigin']
        response = table.delete_item(
            Key={
                'FortuneName': fortune_key,
                'FortuneOrigin': origin_key
            }
        )

api.add_resource(HelloWorld, '/')
api.add_resource(ScanFortune, '/scanfortune')
api.add_resource(ReadFortune, '/readfortune')
api.add_resource(AddFortune, '/addfortune')
api.add_resource(UpdateFortune, '/updatefortune')
api.add_resource(DeleteFortune, '/deletefortune')

if __name__ == '__main__':
    application.run(debug=True)


# @application.route('/')
# def index():
#     return render_template('index.html')


# @application.route("/addfortune/", methods=['POST'])
# def addfortune():
#     fortune = request.form['addfortune']
#     origin = request.form['addorigin']
#     table.put_item(
#         Item={
#         'FortuneName': fortune,
#         'FortuneOrigin': origin
#         }
#     )
#     return render_template('index.html')


# @application.route("/scanfortune/", methods=['GET'])
# def scanfortune():
#     response = table.scan()
#     items = response['Items']
#     print(items)
#     return render_template('index.html', fortunes=items)

# @application.route("/readfortune/", methods=['GET', 'POST'])
# def readfortune():
#     fortune_key = request.form['readfortune']
#     origin_key = request.form['readorigin']
#     response = table.get_item(
#         Key={
#             'FortuneName': fortune_key,
#             'FortuneOrigin': origin_key
#         }
#     )
#     item = response['Item']
#     print(item)
#     return render_template('index.html', fortune=item)




# @application.route("/updatefortune/", methods=['GET', 'POST'])
# def updatefortune():
#     fortune_key = request.form['updatefortune']
#     origin_key = request.form['updateorigin']
#     author = request.form['updateattribute1']
#     color = request.form['updateattribute2']
#     response = table.update_item(
#         Key={
#             'FortuneName': fortune_key,
#             'FortuneOrigin': origin_key
#         },
#         AttributeUpdates={
#             'FortuneAuthor': {
#                 'Value'  : author,
#                 'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
#             },
#             'FortuneColor': {
#                 'Value'  : color,
#                 'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
#             }
#         }
#     )
#     return render_template('index.html')


# @application.route("/deletefortune/", methods=['GET', 'POST'])
# def deletefortune():
#     fortune_key = request.form['deletefortune']
#     origin_key = request.form['deleteorigin']
#     response = table.delete_item(
#         Key={
#             'FortuneName': fortune_key,
#             'FortuneOrigin': origin_key
#         }
#     )
#     return render_template('index.html')

# if __name__ == "__main__":
#         application.run()

