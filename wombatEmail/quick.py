from authenticate import authenticate
# If modifying these scopes, delete the file token.json.
import os
from base64 import urlsafe_b64decode, urlsafe_b64encode
import re
import json
service = authenticate()

DOMAINS = ['google.com']
USERS = ['firebase']


class EmailHandler():
    def __init__(self, service, users_avoid, domains_avoid):
        self.service = service
        self.users_avoid = users_avoid
        self.domains_avoid = domains_avoid
        self.collected_emails = []
        self.important_email()

    def search_email(self, query):
        results = self.service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        return messages

    def important_email(self):
        for msg in self.search_email('me'):
            email = service.users().messages().get(
                userId='me', id=msg['id']).execute()
            headers = [x for x in email['payload']['headers']]
            for i in headers:
                if i['name'] == 'From' or i['name'] == 'Reply-To':
                    regex = re.compile('[^a-zA-Z0-9.]')
                    email_domain = regex.sub('', i['value'].split("@")[1])
                    email_user = regex.sub('', i['value'].split("@")[0])
                    if email_domain in self.domains_avoid and email_user not in self.users_avoid:
                        google_obj = {
                            "email": i['value'],
                            "message": email['snippet'],
                            "id": email['id'],
                            "headers": [x for x in email['payload']['headers']if x['name'] == 'Received']
                        }
                        self.collected_emails.append(google_obj)

    def save_email(self):
        with open('emails.json', 'w') as f:
            json.dump(self.collected_emails, f)


EmailHandler(service, users_avoid=USERS, domains_avoid=DOMAINS).save_email()