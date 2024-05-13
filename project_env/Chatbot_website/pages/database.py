import mysql.connector

def display_message(message):
    # Your Python function logic here
    return message

table_name = "task" # Change this to your table name
 
connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ppd_database"
    )

def connection_mysql():
    # Establishing connection to the database
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ppd_database"
    )
    if connection.is_connected():
        print("Connection successful")
        return connection
    else:
        print("Failed to connect to database")

    


def display_all_data():
    connection = connection_mysql()
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name} ORDER BY task_ID DESC"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
        # Displaying the fetched data
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found")
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
    finally:
        # Closing the cursor
        if 'cursor' in locals():
            cursor.close()


def fetch_tasks_by_status(status):
    connection = connection_mysql()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM task WHERE status = %s"
        cursor.execute(query, (status,))
        rows = cursor.fetchall()

        # Displaying the fetched data
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found")
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
    finally:
        # Closing the cursor
        if 'cursor' in locals():
            cursor.close()




def delete_task_by_id(id):
    if(id!=-1):
      connection = connection_mysql()
      try:
          cursor = connection.cursor()
          query = "DELETE FROM task WHERE task_ID = %s"
          cursor.execute(query, (id,))
          connection.commit()
          print("Task deleted successfully")
      except mysql.connector.Error as e:
          print(f"Error deleting task: {e}")
          connection.rollback()
      finally:
          # Closing the cursor
          if 'cursor' in locals():
              cursor.close()



def update_task_status_by_id(id):
    connection = connection_mysql()
    try:
            cursor = connection.cursor()
            # Fetching the current status of the task
            cursor.execute("SELECT status FROM task WHERE task_ID = %s", (id,))
            current_status = cursor.fetchone()[0]
            cursor.fetchall()  # Consume the unread result

            # Updating the status of the task
            cursor.execute("UPDATE task SET status = %s WHERE task_ID = %s", (1, id))
            connection.commit()
            print("Task status updated successfully")

    except mysql.connector.Error as e:
        print(f"Error updating task status: {e}")
        connection.rollback()
    finally:
        # Closing the cursor
        if 'cursor' in locals():
            cursor.close()


def addTask(sender,emailDate,task,date):
    connection = connection_mysql()
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {table_name} (sender_name,task, date, Email_Date) VALUES (%s,%s, %s, %s)"
        data = (sender,task, date,emailDate)
        cursor.execute(query, data)
        connection.commit()
        print('successful')
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
    finally:
        # Closing the cursor
        if 'cursor' in locals():
          cursor.close()
     



# Fetching tasks where status is 0 or 1
#  fetch_tasks_by_status(connection, 1)



# Deleting the task by ID
# delete_task_by_id(1)



# update task status by id
# update_task_status_by_id(11)

display_all_data()




















# Closing the connection
if connection.is_connected():
    connection.close()
    print("Connection closed")
