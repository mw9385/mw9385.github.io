import requests
for doi in ['10.1016/j.inffus.2022.03.003','10.5302/J.ICROS.2020.20.0014']:
    url=f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,citationCount'
    r=requests.get(url,timeout=20)
    print('DOI', doi, 'status', r.status_code)
    if r.ok:
        d=r.json(); print('title', d.get('title','?'))
        print('citations', d.get('citationCount','?'))
    else:
        print(r.text)
