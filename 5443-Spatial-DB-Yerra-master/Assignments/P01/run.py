from flask import Flask
from flask_cors import CORS, cross_origin
import psycopg2

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def homepage():
    return 'Hl '


@app.route("/findAll")
@cross_origin()
def fetch_all():
    cursor.execute("select * from public.city_codes")
    result = cursor.fetchall()
    return result


@app.route('/findOne/<code>')
@cross_origin()
def get_state(code):
    cursor.execute('''SELECT * FROM public.city_codes WHERE zip_code = ''' + code + '')
    data = cursor.fetchall()
    return data


@app.route('/findClosest/<latitude>/<longitude>')
@cross_origin()
def find_closest(latitude, longitude):
    latitude = str(latitude);
    longitude = str(longitude);

    cursor.execute('SELECT  *, SQRT(POW((69.1 * (public.city_codes.latitude - '+latitude+')) , 2 ) + POW((53 * (public.city_codes.longitude - '+ longitude +')), 2)) AS distance FROM public.city_codes ORDER BY distance ASC LIMIT 1')
    data = cursor.fetchall()
    return data


conn = psycopg2.connect(database="Project1", user='postgres', password='1211')
cursor = conn.cursor()

if __name__ == '__main__':
    app.run(debug=True, port='8089')
