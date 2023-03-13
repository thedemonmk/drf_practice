from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('stock', type=int)
        parser.add_argument('price', type=float)
        
    def handle(self, *args, **options):
        import requests
        import json

        url = "http://127.0.0.1:8000/item/"

        payload = json.dumps({
        "title": options['title'],
        "stock": options['stock'],
        "price": options['price']
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 1f60f2bf84db32b4d20a9e3ddd05542917d00baa'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)