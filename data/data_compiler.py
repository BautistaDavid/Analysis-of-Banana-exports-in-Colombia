# Thanks to the oec.world website. From this site the API was used to collect the data.
import requests
import pandas 

data = pd.DataFrame(columns = ['Year','Continent ID', 'Continent', 'Country ID', 'Country', 'Trade Value'])
for year in range(1997,2021):
  url = f'https://oec.world/olap-proxy/data?Exporter+Country=sacol&HS4=20803&cube=trade_i_baci_a_92&drilldowns=Year,Importer+Country&measures=Trade+Value&parents=true&sparse=false&locale=en&q=Trade%20Value,1&Year={year}' 
  resp = requests.get(url)
  txt = resp.json()
  new_data = pd.DataFrame(txt['data'])
  data = pd.concat([data,new_data])
  
data.to_csv('datos_exportaciones_banano.csv') # This csv file was upload to this repository 
