# notion_habit_tracker_cli
A Python CLI for tracking daily habits with Notion 

![first version screenshot](/git_assets/main_image.png)

## Introduction
Conventional habit trackers usually comprise of check-boxes that you tick or calendar days that you can cross out. But as someone working in the IT industry, nothing can be more satisfying than opening a termainl and hitting that enter key to execute a command, run a script or push code to GitHub. What if you could add and track your habit streaks the same way, as if you're committing code?

Well, now you can! Introducing nhabittracker, a CLI tool that lets you track habits right from the terminal. With simple commands, you can “commit” your habits as if you’re pushing code, combining productivity with the joy of the command line.

The best part? Your progress is automatically synced to a dynamically generated Notion dashboard, giving you a visual way to compare, analyse, and reflect on your streaks—all without ever leaving your workflow.

### Available Commands

For dynamically setting up the dashboard in Notion:
```
nhabittracker setup dashboard "your_dashboard_name"
```

For creating a habit that you'd like to track:
```
nhabittracker create "your_habit_name"
```

For adding a streak to the streak counter for the habit:
```
nhabittracker add "your_habit_name"
```


## How to run

1. Clone this repository in your machine or download the project files via `Code > Download ZIP`. It is recommended to use a Python virtual environment (like [venv](https://docs.python.org/3/library/venv.html)) so that all modules and dependencies can be housed neatly in one place.

2. Open your terminal and `cd` to the repository directory and use `pip` to install the package:

    ```
    pip install .
    ```
3. Use `pip show nhabittracker` to locate the directory where the package was installed. Then, `cd` to the directory.

4. Create a `.env` file in the package directory. A  `.env.example` file has been provided for you. 

5. In the `.env` file, `NOTION_SECRET` is your Internal Integration Secret. To generate this, create an Internal Integration from your Notion account here: [Your Notion Interations Dashboard](https://www.notion.so/profile/integrations). More information about how to set this up can be found here - [Install via internal integration token](https://www.notion.com/help/add-and-manage-connections-with-the-api#install-from-a-developer)

6. In the `.env` file, `PAGE_ID` is the identifier for a blank page where you'd like to set up your Habit Tracker dashboard. To do this, create a new page and make sure your Integration created in step 5 is connected (more on this here: [Add connection to pages](https://www.notion.com/help/add-and-manage-connections-with-the-api#add-connections-to-pages)). The page identifier is the 32 character code that can be found at the end of a Notion page URL

7. The `NOTION_SECRET` and `PAGE_ID` is the bare minimum to use the CLI. You can now use the following command to dynamically create the dashboard setup for habit tracking, which involves creating two databases:

    ```
    nhabittracker setup dashboard "your_dashboard_name"
    ```

> [!NOTE]
> The above command essentially creates two inline databases in your Notion page - one that stores date-timestamped streaks, and the
> other for keeping count of the streaks. The database IDs for these are automatically stored and tracked within the .env file, and 
> you're free to change the page layout to display these databases any way you please. For instance, it's recommended to set the
> first database to a calendar view. However, if you delete the databases and recreate them without using the CLI, the database 
> IDs won't be automatically tracked. You can set them manually yourself in the .env file (keys being MAIN_DB and COUNT_DB), but
> it's recommended to use the 'setup' command to regenerate them.

8. After all has been setup, use the `help` feature to inspect what commands are available:

    ```
    nhabittracker -h
    ```

## Upcoming Work
- Rewriting some of the code to make it more Object Oriented
- CLI feature - to be able to add multiple streaks for the day with the same command
- CLI feature - an optional argument to be able to add a note to a streak that goes to the streak’s page in Notion, kind of like a commit message 