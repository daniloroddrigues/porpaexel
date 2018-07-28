import csv
import re

doc = csv.reader(open('planilia.csv', 'r'))
header = sorted(next(doc))
print(header)
# data = list()

for row in doc:
    name, email, phone, empresa, estado = row

    out_name, out_email, mat, out_empresa, out_estado = '', '', '', '', ''

    if name:
        name = re.search(r'.*', name)
        out_name = name.group().title()
        # print(letter)

    if email:
        milhar = re.compile(r'[\w\._]+@[\a-zA-Z_\.]+\.[a-zA-Z]{2,3}')
        out_email = milhar.match(email).group()
        # print(email.group())

    if phone:
        # phone = re.search(r'\W+', phone)
        # print(phone)
        matches = re.findall(r'\d+', phone)
        z = ''
        list_matches = []
        for m in matches:
            z += m

        list_matches.append(z)
        # print(list_matches)
        for l in list_matches:
            if len(l) == 8:
                """Numeros com 8 digitos"""
                mat = re.sub(r'(\d{0,4})(\d{0,4})', r'(00) \1-\2', l)
                # print(mat)

            if len(l) == 10:
                """Numeros com 10 digitos"""
                mat = re.sub(r'(\d{0,2})(\d{0,4})(\d{0,4})', r'(\1) \2-\3', l)
                # print(mat)

            if len(l) == 11:
                """Numeros com 11 digitos"""
                mat = re.sub(r'(\d{0,2})(\d{0,5})(\d{0,4})', r'(\1) \2-\3', l)
                # print(mat)

            if len(l) == 12:
                """Numeros com 12 digitos"""
                mat = re.sub(r'(\d{0,2})(\d{0,2})(\d{0,4})(\d{0,4})', r'(\2) \3-\4', l)
                # print(mat)

    if empresa:
        empresa = re.search(r'.*', empresa)
        out_empresa = empresa.group().title()

    if estado:
        estado = re.match(r'[A-z]{2}', estado)
        out_estado = estado.group().upper()
        # print(out_estado)

    print(out_name, out_email, mat, out_empresa, out_estado)

    """
    write the row

    with open('data.csv', 'w') as file:
        dic = dict(nome=out_name, email=out_email, telefone=mat, empresa=out_empresa, estado=out_estado)
        print(dic)
        print(sorted(dic.keys()))
        out = csv.DictWriter(file, fieldnames=header)
        out.writeheader()
        out.writerow(dic)
    """