namn = "Tjatte"

match namn:
    case "Joakim":
        print("Rik farbror")
    case "Kalle":
        print("Snäll anka")
    case "Knatte" | "Fnatte" | "Tjatte":
        print("En av Knattarna. Har olikfärgade mössor")
    case "Kajsa":
        print("Kalles flickvän")
    case _:
        print("Någon annan karaktär")

