# Define the WSGI application object

import pprint

from modules.core.db import get_db
from .app_config import *
from flask import redirect


@app.route('/')
def index():
    return redirect('ui')


# Define the database object which is imported
# by modules and controllers


import modules.steps
import modules.config
import modules.logs.endpoints
import modules.sensors
import modules.actor
import modules.notification
import modules.fermenter
from modules.addon.endpoints import initPlugins
import modules.ui.endpoints
import modules.system.endpoints
import modules.buzzer
import modules.stats
import modules.kettle
import modules.recipe_import
import modules.core.db_mirgrate

from .app_config import cbpi
# Build the database:
# This will create the database file using SQLAlchemy


pp = pprint.PrettyPrinter(indent=6)


def init_db():
    print("INIT DB")
    with app.app_context():
        db = get_db()

        try:
            with app.open_resource('../config/schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())

            db.commit()
        except Exception as e:
            pass

init_db()
initPlugins()
cbpi.run_init()

cbpi.run_background_processes()



app.logger.info("##########################################")
app.logger.info("### STARTUP COMPLETE")
app.logger.info("##########################################")