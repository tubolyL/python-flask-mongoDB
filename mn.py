import asyncio
from src import basic_calculations as bc
from persist import mongodb as db


async def main():
    data = db.search()
    average_calc = asyncio.create_task(bc.calculate_avg(data))
    standard_deviation_calc = asyncio.create_task(bc.calculate_std(data))
    sum_calc = asyncio.create_task(bc.calculate_sum(data))

    calculated_average = await average_calc
    calculated_std = await standard_deviation_calc
    calculated_sum = await sum_calc
    return calculated_average, calculated_std, calculated_sum


if __name__ == '__main__':
    print(asyncio.run(main()))


