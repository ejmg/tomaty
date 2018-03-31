"""
tomaty_serialization.py
~~~~~~~~~~~~~

basic serialization to preserve effort on any given day.

:copyright: @ 2018
:author: gabby ortman
:license: MIT, see LICENSE
"""
import json
from pathlib import Path
from datetime import timedelta, datetime
from tomaty.lib.utilities import date_utilities

TOMATY_JSON_PATH = "{}/.tomaty.json".format(Path.home())


class TomatySerializer:
    def __init__(self):
        self._total_time = None
        self.current_date = "{}".format(datetime.now().strftime("%Y_%m_%d"))

    @property
    def total_time(self):
        """Property for the total time a person has tomotoro-ed for a given day.
        Memoizes self._total_time to avoid having to open the json more than
        is necessary.

        :return self._total_time timedelta
        """
        if self._total_time is None:
            self._total_time = self.init_total_time()
        return self._total_time

    def save_tomotoro(self, current_time):
        """
        Saves the time spent tomotoro-ing on current_date.

        :param current_time: total time spent tomotoro-ing to be saved
        """
        f = open(TOMATY_JSON_PATH, 'r+')
        tomaty_json = json.loads(f.read())
        tomaty_json[self.current_date] = str(current_time)
        f.seek(0)
        f.write(json.dumps(tomaty_json))
        f.truncate()
        f.close()

    def init_total_time(self):
        """Initializes the total time spent tomotoro-ing.

        Initializes the .tomaty.json file if it doens't exist and sets time
        to 0:00:00.  Otherwise, attempts to grab the current time spent
        tomotoro-ing today, otherwise sets time to 0:00:00

        :return timedelta object

        """
        data = None
        try:
            f = open(TOMATY_JSON_PATH, 'r+')
            data = f.read()
        except IOError:
            f = open(TOMATY_JSON_PATH, 'w')

        if data:
            tomaty_json = json.loads(data)
            current_time = tomaty_json.get(self.current_date, None)
            if current_time:
                return date_utilities.string_to_timedelta(
                    tomaty_json.get(self.current_date, None))
            tomaty_json[self.current_date] = str(timedelta(0))
            f.close()
            return timedelta(0)
        else:
            tomaty_json = {}
            tomaty_json[self.current_date] = str(timedelta(0))
            tomaty_json_string = json.dumps(tomaty_json)
            f.write(tomaty_json_string)
            f.close()
            return timedelta(0)
