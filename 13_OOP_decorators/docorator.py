def star_decorator(text_func):
    def inside_function():
        print('*' * 30)
        text = text_func()
        print(text.center(30))
        print('*' * 30)

    return inside_function


def get_quote():
    # losowanie cytatu
    return 'Madry cytat'

@star_decorator
def daily_news():
    return 'important!'

def smart_text():
    return 'smart...'


#----
quote = star_decorator(get_quote)
quote()

daily_news()