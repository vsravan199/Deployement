from flask import Flask, render_template, request
import joblib
app = Flask(__name__)
model = joblib.load("dib_79.pkl")
@app.route('/')
def form():
    return render_template('form.html') 
@app.route('/data' , methods = ['POST'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    result = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if result[0] == 1:
         output = 'the person is Diabetic'
    else:
         output = 'person is not Diabetic'    
    return render_template('result.html', output = output)         
if __name__=='__main__':
    app.run(debug = True)