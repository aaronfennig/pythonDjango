from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import json

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("leads_and_clients_db")
    query = "SELECT concat(clients.first_name, ' ', clients.last_name) as name, count(leads.client_id) as leads FROM clients JOIN leads ON leads.client_id = clients.id GROUP BY leads.client_id"
    all_leads = mysql.query_db(query)
    print(all_leads)
    total_leads = 0
    for each in all_leads:
        total_leads += int(each['leads'])
    print("*************************total number of leads**********************",total_leads)
    percentage = int(all_leads[0]["leads"])/total_leads
    print(round(percentage, 3))
    return render_template("index.html", template_all_leads = all_leads, template_total_leads = total_leads, json_leads = map(json.dumps, all_leads))


if __name__ == "__main__":
    app.run(debug = True)