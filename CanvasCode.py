# Group ID - 45110000000082545

from CanvasKeys import *
import requests

def upload_file():
    fileName = 'test.txt'
    file = {'file': open(fileName, 'rb')}

    ## Get upload token
    info = requests.post(
        'https://canvas.instructure.com/api/v1/groups/45110000000082545/files?access_token=' + accessToken,
        data={'name': fileName, 'parent_folder_path': '/'})

    uploadURL = info.json()['upload_url']

    ## Upload the file to the upload URL
    requests.post(uploadURL, files=file)
    print("Done Uploading")



def download_file(fileName = "download.txt"):
    id_num = 0

    #Data For Things In Folder
    hold = requests.get('https://canvas.instructure.com/api/v1/groups/45110000000082545/files?access_token=' + accessToken)

    #Finds the Correct File
    for f in hold.json():
        if f["display_name"] == fileName:
            id_num = f["id"]

    #Gets Public and Makes Download
    info = requests.get('https://canvas.instructure.com/api/v1/files/' + str(id_num) + '/public_url?access_token=' + accessToken, allow_redirects=True)
    public = info.json()["public_url"]
    file = requests.get(public, allow_redirects=True)

    #Writes File
    open(fileName, 'wb').write(file.content)

    print("Done Downloading")
