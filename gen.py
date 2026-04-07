import pandas as pd
import numpy as np

def gen_data(col):
    id = [f"C{i}" for i in range(1,col+ 1)]
    name = [f"Customer_{i}" for i in range(1,col + 1)]
    ex_country = ['VietNam', 'USA', 'ThaiLand', 'Germany', 'Spanish', 'Korea', 'Japan', 'Canada', 'UK']
    rng = np.random.default_rng()
    country = rng.choice(ex_country, size = col)
    year = np.random.randint(1950, 2007, size = col)
    month = np.random.randint(1,12,size = col)
    birthdate = []
    for i in range(0,col):
        if month[i] == 2:
            date = np.random.randint(1,28)
        elif month[i] in [1,3,5,7,8,10,12]:
            date = np.random.randint(1,31)
        else: date = np.random.randint(1,30)
        birth = f"{date}-{month[i]}-{year[i]}"
        birthdate.append(birth)
    score = np.random.randint(0,5000,size = col)
    data = {
        "ID": id,
        "Name": name,
        "Country": country,
        "BirthDate": birthdate,
        "Score": score
    }
    df = pd.DataFrame(data)
    df.to_csv('customers.csv', index = False)
    print('Genegate data successfully!')

gen_data(10000)