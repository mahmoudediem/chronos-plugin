# plugin updated to use the new v3 API
from shareddep import new_func

def plugin_run():
    return f"plugin -> {new_func()}"

if __name__ == "__main__":
    print(plugin_run())
