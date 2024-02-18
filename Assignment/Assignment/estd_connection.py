def estd_connection():          # A function that we create, so we can use it later
    import psycopg2             # A built-in function to communicate with postgres
    conn = psycopg2.connect(    # A built-in method/function of python fot psycopg2
        database = "Crud_student_table",       # Name of the database we create
        user = "postgres",                  # Name of the user by default who has all the authority
        password = "4321",                  # The password that you set up
        host = "127.0.0.1",                 # For most devices, this is the host
        port = "5432"                       # default port for postgresql, host is a house, port is a room
    )
    conn.autocommit = True       # It sets the action we prefer such as update, add, etc to automatically commit without
                                 # us having to commit each time. Similar to git commit but setting it to automatically commit.
    print("Connection established successfully !!")
    cursor = conn.cursor()       # We create an object named cursor and then call the variable which has the connection
    return cursor                # with postgresql stored in it. The method is <variable_storing_connection>.cursor().
                                 # The .cursor() is like a mediator which communicates with database for us.
if __name__ == "__main__":
    estd_connection()