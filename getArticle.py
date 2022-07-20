import requests
import time

for i in range(350):

    print(f"getting{i+1}")
    site_data = requests.get(f"https://8212.teacup.com/kanagawa894/bbs?page={i+1}&")
    with open(f"html/page{i+1}.html", "w") as f:
        f.write(site_data.text)
    time.sleep(3)
