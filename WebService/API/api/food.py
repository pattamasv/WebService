from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json

f = open('food_db.json')
data_food = json.load(f)


class FoodList(Resource):
    def get(self):
        return jsonify({'data_food':data_food})

class FoodsApi(Resource):
    def get(self)-> Response:
        if 'Food' in request.args:
            Food = request.args.get('Food')
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            for i in obj:
                if i['Food'] == Food:
                    res = i
                    break
            res = jsonify(res)
            res.status_code = 200
            return res
        else:
            return Response(status=204)

    @jwt_required()
    def post(self)->Response:
        body = request.get_json()
        print(body)
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        for i in obj:
            data.append(i)
        
        if len(body) > 0:
            data.append(body)

        with open('food_db.json','w') as outfile:
            json.dump(data, outfile)
            response = jsonify(data)
            response.status_code = 200
            return response
    
    @jwt_required()
    def put(self)->Response:
        body = request.get_json()
        key = body['key']
        read = readJsonFile()
        obj = json.loads(read)
        isSucess = False
        data = list()
        for i in obj:
            data.append(i)
            if i['Food'] == key:
                data.remove(i)
                isSucess = True

        del body['key']
        data.append(body)

        if isSucess is True:
            with open('food_db.json','w') as outfile:
                json.dump(data, outfile)
                response = jsonify(data)
                response.status_code = 200
                return response
        else:
            return Response(status=204)
    

class FoodApi(Resource):
    @jwt_required()
    def delete(self,Food: str)->Response:
        key = Food
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        isSucess = False
        for i in obj:
            data.append(i)
            if i['Food'] == key:
                data.remove(i)
                isSucess = True

        with open('food_db.json','w') as outfile:
            json.dump(data, outfile)

        if isSucess is True:
            response = jsonify(data)
            response.status_code = 200;
            return response
        else:
            return Response(status=204)

class TDEEAPI(Resource):
    def get(self)-> Response:
        gender = request.args.get('gender')
        height = float(request.args.get('height'))
        weight = float(request.args.get('weight'))
        age = int(request.args.get('age'))
        activity = request.args.get('activity')
    
        if gender.upper() == 'M':
            bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
        elif gender.upper() == 'F':
            bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            return Response(status_code=204)
        
        bmr = round(bmr)

        if activity.upper() == 'S':
            tdee = bmr * 1.2
        elif activity.upper() == 'L':
            tdee = bmr * 1.375
        elif activity.upper() == 'M':
             tdee = bmr * 1.55
        elif activity.upper() == 'H':
             tdee = bmr * 1.728
        elif activity.upper() == 'A':
             tdee = bmr * 1.9
        else:
            return Response(status_code=204)

        tdee = round(tdee)
        data = {'BMR':bmr,
                'TDEE':tdee}
        res = jsonify(data)
        res.status_code = 200
        return res
    


def readJsonFile():
    with open('food_db.json','r',encoding="utf8") as food:
            data = food.read()
    return data


