import pyodbc
from django.shortcuts import render
from datetime import datetime
import not_for_git

today = datetime.now().strftime("%H:%M")
server = not_for_git.db_server
database = not_for_git.db_name
username = not_for_git.db_user
password = not_for_git.db_pw
driver = '{ODBC Driver 17 for SQL Server}'  # Driver you need to connect to the database


def main(request):
    try:
        cnn = pyodbc.connect(
            'DRIVER=' + driver + ';PORT=port;SERVER=' + server + ';PORT=1443;DATABASE=' + database +
            ';UID=' + username + ';PWD=' + password)
        cursor = cnn.cursor()
        sql = list(cursor.execute("dbo.workshop_screen"))
        cnn.close()
        res = {"main": sql, }
        return render(request, "index.html", context=res)
    except Exception as err:
        with open("error.log", "a") as file_with_error:
            file_with_error.write(str(err) + "\n")
        main(request)
    # for row in sql:
    #     print(row, len(row))
