from flask import Flask,jsonify,request
import threading,string
from db import data,alldata


t1 = threading.Thread(target=data)
t1.start()

app = Flask(__name__)

@app.route('/<string:country>',methods = ['GET', 'POST'])
def getdata(country : str):

    if len(country) < 4:
        country = country.upper()
    else:
        country = string.capwords(country)
    names = ["Country","TotalCases","NewCases","TotalDeaths","NewDeaths","TotalRecovered","ActiveCases","SeriousCritical","TotCases/1m","Deaths/1m","TotalTests","Tests/1m","Continent"]


    if alldata[country] != None :
        CountryStats = dict(zip(names, alldata[country]))
        return jsonify(CountryStats),200
    else:
        return jsonify(f"Error : KeyName {country} not found !")




if __name__ == '__main__':
    app.run()


