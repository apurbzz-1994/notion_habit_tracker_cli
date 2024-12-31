# notion_habit_tracker_cli
A Python CLI for tracking daily habits with Notion 

![first version screenshot](/git_assets/main_image.png)

## Introduction
Most habit trackers rely on checkboxes or calendar days you cross off. But as someone working in the IT industry, few things are more satisfying than opening a termainl and hitting that enter key to execute a command, run a script or push code to GitHub. What if you could track your habits with the same efficiency and satisfaction?

Well, now you can! Introducing **nhabittracker**, a CLI tool that lets you track habits right from the terminal. With simple commands, you can “commit” your habits as if you’re pushing code, combining productivity with the joy of the command line.

The best part? Your progress is automatically synced to a dynamically generated Notion dashboard, giving you a visual way to compare, analyse, and reflect on your streaks—all without ever leaving your workflow.

### Features
- Transforms habit tracking into a command-line experience – Track your habits effortlessly with simple commands, seamlessly fitting into your regular workflow, whether you're running scripts or executing tasks in the terminal.
- Seamlessly integrates with Notion – Automatically syncs with your Notion page via the [Notion API](https://developers.notion.com/) to create and manage streaks, update streak counters, and validate entries to ensure that only one streak is logged per day for each habit.

### Available Commands

For dynamically setting up the dashboard for the first time in Notion:
```
nhabittracker setup dashboard "your_dashboard_name"
```

For creating/initialising a habit that you'd like to track for the first time:
```
nhabittracker create "your_habit_name"
```

For incrementing the streak-counter for the habit. This also supports adding an optional message:
```
nhabittracker add "your_habit_name" -m "optional message"
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

7. You can select a timezone (set to Australia/Melbourne by default) so that certain messages will display the correct time. To do this, add a `TIMEZONE` key to the `.env` file and add the code for your desired timezone. All timezone codes can be found [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568).

8. The `NOTION_SECRET` and `PAGE_ID` is the bare minimum to use the CLI. You can now use the following command to dynamically create the dashboard setup for habit tracking, which involves creating two databases:

    ```
    nhabittracker setup dashboard "your_dashboard_name"
    ```

> [!NOTE]
> The above command creates two inline databases on your Notion page: one for storing date-timestamped streaks and another for 
> tracking streak counts. The database IDs are automatically stored and managed in the `.env` file, giving you the flexibility 
> to customize your page layout. For example, it’s recommended to display the first database in a calendar view for better 
> visualization. However, if you delete and recreate the databases outside of the CLI, their IDs will no longer be 
> tracked automatically. In such cases, you can manually update the `.env` file with the appropriate 
> IDs (`MAIN_DB` and `COUNT_DB`). That said, it’s best to use the `setup` command to regenerate the databases and ensure 
> seamless integration.


9. After all has been setup, use the `help` feature to inspect what commands are available:

    ```
    nhabittracker -h
    ```

## Upcoming Work
- Rewriting some of the code to make it more Object Oriented
- CLI feature - to be able to add multiple streaks for the day with the same command
- ~~CLI feature - an optional argument to be able to add a note to a streak that goes to the streak’s page in Notion, kind of like a commit message~~ 
- Data export feature with date filter for data backup or import to other platforms (for creating visualisations, for example)