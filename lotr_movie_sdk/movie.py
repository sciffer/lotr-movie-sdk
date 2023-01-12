"""Lord Of The Rings Movie SDK, based on the api exposed by: https://the-one-api.dev/."""
import requests


class Movie:
    def __init__(self, key: str, url: str = "https://the-one-api.dev/v2"):
        """Initialization of the movie SDK that sets the api key & URL of the endpoint.

        Args:
            key (str): String representing the api key.
            URL (str): Optional parameter - a string representing the base URL for the API endpoint
                        (defaults to https://the-one-api.dev/v2).

        Returns:
            NULL

        Examples:
            .. code:: python

                >>> hello("Roman")
                'Hello Roman!'
        """
        self.headers = {"Accept": "application/json", "Authorization": f"Bearer {key}"}
        self.base_url = url.rstrip("/")
        return

    def _http_get(self, path: str):
        """Make http get call to the endpoint with the baseline path + the path parameter.
        Will return the response or raise an exception if it failed.

        Returns:
            content (json): the content of the response

        Examples:
            .. code:: python
                >>> self._http_get("movie")
                {response-content...}
        """
        try:
            response = requests.get(f"{self.base_url}/{path.lstrip('/')}", headers=self.headers)
            response.raise_for_status()
            return response.json()["docs"]
        except Exception as e:
            print(f"Failed to query {self.base_url}/{path.lstrip('/')} with error: {e}")
            raise (e)

    def list(self):
        """Get list of all the movies with their metadata.

        Returns:
            json: list of movies with their metadata

        Examples:
            .. code:: python

                >>> m.list()
                '[{"_id":"45t5t45t454",'name':'movie1',....},...]'
        """
        return self._http_get("movie")

    def get(self, id: str):
        """Get the metadata of a movie with the specified id.

        Args:
            id (str): String representing the movie id.

        Returns:
            json: movie details

        Examples:
            .. code:: python

                >>> m.get("345t453t3")
                '{"_id":"345t453t3","name":"movie1",....}'
        """
        return self._http_get(f"movie/{id}")

    def quotes(self, id: str):
        """List all the quotes of a movie with the specified id.

        Args:
            id (str): String representing the movie id.

        Returns:
            json: list of movie quotes

        Examples:
            .. code:: python

                >>> m.quotes("345t453t3")
                '[{"_id":"34r43r43r","quote":"Hello world"},....]'
        """
        return self._http_get(f"movie/{id}/quote")
