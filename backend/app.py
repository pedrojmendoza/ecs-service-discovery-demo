from flask import Flask, render_template
import socket
import requests
import boto3
app = Flask(__name__)
servicediscovery = boto3.client("servicediscovery")


@app.route("/ping")
def ping():
    return "", 200


@app.route("/")
def hello():
    resp = servicediscovery.list_services(
        Filters=[{'Name': 'NAMESPACE_ID', 'Values': ['ns-as54folk72oxsl5m']}]
    )
    service_obj = [service for service in resp.get('Services', []) if "backend" not in service['Name']]
    services = []
    for service in service_obj:
        services.append({
            'name': service['Name'],
            'addr': socket.gethostbyname(service['Name']+".ecs-local"),
            'num_hosts': len(servicediscovery.list_instances(ServiceId=service['Id'])['Instances']),
            'text': requests.get("http://"+service['Name']+".ecs-local").content.decode("utf-8")
        })
    return render_template("index.html", services=services)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
