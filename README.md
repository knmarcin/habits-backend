# habits-backend

## Purpose

The main purpose of this project is allowing user to:
- Create/Update/Delete "Habit"
- Complete/uncomplete a "Habit"

## Endpoints
```/habits``` ```GET``` ```POST```

```/habits/<int:pk>``` ```GET``` ```PUT``` ```DELETE```

```/count/<int:pk>``` ```POST``` with body ```{"habit":<pk>}``` 

## TO DO:
 
- ```{"habit":<pk>}``` -> ```{"habit":...,"date":...}``` so u can edit past items
- add login system, etc
- setup on heroku, allowing netlify app to connect