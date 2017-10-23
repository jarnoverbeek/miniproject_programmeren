import requests
import xmltodict

auth_details = ('jarno.verbeek@student.hu.nl', 'm4EvylGryROkalqWux4tEkLtSFtx0dkvqQlEgzgf_2Brk1eLLgTLWQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=tiel'
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)
print(vertrekXML)