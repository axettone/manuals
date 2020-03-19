# How to mount a Samba partition in macOS from the command line

Mount:

`mount_smbfs //user@server_ip/folder /mnt_point`

Unmount:

`umount /mnt_point`

You can do this without root permission, creating the mounpoint anywhere in your HOME folder.

> Source: https://apple.stackexchange.com/questions/697/how-can-i-mount-an-smb-share-from-the-command-line

