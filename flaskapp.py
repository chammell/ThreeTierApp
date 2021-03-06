from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'acloudguru.cqsq6q6oma7l.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'acloudguru'
app.config['MYSQL_PASSWORD'] = 'cbh12345'
app.config['MYSQL_DB'] = 'testdb'
mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT data FROM example WHERE id = 1''')
	rv = cur.fetchall()
	return str(rv)

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('example.html')

@app.route('/addone/<string:insert>', methods=['GET', 'POST'])
def add(insert):
	cur = mysql.connection.cursor()
	cur.execute('''INSERT into example(data) VALUES(%s)''', (insert,))
	mysql.connection.commit()
	return "Done"

@app.route("/getlast")
def getlast():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM example ORDER BY ID DESC LIMIT 1''')
	rv = cur.fetchall()
	return str(rv)

@app.route("/getten")
def getten():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM example ORDER BY ID DESC LIMIT 10''')
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
	app.run(debug=True)
