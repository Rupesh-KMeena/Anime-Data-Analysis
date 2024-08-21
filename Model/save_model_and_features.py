import pickle

# Replace 'model.pkl' with the path to your saved model file
model_filename = 'path/to/your/model.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Now you can use `model` for predictions

