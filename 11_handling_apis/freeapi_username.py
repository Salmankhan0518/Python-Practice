import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Faild to fetch user data")
    
def get_a_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        joke = joke_data["content"]
        return joke
    else:
        raise Exception("Faild to fetch joke data")
    



def main():
    try:
        joke = get_a_random_joke()
        username, country = fetch_random_user_freeapi()
        print(f"Joke: {joke}")
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()
