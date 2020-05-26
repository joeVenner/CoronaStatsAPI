from flask import Flask,jsonify,request
import threading,string
from db import data,alldata


t1 = threading.Thread(target=data)
t1.start()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/<string:country>',methods = ['GET', 'POST'])
def getdata(country : str):

    if len(country) < 4:
        country = country.upper()
    else:
        country = string.capwords(country)
    names = ["id","Country","TotalCases","NewCases","TotalDeaths","NewDeaths","TotalRecovered","ActiveCases","SeriousCritical","TotCases/1m","Deaths/1m","TotalTests","Tests/1m","-","Continent"]


    if alldata[country] != None :
        CountryStats = dict(zip(names, alldata[country]))
        return jsonify(CountryStats),200
    else:
        return jsonify(f"Error : KeyName {country} not found !")




if __name__ == '__main__':
    app.run()


