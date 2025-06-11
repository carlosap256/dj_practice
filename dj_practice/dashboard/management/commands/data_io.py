import json
import os
import logging
from datetime import datetime

from django.core.management.base import BaseCommand
# from pytz import UTC

from dashboard.thunder_coop_api.serializers import deserialize_bulk
from dashboard.thunder_coop_api.get_json import data_importer
from dashboard.thunder_coop_api.exporter import DataExporter


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--pull",
            # nargs="?",
            # type=str,
            action="store_true",
            # default="",
            help="Get latest phases file from an optional URL",
        )
        parser.add_argument(
            "-i",
            "--input",
            type=str,
            help="Import phases from a json file",
        )
        parser.add_argument(
            "-o",
            "--output",
            action="store_true",
            help="Export all stored phases as a json file",
        )
        parser.print_help()

    def handle(self, *args, **kwargs):
        logger.info(f"Args {args}  kwargs {kwargs}")
        pull = kwargs["pull"]
        output = kwargs["output"]
        input = kwargs["input"]

        if pull:
            logger.info(f"Importing data from url  '{pull}'")
            new_objects_added = data_importer()
            logger.info(f"Added {new_objects_added} objects to the database")
        if output:
            logger.info(f"Exporting data to /tmp/out.json")
            data_exporter = DataExporter()
            json_data = data_exporter.export_to_json()
            data_exporter.json_to_file(json_data, '/tmp/out.json')
            logger.info(f"Done")
        if input:
            logger.info(f"Import data from {input}")

            with open(os.path.join(input)) as input_file:                
                deserialize_bulk(input_file.read())
            
                logger.info(f"Done")
            
