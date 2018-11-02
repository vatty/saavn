from flask import request
from flask_restful import abort, Resource
from database import db_handler as db


class GetAllItems(Resource):
    

class TotalUids(Resource):
    def __init__():
        self.type = 'uids'
		
	def post(self):
        try: 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetTotalUids',(_userId,))
            data = cursor.fetchall()

            item=data[0]
            
            return {'StatusCode':'200','Items':item}

        except Exception as e:
            return {'error': str(e)}

	

class TotalUniqueUids(Resource):
    def __init__():
        self.type = 'uniqueuids'

    def post(self):
        try: 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetUniqueTotalUids',(_userId,))
            data = cursor.fetchall()

            item=data[0]
            
            return {'StatusCode':'200','Items':item}

        except Exception as e:
            return {'error': str(e)}


class TotalStreams(Resource):
    def __init__():
        self.type = 'streams'

    def post(self):
        try: 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetTotalStreams',(_userId,))
            data = cursor.fetchall()

            item=data[0]
            
            return {'StatusCode':'200','Items':item}

        except Exception as e:
            return {'error': str(e)}


class AverageStreams(Resource):
    def __init__():
        self.type = 'averagestreams'

    def post(self):
        try: 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetAvgStreamsPerUser',(_userId,))
            data = cursor.fetchall()

            item=data[0]
            
            return {'StatusCode':'200','Items':item}

        except Exception as e:
            return {'error': str(e)}

