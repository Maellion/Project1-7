patient = input("Are you a child or adult?: ").lower()

if patient == "adult":
    symptons_TB = input("Are there any symtoms for TB?: [Yes/No] ").lower()

    if symptons_TB == "yes":
        print("Treat as likely TB patient and perform full TB exam")

    elif symptons_TB == "no":
        print("Have patient report back if unwell; return in 1 month for checkup")

elif patient == "child":
    tb_test = input("Can TB test be given? [Yes/No] ").lower()

    if tb_test == "yes":
        print("Administer TB test\n"
              "Assess TB test results and child's condition")

    elif tb_test == "no":
        child_well = input("Is the child well? [Yes/No] ").lower()

        if child_well == "yes":
            print("6 months preventive isoniazid\n"
                  "Have parents bring in if child shows any symptoms")

        elif child_well == "no":
            print("Take full history. Examine for TB\n"
                  "If TB likely diagnosis treat for TB\n"
                  "If other diagnosis more likely, treat as needed and watch for TB symptoms")
