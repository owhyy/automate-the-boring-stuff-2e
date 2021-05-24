import pyinputplus as pyip


def sandwich_maker():
    bread_types = ["wheat", "white", "sourdough"]
    bread_prices = [0.2, 0.25, 0.3]
    protein_types = ["chicken", "turkey", "ham", "tofu"]
    protein_prices = [1.5, 1.7, 2, 1.75]
    cheese_types = ["cheddar", "Swiss", "mozarella"]
    cheese_prices = [0.5, 0.7, 0.9, 0.75]
    dough = pyip.inputMenu(
        bread_types,
        numbered=True,
        prompt="Please enter preferred bread type :\n",
    )
    print("%s choosen succesfully!" % dough)

    protein = pyip.inputMenu(
        protein_types, numbered=True, prompt="Please enter preferred protein type :\n"
    )
    print("%s choosen succesfully!\n" % protein)

    cheese = pyip.inputMenu(
        cheese_types, numbered=True, prompt="Please enter preferred cheese type :\n"
    )
    print("%s choosen succesfully!\n" % cheese)

    additional_options = [
        "mayo",
        "mustard",
        "lettuce",
        "tomato",
    ]
    additional_options_prices = 0.25
    choices = []
    number_of_options = 0
    for option in additional_options:
        ch = pyip.inputYesNo(prompt=option.title() + "?\n")
        if ch == "yes":
            choices.append(option)
            number_of_options += 1
        else:
            choices.append("no " + option)

    number = pyip.inputInt(min=1, prompt="How many sandwiches?\n")

    price = 0
    price += (
        bread_prices[bread_types.index(dough)]
        + protein_prices[protein_types.index(protein)]
        + cheese_prices[cheese_types.index(cheese)]
        + (number_of_options * additional_options_prices)
    ) * number

    if number == 1:
        print(
            "Order placed! %s sandwich" % number,
            dough,
            protein,
            cheese,
            " ".join(choices),
        )
        print("Price: %.2f$\n" % price)
    else:
        print(
            "Order placed! %s sandwiches: " % number,
            dough,
            protein,
            cheese,
            " ".join(choices),
        )
        print("Price: %.2f$\n" % price)


sandwich_maker()
