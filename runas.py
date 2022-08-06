import ctypes
import subprocess
import os

'''
Coppy Script, app.txt, APP vào cùng 1 folder:
    - script: file chạy để cài đặt APP dưới quyền admin
    - app.txt: file chứa tên APP (vd: hotfix_ABC.exe), hotfix cần cài đặt
    - APP: tên app cần cài.

'''

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

if __name__ == '__main__':
    #print (ctypes.windll.shell32.IsUserAnAdmin())
    if is_admin():
        #print("u are admin and UAC is OFF")
        exit("U r Admin, just run APP directly")
    else:
        #print("u are not admin, or UAC is ON")
        # Replace as your own user/password
        username = "test"
        password = "Testing@123"
        credentials = "(New-Object System.Management.Automation.PSCredential -ArgumentList @('" + str(username) + "',(ConvertTo-SecureString -String '" + str(password) + "' -AsPlainText -Force)))"

        # Get current script directory path
        BasePath = os.path.dirname(os.path.realpath(__file__))
        try:
            f = open(BasePath + "\\app.txt", "r")
            file = f.readline()
            f.close()
            app = os.path.join(BasePath, file)
            print("APP name:" + file)
            print("Full path:" + app)
        except:
            exit("An exception occurred, check your File")

        ps_cmd = "Start-Process '" + str(app) +"' -Credential " + str(credentials)
        info = run(ps_cmd)
        if info.returncode != 0:
            print("An error occured: %s", info.stderr)
        else:
            print("Executed successfully!")