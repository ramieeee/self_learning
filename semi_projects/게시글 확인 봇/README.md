This code is for checking website boards new uploads and send notify through Line Notify API.

Inside the code, TOKEN veriable should be filled with your own token at https://notify-bot.line.me/en/



To distribute, I have chose pyinstaller to be used so the user could just double click the exe file without installation of libs and python interpreter etc.



The process of the program is as below.

1. checks websites with bs4
2. saves new upload's number in .data file
3. compares .data file with the new upload's number to distinguish if the upload is fresh
4. send Line Notify if the upload is fresh
5. overwrites .data file with the new upload num

