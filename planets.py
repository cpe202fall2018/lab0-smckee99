def weight_on_planets():
    # get input from user on what their weight is
    earthweight = float(input("What do you weigh on earth? "))

    mars = earthweight * .38
    jupiter = earthweight * 2.34

    # print out the adjusted weights
    print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (mars, jupiter))

    if __name__ == '__main__':
        weight_on_planets()