def categories(request):
    categories = [
    'Programing',
    'Food',
    'Travel',
    'Study',
    ]
    return {'categories':categories}