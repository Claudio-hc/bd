from flask import Flask, render_template, json, request, redirect, url_for
from flask_mysqldb import MySQL 


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp1'

mysql = MySQL(app)
# listar
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario')
    data = cur.fetchall()
    return render_template('inicio.html', users = data)

#insertar
@app.route('/insert',methods=['POST'])
def insert():
       nombre=request.form['nombre']
       correo=request.form['correo']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO usuario (nombre, correo) VALUES (%s,%s)',(nombre, correo))
       mysql.connection.commit()
       return redirect('/')

#delete
@app.route('/delete/<string:id>', methods=['POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuario WHERE id=%s',(id))
    mysql.connection.commit()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)