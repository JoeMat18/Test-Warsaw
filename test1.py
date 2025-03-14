import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Transport_Node': ['Centrum', 'Politechnika', 'Mlociny', 'Dworzec Wileński'],
    'Passenger_Flow': [44800, 37700, 27100, 28800]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
plt.bar(df['Transport_Node'], df['Passenger_Flow'], color='skyblue')
plt.title("Пассажиропоток транспортных узлов Варшавы")
plt.xlabel("Транспортный узел")
plt.ylabel("Пассажиропоток (в день)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
