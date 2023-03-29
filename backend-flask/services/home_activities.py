from datetime import datetime, timedelta, timezone
import logging
from lib.db import db

class HomeActivities:
  def run(cognito_user_id=None):
   #logging disabled  based on spend 
    #logger.info("HomeActivities")
    #  now = datetime.now(timezone.utc).astimezone()
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results