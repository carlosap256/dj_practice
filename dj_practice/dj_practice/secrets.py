import os
import logging

logger = logging.getLogger(__name__)

def get_secret_file_content_from_secret_name(secret_name):

    with open(os.path.join("/", "run", "secrets/", secret_name)) as secret_file:
      filecontent = secret_file.read()
      logger.info(f"Secret {secret_name} is '{filecontent}'")
    return filecontent
