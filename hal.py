import json
import sqlite3
from sqlite3 import Error
import time

# flask ui with nice icons
# show last N actions 
# actions per room?
# share on git and hass forum

 
db_file = "z:\home-assistant_v2.db"
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, 10)
    except Exception as e:
        print(e)
        
    return conn
 
 
def get_latest_events(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    events = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM events LIMIT 100")
 
    event_rows = cur.fetchall()

    return event_rows
 
 
def main():
    database = db_file
    # create a database connection
    conn = create_connection(database)
        
    with conn:
        # for row in get_latest_events(conn):
        for event_id, event_type, event_data, origin, time_fired, created, context_id, context_user_id in get_latest_events(conn):
            print("------------------------------")
            print("Event ID:", event_id)
            print("Event Type:", event_type)
            if event_type == "state_changed":
                print("STATE CHANGED")
                # ARE STATE CHANGES THE ONLY THINGS I CARE ABOUT?
                state_change = json.loads(event_data)
                print(state_change["entity_id"])
                print(state_change["old_state"]["state"])
                print(state_change["old_state"]["last_changed"])
                print(state_change["new_state"]["state"])
                print(state_change["new_state"]["last_changed"])

            
            else:
                print("Event Data:", event_data)

                
if __name__ == '__main__':
    main()