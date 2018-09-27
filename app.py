from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True


class DataBase:
    def __init__(self, database="Films"):
        self.client = MongoClient()
        self.db = self.client[database]

    def insert_user(self, email, password, user_name):
        if self.user_check(email=email)["status"]:
            return {"status": 0, "message": "User already exists."}
        else:
            table = self.db['users']
            table.insert_one({
                'email': email,
                'password': password,
                'user_name': user_name
            })
            return {"status": 1, "message": "User added successfully."}

    def user_check(self, email, password=None):
        table = self.db['users']
        account = table.find_one({
            'email': email
        })
        if account:
            email = account['email']
            passwd = account['password']
            if password == passwd:
                return {"status": 1, "name": account["user_name"], "message": "User logged in."}
            elif password != passwd and password is not None:
                return {"status": 0, "message": "Wrong password."}
            return {"status": 1, "email": email, "password": passwd}
        else:
            return {"status": 0, "message": "User not found"}

    def delete_user(self, email):
        table = self.db["users"]
        if self.user_check(email=email)["status"]:
            res = table.delete_one({"email": email})
            print(res)
            return {"status": 1, "message": "User removed successfully."}
        else:
            return {"status": 0, "message": "User not exists."}

    def insert_films(self, f_id, name, age, price_of_ticket, tickets):
        if self.film_check(f_id=f_id)["status"]:
            return {"status": 0, "message": "Film already exists."}
        else:
            table = self.db['movies']
            table.insert_one({
                '_id': f_id,
                'name': name,
                'age': age,
                'price_of_ticket': price_of_ticket,
                'tickets': tickets
            })
            return {"status": 1, "message": "Movie added successfully."}

    def film_check(self, f_id):
        table = self.db['movies']
        movie = table.find_one({
            '_id': f_id
        })
        if movie:
            _id = movie['_id']
            name = movie['name']
            return {"status": 1, "_id": _id, "name": name}
        else:
            return {"status": 0, "message": "Movie not found"}

    def show_all_movie(self):
        table = self.db['movies']
        list_of_movies = []
        for movie in table.find():
            list_of_movies.append(movie)
        return {"status": 1, "movies": list_of_movies}


@app.route('/')
def hello_world():
    return "this home page"


@app.route('/new/user', methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data['name']
    password = user_data['pass']
    email = user_data['email']
    user = db.insert_user(email=email, user_name=username, password=password)
    if user["status"]:
        return jsonify({"status": 1, "message": "User added successfully."})
    else:
        return jsonify({"status": 0, "message": user["message"]})


@app.route('/login', methods=["POST"])
def login():
    user_data = request.get_json()
    email = user_data['email']
    password = user_data['pass']
    data = db.user_check(email=email, password=password)
    return jsonify(data)


@app.route('/user/remove', methods=["POST"])
def delete_user():
    user_data = request.get_json()
    email = user_data["email"]
    res = db.delete_user(email=email)
    return jsonify(res)


@app.route('/authorize', methods=['POST'])
def authorize():
    return jsonify({"this_is": "json"})


if __name__ == '__main__':
    db = DataBase()
    app.run()
