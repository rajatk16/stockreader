#!/usr/local/bin/python3

from stockreader import StockReader
import matplotlib.pyplot as plt

google = StockReader("GOOGL")
# stock_history = google.stock
# print(stock_history.head())

# google.plot_stock()

# google.plot_stock(
#   start_date='2004-08-19',
#   end_date='2019-12-10',
#   stats=[
#     'Daily Change',
#     'y',
#     'Open',
#     'Adj. Close',
#     'Volume'
#   ],
#   plot_type='pct'
# )

# google.buy_and_hold(
#     start_date='2004-08-19',
#     end_date='2019-12-10',
#     nshares=100
# )

# google.weekly_seasonality = True
# model, model_data = google.create_prophet_model()
# model.plot_components(model_data)
# plt.show()

google.changepoint_date_analysis(search='pixel')

# model, future = google.create_prophet_model(days=200)
