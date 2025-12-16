import requests


class Brewery:
    def __init__(self, b_id: str, name: str, city: str, state: str):
        self.id = b_id
        self.name = name
        self.city = city
        self.state = state

    def __str__(self):
        return f"Browar: {self.name}, Miasto: {self.city}, Stan: {self.state}"


def fetch_breweries():
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        breweries = []
        for item in data:
            brewery = Brewery(
                b_id=item.get("id"),
                name=item.get("name"),
                city=item.get("city"),
                state=item.get("state_province")
            )
            breweries.append(brewery)

        for b in breweries:
            print(b)

    except requests.exceptions.RequestException as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    fetch_breweries()