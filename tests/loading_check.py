import pickle

# Loading from a .pkl file
with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("ml/model.pkl", "rb") as f:
    processer = pickle.load(f)
