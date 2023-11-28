# IMDB API TESTS :


This project contains multiple test classes for testing various IMDB APIs using the RapidAPI platform. The tests utilize the `unittest` framework and the `requests` library.

## TestIMDBFilmographyAPI

### Overview

This test class is designed to test the IMDB get all filmography API. It verifies that the API can successfully retrieve filmography information for a specific actor or actress.

### Test Case

- **test_get_all_filmography:**
  - **Description:** Test the IMDB get all filmography API for a specific actor or actress.
  - **Query Parameter:** 'nconst': 'nm0001667' (Sample actor ID)
  - **Assertions:**
    - Verify the HTTP status code is 200.
    - Verify the response data is a dictionary.

## TestIMDBAPI

### Overview

This test class is designed to test the IMDB auto-complete API. It checks whether the auto-complete feature works as expected for IMDB search queries.

### Test Case

- **test_imdb_api:**
  - **Description:** Test the IMDB auto-complete API by sending a request with query parameters.
  - **Query Parameter:** 'q': 'game%20of%20thr' (Sample search query)
  - **Assertions:**
    - Verify the HTTP status code is 200.
    - Verify the response data contains the key 'd'.
    - Verify that results are present in the response.

## TestIMDBActorsAPI

### Overview

This test class is designed to test the IMDB actors list API, specifically for actors born today.

### Test Case

- **test_actors_born_today:**
  - **Description:** Test the IMDB actors list API for actors born today.
  - **Query Parameters:** 'month': '7', 'day': '27' (Assuming the test is run on the 27th of July)
  - **Assertions:**
    - Verify the HTTP status code is 200.
    - Verify the response data is a list of actors.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/imdb-api-tests.git
    cd imdb-api-tests
    ```

2. Install dependencies:

    ```bash
    pip install requests
    ```

3. Run the tests:

    ```bash
    python test_imdb_api.py
    ```

    ```bash
    python test_imdb_filmography_api.py
    ```

    ```bash
    python test_imdb_actors_api.py
    ```

## Notes

- Make sure to replace the API key in the test classes with your RapidAPI key.

- Ensure an internet connection is available when running the tests.

- Customize the query parameters in the test cases based on your testing needs.

---

