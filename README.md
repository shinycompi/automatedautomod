# automoderator_automator

A Python utility for automating reddit's automoderator by setting time dependent rules.


## Sharing, distributing, and contributing to this project

Please be advised that this project is currently private. It hasn't been sanitized of secrets, tested extensively, or documented properly. Do not share it or distribute it without authorization.

The project also doesn't have a contribution workflow or contributing guidelines. This will be updated in the future.


## Installation and compatibility

The automoderator_automator has been tested on Python 3.8.10 on Ubuntu 20.04. It *should* work on any machine capable of running that version of Python.

To run the application the config.ini file must contain the following information: `client_id`, `client_secret`, and `user_agent`.  `client_id` and `client_secret` are provided by reddit when you register the application. `user_agent` identifies the application to the reddit overlords.

The first and current instance of this application was registered by /u/adolfojp. If you want authorization to run this script on your computer contact /u/adolfojp so he can authorize you on reddit. If you want to work independently on this application register the application yourself and change the aforementioned variables.


## Setting the rules

The currently available rules are mon-off, tue-off, wed-off, thu-off, fri-off, sat-off, sun-off

Those rules tell the automoderator_automator to comment out (and back in) the corresponsing sections on the automoderator configuration page. Sections are delimited with `# rule-start` and `# rule-end`. Example for removing the meme rule on mondays:

```
### remove all meme flaired posts
# rule-start mon-off 
type: submission
flair_template_id: [928f2da2-86a3-11ec-8628-a6b4cfaf41d8] # Meme/Funpost flair
comment_stickied: true
comment: |
        /r/Windows is currently only accepting any meme submissions on Mondays in the UTC timezone, please resubmit then. In the mean time, your submission may be a good fit in /r/PCMasterRace, /r/WindowsMemes, or possibly even /r/LinuxMemes.
    
        ----
action: remove
action_reason: Meme post
Moderators_exempt: false
# rule-end
```

It is important to not add comments inside of those rule delimiters. The application is still not smart enough to differentiate comments from code.


## Running from the command line

`automoderator_automoderator.py` can be imported as a module but if you want to use the application from the command line `apply_day_rules.py` has been provided for that purpose. You use it like this:

```
python3 ./apply_day_rules.py --username username --password password --subreddit subreddit
```

You can use the --force flag to suppres the confirmation message. This is useful for running unnatended instances of the script.


## Running the script on a schedule

On Linux systems you can use cron for this purpose. If you want to run the command every day at zero hours, for example, you add the following after running `crontab -e`.

```
00 00 * * * ./python3 apply_day_rules.py --username username --password password --subreddit subreddit --force
```

You can use whatever scheduling application you have on your operating system. On Windows you should be able to use Task Scheduler but it hasn't been tested.


## Utilities

`post_test_posts.py` has been provided to post test posts on reddit. It's a simple utility so you need to hard code the post information on the python file itself. You can run it like this:

```
python3 ./post_test_posts.py --username username --password password --subreddit subreddit
```

You can also make it run silently with the --force flag and you can also schedule it with tools like cron.