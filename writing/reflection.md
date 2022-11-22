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

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the program
TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

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
