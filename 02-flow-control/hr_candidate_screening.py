# ----------------------------------------------------------
# HR Candidate Screening
# Asks for a candidate's assessment score and location, then
# prints a hiring decision: hired if the score is 75 or above
# and the candidate is based in the US or Canada, offered
# another role if the score is 75+ but they're based elsewhere,
# or rejected if the score is below 75.
# ----------------------------------------------------------

print("------------------------- HR Program -------------------------")

assessment_score = int(input("Enter candidate's assessment score: "))
location = input("Enter candidate's location: ").lower()

if (location == "us" or location == "canada") and assessment_score >= 75:
    print(f"Your assessment score is {assessment_score}/100! You're hired!")
elif location != "us" and location != "canada" and assessment_score >= 75:
    print(
        f"Apologies, you are based in {location} but this role requires you to be based in the US/Canada. Would you be interested in another role?"
    )
else:
    print(
        "Thank you for your interest, we regret to inform you that we will not be moving forward with your application."
    )
