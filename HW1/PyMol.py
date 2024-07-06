import requests
import json

url = "https://search.rcsb.org/rcsbsearch/v2/query?json="
query = {
  "query": {
    "type": "terminal",
    "service": "text",
    "parameters": {
      "attribute": "rcsb_entry_info.structures_keywords",
      "operator": "contains_phrase",
      "value": "ligand"
    }
  },
  "return_type": "entry"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(query))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
