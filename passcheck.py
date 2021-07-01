import requests
import hashlib
import sys

def request_api_data(query_char):# First 5 characters of password is sent to the server
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)# response of the server recorded when request is sent
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_passwords_leaks_count(hashes, hash_to_check):# Hashs which we recieved from response and tail of our hash is sent as input
    hashes = (line.split(':') for line in hashes.text.splitlines()) # We converted into tuple which has hashs and the count of the hashs divided 1 into 2
    for h,count in hashes:# Take each hash and its count and check with the tail of your hash if something maches if mached we take no. of times the password has been breached or pwned or hacked.
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # Generates all captial hexadecimal characters of fixed length of password.
    first5_char, tail = sha1password[:5], sha1password[5:] # Division of hexadecimal characters
    response = request_api_data(first5_char) # First 5 characters are only being sent to check if hash present in the database has this 5 characters of hash in them .these are sent o request_api_data function
#    print(response)
    return get_passwords_leaks_count(response, tail) # Now we take the response which contains hashes and count of them breached and check with the tail of the hash of your password.

def main(args):
    for password in args:
        count = pwned_api_check(password) #Passwords that are given in input are sent one by one to pwned_api_check function
        if count:
            print(f'{password} was found {count} times...you should probably change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'Done!'

if __name__ == '__main__': # If this file is imported then it deosnot run
  sys.exit(main(sys.argv[1:]) ) # We input python filename and then passwords which you wan to check the strength atmost 1.If something goes wrong we make sure to come back to cmd.line by using sys.exit.
