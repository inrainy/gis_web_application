
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')

    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World!')


#실습2

def check_positive(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated


@check_positive
def rect_area(width, height):
    return width * height

@check_positive
def tria_area(width, height):
    return width * height * 1/2


tria_area(10, 20)