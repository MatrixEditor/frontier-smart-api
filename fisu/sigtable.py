from json import load

def load_file_signatures(path: str):
  if not path or not path.endswith('json'):
    return

  with open(path, 'r') as _file:
    return load(_file)
