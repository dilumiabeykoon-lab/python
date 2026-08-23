day=3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

grade="B"
match grade:
    case"A":
        print("Excellent")
    case"B":
        print("Good")
    case"C":
        print("Average")
    case _:
        print("Invalid")

fruit="apple"
match fruit:
    case "apple"|"mango":
        print("Sweet fruit")
    case "Lemon":
        print("Sour fruit")
    case _:
        print("Unknown fruit")

age=20
match age:
    case x if x>=18:
        print("Adult")
    case _:
        print("Minor")
