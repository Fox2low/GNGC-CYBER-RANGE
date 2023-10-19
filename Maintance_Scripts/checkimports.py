import importlib

def check_python_imports(imports):
    missing_imports = []
    for module_name in imports:
        try:
            importlib.import_module(module_name)
        except ImportError:
            missing_imports.append(module_name)
            
    return missing_imports

if __name__ == "__main__":
    required_imports = [
        "flask",
        "flask_login",
        "werkzeug",
        "sqlalchemy",
        "re",
        "socket",
        "sys",
        "os",
        "time",
        "threading",
        "mysqlclient",
        "pymysql",
    ]
    missing_modules = check_python_imports(required_imports)

    if missing_modules:
        print("Missing Python imports:")
        for module in missing_modules:
            print(f" - {module}")
        print("")
        print("You can fix this by running ./setup.sh, and agree to install python dependencies")
    else:
        print("Python imports: Pass")
