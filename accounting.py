melon_cost = 1.00

def get_payment_data(path_file):

  payment_data = open(path_file)

  for line in payment_data:
    order = line.split("|")

    customer_name = order[1]
    first_name = customer_name.split(" ")[0]

    melon_count = float(order[2])
    paid = float(order[3])

    expected_price = melon_cost *  melon_count
    owes = expected_price - paid
    owed = paid - expected_price


    print(f"{customer_name} paid ${paid:.2f}, expected ${expected_price:.2f}")

    if expected_price < paid:
      print(f"\t{first_name} has overpaid for their melons and is owed ${owed:.2f}.")

    elif expected_price > paid:
      print(f"\t{first_name} has underpaid for their melons and owes ${owes:.2f}.")

  payment_data.close()


get_payment_data("customer-orders.txt")
