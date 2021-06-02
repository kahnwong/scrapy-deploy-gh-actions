import yaml
import os

### update apikey value
with open('scrapinghub.yml', 'r') as f:
    d = yaml.load(f.read(), Loader=yaml.FullLoader)
    d['apikey'] = os.environ['APIKEY']

### update config to file
with open('scrapinghub.yml', 'w') as f:
    yaml.dump(d, f, default_flow_style=False)
