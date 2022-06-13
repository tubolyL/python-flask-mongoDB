from unittest import IsolatedAsyncioTestCase
from src import basic_calculations as bc

dataTest = [{'priceUsd': '1'}, {'priceUsd': '2'}, {'priceUsd': '3'}, {'priceUsd': '4'},
            {'priceUsd': '5'}, {'priceUsd': '6'}, {'priceUsd': '7'}]


class TestCalc(IsolatedAsyncioTestCase):
    async def test_calculate_avg(self):
        result = await bc.calculate_avg(dataTest)
        self.assertEqual(result, (4, 'avg'))

    async def test_calculate_sum(self):
        result = await bc.calculate_sum(dataTest)
        self.assertEqual(result, (28, 'sum'))

    async def test_calculate_std(self):
        result = await bc.calculate_std(dataTest)
        self.assertEqual(result, (2, 'std'))
