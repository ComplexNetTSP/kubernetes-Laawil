from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Getting the current server hostname and date
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Information to display
    name = "Mohamed Ali HOUAS"
    project_name = "site_web_flask"
    version = "V1"
    
    # Return HTML with all information
    return f"""
    <html>
        <body>
            <h1>Mon projet : {project_name}</h1>
            <p>nom :  {name}</p>
            <p>version: {version}</p>
            <p>nom hôte : {hostname}</p>
            <p>date actuelle : {current_date}</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 
