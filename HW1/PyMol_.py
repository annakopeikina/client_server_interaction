import requests
import json

def search_structures(keyword):
    url = "https://search.rcsb.org/rcsbsearch/v2/query?json="
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": "struct.title",
                "operator": "contains_phrase",
                "value": keyword
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
        return data['result_set']
    else:
        print(f"Error: {response.status_code}")
        return []

def get_structure_info(pdb_id):
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"

# Ввод ключевого слова пользователем
keyword = input("Введите ключевое слово для поиска: ")

# Поиск структур по ключевому слову
result_set = search_structures(keyword)

if result_set:
    print(f"Найдено {len(result_set)} структур по ключевому слову '{keyword}':\n")
    pdb_ids = [result['identifier'] for result in result_set[:10]]  # Ограничимся 10 результатами для примера
    
    for pdb_id in pdb_ids:
        structure_info = get_structure_info(pdb_id)
        print(f"Информация для PDB ID {pdb_id}:")
        print(json.dumps(structure_info, indent=4))
        print("\n" + "="*50 + "\n")
else:
    print(f"По ключевому слову '{keyword}' ничего не найдено.")
