def cheap_price(bread_sold):
    
    old_price = 3.49 * 0.6
    discounted_bread = old_price * bread_sold
    
    return discounted_bread 

def normal_price(bread_sold):
    
    fresh_price = 3.49
    price_bread = fresh_price * bread_sold

    return price_bread

def run():
    bread_sold = int(input("Enter how many loaf of bread were sold:"))
    print(f'if the bread was fresh the price would be {round(normal_price(bread_sold),2)}, the price with discount is {round(cheap_price(bread_sold),2)}')



if __name__ == '__main__':
    run()