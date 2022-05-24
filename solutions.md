Intro:

    Fearless is creating a prototype for an application called Project Purple Cow. As a Software Engineer on the project team, I have been asked to create a series of proofs of concept that supports the customer's public health and social justice initiatives. 

Technologies:

    I started the process by creating a public repository using Github at https://github.com/Celis1/PurpleCow. This allows the development team to have access to an opensource version control software while simultaniously managing all changes regardeing each teammembers code base. Since there were no restriction on the technolgies I was allowed to use, python was used as the backend because this allows the most flexablilty while prototyping and has a quick time to development. As the project prototype is a webapp, I used the flask module which allows the use of web programming languages like html, css, and javascript. Docker is also a key component to this software as it creates a constant testing envoirnment accross the developments teams local machines, which helps to reduce bugs. Just like any other docker container, in order to create a docker container you must create a docker image from the provided docker file. Then its as simple as running the command '$docker run -d -p 3000:5000 docker_container_name'. Because this is a prototype software, it's important to include a bash script that enables the docker image and container to be created and run. On first startup, use '$sh run_docker_app.sh' which will create the image and start the web app on the recommender port. As more requirments will likely grow in the future, this will allow the addition of any configurations to the software on startup. 

Functionality: 

    The most important requirement for this project was that ID and Name are key-value pairs. My assumption was that each of these items were meant to be their own dictionary. The database for the application is being held in memeory on server startup. To view the entire database navigate to the url endpoint /all_items or call a get request to this endpoint without passing any params. Currently the collection of items is a list of dictionary objects, this allows for quick storage and creation of the items object. In order to modify the database from the api call the /items endpoint and pass in three parameters. The first param is action which can be get, post, delete, or delete_all. This allows for easy interaction with the server side database. ID is a numerical value and Name is a case sensity name that is associated with an ID. When adding to the database, all duplicates will be ignored as well as any posts that are missing either an ID or a Name. Please view the file access_api.py this contains get and post request wich help demonstrate the api's functionality. 

Improvments:

    - add branches for team members on github
    -change storage theme to { 107 : {'name':'mark} , 108 : {'name':'joe}} where each number is the id (my assumption was id and name had to be keys)
    -add better type checking for incoming request also making the id and names standerd definition format(ex: id could be an int id: 17734 or id could be a hash id: f8gn90pq2)
    -names should either be all lowercase or capitalize the first character
    -sorting method based on id number or alphabetical sorting for name
    -add a real saving database option 
    -all print statements should be log statements that also save the interactions with users
    -authentication so people outside the system don't have access to this api
