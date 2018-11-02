
DBName = "saaavn"
db_connection = mysql.connect()
db_handler = MySQLDBHandler(DBName) 

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'vatsal'
app.config['MYSQL_DATABASE_PASSWORD'] = 'vatsal123'
app.config['MYSQL_DATABASE_DB'] = 'saavn'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


class MySQLDBHandler():
        def __init__(self,db_name):
                self.db = db_name

        def check_if_exists(self,type,id):
                # Find a way to not make this call, 2 db calls too much


        def create(self, type, obj):
                check_if_exists()
                pass

        def read(self, type, obj_id, filter):
                check_if_exists()
                pass

        def update(self, type, obj_id, obj):
                check_if_exists()
                pass

        def delete(self, type, obj_id):
                check_if_exists()
                pass

