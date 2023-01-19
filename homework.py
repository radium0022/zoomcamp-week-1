# question 1 (in terminal)

# docker build --help

# question 2 (in terminal) 

# docker run -it --entrypoint=bash --name my_container python:3.9
# pip list 

# SQL questions done in pg admin

question_3 = """
SELECT
	COUNT(*) AS counter
FROM green_taxi_data
WHERE DATE_TRUNC('day', lpep_pickup_datetime) = '2019-01-15'
	AND DATE_TRUNC('day', lpep_dropoff_datetime) = '2019-01-15'
"""

question_4 = """
SELECT
	*
FROM green_taxi_data
WHERE trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_data)
"""

question_5 = """
SELECT
	passenger_count,
	COUNT(*)
FROM green_taxi_data
WHERE DATE_TRUNC('day', lpep_pickup_datetime) = '2019-01-01'
	AND DATE_TRUNC('day', lpep_dropoff_datetime) = '2019-01-01'
	AND passenger_count IN (2,3)
GROUP BY 
	1
"""

question_6 = """SELECT
	zx."Zone",
	COUNT(*) AS counter
FROM green_taxi_data g
LEFT JOIN zones z ON g."PULocationID" = z."LocationID"
LEFT JOIN zones zx ON g."DOLocationID" = zx."LocationID"
WHERE z."Zone" = 'Astoria'
GROUP BY 1
ORDER BY 2 DESC
"""
