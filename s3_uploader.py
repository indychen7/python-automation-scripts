import boto3
import os

# 🔹 NOTE: Ensure you have AWS credentials set up using `aws configure`

# ✅ Replace with your actual S3 bucket name
S3_BUCKET_NAME = "your-bucket-name"

def upload_to_s3(file_path):
    s3 = boto3.client("s3")

    if not os.path.exists(file_path):
        print("❌ ERROR: File not found.")
        return

    file_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, S3_BUCKET_NAME, file_name)
        print(f"✅ Successfully uploaded {file_name} to S3 bucket: {S3_BUCKET_NAME}")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to upload: ").strip()
    upload_to_s3(file_path)
