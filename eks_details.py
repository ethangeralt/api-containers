import boto3
from flask import Flask, jsonify
client = boto3.client('eks')
app = Flask(__name__)

def add_description():
    addon_details = client.list_addons(
        clusterName='moka'
    )
    details = []
    for detail in addon_details['addons']:
        describe_addon = client.describe_addon(
            clusterName='moka',
            addonName=detail
        )
        details.append(f"Addon {describe_addon['addon']['addonName']} -- {describe_addon['addon']['addonVersion']} is in {describe_addon['addon']['status']} state")
    return details  

@app.route('/addons_state', methods=['GET'])
def main_function():
    details_of_addons = add_description()
    return details_of_addons

@app.route('/addons', methods=['GET'])
def tain_function():
    details_of_addons = add_description()
    return details_of_addons

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5009)
