# import logging

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # get a list with each line from the textarea input
        vat_ids = request.form.get("vat_ids").split()
        app.logger.debug(vat_ids)

        # loop through VAT-IDS and validate them
        for vat_id in vat_ids:
            state = vat_id[:2]
            vat_number = vat_id[2:]
            app.logger.debug(f"{state}, {vat_number}")

            # validate VAT-IDs
            #TODO

        return render_template("index.html")
    
    else:
        # just return the homepage
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)