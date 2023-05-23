# Simple Flask REST for AWS RDS Database Testing

# Download and setup

Step-1: Creating venv
  ```bash
    python -m venv venv
    ./venv/Scripts/activate
  ```

Step-2: Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
Step-2: Running application
Powershell
```bash
  > $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"
  > flask run
```

# Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
# Common Issues
1. Creating __pycache__ files
  Windows-powershell-Solution:
  ```bash
    $env:PYTHONDONTWRITEBYTECODE=1
  ```


# Common Errors
1. While activating venv this error occures in Windows:

    ```bash
        + CategoryInfo          : SecurityError: (:) [], PSSecurityException
        + FullyQualifiedErrorId : UnauthorizedAccess
    ```
    Solution:
    Execute this command and retry activating venv.
    ```bash
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```