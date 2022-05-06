import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep = "\n")
id_url = str(input("Enter an id from ceneo: "))

opinions = pd.read_json(f"opinions/{id_url}.json")
print(opinions)