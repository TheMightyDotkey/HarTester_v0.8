import subprocess
import time

def git():
    """This module updates the local repo to match the remote one."""
    
    print('Update')
    time.sleep(2)
    localrepo = 'C:\\Users\\nwilczewski\\source\\repos\\TheMightyDotkey\\HarTester_v0.8'
    subprocess.run(["git", "fetch", "origin"], cwd = localrepo)
    subprocess.run(["git", "reset", "--hard", "origin/master"], cwd = localrepo)

def main():

    git()

if __name__ == '__main__':
    main()
