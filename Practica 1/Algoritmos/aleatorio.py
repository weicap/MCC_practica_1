import random
import pandas as pd

# GENERAR DATOS ALEATORIOS ________________________

random_numbers = random.sample(range(100000), 50000)
random_numbers = pd.DataFrame(random_numbers)
random_numbers.to_csv('random_numbers.csv', index=False, header=False)


# CREAR LISTA _____________________________________
df = pd.read_csv('random_numbers.csv')
df.columns = [0]
lista = df[0].iloc[:50000].tolist()
print(lista)