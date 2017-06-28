from flask import Flask
from flask.ext.mysqldb import MySQL

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

if __name__ == '__main__':
app.run(debug=True)
