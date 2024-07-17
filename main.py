import instaloader
from colorama import Fore, init
import pyfiglet
import time

init(autoreset=True)

def logo():
    proj_name = pyfiglet.figlet_format("Insta-scrapper", font='rev')
    print(Fore.GREEN + proj_name)
    print(Fore.WHITE + '-' * 80)
    print(Fore.WHITE + f'[📩] Developed By @Eyad156 \n[📢] Youtube Channel: https://www.youtube.com/@Driply1704')
    print(Fore.WHITE + '-' * 80)
def main():
    logo()
    user_name = input(Fore.CYAN + "Enter Username -> ")

    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, user_name)
        loader.download_profile(user_name, profile_pic_only=False)
        print(Fore.GREEN + "Profile and posts downloaded successfully.")
        
        print(Fore.WHITE + '-' * 40 + 'Instagram Scrapper' + '-' * 40)
        print(Fore.WHITE + f"Username: " + Fore.MAGENTA + f"{profile.username}")
        print(Fore.WHITE + f"Full Name: " + Fore.MAGENTA + f"{profile.full_name}")
        print(Fore.WHITE + f"Followers: " + Fore.MAGENTA + f"{profile.followers}")
        print(Fore.WHITE + f"Following: " + Fore.MAGENTA + f"{profile.followees}")
        print(Fore.WHITE + f"Number of Posts: " + Fore.MAGENTA + f"{profile.mediacount}")
        print(Fore.WHITE + '-' * 40 + 'Instagram Scrapper' + '-' * 40)
        
        time.sleep(5)
    except instaloader.exceptions.ProfileNotExistsException:
        print(Fore.RED + "The user not found.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
