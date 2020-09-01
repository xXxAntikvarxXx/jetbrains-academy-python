from datetime import datetime, timedelta

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']

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
    print("All tasks:")
    tasks = session.query(TaskModel).order_by(TaskModel.deadline).all()
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.task}. "
                  f"{task.deadline.day} "
                  f"{task.deadline.strftime('%b')}")
    else:
        print("Nothing to do!")


def get_week_tasks():
    today = datetime.today().date()
    for days in range(7):
        deadline = today + timedelta(days=days)
        print(
            WEEKDAYS[deadline.weekday()],
            deadline.day,
            deadline.strftime(f"%b:")
        )
        tasks = session.query(TaskModel).filter(
            TaskModel.deadline == deadline
        ).all()
        if tasks:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task.task}")
        else:
            print("Nothing to do!")
        if days != 6:
            print()


def get_today_tasks():
    today = datetime.today().date()
    print(today.strftime(f"Today %d %b:"))
    tasks = session.query(TaskModel).filter(
        TaskModel.deadline == today
    ).all()
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.task}")
    else:
        print("Nothing to do!")


def add_task():
    print("Enter task")
    task = input()
    print("Enter deadline")
    deadline = datetime.strptime(input(), "%Y-%m-%d").date()
    task = TaskModel(task=task, deadline=deadline)
    session.add(task)
    session.commit()
    print("The task has been added!")


def get_missed_tasks():
    print("Missed tasks:")
    tasks = session.query(TaskModel).filter(
        TaskModel.deadline < datetime.today().date()
    ).order_by(TaskModel.deadline).all()
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.task}. "
                  f"{task.deadline.day} "
                  f"{task.deadline.strftime('%b')}")
    else:
        print("Nothing is missed!")


def delete_tasks():
    print("Choose the number of the task you want to delete:")
    tasks = session.query(TaskModel).order_by(TaskModel.deadline).all()
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.task}. "
                  f"{task.deadline.day} "
                  f"{task.deadline.strftime('%b')}")
        session.delete(tasks[int(input()) - 1])
        session.commit()
        print("The task has been deleted!")
    else:
        print("Nothing to delete!")


menu = {
    "0": None,
    "1": get_today_tasks,
    "2": get_week_tasks,
    "3": get_all_tasks,
    "4": get_missed_tasks,
    "5": add_task,
    "6": delete_tasks,
}
menu_msg = """1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
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
