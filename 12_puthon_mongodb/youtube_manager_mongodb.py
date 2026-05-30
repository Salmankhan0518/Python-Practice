from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.4anmxby.mongodb.net/")
# not a good idea to include id and password in code file

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        


if __name__ == "__main__":
    main()