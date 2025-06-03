import os

def get_secret_file_content_from_secret_name(secret_name):

    with open(os.path.join("/", "run", "secrets/", secret_name)) as secret_file:
      return secret_file.read()
    