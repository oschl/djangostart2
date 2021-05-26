from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()  # instantiate list of board names

    for board in boards:
        boards_names.append(board.name)  # append the name of the current board to the list of boards

    response_html = '<br>'.join(boards_names)  # join all items together separated by <br>

    return HttpResponse(response_html)