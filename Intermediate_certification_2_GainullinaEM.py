import psycopg2
from tabulate import tabulate

# Database configuration
db_host= 'localhost'
db_port= 5432
db_name= 'demo'
db_user= 'postgres'
db_password= 'postgres'


if __name__ == '__main__':
    try:
        # Connect to the database
        connection = psycopg2.connect(
                    host=db_host,
                    port=db_port,
                    database=db_name,
                    user=db_user,
                    password=db_password,
                    options="-c search_path=bookings"
                    )

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM delayed_flights_v")
        result = cursor.fetchall()
        #print(result)
        print(tabulate(result, headers=['flight_no', 'departure_airport', 'arrival_airport', 'aircraft_code', 'scheduled_departure'], tablefmt='psql'))

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
