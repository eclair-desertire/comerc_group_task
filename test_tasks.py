import pandas as pd

data={
    'Name':['Alex','Justin','Set','Carlos','Gareth','John','Bob'],
    'Surname':['Smur','Forman','Carey','Carey','Chapman','James','James'],
    'Age':[21,25,35,40,19,27,25],
    'Job':['Python Developer','Java Developer','Project Manager','Enterprise architect','Python Developer','IOS Developer','Python Developer'],
    'Datetime':['2022-01-01T09:45:12','2022-01-01T11:50:25','2022-01-01T10:00:45','2022-01-01T09:07:36','2022-01-01T11:54:10','2022-01-01T09:56:40','2022-01-01T09:52:45']
    }

df=pd.DataFrame(data)

print(df)