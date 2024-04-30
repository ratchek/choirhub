# Runs django server and also runs the scss watcher

from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line
import subprocess
import sys
import os

class Command(BaseCommand):
    help = 'Runs the Django server and the SASS watcher'

    def handle(self, *args, **options):
        try:
            # Starting the SASS watcher
            self.stdout.write(self.style.SUCCESS('Starting SASS watcher...'))
            sass_process = subprocess.Popen(
                ['python', 'manage.py', 'sass', 'static/scss/', 'static/css/', '--watch']
            )

            # Starting the Django server
            self.stdout.write(self.style.SUCCESS('Starting Django server...'))
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choirs.settings")
            execute_from_command_line(['manage.py', 'runserver'])

        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('Stopping server and SASS watcher...'))
            sass_process.terminate()
            sys.exit()


