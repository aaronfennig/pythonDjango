from product import product
from store import store

buy_more = store("Buy More")
ps5 = product("Playstation 5", 500, "Video Games")
ps5.update_price(800)
xboxSeriesX = product("XBox Series X", 500, "Video Games")
ps5.print_info()
buy_more.add_product(ps5).add_product(xboxSeriesX).printProductList()
buy_more.inflationAdjustment()
buy_more.setClearance()
buy_more.sell_product(ps5).printProductList()
