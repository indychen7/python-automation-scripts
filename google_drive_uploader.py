from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# ✅ Authenticate and authorize Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Opens a browser for authentication
drive = GoogleDrive(gauth)

def upload_file(file_path):
    file_name = file_path.split("/")[-1]
    gfile = drive.CreateFile({"title": file_name})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"✅ File '{file_name}' uploaded successfully to Google Drive.")

if __name__ == "__main__":
    file_path = input("Enter the full path of the file to upload: ").strip()
    upload_file(file_path)
