def new_decorator(original_func):
    def wrap_func():
        print("extra code before original func")
        original_func()
        print("extra code after original func")
    return wrap_func

@new_decorator
def func_needs_decortaor():
  print("func need decorator")

#decorated_func = new_decorator(func_needs_decortaor)
#decorated_func()

func_needs_decortaor()