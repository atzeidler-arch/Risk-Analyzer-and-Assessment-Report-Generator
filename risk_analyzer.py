"""
Risk Assessment Report Generator

Author: Andrew Zeidler

Description:
This script reads scenario data from a CSV file, calculates a risk score
for each location, classifies each scenario by risk level, and writes a
summary report.
"""

import csv


# Reads CSV data and stores each row as a dictionary
def read_data(filename):
    scenarios = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            scenario = {
                "location": row["location"].strip(),
                "visibility": row["visibility"].strip().lower(),
                "terrain_complexity": row["terrain_complexity"].strip().lower(),
                "signal_strength": row["signal_strength"].strip().lower(),
                "enemy_presence": row["enemy_presence"].strip().lower(),
                "accessibility": row["accessibility"].strip().lower(),
                "weather_conditions": row["weather_conditions"].strip().lower(),
                "time_of_day": row["time_of_day"].strip().lower(),
                "civilian_presence": row["civilian_presence"].strip().lower()
            }

            scenarios.append(scenario)

    return scenarios


# Calculates a numeric risk score for one scenario
def calculate_risk_score(scenario):
    score = 0

    if scenario["visibility"] == "low":
        score += 2
    elif scenario["visibility"] == "medium":
        score += 1

    if scenario["terrain_complexity"] == "high":
        score += 2
    elif scenario["terrain_complexity"] == "medium":
        score += 1

    if scenario["signal_strength"] == "weak":
        score += 2
    elif scenario["signal_strength"] == "moderate":
        score += 1

    if scenario["enemy_presence"] == "yes":
        score += 2

    if scenario["accessibility"] == "difficult":
        score += 2
    elif scenario["accessibility"] == "moderate":
        score += 1

    if scenario["weather_conditions"] == "storm":
        score += 2
    elif scenario["weather_conditions"] == "rain":
        score += 1

    if scenario["time_of_day"] == "night":
        score += 1

    if scenario["civilian_presence"] == "full":
        score += 2
    elif scenario["civilian_presence"] == "limited":
        score += 1

    return score


# Converts numeric score into risk category
def classify_risk(score):
    if score >= 11:
        return "HIGH"
    elif score >= 6:
        return "MODERATE"
    else:
        return "LOW"


# Builds a list of completed assessments
def assess_scenarios(scenarios):
    results = []

    for scenario in scenarios:
        score = calculate_risk_score(scenario)
        risk_level = classify_risk(score)

        result = {
            "location": scenario["location"],
            "score": score,
            "risk_level": risk_level
        }

        results.append(result)

    return results


# Counts how many scenarios fall into each risk category
def count_risk_levels(results):
    counts = {
        "HIGH": 0,
        "MODERATE": 0,
        "LOW": 0
    }

    for result in results:
        counts[result["risk_level"]] += 1

    return counts


# Writes the report to a text file
def write_report(results, counts, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("--- Risk Assessment Report ---\n\n")

        for result in results:
            file.write(
                f"{result['location']}: {result['risk_level']} RISK "
                f"(Score: {result['score']})\n"
            )

        file.write("\n--- Summary ---\n")
        file.write(f"High Risk Scenarios: {counts['HIGH']}\n")
        file.write(f"Moderate Risk Scenarios: {counts['MODERATE']}\n")
        file.write(f"Low Risk Scenarios: {counts['LOW']}\n")


# Collects one scenario directly from user input
def get_user_scenario():
    scenario = {
        "location": input("Enter scenario name: ").strip(),
        "visibility": input("Visibility (low/medium/high): ").strip().lower(),
        "terrain_complexity": input("Terrain complexity (low/medium/high): ").strip().lower(),
        "signal_strength": input("Signal strength (weak/moderate/strong): ").strip().lower(),
        "enemy_presence": input("Enemy presence (yes/no): ").strip().lower(),
        "accessibility": input("Accessibility (easy/moderate/difficult): ").strip().lower(),
        "weather_conditions": input("Weather conditions (clear/rain/storm): ").strip().lower(),
        "time_of_day": input("Time of day (day/night): ").strip().lower(),
        "civilian_presence": input("Civilian presence (none/limited/full): ").strip().lower()
    }

    return scenario


# Assesses one user-entered scenario
def assess_single_scenario():
    scenario = get_user_scenario()
    score = calculate_risk_score(scenario)
    risk_level = classify_risk(score)

    print("\n--- Individual Scenario Assessment ---")
    print(f"Location: {scenario['location']}")
    print(f"Risk Level: {risk_level}")
    print(f"Risk Score: {score}")


def main():
    data_file = "risk_data.csv"
    report_file = "risk_report.txt"

    print("1. Analyze CSV dataset")
    print("2. Assess an individual scenario")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        scenarios = read_data(data_file)
        results = assess_scenarios(scenarios)
        counts = count_risk_levels(results)

        print("\n--- Risk Assessment Results ---")
        for result in results:
            print(
                f"{result['location']}: {result['risk_level']} RISK "
                f"(Score: {result['score']})"
            )

        print("\n--- Summary ---")
        print(f"High Risk Scenarios: {counts['HIGH']}")
        print(f"Moderate Risk Scenarios: {counts['MODERATE']}")
        print(f"Low Risk Scenarios: {counts['LOW']}")

        save = input("\nSave full report to file? (yes/no): ").strip().lower()

        if save in ["yes", "y"]:
            write_report(results, counts, report_file)
            print(f"\nReport written to {report_file}")
        else:
            print("\nReport not saved.")

    elif choice == "2":
        assess_single_scenario()

    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()