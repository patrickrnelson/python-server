from flask import Flask, jsonify
from flask import render_template
import connexion
import psycopg2

app = Flask(__name__)

# Connect to your postgres DB
conn = psycopg2.connect(
  # Change this info to fit your DB
  """
  dbname=python-db
  host=localhost
  user=patricknelson
  port=5432
  """
) 

# Open a cursor to perform database operations
cur = conn.cursor()

### Static Data for local requests
# consoles = [{
#   'name': 'Xbox Series X',
#   'id': 0,
#   'description': "The Xbox Series X has higher end hardware, and supports higher display resolutions - up to 8K resolution - " 
#                   "along with higher frame rates and real-time ray tracing; it also has a high-speed solid-state drive to reduce loading times.",
#   'price': "$500 USD"
# },
# {
#   'name': 'Xbox Series S',
#   'id': 1,
#   'description': "The less expensive Xbox Series S uses the same CPU, but has a less powerful GPU, has less memory and internal storage, " 
#                   "and lacks an optical drive.",
#   'price': "$300 USD"
# },
# {
#   'name': 'Playstation 5',
#   'id': 2,
#   'description': "The PlayStation 5's main hardware features include a solid-state drive customized for high-speed data streaming to "
#                   "enable significant improvements in storage performance, an AMD GPU capable of 4K resolution display at up to 120 frames per second, "
#                   "hardware-accelerated ray tracing for realistic lighting and reflections and the Tempest Engine allowing for hardware-accelerated 3D audio effects.",
#   'price': "$500 USD"
# }]

## DB GET Route
@app.route('/allconsoles', methods=['GET'])
def get_all_consoles():
  # conn = None
  # try:
    # params = config()
  # Execute a query
  cur.execute('SELECT * FROM "consoles"')
  # Retrieve query results
  records = cur.fetchall()
  print("The number of consoles: ", cur.rowcount)
  for row in records:
    print(row)
  return jsonify({'consoles': records})
  cur.close()
  # except (Exception, psycopg2.DatabaseError) as error:
  #   print(error)
  # finally:
  #   if conn is not None:
  #     conn.close()

## DB PUT route
@app.route('/updateconsole/<int:id>', methods=['PUT'])
def update_console(id):
  # conn = None
  try:
    # params = config()
    # Execute a query
    cur.execute("""
      UPDATE "consoles"
      SET "description" = 'XYZ'
      WHERE "id" = %s;
      """,
      [id]
    )
    # Retrieve query results
    # records = cur.fetchall()
    print("The number of updated consoles: ", cur.rowcount)
    # print(records)
    return jsonify({'result': 'success'})
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

### Local routes
# @app.route('/')
# def index():
#   return "Welcome to the API"

# @app.route('/consoles', methods=['GET'])
# def get():
#   return jsonify({'Consoles': consoles})

# @app.route('/consoles/<int:id>', methods=['GET'])
# def get_console(id):
#   return jsonify({'console': consoles[id]})

# @app.route('/consoles', methods=['POST'])
# def create():
#   console = { 
#     'name': 'Playstation 5 Digital',
#     'id': 3,
#     'description': "The PlayStation 5 Digital has all of the same hardware components as the regular PS5 except the disc drive.",
#     'price': "$400 USD"
#   }
#   consoles.append(console)
#   return jsonify({'Created': console})

# @app.route('/consoles/<int:id>', methods=['PUT'])
# def console_update(id):
#   consoles[id]['description'] = "XYZ"
#   return jsonify({'console':consoles[id]})

# @app.route('/consoles/<int:id>', methods=['DELETE'])
# def delete(id):
#   consoles.remove(consoles[id])
#   return jsonify({'result': True})


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    # app.run(debug=True)
    get_all_consoles()