print("Hello, World!")
print("I am learning AI!!")
import requests 
response = requests.get("https://api.github.com")
print(response.status_code) #should return 200 if successful.
