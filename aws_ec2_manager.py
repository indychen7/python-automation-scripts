import boto3

# ✅ Replace with your AWS EC2 instance ID
INSTANCE_ID = "i-006fe54a13c5da7c9"

# ✅ Create EC2 client
ec2 = boto3.client("ec2")

def start_instance():
    try:
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        print(f"✅ EC2 instance {INSTANCE_ID} is starting...")
    except Exception as e:
        print(f"❌ ERROR: {e}")

def stop_instance():
    try:
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        print(f"✅ EC2 instance {INSTANCE_ID} is stopping...")
    except Exception as e:
        print(f"❌ ERROR: {e}")

def check_instance_status():
    try:
        response = ec2.describe_instance_status(InstanceIds=[INSTANCE_ID])
        status = response["InstanceStatuses"]
        if status:
            print(f"🔹 EC2 instance {INSTANCE_ID} is currently: {status[0]['InstanceState']['Name']}")
        else:
            print(f"🔹 EC2 instance {INSTANCE_ID} is currently stopped.")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    print("\nAWS EC2 Instance Manager")
    print("1️⃣ Start Instance")
    print("2️⃣ Stop Instance")
    print("3️⃣ Check Instance Status")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        start_instance()
    elif choice == "2":
        stop_instance()
    elif choice == "3":
        check_instance_status()
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
