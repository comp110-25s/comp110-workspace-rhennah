"""Planning a Tea Party!"""

__author__: str = "730470881"


def main_planner(guests: int) -> None:
    """Detailining Cost & # of Teabags/Treats Needed According to # of Guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Defining Teabags Needed According to # of People"""
    return 2 * people


def treats(people: int) -> int:
    """Defining Treats Needed According to # of Teabags"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Defining Cost Based on # of Teabags & Treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
