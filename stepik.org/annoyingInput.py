def get_int(start_message, error_message, end_message):
    try:
        print(start_message)
        inp = int(input())
        print(end_message)
        return inp
    except ValueError:
        return get_int(error_message, error_message, end_message)



# def get_int(start_message, error_message, end_message):
#     print(start_message)
#     while True:
#         try:
#             d = int(input())
#             break
#         except ValueError:
#             print(error_message)
#     print(end_message)
#     return d


print(get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.'))
