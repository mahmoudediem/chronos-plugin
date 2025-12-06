# plugin still uses the legacy v2 API
from shareddep import legacy_func

def plugin_run():
    return f"plugin -> {legacy_func()}"

if __name__ == "__main__":
    print(plugin_run())