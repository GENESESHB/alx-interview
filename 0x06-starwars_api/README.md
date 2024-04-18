![api](https://th.bing.com/th/id/OIP.LyZElmzYJHV9_DCgiR4HGQHaEG?rs=1&pid=ImgDetMain)
# 0x06. Star Wars API
## Task
    Write a script that prints all characters of a Star Wars movie:

    The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
    Display one character name per line in the same order as the “characters” list in the /films/ endpoint
    You must use the Star wars API
    You must use the request module

    GitHub repository: alx-interview
    Directory: 0x06-starwars_api
    File: 0-starwars_characters.js

## Example
    blezyukatu@ubuntu:~/0x06$ ./0-starwars_characters.js 3
    Luke Skywalker
    C-3PO
    R2-D2
    Darth Vader
    Leia Organa
    Obi-Wan Kenobi
    Chewbacca
    Han Solo
    Jabba Desilijic Tiure
    Wedge Antilles
    Yoda
    Palpatine
    Boba Fett
    Lando Calrissian
    Ackbar
    Mon Mothma
    Arvel Crynyd
    Wicket Systri Warrick
    Nien Nunb
    Bib Fortuna
    alexa@ubuntu:~/0x06$ 

## Resources
- [swapi-api.hbtn.io](https://swapi-api.hbtn.io/)    
- [request module](https://github.com/request/request)  


### 1. Importing Libraries and Setting Constants
```javascript
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';
```
Explanation:
- We import the `request` library, which allows us to make HTTP requests.
- We define a constant `API_URL` which stores the base URL for the Star Wars API (SWAPI).

### 2. Defining the getRequest Function
```javascript
// Function to make an HTTP GET request
function getRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
```
Explanation:
- This function `getRequest` is used to make HTTP GET requests.
- It returns a Promise that resolves with the parsed JSON response if the request is successful.
- If the request fails or the response status code is not 200, it rejects the Promise with an error.

### 3. Defining the getFilmCharacters Function
```javascript
// Function to fetch characters from a film
async function getFilmCharacters(filmId) {
  try {
    const response = await getRequest(`${API_URL}/films/${filmId}/`);
    const charactersURL = response.characters;
    const characterNames = await Promise.all(
      charactersURL.map(async url => {
        const character = await getRequest(url);
        return character.name;
      })
    );
    return characterNames.join('\n');
  } catch (error) {
    throw new Error(`Error fetching characters: ${error.message}`);
  }
}
```
Explanation:
- This function `getFilmCharacters` is responsible for fetching characters from a given film ID.
- It first makes a GET request to SWAPI to get information about the specified film.
- Then, it extracts the character URLs from the response and makes parallel requests to fetch information about each character.
- Finally, it returns a string containing the names of all characters joined by a newline character.
- If any error occurs during the process, it throws an error with an informative message.

### 4. Defining the main Function
```javascript
async function main() {
  try {
    // Check if a film ID is provided as a command line argument
    if (process.argv.length <= 2) {
      console.error('Please provide a film ID');
      process.exit(1);
    }

    const filmId = process.argv[2];
    const characters = await getFilmCharacters(filmId);
    console.log(characters);
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}
```
Explanation:
- The `main` function serves as the entry point of the script.
- It checks if a film ID is provided as a command line argument. If not, it prints an error message and exits.
- If a film ID is provided, it calls the `getFilmCharacters` function to fetch and print the characters of the specified film.
- Any errors that occur during the execution are caught, and an error message is printed before exiting the script.

### 5. Calling the main Function
```javascript
// Entry point of the script
main();
```
Explanation:
- This line calls the `main` function to start the execution of the script. It's the entry point of the program.
