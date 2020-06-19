# Street-Weather
Weather App in Python 

Requirements : 

- Have Python3 installed and updated
- Have Tkinter installed (pip install tkinter)
- Have Pillow installed (pip install Pillow)
- Have MatPlotLib installed (pip install MatPlotLib)
- Have MariaDB installed (pip install mysql.connector)

In the folder Model, you can find a .sql file.
In a terminal (Linux command) run this to import database :

To access to MySQL console
<code>
  mysql -u root -p (just type mysql if you're using root user)
</code>
mysql> CREATE DATABASE streetweather; -> To create the database

Go back to terminal by pressing CTRL+D then type :
<code>
  mysql -u username -p streetweather < streetweather.sql
</code>
