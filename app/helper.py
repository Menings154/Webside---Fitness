from app import db
from app.models import User
from flask_login import current_user

def test():
    print(User.query.all())
    print(current_user.id)
    print(current_user.datapoints.all())
    return transform_datapoints(datapoints=current_user.datapoints.all(), field='weight')

def transform_datapoints(datapoints, field): # wie macht man das genereller?
    """ Transform the datapoint list into x and y data for the plotting."""
    x = []
    y = []
    for i in datapoints:
        x.append(i.timestamp)
        y.append(i.weight)
    return x, y