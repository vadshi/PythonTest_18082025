tasks
=====

Project task tracking / todo list

Usage
-----

Here's a demo of how it works:

    $ tasks add a todo

    $ tasks add -o Brian another task

    $ tasks list
         ╷       ╷       ╷
      ID │ state │ owner │ summary
    ╺━━━━┿━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━╸
      1  │ todo  │       │ a todo
      2  │ todo  │ Brian │ another task
         ╵       ╵       ╵

    $ tasks update 1 -o Brian

    $ tasks finish 1

    $ tasks
      ID │ state │ owner │ summary
    ╺━━━━┿━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━╸
      1  │ done  │ Brian │ a todo
      2  │ todo  │ Brian │ another task
         ╵       ╵       ╵

    $ tasks delete 1

    $ tasks
      ID │ state │ owner │ summary
    ╺━━━━┿━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━╸
      2  │ todo  │ Brian │ another task
         ╵       ╵       ╵

    $ tasks --help
    Usage: tasks [OPTIONS] COMMAND [ARGS]...

      Tasks is a small command line task tracking application.

    Options:
      --help  Show this message and exit.

    Commands:
      add      Add a task to db.
      config   List the path to the Tasks db.
      count    Return number of tasks in db.
      delete   Remove task in db with given id.
      finish   Set a task state to 'done'.
      list     List tasks in db.
      start    Set a task state to 'in prog'.
      update   Modify a task in db with given id with new info.
      version  Return version of tasks application
