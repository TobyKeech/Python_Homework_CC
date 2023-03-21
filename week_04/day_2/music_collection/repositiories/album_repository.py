from db.run_sql import run_sql
from models.album import Album
import repositiories.artist_repository as artist_repository


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select ( row ['artist_id'])
        # create a new Task object
        new_album = Album(row['title'],
                     row['genre'], 
                     artist, 
                     row ['id']
                     )
        # append to the list
        albums.append(new_album)

    return albums

# delete_all
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# # delete(id)
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# # save(task)
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id)\
            VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0] ['id']
    album.id = id
    return album

# # select(id)
def select(id):
    task = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

#     if len(results) > 0:
#         selected_task = results[0]
#         user = user_repository.select ( selected_task ['user_id'] )
#         task = Task(selected_task['description'],
#                     user,
#                     selected_task['duration'],
#                     selected_task['completed'],
#                     selected_task['id']
#                     )
#     return task

# # update(task)
# def update(task):
#     sql = """UPDATE tasks 
#             SET (description, user_id, duration, completed) 
#             = (%s,%s,%s,%s) 
#             WHERE id = %s """
#     values = [task.description, task.user.id, task.duration, task.completed,
#                task.id]
#     run_sql(sql,values)


# def tasks_for_user(user):
#     sql = "SELECT * FROM tasks WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql,values)

#     user_tasks = []
#     for row in results:
#         task = Task(
#                     row['description'],
#                      user, 
#                      row['duration'], 
#                      row['completed'], 
#                      row['id']
#                     )
        
#         user_tasks.append(task)

#     return user_tasks