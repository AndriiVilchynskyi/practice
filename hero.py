hero = {"strange": 0, "health": 0, "inteligence": 0, "agility": 0}
max_points = 30
choice = None
while choice != "0":
    print("""
     
        Переводчик с гикского на русский
        О - Exit
        1 Show hero attributes and points
        2 Increase hero points
        3 Decrease hero points
        """)
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("Bye")
    elif choice == "1":
        print(hero)
    elif choice == "2":
        attribute = input("enter hero attribute: ")
        value = input("enter the value of hero attribute: ")
        value = int(value)
        free_stats = max_points - sum(hero.values())
        if attribute in hero and free_stats >= value:
            hero[attribute] += value
            free_stats = max_points - sum(hero.values())
            print(hero)
            print(f"you have {free_stats} points left")
        else:
            print("You don't have enough points")
    elif choice == "3":
        attribute = input("enter hero attribute: ")
        value = input("enter the value of hero attribute: ")
        value = int(value)
        hero[attribute] -= value
        if attribute in hero and hero[attribute] > 0:
            print(f"You can decrease {attribute}")
            print(f"Free attributes to decrease  {hero[attribute]}")
        else:
            print("Point can`t be lower then 0")
            hero[attribute] += value
    else:
        print("You wrote the wrong option")






















        # free_stats = max_stats - sum(hero.values())
        # if sum(hero.values()) + int(value) <= max_stats and attribute in hero:
        #     hero[attribute] = int(value)
        #     print(hero)
        #     print(f"You have {free_stats} stats left")
        # elif attribute not in hero[attribute]:
        #     print("There is no attribute", attribute)
        # elif int(value) > free_stats:
        #     print("You doesn't have")
