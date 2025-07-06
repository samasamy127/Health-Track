# 🩺 Health Track

## 🧠 Problem Description

Maintaining and monitoring health parameters is vital for a healthy lifestyle, yet most individuals rely on manual tracking or scattered data, making it difficult to detect trends or issues. Common problems include:

* No centralized log for health data
* Difficulty identifying abnormal health metrics
* Lack of alerts for health risks
* Poor visualization of progress or health trends

**Health Track** addresses these issues by providing a complete tool for health monitoring. Users can input health data such as weight, height, blood pressure, and heart rate either manually or via file upload. The program then:

* Calculates BMI, averages, and trends
* Categorizes results (e.g., underweight, elevated BP)
* Issues warnings for abnormal values
* Generates a comprehensive health report

---

## 👥 Team Contribution

### **Sama Samy**

Developed the following functions:

1. `bmi_calculate()`: Computes BMI using `BMI = weight / (height^2)`
2. `categorize_bmi()`: Classifies BMI as *underweight*, *normal*, *overweight*, or *obese*
3. `average_value()`: Calculates the weekly average for each health metric
4. `find_maximum()`: Finds the highest value among the metrics
5. `find_minimum()`: Finds the lowest value among the metrics
6. `calculate_bp_category()`: Categorizes blood pressure as *normal*, *elevated*, or *hypertension*
7. `collect_data_from_user()`: Collects data manually from the user

✅ Integrated BMI and BP classification into the main workflow.

---

### **Nouran Fares**

Developed the following functionalities:

1. `read_data()`: Reads user data from a file
2. `write_data()`: Writes processed data and health metrics to an output file
3. `check_health_warning()`: Detects and reports abnormal metrics
4. `validate_input()`: Validates user inputs for correctness
5. `export_full_report()`: Generates a detailed health report with all metrics and warnings
6. `collect_data_from_file()`: Collects data from user-specified file

✅ Integrated all functions into the `main()` function, ensuring correct execution flow.

---

## 📖 User Manual

### 1️⃣ Getting Started

* Place the input file (if using file input) in the **same directory** as the program.

### 2️⃣ Input Options

* **File Input**: Use a structured file containing daily health metrics.
* **Manual Input**: Enter values directly through on-screen prompts.

### 3️⃣ Program Features

* **Health Tracking**

  * Compute and categorize BMI.
  * Classify blood pressure (normal/elevated/hypertension).
  * Calculate weekly averages of all metrics.
  * Identify maximum and minimum values.
  * Issue warnings when values are outside healthy limits.

* **Health Report**

  * Exports a comprehensive report (`output_file.txt`) containing:

    * All input metrics
    * Categorized results
    * Weekly trends
    * Warnings

### 4️⃣ How to Run

1. Choose input method: Manual or File
2. Provide required data
3. The program will:

   * Analyze data
   * Show warnings if any
   * Generate an output file with full analysis

✅ **Open `output_file.txt`** to view your detailed health report.
