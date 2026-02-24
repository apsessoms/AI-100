
import os # import Python's built in OS module that lets you interact w/ env variables, file system, and process info
from flask import Flask, jsonify # import Flask and jsonify from the flask package. Flask used to create the web app & jsonify returns JSON response 

app = Flask(__name__) # creates the web app & app is the variable storing the Flask app 

@app.get("/") # the @ is a decorator that modifies or registers a function. When somebody makes a GET req to /, it will run the function below
def root(): # this function runs when someone visits "https://yourapp.azurewebsites.net/"
        api_key_loaded = bool(os.getenv("OPENAI_API_KEY", "")) # this shows if the app successfully loaded the Key Vault Secret
        return jsonify(
        status="ok",
        message="Deployed via GitHub Actions + OIDC",
        key_vault_secret_loaded=api_key_loaded,
        azure_openai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        azure_openai_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
    )

@app.get("/healthz") # another decorator that registers a health check endpoint. /healthz is commonly used by Kubernetes, Load Balancers, and Monitoring systems
def healthz():
    return "ok", 200 # 200 is the HTTP status code for OK, so this means the app is healthy and responding to requests
