# helpers.py

def write2file(string_):
    with open('Best_Shows.csv', 'a') as f:
        f.write(string_)