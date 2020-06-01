import os
import re
import requests

jobs = {
    "82515105f43940ec8136": "IBN Zettel",
    "ff5f3ac42c724ae4940c": "IBN Folien",
    "e1eaccb7bc614b338681": "IBN Videos",
}

url_list = "https://heibox.uni-heidelberg.de/api/v2.1/share-links/{}/dirents"
url_file = "https://heibox.uni-heidelberg.de/d/{}/files/?p={}&dl=1"

for job, folder in jobs.items():
    os.makedirs(folder, exist_ok=True)
    r = requests.get(url_list.format(job))
    r.raise_for_status()
    items = r.json()["dirent_list"]
    for item in items:
        if item["is_dir"]:
            msg = "is_dir"
            raise NotImplementedError(msg)
        if item["file_path"] != "/" + item["file_name"]:
            msg = "file_path"
            raise NotImplementedError(msg)
        filename = item["file_name"]
        filename = re.sub(r"[^A-Za-z0-9._-]", "_", filename)
        filename = os.path.join(folder, filename)
        if os.path.isfile(filename):
            if os.path.getsize(filename) == item["size"]:
                print("Skipping {}".format(filename))
                continue
        status = "\r{{: >3.0f}}% Downloading {}".format(filename)
        print(status.format(0), end="")
        item["file_path"] = requests.utils.quote(item["file_path"])
        r = requests.get(url_file.format(job, item["file_path"]), stream=True)
        r.raise_for_status()
        with open(filename, "wb") as fh:
            progress = 0
            bufsize = 1 * 10 ** 6  # 1 MB
            for buf in r.iter_content(bufsize):
                fh.write(buf)
                progress += len(buf)
                percent = progress / item["size"] * 100
                print(status.format(percent), end="")
            print()
            if progress != item["size"]:
                msg = "size mismatch"
                raise RuntimeError(msg)
