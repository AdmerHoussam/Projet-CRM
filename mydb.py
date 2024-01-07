import mysql.connector

try:
    # Connect to the MySQL server and set the authentication plugin to 'mysql_native_password'
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1234',
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object
    cursorObject = dataBase.cursor()

    # Modify the user authentication method to 'mysql_native_password'
    cursorObject.execute("ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY '1234'")
    dataBase.commit()

    # Create a database named 'CR'
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS CR")

    # Commit the changes
    dataBase.commit()

    print("Database 'CR' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursorObject' in locals():
        cursorObject.close()
    if 'dataBase' in locals() and dataBase.is_connected():
        dataBase.close()

