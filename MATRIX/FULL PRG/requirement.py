import sys
import subprocess
import importlib



def check_and_install_libraries(required_libraries):
  missing_libraries = []
  for library in required_libraries:
    try:
      importlib.import_module(library)
    except ImportError:
      missing_libraries.append(library)

  if missing_libraries:
    print(f"The following libraries are required but not installed: {', '.join(missing_libraries)}")
    try:
      subprocess.run(["pip", "install"] + missing_libraries, check=True)
      print("Successfully installed missing libraries.")
    except subprocess.CalledProcessError:
      print("Error installing libraries using pip. Please install them manually.")
      return False
  else:
    # Return a string indicating successful library presence
    return "All required libraries are present. You can now use Main.py"

# List of required libraries for the code
required_libraries = [
  "speech_recognition",
  "pyttsx3",
  "webbrowser",
  "subprocess",
  "selenium",
  "webdriver_manager",
  "importlib",
  "sys",
  "time",
  "os",
  "random",
  "datetime",
  "google.generativeai",
]

# Call the function and store the returned value (string or False)
result = check_and_install_libraries(required_libraries)

# Print the appropriate message based on the result
if result:
  print(result)  # Print the success message if libraries are present
else:
  print("Failed to install required libraries. Please install them manually and restart the script.")
  sys.exit(1)
