#!/usr/bin/python3
import subprocess
import os

def greenPrint(string):
    print(f"\033[92m{string}\033[0m")

veracrypt_volume = os.path.expanduser("~/blobs/test")
mount_directory = os.path.expanduser("~/mnt_backup/")
backup_paths = ["~/money.xls", "~/kmvault", "~/.bashrc", "~/.config"]
# backup_paths.append("~/drv")

if not os.path.exists(mount_directory):
    print(f'creating mount directory at {mount_directory}')
    os.makedirs(mount_directory)

veracrypt_mount_command = ["veracrypt", "-t", "-k", "", "--pim=0", "--protect-hidden=no", veracrypt_volume, mount_directory]
print("$", " ".join(veracrypt_mount_command))
subprocess.run(veracrypt_mount_command, check=True)
print(f"Mounted backup volume at {mount_directory}")

for path in backup_paths:
    expanded_path = os.path.expanduser(path)
    rsync_command = ["rsync", "-rp", "--del", "--info=progress2", expanded_path, mount_directory]
    print(f"Copying {path}...")
    subprocess.run(rsync_command, check=True)

subprocess.run(["veracrypt", "-d", mount_directory], check=True)
print(f"Unmounted backup vault at {mount_directory}")

greenPrint(f"Backup complete at {veracrypt_volume}")
