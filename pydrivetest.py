from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


file = drive.CreateFile({'title': 'example69.csv'})
file.SetContentFile('example69.csv')
file.Upload() # Upload file.
file.SetContentFile('example69.csv')
file.Upload() # Update content of the file.