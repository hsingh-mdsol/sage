import pandas as pd
import requests


class NPPES:
    def url(self, npi: str):
        """
        """
        api_url = f"https://npiregistry.cms.hhs.gov/api/?number={npi}&enumeration_type=&" \
                  "taxonomy_description=&first_name=&use_first_name_alias=&last_name=&organization_name=&" \
                  "address_purpose=PRIMARY&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=on&version=2.1"
        return api_url

    def get_data(self, npi: str):
        """
        """
        response = requests.get(self.url(npi))
        if len(response.json()['results']) != 0:
            d = {'npi': response.json()['results'][0]['number']}
            # sometimes the url switches the order of mailing or location address so need to search for location
            for i in response.json()['results'][0]['addresses']:
                if i['address_purpose'] == 'LOCATION':
                    break
            d.update(i)
            return pd.DataFrame(d, index=[0])
        else:
            return pd.DataFrame()
