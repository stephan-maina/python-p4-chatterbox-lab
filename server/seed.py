#!/usr/bin/env python3
from app import db
from models import TodoItem

# Create and add some initial tasks to the database
def seed_data():
    with db.app.app_context():
        db.create_all()

        task1 = TodoItem(text='Playing PS5', completed=False)
        task2 = TodoItem(text='Swimming', completed=False)
        task3 = TodoItem(text='Gym', completed=False)
        task4 = TodoItem(text='Nature walk', completed=False)
        task5 = TodoItem(text='Road trip with friends', completed=False)

        db.session.add(task1)
        db.session.add(task2)
        db.session.add(task3)
        db.session.add(task4)
        db.session.add(task5)

        db.session.commit()

