import unittest
import requests


class TestIMDBAPI(unittest.TestCase):
    """
    A test class for the IMDB auto-complete API.

    Attributes:
        api_key (str): The RapidAPI key for authentication.
        url (str): The URL for the IMDB auto-complete API.
        headers (dict): The headers containing the RapidAPI key and host information.
    """

    def setUp(self):
        """
        Set up necessary configurations before each test case.
        """
        self.api_key = "0d1e940104msh3106e6927b3e900p1efdf1jsne8ac278667d0"
        self.url = "https://imdb8.p.rapidapi.com/auto-complete"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
        }

    def test_imdb_api(self):
        """
        Test the IMDB auto-complete API by sending a request with query parameters.

        The API is tested with a sample query parameter 'game%20of%20thr'.
        The response status code, headers, and content are printed.
        Asserts are used to check the expected structure of the JSON response.

        Raises:
            AssertionError: If the HTTP status code is unexpected or the response data lacks the expected structure.
        """
        query_params = {"q": "game%20of%20thr"}

        response = requests.get(self.url, headers=self.headers, params=query_params)

        # Print the request details
        print(f"Request URL: {response.request.url}")
        print(f"Request Headers: {response.request.headers}")
        print(f"Request Params: {response.request.url.split('?')[1]}")

        # Print the response details
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.text}")

        # Assert HTTP status code
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")

        # Assert JSON response structure
        data = response.json()
        self.assertIn("d", data, "Expected key 'd' not found in the response data")
        self.assertTrue(data["d"], "No results found in the response")


if __name__ == '__main__':
    unittest.main()
