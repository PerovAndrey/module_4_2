def test_function():
    def inner_function():
        print('Я в области видимости функции "test_function"')

    inner_function()


test_function()

# inner_function() - вызов вне пространства функции test_function выдаст ошибку:
#                    NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
