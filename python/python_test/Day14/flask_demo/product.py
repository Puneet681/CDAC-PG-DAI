from flask import Flask,render_template,redirect,request,url_for
app = Flask(__name__)

import sqlite3
con = sqlite3.connect('/home/dai/Desktop/Python/flask_demo/mydb.db',check_same_thread= False)

if con!=None:
    print('Connection Done')

cur = con.cursor()

@app.route('/')
def home():
    return render_template('hellowrold.html')

@app.route('/products')
def displayproduct():
    #return "in Display"
    cur.execute("select * from product")
    rows = cur.fetchall()
    return render_template("displayproduct.html",data=rows)

@app.route('/acceptproduct')
def displayform():
    return render_template('productdata.html')

@app.route('/products/addproduct',methods = ['POST'])
def addproduct():
    pid = request.form.get('pid')
    pname = request.form.get('pname')
    qty = request.form.get('qty')
    Price = request.form.get('Price')
    cur.execute('insert into product values(?,?,?,?)',(pid,pname,qty,Price))
    con.commit()
    return redirect('/products')

    
if __name__ == '__main__':
    app.run(debug=True)