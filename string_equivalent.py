import re


pattern = r"([가-힣a-zA-Z0-9/\(\)\-]+)\(M?\d{3}\.\d{3}\)\s*-\s*[가-힣a-zA-Z0-9/\(\)\-]+|M?\d{3}\.\d{3}\s*[가-힣a-zA-Z0-9/\(\)\-]+\s*[가-힣a-zA-Z0-9/\(\)\-]+"

def are_strings_equivalent(str1, str2):
    
    
    match1 = re.fullmatch(pattern, str1)
    match2 = re.fullmatch(pattern, str2)

    return bool(match1) and bool(match2)


