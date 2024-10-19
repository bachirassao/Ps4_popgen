import requests

def get_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    if response.status_code == 200:
        breeds = response.json()["message"]
        return breeds
    else:
        return None

def get_breed_image(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    if response.status_code == 200:
        image_url = response.json()["message"]
        return image_url
    else:
        return None

def main():
    breeds = get_breeds()
    if not breeds:
        print("Failed to retrieve breeds list.")
        return
    
    while True:
        user_input = input("Enter a dog breed (or type 'done' to exit): ").lower()
        
        if user_input == "done":
            break
        
        if user_input in breeds:
            image_url = get_breed_image(user_input)
            if image_url:
                print(f"Here is an image of a {user_input}: {image_url}")
            else:
                print("Failed to retrieve image. Try again!")
        else:
            print("Try again!")

if __name__ == "__main__":
    main()