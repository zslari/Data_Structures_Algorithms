# Demos the Message Class from emailMessage.py

from emailMessage import Message

# Creating sample message 1
wishList = Message("Zafir Lari", "JohnnyAppleSeed@gmail.com")
wishList.append("When movie theaters reopen")
wishList.append("we should watch the following movies: ")
wishList.append("James Bond")
wishList.append("Tenet")
wishList.append("Dune")

# Display the contents of sample message 1
print(wishList.to_string())

# Entering a sender greater than 50 characters defaults to blank sender
wishList_Two = Message("abcdefghikjklmnopqrstuvwxyzaabcdefghikjklmnopqrstuvwabcdefghi",
                       "testrecipient@yahoo.com")
wishList_Two.append("A valid message goes here")
print(wishList_Two.to_string())

# Entering a recipient greater than 50 characters defaults to blank recipient
wishList_Two = Message("testsender@yahoo.com",
                       "abcdefghikjklmnopqrstuvwxyzaabcdefghikjklmnopqrstuvwabcdefghi")
wishList_Two.append("Here's another valid message")
print(wishList_Two.to_string())

# Entering a message body greater than 50 characters results in no action
wishList_Two.append("Hello what is your favorite TV Show, mine is The Office ")
print(wishList_Two.to_string())


"""
TEST RUN OUTPUTS:
From: Zafir Lari
To: JohnnyAppleSeed@gmail.com
When movie theaters reopen
we should watch the following movies: 
James Bond
Tenet
Dune


From: 
To: testrecipient@yahoo.com
A valid message goes here


From: testsender@yahoo.com
To: 
Here's another valid message


From: testsender@yahoo.com
To: 
Here's another valid message



Process finished with exit code 0

"""
