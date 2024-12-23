# notion_habit_tracker_cli
A Python CLI for tracking daily habits with Notion 

> [!NOTE]
> This is still a Work In Progress

![first version screenshot](/git_assets/main_image.png)

## Introduction
In progress


## How to run

1. Clone this repository in your machine or download the project files via `Code > Download ZIP`. It is recommended to use a Python virtual environment (like [venv](https://docs.python.org/3/library/venv.html)) so that all modules and dependencies can be housed neatly in one place.

2. Open your terminal and `cd` to the repository directory and use `pip` to install the package:

    ```
    pip install .
    ```
3. Use `pip show nhabittracker` to locate the directory where the package was installed. Then, `cd` to the directory.

4. Create a `.env` file in the package directory. A  `.env.example` file has been provided for you. 

5. In the `.env` file, `NOTION_SECRET` is your Internal Integration Secret. To generate this, create an Internal Integration from here: [Your Notion Interations Dashboard](https://www.notion.so/profile/integrations). More information about how to set this up can be found here - [Install via internal integration token](https://www.notion.com/help/add-and-manage-connections-with-the-api#install-from-a-developer)

6. In the `.env` file, `PAGE_ID` is the identifier for a blank page where you'd like to set up your Habit Tracker dashboard. To do this, create a new page and make sure your Integration created in step 5 is connected (more on this here: [Add connection to pages](https://www.notion.com/help/add-and-manage-connections-with-the-api#add-connections-to-pages)). The page identifier is the 32 character code that can be found at the end of a Notion page URL

7. The `NOTION_SECRET` and `PAGE_ID` is the bare minimum to use the CLI. You can now use the following command to dynamically create the dashboard setup for habit tracking, which involves creating two databases:

    ```
    nhabittracker setup dashboard "your_dashboard_name"
    ```

> [!NOTE]
> If you would like the tool to automatically detect the database, the word `Streak` needs to be present in the naming. If you'd like
> to name it something else, you'll have to track the databases manually. To do this, provide values for the `MAIN_DB_ID` and
> `COUNT_DB_ID` respectively in the `.env` file and also changing `USE_DB_IDS` to  `YES`.
> The IDs can be located by opening the databases as a full page and then grabbing
> the 32 character code at the end of the page URL

8. After all has been setup, use the `help` feature to inspect what commands are available:

    ```
    nhabittracker -h
    ```