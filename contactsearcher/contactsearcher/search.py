"""Search for an email address given a fragment of a job description."""

from typing import List

import csv
from input import contacts
# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # create an empty list of the contacts
    print(f"job_description = {job_description}")
    print(f"contacts = {contacts}")
    contacts_list = []
    # --> refer to the file called inputs/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # --> iterate through each line of the file and extract the current job
    for contact_line in csv.reader(
        contacts.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # extract the current job for the contact on this line of the CSV
        current_contact_job = contact_line[1]
        # the job description matches and thus we should save it in the list
        if job_description in current_contact_job.lower():
            contacts_list.append(contact_line)
    # return the list of the contacts who have a job description that matches
    return contacts_list