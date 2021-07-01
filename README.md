# Password-strength-checker
Summary:

A python file which checks your password if it has been breached or safe to use securely without trusting website's https connection and also send only 5 hexadecimal characters of hash to server to make sure server is not compromised and get checks done on your own personal computer without trusting any other device.

INPUT:

python passcheck.py Dragon password qwerty Sample123 Andrew#6218


OUTPUT:

Dragon was found 18384 times...you should probably change your password

password was found 3861493 times...you should probably change your password

qwerty was found 3993346 times...you should probably change your password

Sample123 was found 53904 times...you should probably change your password

Andrew#6218 was NOT found. Carry on!
Done!

(*) NOTE : Inputs must be given in the command line and in the directory where your python file is present.Based on your python version you can use python/python3

In Detail:

Step 1: User runs passcheck.py along with his desired number of passwords which can be given as a input separated by spaces between them and then click enter to run the program in the command line.

Step 2: Each password is sent to pwned api check function and are checked if they are found in any security breaches.

Step 3: In pwned api check function we calculate hash using sha1 algorithm and generates hexadecimal characters.

Step 4: Though hash can be sent to pwned server via secure https connection we only send first 5 hexadecimal characters to pwned server. We do not send all the characters to server at a time instead only 5 because we take initial precaution incase if server is compromised, and your password can be decrypted by higher performance hardware systems which we don't want to take chance of. 

Step 5: By using request-api-data function python code what it does is after sending each password's first 5 hexadecimal hash it retrieves a set of hashes from the server which contains the first 5 characters same as the hash sent to it.  

Step 6: To get-passwords-leakcount-function we give 2 parameters as input one parameter which has response having all hashes that start with same 5 characters of your passwords hash and as second parameter your tail of hash which you divided separating first 5 digits from the rest of characters.

Step 7: In the above function we take one hash at a time and separate first 5 characters from rest of characters and check with our tail of characters to see if they match.All hashes are checked with this procedure and if they match we retrieve the count of the password number of times it has been breached and print it out.

Step 8: This way we check if all the passwords that given as input are breached or safe to use.

Step 9: In case you are still more cautious if there can be some history saved in your command line which contain your passwords. Then you can make a text file containing your passwords and make python read your files to avoid history problem.

Finally! That's it we have created a python file which checks your password securely without trusting websites https connection and also send only 5 characters of hash to server to make sure server is not compromised and get checks done on your own personal computer without trusting any other device.
