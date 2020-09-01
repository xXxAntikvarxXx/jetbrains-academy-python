from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


BaseModel = declarative_base()


class TaskModel(BaseModel):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


engine = create_engine("sqlite:///todo.db?check_same_thread=False")
BaseModel.metadata.create_all(engine)

session = sessionmaker(bind=engine)()


def get_all_tasks():
    print("Today:")
    rows = session.query(TaskModel).all()
    if rows:
        for index, row in enumerate(rows, 1):
            print(f"{index}. {row.task}")
    else:
        print("Nothing to do!")


def add_task():
    print("Enter task")
    task = TaskModel(task=input())
    session.add(task)
    session.commit()
    print("The task has been added!")


menu = {
    "0": None,
    "1": get_all_tasks,
    "2": add_task
}
menu_msg = """1) Today's tasks
2) Add task
0) Exit"""

while True:
    print(menu_msg)
    action = menu.get(input())
    if action is not None:
        print()
        action()
        print()
    else:
        break

print("Bye!")
