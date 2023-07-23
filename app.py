from flask import Flask, request, jsonify, send_file
from database.load import load_dataset
from utils import check_required_params
from agent.generate import generate_asset_reports
import pandas as pd


app = Flask(__name__)


def load_data():
    global trip_data
    global location_data
    trip_data,location_data = load_dataset()
    

@app.before_first_request
def before_first_request_func():
    load_data()

@app.route('/asset_report', methods=['GET'])
def generate_report():
    # Specify list of expected parameters in the form
    required_params = ['start_time', 'end_time']
    global location_data
    global trip_data

    # Check if all required arguments are present in the request and are not Null
    check = check_required_params(required_params, request.args)
    if check != 200:
        return jsonify(check), 400
    
    start_time_epoch = request.args.get('start_time')
    end_time_epoch = request.args.get('end_time')

    
    reports = generate_asset_reports(start_time_epoch, end_time_epoch,location_data,trip_data)
    if isinstance(reports, pd.DataFrame):

        excel_file ='data.xlsx'
        reports.to_excel(excel_file, index=False)

        # return the excel file as a response
        return send_file(excel_file, as_attachment=True, download_name='data.xlsx')
    else:
        return jsonify({'error':reports}), 400
    

if __name__ == '__main__':
    app.run(debug=True)


