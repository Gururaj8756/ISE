from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserName

@csrf_exempt
def dialogflow_webhook(request):
    if request.method == 'POST':
        data = request.json

        user_name = data.get('queryResult', {}).get('parameters', {}).get('name', '')
        session_id = data.get('session', '')

        UserName.objects.create(session_id=session_id, name=user_name)

        response_text = f'Thank you, {user_name}, for providing your name!'
        response = {'fulfillmentText': response_text}
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request method'})
