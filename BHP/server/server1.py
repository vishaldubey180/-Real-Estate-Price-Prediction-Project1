from flask import Flask, request, jsonify
app = Flask(__name__)
import  util

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()
                        })
    response.headers.add('Access-control-allow-origin', '*')
    return response


if __name__ == '__main__':
    print("starting python flask server for home price prediction")
    app.run()