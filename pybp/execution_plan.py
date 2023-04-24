import sqlite3
import os

class ExecutionPlan:
  """
  Class to represent an execution plan saved in a sqlite DB.
  """

  def __init__(self, options, actions):
    self.options = options
    self.actions = actions

  @staticmethod
  def _create_template_db(cursor):
    # Create options table
    cursor.execute("""
    CREATE TABLE options (
      key TEXT, 
      value TEXT
    )
    """)

    # Create actions table
    cursor.execute("""
      CREATE TABLE actions (
        command TEXT,
        path TEXT,
        status TEXT CHECK(status IN ('PLANNED', 'RUNNING', 'FINISHED'))
      )
    """)

  @staticmethod
  def serialize(plan, path):
    if os.path.exists(path):
      print("Warning! File already exists and will be overwritten.")
      os.remove(path)

    con = sqlite3.connect(path)
    cursor = con.cursor()

    ExecutionPlan._create_template_db(cursor)

    # insert options map into table
    data = [(k, v) for k, v in plan.options.items()]
    cursor.executemany("INSERT INTO options VALUES (?, ?)", data)

    # insert actions list into table
    data = [(a.command, a.path, a.status) for a in plan.actions]
    cursor.executemany("INSERT INTO actions VALUES (?, ?, ?)", data)

    con.commit()
    con.close()

  @staticmethod
  def parse(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()

    # parse options table
    res = cursor.execute("SELECT key, value FROM options")
    raise NotImplementedError("Continue implementing pls")
