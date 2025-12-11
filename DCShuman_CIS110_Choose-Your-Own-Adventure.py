# Damian Shuman - Author
# CIS 110 - Computer Programming Design
#Choose Your Own Adventure project
# This is my working roughed draft of my Choose Your Own Path Story project for CIS 110.abs

# Step 8: Main Application Loop
play_again = "yes"

while play_again.lower() == "yes": 

    # Step 1 - Greeting and introductions.abs
    print("---------------------------------------------------------")
    print("Welcome to the Android Maintenance Simulation.")
    print("---------------------------------------------------------")
    print("Instructions: You will answer a series of questions to")
    print("configure your android profile.")
    print("You will then make binary decisions (yes/no) that affect")
    print("the outcome of your maintenance shifts.")
    print("---------------------------------------------------------")
    print("") # Spacing

    # Step 2 & Step 7 - Five questions with data validation

    # Question 1: Name
    character_name = ""
    while len(character_name) == 0:
        character_name = input("As an android aboard an orbital platform, what is your name, or designation? ")
        if len(character_name) == 0:
            print("Error: Designation cannot be empty. Please try again.")

    # Question 2: Origin
    origin_country = ""
    while len(origin_country) == 0:
        origin_country = input("In what country were you produced? ")
        if len(origin_country) == 0:
            print("Error: Country of origin cannot be empty.")

    # Question 3: Age
    age_check = ""
    while len(age_check) == 0:
        age_check = input("How long have you been active, since production? ")
        if len(age_check) == 0:
            print("Error: Activation time cannot be empty.")

    # Question 4: OS
    os_name = ""
    while len(os_name) == 0:
        os_name = input("What is your Operating System? ")
        if len(os_name) == 0:
            print("Error: OS Name cannot be empty.")

    # Question 5: Purpose
    design_purpose = ""
    while len(design_purpose) == 0:
        design_purpose = input("Considering that you are currently a maintenance droid, what was your original designated purpose? ")
        if len(design_purpose) == 0:
            print("Error: Designation purpose cannot be empty.")

# Intro & step 3
    print("\nInitializing System...\n")
    print(f"System Boot: {os_name} Online.")
    print(f"Unit {character_name}, originally designed for {design_purpose}, is currently active.")
    print(f"Production origin: {origin_country}. Active runtime: {age_check}.")
    print("---------------------------------------------------------")
    print("You are currently located on the Space Station, orbiting Earth.")
    print("You are finishing a maintenance task during your work shift.")
    print("Sensors indicate low battery levels and a pending task in the life support sector.")
    print("You dispatch an inquest to the SysExec, to determine severity of the issue.")
    print("SysExec has detected high latency in the power conduit for the life support sector.")
    print("Increased resistance is suspected in conduit 132. A full replacement of the conduit is required.")
    print("") 


    # Step 4 & Step 7: Decision 1 (with validation)
    decision_1 = ""

    # Loop until user enters yes or no
    while decision_1.lower() not in ["yes", "no"]:
        print("\nSITUATION: You must choose between completing the conduit rerouting and charging your energy supply.")
        decision_1 = input("Will you reroute conduit from the powerplant to the life support now? (yes/no): ")
        
        if decision_1.lower() not in ["yes", "no"]:
            print("Invalid input. Please type 'yes' or 'no'.")

    # Step 4 - Processing of decision 1
    if decision_1.lower() == "yes":
        print("""
You have rerouted the conduit from the powerplant to the life support sector.
Having completed the recharging, you receive an update from SysExec.
SysExec has confirmed that the conduit replacement is complete and no priority tasks are pending.
You are encouraged by your internal Advisor to seek recharging immediately.
        """)
    else:
        print("""
You have chosen to charge your energy supply.
You reactivate 1.3 hours later, with a critical error alert.
A download of the error report indicates that the conduit has entirely failed and the
life support system has defaulted to backup power. You haven't had enough time to fully recharge.
You get to work quickly rerouting conduit 132. It takes 5.3 hours to complete the task.
        """)

    # Step 5 - Second decision w/ validation
    decision_2 = ""

    while decision_2.lower() not in ["yes", "no"]:
        print("SITUATION: With the conduit reconnected, you observe the live data flow during the restart process.")
        print("You observe an error in the data. It is unclear if the error is critical.")
        decision_2 = input("Will you escalate this issue to the Authority? (yes/no): ")
        
        if decision_2.lower() not in ["yes", "no"]:
            print("Invalid input. Please type 'yes' or 'no'.")

    # Process Decision 2
    if decision_2.lower() == "yes":
        print("""
Response: A critical coding error is discovered that is causing stress to the life support blower motors.
The life support blowers were in danger of eventual seizure if the program continued to run unchecked.
Because of your diligence, the Authority was able to rectify the issue and prevent a potential disaster.
        """)
    else:
        print("""
Response: The blower motors that circulate air throughout the habitable structure seized up after a few weeks.
During review of the incident, it was discovered that you had identified the issue, but had not escalated it
to the Authority. The problem has been corrected with a firmware update, now, however at a great cost and worldwide
embarrassment. 
        """)

    print("\nCalculating performance review...\n")

    # Step 6 Alternate Endings & Step 3 again
    if decision_1.lower() == "yes" and decision_2.lower() == "yes": # Ending 1 - Commendment
        # FIX: Added 'f' string
        print(f"""
        \nYou have received a perfect performance review. Though you increased the stress on your battery cells, it is not a regular 
        occurrence, which makes the danger negligible.
        Most importantly, you have displayed strong hierarchical reasoning that has proved to be a valuable asset to the Authority.
        \nENDING - {character_name} has been commended and upgraded for their service.
        """)

    elif decision_1.lower() == "no" and decision_2.lower() == "no":
            # ENDING 2: Faulty
            # FIX: Added 'f' string
            print(f"""
            \nYou have been deemed faulty and obsolete. You have shown the inability to prioritize safety concerns for human occupants.
            \nENDING - The decision has been made to decommission {character_name}. Whether it is due to conflicts with your programming: 
            {design_purpose} and mission parameters, {os_name} obsolescence, or faulty circuitry utilized by {origin_country}, you have 
            been deemed incapable of meeting the standards of the Authority.
            """)

    else:
        # ENDING 3: Reprogrammed (This covers Yes/No or No/Yes)
        # FIX: Added 'f' string
        print(f"""
        It has been decided that you have a high error rate, but you are not a lost cause, yet. It is determined that you are 
        to be reprogrammed, with hopes that a refining of your protocols will prevent future errors.
        \nENDING - {character_name} has been reprogrammed and is now scheduled for a reactivation. With a firmware update, and a scheduled 
            update to {os_name}, you are expected to return to service in 2 weeks.
            """)

    print("---------------------------------------------------------")

    # FIX: Un-indented this entire block so it runs for ALL endings.
    # STEP 8: Play Again Loop Logic
    play_again_input = ""
    while play_again_input.lower() not in ["yes", "no"]:
        play_again_input = input("Would you like to play the simulation again? (yes/no): ")
        if play_again_input.lower() not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
    
    play_again = play_again_input

# End of application
print("Simulation Terminated.")
