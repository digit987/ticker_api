from django.http import JsonResponse
from .models import Ticker
from datetime import datetime, timedelta

def get_ticker_data(request):
    try:
        # Extract parameters from URL
        params = request.GET.dict()
        ticker = params.get('ticker')
        columns = params.get('column').split(',')
        period = params.get('period')

        # Ensure all required parameters are provided
        if not all([ticker, columns, period]):
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        # Calculate start date based on period
        today = datetime.today()
        start_date = today - timedelta(days=365*int(period[:-1]))

        # Filter data based on ticker and date range
        ticker_data = Ticker.objects.filter(ticker=ticker)

        # Prepare response data
        response_data = []
        for data in ticker_data:
            # Extract year from the date string in the format 'mm/dd/yyyy'
            data_year = int(data.date.split('/')[-1])
            if data_year >= start_date.year:
                data_dict = {'date': data.date}
                for column in columns:
                    data_dict[column] = getattr(data, column)
                response_data.append(data_dict)

        return JsonResponse(response_data, safe=False)

    except ValueError:
        return JsonResponse({'error': 'Invalid parameter value'}, status=400)
