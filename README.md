# RESTful Back-end Microservices and APIs for a Server-side Wordle Game

## Group Members:

   Marco Andrade

   Javier Diaz

   Quauhtli Garcia-Brindis

   Dylan Ngo

## Run and test the services:

1. Go to the /api directory:

    ```
    cd api
    ```

2. Initialize the databases:

    ```
    ./bin/init.sh
    ```

3. Start the services:

    ```
    foreman start
    ```

4. Test the services using curl, HTTPie, or automatic docs
    
    * Use the following links with curl and HTTPie :

    `http://localhost:5000/validate?guess={your_guess}` for "Validate Guess" service

    e.g. `http://localhost:5000/validate?guess=apple`

    and

    `http://localhost:5100/games/{game_id}?guess={valid_guess}` for "Check Guess against Answer" service

    e.g. `http://localhost:5100/games/244?guess=apple`



    * Automatic docs:

    `http://localhost:5000/docs` for "Validate Guess" service 

    and 

    `http://localhost:5100/docs` for "Check Guess against Answer" service