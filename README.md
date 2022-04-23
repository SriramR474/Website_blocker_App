Do you ever need to block some social media websites because you think it wasting your time?

I have created a Website blocker GUI using Python Tkinter and SQLite. 

There are so many extensions in Chrome and other browsers to block websites but most of them are having limited access without paying a subscription. So I created a simple app to block and unblock websites.

Basically, it will re-route the Websites which you need to block to your localhost IP address. This will be done in the below hosts file.

hosts_path = "C:\Windows\System32\drivers\etc\hosts"

(note: incase after adding the desired websites in your blocklist, if it still not blocked then kindly delete your browser history and cache and then check it)

The app having these functionalities

Set Password -- mention your password in the space given for the password and then click the Set password button.

View all -- click this button when you need to see all the websites you have blocked till now.

Add Website -- Enter the web address and select a date till which you want to block this site. Then click Add website button.

Remove Website -- click view all. select the Website which you want to unblock from that list. Click Remove website. If you have set up a password already it will ask for that password before removing the website.

Refresh -- click the refresh button to unblock all the websites whose block dates have been expired.

Change Password -- Enter your old password in the (Password box) and your new password in the (New Password box). Then click Change password button.

Close -- close the app

(note: Since this app makes changes in the hosts file, it needs to Run as administrator all the time. 
       You need administrator privilege on your computer. If you need you can take a backup of hosts file which is in the hosts_path mentioned above before running this app.)
