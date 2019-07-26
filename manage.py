#!/usr/bin/env python
import os
import sys
import pymysql
pymysql.install_as_MySQLdb()

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE",
    #                       "<app_name>.config.settings.local_settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "project.product_settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)