import requests
from rgx import clean_company_name


def connect_functions():
    response = requests.get('http://127.0.0.1:5000/companies')
    companies = response.json()['companies']  # get the list of companies
    clean_companies = []

    for company in companies:

        name = company['name']
        purified_name = clean_company_name(name)

        post_data = {
            purified_name: {
                     'country iso': company['country iso'],
                     'city': company['city'],
                     'nace': company['nace'],
                     'website': company['website']}}

        post_response = requests.post('http://127.0.0.1:5000/cleanedCompanies', json=post_data)

        if post_response.status_code != 200:
            print(f'Error posting {name}: {post_response.text}')
        else:
            print(f'Successfully posted {name}!')

        print(f'Total {len(clean_companies)} companies successfully posted.')


connect_functions()
