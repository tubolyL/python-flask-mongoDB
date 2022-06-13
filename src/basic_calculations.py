import numpy


async def calculate_avg(data: list) -> tuple:
    """
    Takes data from database and returns average of numbers in data
    :param data: json fie that contains 'priceUsd'
    :return: The result of the calculation
    """
    i = 0
    price_sum = 0
    for price in data:
        i += 1
        price_sum += numpy.double(price['priceUsd'])
    average = price_sum/i
    return average, "avg"


async def calculate_sum(data: list) -> tuple:
    """
    Takes data from database and returns sum of numbers in data
    :param data: json fie that contains 'priceUsd'
    :return: The result of the calculation
    """
    price_sum = 0
    for price in data:
        price_sum += numpy.double(price['priceUsd'])
    return price_sum, "sum"


async def calculate_std(data: list) -> tuple:
    """
    Takes data from database and returns standard deviation of numbers in data
    :param data: json fie that contains 'priceUsd'
    :return: The result of the calculation
    """
    price_data = numpy.array(
        [price['priceUsd'] for price in data]).astype(float)
    standard_deviation = numpy.std(price_data)
    return standard_deviation, "std"
