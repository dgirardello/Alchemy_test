from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/search')
def api_search():
    response = {
            "data": [
                {
                    "id": 1,
                    "name": "ISS Executor",
                    "status": "Operational"
                },
                {
                    "id": 2,
                    "name": "Devastator",
                    "status": "Operational"
                },
                {
                    "id": 3,
                    "name": "Indomitable",
                    "status": "Operational"
                },
                {
                    "id": 4,
                    "name": "Valiant",
                    "status": "Operational"
                },
                {
                    "id": 5,
                    "name": "NCC-1701 Enterprise",
                    "status": "Destroyed"
                },
                {
                    "id": 6,
                    "name": "USS Discovery",
                    "status": "Unknown"
                },
                {
                    "id": 7,
                    "name": "42",
                    "status": "Operational"
                },
                {
                    "id": 8,
                    "name": "Asimov",
                    "status": "Operational"
                }
        ]
    }
    return jsonify(response)


@app.route('/get_ship')
def api_get_ship():
    args = request.args
    print(args)
    if len(args) < 1:
        return jsonify({'message': 'Imperal Server Error, Palpatine Destroyed'}), 500
    elif args['id'] == '1':
        response = {
            "id": 1,
            "name": "Devastator",
            "class": "Star Destroyer",
            "crew": 35000,
            "image": "https:\\url.to.image",
            "value": 1999.99,
            "status": "operational",
            "armament": [
                {
                    "title": "Turbo Laser",
                    "qty": "60"
                },
                {
                    "title": "Ion Cannons",
                    "qty": "60",
                },
                {
                    "title": "Tractor Beam",
                    "qty": "10",
                },
            ]
        }
        return jsonify(response)
    else:
        return jsonify({"message": "Not Found, This is not the ship you are looking for"}), 404

