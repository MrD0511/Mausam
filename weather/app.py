from flask import Flask,render_template,request,session
from weather import Weather
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
@app.route("/Home",methods=['GET','POST'])
def index():
    c=str(request.form.get("city"))
    if c!='None':
        weath=Weather(c)
        try:
            res=weath.weather()
        except:
            return render_template('index.html',val=c)
        return render_template('index.html',val=c,loc=res['location']['name'],country=res['location']['country'],time=res['location']['localtime'],
                            time_zone=res['location']['timezone_id'],temp=res['current']['temperature'],wind=res['current']['wind_speed'],
                            wind_dir=res['current']['wind_dir'],description=res['current']['weather_descriptions'][0],
                            pressure=res['current']['pressure'],hum=res['current']['humidity'],fl=res['current']['feelslike'])
    else:
        return render_template('index.html',val=c)
@app.route("/About")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)