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
    
    * Use the following request URLs with curl or HTTPie :

        - "Validate Guess" service: 
            
            * To validate a guess: `http://localhost:5000/validate?guess={your_guess}`

            * To add a new/possible guess: `http://localhost:5000/add_guess?guess={new_word}`

            * To remove a bad guess: `http://localhost:5000/remove_guess?guess={bad_word}`
        

        - "Check Guess against Answer" service: 

            * To check a valid guess against the answer: `http://localhost:5100/check?game_id={game_id}&guess={valid_guess}`

            * To add a new/possible answer: `http://localhost:5100/add_answer?answer={new_answer}`
            
            * To update/change the answer of an existing game: `http://localhost:5100/change_answer?game_id={game_id}&new_answer={new_answer}`

    * Automatic docs:

        "Validate Guess" service: `http://localhost:5000/docs` 

        "Check Guess against Answer" service: `http://localhost:5100/docs`
