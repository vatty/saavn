from flask import Flask
from flask_restful import Api
import api_views as views
from flask.ext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

# URLs
api.add_resource(views.TotalUids, '/uids')
api.add_resource(views.TotalUniqueUids, '/uniqueuids')
api.add_resource(views.TotalStreams, '/streams')
api.add_resource(views.AverageStreams, '/averagestreams')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8000")
    
