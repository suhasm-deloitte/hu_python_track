def ratings():
    movies = ["RRR", "KGF", "HIT"]
    for movie in movies:
        print("Rating For Movie:", movie)

        for i in range(len(movies)):
            rating = int(input("Enter Movie rating: "))
            if rating < 1 or rating > 10:
                print("That's not a Valid number!")
                continue
            break
        print("*" * rating)


ratings()
