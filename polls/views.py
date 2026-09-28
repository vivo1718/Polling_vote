from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

# Temp data store (resets when the server restarts)
poll_data = {
    "question": "Which Python framework do you prefer?",
    "options": {
        "django": {"text": "Django", "votes": 0},
        "fastapi": {"text": "FastAPI", "votes": 0}
    }
}

def poll_view(request):
    return render(request, 'polls/vote.html', {'poll': poll_data})

def vote_submit(request):
    if request.method == 'POST':
        selected_option = request.POST.get('choice')
        
        if selected_option in poll_data['options']:
            poll_data['options'][selected_option]['votes'] += 1
            
        total_votes = sum(opt['votes'] for opt in poll_data['options'].values())
        
        results = []
        for key, opt in poll_data['options'].items():
            percentage = (opt['votes'] / total_votes * 100) if total_votes > 0 else 0
            results.append({
                'text': opt['text'],
                'votes': opt['votes'],
                'percentage': round(percentage, 1)
            })
            
        return render(request, 'polls/results.html', {
            'question': poll_data['question'],
            'results': results,
            'total_votes': total_votes
        })
        
    return redirect('poll_view')
