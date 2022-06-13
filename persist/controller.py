import asyncio
import logging
import multiprocessing
import flask
from flask import Blueprint, request
import src.basic_calculations as calc
from persist import mongodb
import datavisualization as dv

bitcoinapp_api = Blueprint('bitcoin', __name__, url_prefix='/bitcoin')


@bitcoinapp_api.route('/update-data', methods=['GET'])
def upload_data():
    return mongodb.update()


@bitcoinapp_api.route('/upload-data', methods=['POST'])
def update_data():
    return mongodb.upload(request.json)


@bitcoinapp_api.route('/basic-calculations', methods=['GET'])
async def basic_calculation():
    try:
        data = mongodb.search()
        sum_task = asyncio.create_task(calc.calculate_sum(data))
        avg_task = asyncio.create_task(calc.calculate_avg(data))
        std_task = asyncio.create_task(calc.calculate_std(data))
        calculated_sum = await sum_task
        calculated_avg = await avg_task
        calculated_std = await std_task
        return f'sum: {calculated_sum}; average: {calculated_avg}; standard deviation: {calculated_std}'
    except Exception as e:
        logging.exception(e)
        return "An exception occurred"


@bitcoinapp_api.route('/basic-calculations-upload', methods=['GET'])
async def basic_calculation_upload():
    try:
        data = mongodb.search()
        sum_task = asyncio.create_task(calc.calculate_sum(data))
        avg_task = asyncio.create_task(calc.calculate_avg(data))
        std_task = asyncio.create_task(calc.calculate_std(data))
        calculated_sum = await sum_task
        calculated_avg = await avg_task
        calculated_std = await std_task

        await mongodb.upload_calculation_data(calculated_sum[0], calculated_sum[1])
        await mongodb.upload_calculation_data(calculated_avg[0], calculated_avg[1])
        await mongodb.upload_calculation_data(calculated_std[0], calculated_std[1])

        return "Upload Successful"
    except Exception as e:
        logging.exception(e)
        return "An exception occurred"


@bitcoinapp_api.route('/polynomial-analysis', methods=['GET'])
def polynomial_analysis():
    try:
        p = multiprocessing.Process(target=dv.polynomial_analysis())
        p.start()
        p.join()
        return flask.send_file('pictures/polynomial_analysis.png')
    except Exception as e:
        logging.exception(e)
        return "An exception occurred"
