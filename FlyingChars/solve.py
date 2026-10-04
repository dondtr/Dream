import requests

if __name__ == "__main__":
    url = "http://host3.dreamhack.games:21561"
    for i in range(20):
        r = requests.get(url+f"/static/images/{i}.png")
        open(f"{i}.png", "wb").write(r.content)
