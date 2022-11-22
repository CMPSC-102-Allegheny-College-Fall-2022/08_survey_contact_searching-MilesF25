# Contact Searching

TODO: Make sure that you delete all of the TODO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## AMiles Franck

## Program Output

### What is the output from running the following commands?

something is wrong with the import statement, this the code without it

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
```python
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":
The contacts file contains 100 people in it! Let's get searching!
```


- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`
```python
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":
The contacts file contains 100 people in it! Let's get searching!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```python
from contactsearcher import search
```
This code allows me to use the search function that was written in the search file in main file.
I can use it in the main file because I used the built in import function.

#### The source code statement that extracts the current job description for a contact

```python
  current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            contacts_list.append(contact_line)
```
This code sets current contact job equal to the first index in the contact_line list,
next it the code checks to see if the job description is in the current_contact_job
if it is it will add the job that is in the list to the contact list.

#### Invocation of the function called `search_for_email_given_job`

```python
search_for_email_given_job({job_description},contacts_file)
```

#### Test case for the function called `search_for_email_given_job`
```python
def test_find_multiple_matching_result():
    """Check to ensure that search for contacts works for multiple matches."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engineer", contacts_database)
    assert len(contacts_list) == 2
```
This code checks to see the function search_for_email_given_job works.
This code sets contaacts_database equal to a random email and job description.
Then it calls the search_for_email_given_job on engineer and contacts_database
then it sets the output from the function equal to contacts_list
Finally the assert function is used to make sure that the length of contacts_list
is equal to two.

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the program
TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

This function call, calls contactsearcher and gives it the job description and the file.
The first thing the function does is use an if statement to make sure that a file is given, if it is
no file is given, then the program will say no contacts file specified!. If it is the correct
file then the program will read in the file, then it will use the splitlines function to seperate 
the emails from the job descriptions. Next the program gets the length of the file after using the
splitlines function and stores it inside a variable. Then it prints a message telling the user
that the search will begin. If the file is not correct then it print he contacts file does not exist. 
If the file is correct then it will begin the search, the progrma will use the search_for_email_given_job
function to find the correct email and job descriptions and it will print them out.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

I struggle with being able to write code. I am good at reading code but when it comes to writting it
I have struggle with figuring out what is required of me and what I need to write. I have not overcome this
challenge.

### Based on your experiences with this project, what is one way in which you want to improve?

I want to be able at understanding what the problems are asking me to do and I want to be
better at writing code. I was only able to complete a few todos on my own, everything else I had to
get help.
