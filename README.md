# CoronaStatsAPI
CoronaStatsAPI is a Python Rest API To Get The Latest Corona Statistics In Every Country


# Request To the API 
![Logo](https://i.ibb.co/9sx4PdD/apicorona.png)

This is a screenshot from POSTMAN(it's an app to make web requests) it returns a json of the COVID19 Stats  in US.


-------------
# Installation

You can download CoronaStatsAPI source code by cloning the [Git Repo](https://github.com/joeVenner/CoronaStatsAPI.git) and simply installing its requirements:

```
~ ❯❯❯ git clone https://github.com/joeVenner/CoronaStatsAPI.git

~ ❯❯❯ cd CoronaStatsAPI/

~/CoronaStatsAPI ❯❯❯ pip install -r requirements.txt

~/CoronaStatsAPI ❯❯❯python CoronaStatsAPI.py

```

# Usage

Make a Post or Get request to the link https://covidstatistics.herokuapp.com/usa <br/>
You can change the 'usa' by any other country name like : india,uk,spain,france...

 
``` 
Python
  import requests
  response = requests.get('https://covidstatistics.herokuapp.com/usa')
  data = response.json()
  print(data)
```
```
Output: 

{'ActiveCases': '824,466',
 'Continent': 'North America',
 'Country': 'USA',
 'Deaths/1m': '175',
 'NewCases': '+11,909',
 'NewDeaths': '+1,065',
 'SeriousCritical': '14,145',
 'Tests/1m': '17,471',
 'TotCases/1m': '3,088',
 'TotalCases': '1,022,265',
 'TotalDeaths': '57,862 ',
 'TotalRecovered': '139,937',
 'TotalTests': '5,782,860'})
```

Author: [Joe](mailto:ylafrimi@gmail.com).
