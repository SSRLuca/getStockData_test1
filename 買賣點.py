import twstock as t

stock=t.Stock("0056")
b=t.BestFourPoint(stock)
buy=b.best_four_point_to_buy()
sell=b.best_four_point_to_sell()
mix=b.best_four_point()
print(f"分析結果: \n {buy}")

#Terminal
#command : twstock -b {stock_code} 
#example: twstock -b 0056 
