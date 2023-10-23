from filestack import Client

api_key = "api_key"

client = Client(api_key)

new_link = client.upload(filepath="weather.txt")

print(new_link.url)

# file = client.upload(
#     "https://res.cloudinary.com/demo/image/upload/c_scale,w_300/sample.jpg",
#     params={
#         "folder": "my-folder",
#         "filename": "my-filename",
#         "public_id": "my-public-id",
#         "transformation": [
#             {
#                 "width": 300,
#                 "height": 300,
#                 "crop": "scale"
#             }
#         ]
#     }
# )

