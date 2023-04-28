import re


def clean_company_name(company_name):
    #unwanted characters
    company_name = re.sub(r',.*', '', company_name)
    company_name = re.sub(r'\(.*\)', '', company_name)
    company_name = re.sub(r'"', '', company_name)
    company_name = re.sub(r'\s-\s|\s-\w+', ' ', company_name)
    #re legal entities
    company_name = re.sub(r'\bLtd\.?\b|\bLIMITED\b', '', company_name, flags=re.IGNORECASE)
    company_name = re.sub(r'\bInc\.?|\bIncorporated\b', '', company_name, flags=re.IGNORECASE)
    company_name = re.sub(r'\bLLC\.?\b', '', company_name, flags=re.IGNORECASE)
    return company_name.strip()






