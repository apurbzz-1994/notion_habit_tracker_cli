import requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_SECRET")
PAGE_ID = os.getenv("PAGE_ID")

# set headers globally
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def send_post_request_to_notion(endpoint_url, json_payload, success_message = None):
    requested_response = None
    try:
        response = requests.post(endpoint_url, json=json_payload, headers=headers)
        requested_response = response.json()
        if success_message!= None:
            print(success_message)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
    finally:
        return requested_response
    


def send_patch_request_to_notion(endpoint_url, json_payload):
    requested_response = None
    try:
        response = requests.patch(endpoint_url, json=json_payload, headers=headers)
        requested_response = response.json()
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
    finally:
        return requested_response



def send_get_request_to_notion(endpoint_url):
    requested_response = None
    try:
        response = requests.get(endpoint_url, headers=headers)
        requested_response = response.json()
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
    finally:
        return requested_response


def extract_page_id_from_url(page_link):
    page_link_split = page_link.split("-")
    page_id = page_link_split[len(page_link_split) - 1]
    return page_id


def create_db_in_notion(page_id, db_name, props):
    endpoint = "https://api.notion.com/v1/databases/"

    #payload to send here
    payload = {

    #denotes the parent page the database is housed in   
    "parent": {
        "type": "page_id",
        "page_id": page_id
    },

    #database title
     "title": [
        {
            "type": "text",
            "text": {
                "content": db_name,
            }
        }
    ],

    #database columns
    "properties": props,

    #denoting that the database should be an inline block in the page
     "is_inline": True

    }

    #request here, possibly in a try-catch block
    send_post_request_to_notion(endpoint, payload)


def initialise_notion_dashboard_page(page_id, main_db_name):
    #create main database
    main_db_properties = {
         "Title": {
            "title": {}
        },
        "Date": {
            "date": {}
        },
        "Streak Type": {
            "select": {
                "options": []
            }
        }
     }
    
    #properties for streak count
    streak_count_db_properties = {
         "Streak": {
            "title": {}
        },
        "Last Recorded": {
            "date": {}
        },
        "Streak Count": {
            "number": {
                "format": "number"
            }
        }
     }
    
    create_db_in_notion(page_id, main_db_name, main_db_properties)
    create_db_in_notion(page_id, "Streak Counter ️‍🔥", streak_count_db_properties)

    print(f"Yay! 😇 Your Notion dashboard is now ready here: https://www.notion.so/Python-Script-Test-Page-{page_id}")



'''
db_to_find values:
main_db
count_db
'''
def find_database_id_in_notion(page_id, db_to_find):
    endpoint = f"https://api.notion.com/v1/blocks/{page_id}/children"

    database_id = None

    use_db_id = os.getenv("USE_DB_IDS")

    if use_db_id == "NO":
        all_page_blocks = send_get_request_to_notion(endpoint)["results"]

        #loop through blocks to find any database block
        #then, do a name match (the last word should be Streak)
        for each_block in all_page_blocks:
            if each_block['type'] == "child_database":
                database_title = each_block['child_database']['title']

                if db_to_find == "main_db":
                    database_title_split = database_title.split(" ")
                    keyword_search = database_title_split[len(database_title_split) - 1]
                    #only consider if database name has a keyword match
                    if keyword_search.lower() == "streak":
                        database_id = each_block["id"]
                elif db_to_find == "count_db":
                    if "streak counter" in database_title.lower():
                        database_id = each_block["id"]
                else:
                    print("Script Erro: db_to_find can only look for main_db and count_db")
    else:
        if db_to_find == "main_db":
            database_id = os.getenv("MAIN_DB_ID")
        elif db_to_find == "count_db":
            database_id = os.getenv("COUNT_DB_ID")
        else:
            print("Script Erro: db_to_find can only look for main_db and count_db")
    return database_id
    


def find_streak_from_count_db(page_id, streak_name):
    db_id = find_database_id_in_notion(page_id, 'count_db')
    endpoint = f"https://api.notion.com/v1/databases/{db_id}/query"


    payload = {
        "filter": {
            "property": "Streak",
            "title": {
                "contains": streak_name
            }    
        }   
    }

    response = send_post_request_to_notion(endpoint, payload)
    return response




def add_streak_page_to_notion_db(page_id, streak_name, streak_date_entry):
    endpoint = "https://api.notion.com/v1/pages"
    db_id = find_database_id_in_notion(page_id,'main_db')

    payload = {
        "parent": { "database_id": db_id },

        #database columns
        "properties": {
            "Title": {
                "title": [
				{
					"text": {
						"content": streak_name
					}
				}
			]
            },
            "Date": {
                "date": {"start": streak_date_entry, "end": None}
            },
            "Streak Type": {
                "select": {
                   "name": streak_name
                }
            },
        }
    }
    #append streak page to database
    send_post_request_to_notion(endpoint, payload)



def add_new_streak_to_count_db(page_id, streak_name):
    endpoint = "https://api.notion.com/v1/pages"
    db_id = find_database_id_in_notion(page_id,'count_db')

    #add a check here so that an existing streak cannot be entered twice
    streak_check = find_streak_from_count_db(page_id, streak_name)

    #no result means streak doesn't already exist, so can go ahead
    if len(streak_check['results']) == 0:
        payload = {
            "parent": { "database_id": db_id },

            #database row appended with no date and count set to zero
            "properties": {
                "Streak": {
                    "title": [
                    {
                        "text": {
                            "content": streak_name
                        }
                    }
                ]
                },
                "Streak Count": {
                    "number": 0
                },
            }
        }
        #append streak page to database
        send_post_request_to_notion(endpoint, payload)
        print(f"Habit {streak_name} created! 🌻🌻")
        print("Feel free to start traking this daily anytime by adding a streak using the 'add' command")
    else:
        print(f"{streak_name} already exists!")



def update_streak_counter_value(page_id, new_value, streak_date_entry):
    endpoint = f"https://api.notion.com/v1/pages/{page_id}"
    if isinstance(new_value, int) and new_value >= 0:
        payload = {
            "properties":{
                "Streak Count": {
                    "number": new_value
                }, 
                "Last Recorded": {
                "date": {"start": streak_date_entry, "end": None}
            }
            }
        }

        #make patch request
        send_patch_request_to_notion(endpoint, payload)


def record_streak(page_id, streak):
    #query the streak from count DB, should return empty list if not found 
    #and only one response if found
    found_streak = find_streak_from_count_db(page_id, streak)
    streak_date_entry = datetime.now().astimezone(timezone.utc).isoformat()
    
    #if streak not found, prompt user to create one
    if len(found_streak['results']) == 0:
        print("This habit was not found 😞")
        print("Please use the 'create' command to add a habit before starting a streak")
    #streak found
    else:
        streak_count = found_streak['results'][0]['properties']['Streak Count']['number']
        streak_page_id = found_streak['results'][0]['id']

        #this is a new streak that is being entered
        if streak_count == 0:
            update_streak_counter_value(streak_page_id, 1, streak_date_entry)
            add_streak_page_to_notion_db(page_id, streak, streak_date_entry)
            print(f"Streak added! 🤩 Congrats on starting {streak}🎉🎉🎉🥳! This is day 1")
        #streak is already going
        #check if gaps in streak
        else:
            last_streak_date = found_streak['results'][0]['properties']['Last Recorded']['date']['start']
            last_streak_date_obj = datetime.strptime(last_streak_date, "%Y-%m-%dT%H:%M:%S.%f%z")
            now_streak_date_obj = datetime.strptime(streak_date_entry, "%Y-%m-%dT%H:%M:%S.%f%z")
            streak_daily_limit_date_obj = last_streak_date_obj + timedelta(hours = 24)
            streak_end_limit_date_obj = streak_daily_limit_date_obj + timedelta(hours = 24)

            time_difference = now_streak_date_obj - last_streak_date_obj
            days = time_difference.days

            #adding a check here so that last streak date cannot be in the future
            if last_streak_date_obj > now_streak_date_obj:
                print("Script Error: Last recorded streak cannot be in the future. It seems you may have manually made changes to the Notion DB")
            else:
                #this means streak has already been entered for the day
                if now_streak_date_obj > last_streak_date_obj and now_streak_date_obj < streak_daily_limit_date_obj:
                    print(f"You've already done {streak} for the day. Good job!💪💪")
                    #streak is still going, increment by correct amount
                else:
                    if now_streak_date_obj > streak_daily_limit_date_obj and now_streak_date_obj < streak_end_limit_date_obj:
                        new_streak_count = streak_count + 1
                        update_streak_counter_value(streak_page_id, new_streak_count, streak_date_entry)
                        add_streak_page_to_notion_db(page_id, streak, streak_date_entry)
                        print(f"Streak added for the day! Good on you for continuing to {streak} for {new_streak_count} days straight! 😺💪💪")
                    else:
                        update_streak_counter_value(streak_page_id, 1, streak_date_entry)
                        add_streak_page_to_notion_db(page_id, streak, streak_date_entry)
                        print(f"Oh noes! 😭 you last did {streak} {days} days ago")
                        print("So you gotta start over! 😔 Your streak count has been reset to 1")
                   

                
def main():
    initialise_notion_dashboard_page(PAGE_ID, "Apurba's 2025 Streak")




if __name__ == '__main__':
    main()
