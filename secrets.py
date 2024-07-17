def get(name):
    with open(f'/run/secrets/{name}') as f:
        return f.read()