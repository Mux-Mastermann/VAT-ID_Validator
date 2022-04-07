import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # get a list with each line from the textarea input
        vat_ids = request.form.get("vat_ids").split()
        results = []
        app.logger.debug(vat_ids)

        # loop through VAT-IDS and validate them
        for vat_id in vat_ids:
            state = vat_id[:2]
            vat_number = vat_id[2:]
            app.logger.debug(f"{state}, {vat_number}")

            # validate input against API specs
            #TODO

            # validate VAT-IDs
            api_call = check_vat_id(state, vat_number)
            if api_call["success"]:
                if api_call["data"]["valid"]:
                    result = "Valid"
                else:
                    result = "Invalid"
            else:
                result = api_call["error_message"]
            
            results.append({"vatid": vat_id, "result": result})

        return render_template("index.html")
    
    else:
        # just return the homepage
        return render_template("index.html")


def check_vat_id(state:str, vat_number: str):
    endpoint = "https://vies-api.deta.dev/check-vat-id"

    parameter = {
        "state": state,
        "vat_number": vat_number
    }

    response = requests.get(url=endpoint, params=parameter)

    return response.json()


if __name__ == "__main__":
    app.run(debug=True)