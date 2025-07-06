def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                data.append(line.strip().split(','))
        return data
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

def write_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for record in data:
                file.write(','.join(map(str, record)) + '\n')
    except Exception as e:
        print(f"Error writing data: {e}")

def bmi_calculate(height, weight):
    try:
        height_m = height / 100
        return weight / (height_m ** 2)
    except ZeroDivisionError:
        print("Error: Height cannot be zero.")
        return None

def categorize_bmi(bmi):
    if bmi <= 0:
        return "Error: BMI must be greater than 0."
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def average_value(values):
    if not values:
        return None
    return sum(values) / len(values)

def find_maximum(metrics):
    result = {}
    for key, values in metrics.items():
        result[key] = max(values)
    return result

def find_minimum(metrics):
    result = {}
    for key, values in metrics.items():
        result[key] = min(values)
    return result

def check_health_warning(metrics, averages):
    thresholds = {
        "Height": (120, 250),
        "Weight": (40, 200),
        "Systolic BP": (90, 140),
        "Diastolic BP": (60, 90),
        "Heart Rate": (60, 100)
    }

    warnings = {}
    for key, values in metrics.items():
        warnings[key] = []
        for value in values:
            if value < thresholds[key][0] or value > thresholds[key][1]:
                warnings[key].append(value)
    return warnings

def validate_input(value, min_value=0, max_value=300):
    try:
        value = float(value)
        if value is not None and value > max_value:
            if value is not None and value < min_value:
                return False
            return False
        return True
    except ValueError:
        return False

def calculate_bp_category(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated"
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "High Blood Pressure (Hypertension) Stage 1"
    elif 140 <= systolic or 90 <= diastolic:
        return "High Blood Pressure (Hypertension) Stage 2"
    elif systolic > 180 or diastolic > 120:
        return "Hypertensive Crisis – Consult your doctor immediately"
    return "Undefined"

def export_full_report(file_path, data, averages, max_values, min_values, warnings, bmi_values, bmi_categories, bp_categories):
    try:
        with open(file_path, 'w') as file:
            file.write("Health Report:\n\n")
            file.write("Averages:\n")
            for key, value in averages.items():
                file.write(f"  {key}: {value:.2f}\n")

            file.write("\nMaximum Values:\n")
            for key, value in max_values.items():
                file.write(f"  {key}: {value}\n")

            file.write("\nMinimum Values:\n")
            for key, value in min_values.items():
                file.write(f"  {key}: {value}\n")

            file.write("\nWarnings:\n")
            for key, values in warnings.items():
                if values:
                    file.write(f"  {key}: {values}\n")

            file.write("\nBMI Values and Categories:\n")
            for day, (bmi, category) in enumerate(zip(bmi_values, bmi_categories), start=1):
                file.write(f"  Day {day}: BMI = {bmi}, Category = {category}\n")

            file.write("\nBlood Pressure Categories:\n")
            for day, category in enumerate(bp_categories, start=1):
                file.write(f"  Day {day}: {category}\n")
    except Exception as e:
        print(f"Error exporting report: {e}")

def collect_data_from_user(num_days):
    metrics = {"Height": [], "Weight": [], "Systolic BP": [], "Diastolic BP": [], "Heart Rate": []}
    bmi_values = []
    bmi_categories = []
    bp_categories = []

    for day in range(1, num_days + 1):
        print(f"Day {day}:")
        height = float(input("  Enter your height in cm: "))
        weight = float(input("  Enter your weight in kg: "))
        systolic = int(input("  Enter your systolic blood pressure: "))
        diastolic = int(input("  Enter your diastolic blood pressure: "))
        heart_rate = int(input("  Enter your heart rate: "))

        metrics["Height"].append(height)
        metrics["Weight"].append(weight)
        metrics["Systolic BP"].append(systolic)
        metrics["Diastolic BP"].append(diastolic)
        metrics["Heart Rate"].append(heart_rate)

        bmi = bmi_calculate(height, weight)
        bmi_values.append(bmi)
        bmi_categories.append(categorize_bmi(bmi))
        bp_categories.append(calculate_bp_category(systolic, diastolic))

    return metrics, bmi_values, bmi_categories, bp_categories

def collect_data_from_file(file_path):
    data = read_data("health_data.txt")
    if not data:
        return None, None, None, None

    metrics = {"Height": [], "Weight": [], "Systolic BP": [], "Diastolic BP": [], "Heart Rate": []}
    bmi_values = []
    bmi_categories = []
    bp_categories = []

    for record in data:
        height, weight, systolic, diastolic, heart_rate = map(float, record[:5])
        metrics["Height"].append(height)
        metrics["Weight"].append(weight)
        metrics["Systolic BP"].append(systolic)
        metrics["Diastolic BP"].append(diastolic)
        metrics["Heart Rate"].append(heart_rate)

        bmi = bmi_calculate(height, weight)
        bmi_values.append(bmi)
        bmi_categories.append(categorize_bmi(bmi))
        bp_categories.append(calculate_bp_category(systolic, diastolic))

    return metrics, bmi_values, bmi_categories, bp_categories

def main():
    print("Welcome to the Health Metrics Tracker!")
    input_method = input("Would you like to enter data manually or from a file? (manual/file): ").strip().lower()

    if input_method == "manual":
        num_days = int(input("How many days of health metrics would you like to track? "))
        metrics, bmi_values, bmi_categories, bp_categories = collect_data_from_user(num_days)
    elif input_method == "file":
        file_path = input("Enter the file path: ").strip()
        metrics, bmi_values, bmi_categories, bp_categories = collect_data_from_file(file_path)
        if metrics is None:
            print("Error: Unable to read data from file.")
            return
    else:
        print("Invalid input method. Please choose 'manual' or 'file'.")
        return

    averages = {key: average_value(values) for key, values in metrics.items()}
    max_values = find_maximum(metrics)
    min_values = find_minimum(metrics)
    warnings = check_health_warning(metrics, averages)

    report_path = "health_report.txt"
    export_full_report(report_path, metrics, averages, max_values, min_values, warnings, bmi_values, bmi_categories, bp_categories)
    print(f"Health report exported to {report_path}")

if __name__ == "__main__":
    main()