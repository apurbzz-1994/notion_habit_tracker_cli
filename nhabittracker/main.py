from nhabittracker.habit_tracker_util import *
import argparse
from dotenv import load_dotenv
import os

load_dotenv()
PAGE_ID = os.getenv("PAGE_ID")

def create(args):
    add_new_streak_to_count_db(PAGE_ID, args.streak_name)

def add(args):
    record_streak(PAGE_ID, args.streak_name)

def setup(args):
    if args.setup_name.lower() == "dashboard":
        initialise_notion_dashboard_page(PAGE_ID, args.setup_option)
    else:
        print("Incorrect argument provided. Use '-h' to inspect")


def main():
    parser = argparse.ArgumentParser(description="This CLI allow you to create and add daily streaks to a Notion dasboard")
    subparsers = parser.add_subparsers(help="Available subcommands")

    #create subcommand
    create_parser = subparsers.add_parser("create", help="Create a streak")
    create_parser.add_argument("streak_name", help="The name of the habit that you would like to create a streak for")
    create_parser.set_defaults(func=create)

    #add subcommand
    add_parser = subparsers.add_parser("add", help="Start a streak or add a daily streak")
    add_parser.add_argument("streak_name", help="Name of the habit that you'd like to add a streak count for")
    add_parser.set_defaults(func=add)

    #setup subcommand
    setup_parser = subparsers.add_parser("setup", help="Setting up things on the notion side, like the dashboard")
    setup_parser.add_argument("setup_name", help="Use 'dashboard' to dynamically set up a dashboard with databases in Notion")
    setup_parser.add_argument("setup_option", help="For 'dashboard', type in the name you'd like the dashboard to have. If you'd like for the database to be detected automatically, use the word 'Streak' in the name")
    setup_parser.set_defaults(func=setup)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()


