import requests
import os

GITHUB_USERNAME = "indychen7"  # ✅ Replace with your GitHub username

# 🔹 NOTE: Generate your GitHub Personal Access Token at:
# 🔹 https://github.com/settings/tokens
# 🔹 Select "Generate new token (classic)"
# 🔹 Set Expiration (90 days or No Expiration)
# 🔹 Enable these permissions:
#     ✅ repo (Full control of private repositories)
#     ✅ read:org (Read org details if needed)

# 🔹 Get the GitHub token securely from user input (FIXED: No more freezing)
GITHUB_TOKEN = input("Enter your GitHub Personal Access Token: ").strip()

# ✅ Check if token is empty and exit if missing
if not GITHUB_TOKEN:
    print("❌ ERROR: GitHub Token is missing! Please enter a valid token.")
    exit(1)

def clone_all_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        if not repos:
            print("ℹ️ No repositories found.")
            return

        os.makedirs("cloned_repos", exist_ok=True)  # Create a folder for repos

        for repo in repos:
            repo_name = repo["name"]
            clone_url = repo["clone_url"]
            print(f"🔄 Cloning {repo_name}...")
            os.system(f"git clone {clone_url} cloned_repos/{repo_name}")

        print("\n✅ All repositories cloned successfully!")

    else:
        print(f"❌ ERROR: Failed to fetch repositories. HTTP {response.status_code}")
        print("➡️ Check your token and permissions.")

if __name__ == "__main__":
    clone_all_repos()
