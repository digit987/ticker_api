import pandas as pd
from django.core.management.base import BaseCommand
from ticker_api_app.models import Ticker

class Command(BaseCommand):
    help = 'Populate ticker table from CSV file'

    def handle(self, *args, **kwargs):
        # Populating ticker table
        ticker_data = pd.read_csv('ticker_api_app/dataset/Sample-Data-Historic.csv')
        for _, row in ticker_data.iterrows():    
            Ticker.objects.create(
                ticker=row['ticker'],
                date=row['date'],
                revenue=row['revenue'],
                gp=row['gp'],
                fcf=row['fcf'],
                capex=row['capex']
            )
