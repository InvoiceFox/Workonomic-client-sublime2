Workonomic-client-sublime2
==========================

A SublimeText 2 client for Workonomic (http://workonomic.cc) time-tracker.

State
-----

The very crude initial version. If you are a SublimeText user, you are encourage to improve it. It's very simple code.

Things to do next:
------------------

- figure our where the api-token should be stored (so it's not in the code), what are the conventions
- can we display the response somewhere better than in a messagebox?
- can we make the websocket client so the communication will be 2-directional?

Install
-------

Clone this repo to your Packages directory.

Enter your APITOKEN in Workonomic/plugin_workonomic.py

Use via python shell
--------------------

    window.run_command("workonomic", {"message": "list projs"})

Add to Command Panel
--------------------

Add this line to JSON (and take care of the commas) in Packages/Default/Default.sublime-commands

    { "caption": "Workonomic", "command": "workonomic" }

Use via Command Panel
---------------------

Ctrl+Shift+p  start typing "workonomic" and select the option. The prompt will appear below where you enter your message.

Examples
--------

    show my projs

    create project abc

    started working on abc 20 mins ago

    note: i've fixed the bug 100

    stopped at 1700
    

For more info look at chat examples on: http://workonomic.cc/help-main-en.html


License
-------

GNU GPL v2
