# The Wedding Shop Rover Problem

## Design decisions

1. Disallow rover from leaving the positive x,y grid defined by (0,0) and (x_max, y_max) where {x_max, y_max} >= 0
2. It is not an error if the rover hits one of these invisible walls, just like a computer game nothing happens and
the rover stays where it is if it tries to go through a "wall".
2. Ignore multiple rovers crossing over each other to keep problem simple.

## How to run

Project can be run stand alone (it has no external dependencies), but I built it using Docker and docker-compose.
Running the example inputs can be done as follows:

`docker-compose run rover python -m rover`


## Unit tests

`docker-compose up` will run the unit tests.

Alternatively you can specify the command in full as 
`docker-compose run rover python -m unittest`
