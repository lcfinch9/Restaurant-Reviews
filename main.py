#### ---- OPEN FILE ---- ####

with open("reviews.txt", "r") as file:
    text_list = file.readlines()
    review_list = {}
    names = []
    ratings = []
    reviews = []
    for line in text_list:
        line_list = line.split(" | ")
        names.append(line_list[0])
        ratings.append(int(line_list[1]))
        reviews.append(line_list[2].strip())
    review_list["names"] = names
    review_list["ratings"] = ratings
    review_list["reviews"] = reviews

    ## -- Restaurant overview calculation -- ##

    total = 0
    for num in review_list["ratings"]:
        total += num
    avg_rating = total / len(review_list["ratings"])
    last_name = review_list["names"][-1]
    last_review = review_list["reviews"][-1]

    ## -- Restaurant overview output -- ##

    print("Welcome to Breezy Burgers - The best burger spot in town!", end="\n\n")
    print("~-" * 20, end="\n\n")
    print("Reviews:", len(review_list["ratings"]))
    print("Average Rating:", avg_rating, end="\n\n")
    print("SPOTLIGHT REVIEW:")
    print(last_review, "-", last_name, end="\n\n")
    print("~-" * 20, end="\n\n")

#### ---- USER INPUT ---- ####

choice = input("Enter \"A\" to see all reviews, or \"N\" to leave a new review (A/N): ").lower()
print()

## -- New review -- ##

if choice == "n":
    with open("reviews.txt", "a") as file:
        name = input("Enter your name: ")
        review = input("Enter your review: ")
        stars = int(input("How many stars would you give this restaurant (1-5): "))
        
        ## -- Input validation -- ##
        
        while stars < 1 or stars > 5:
            stars = int(input("How many stars would you give this restaurant (1-5): "))
        print(name, stars, review, sep=" | ", file=file)

## -- Display all reviews -- ##

if choice == "a":
    print("REVIEWS:")
    for i in range(len(review_list["names"])):
        print("*" * review_list["ratings"][i], review_list["reviews"][i])
        print("\t - ", review_list["names"][i], end="\n\n")
