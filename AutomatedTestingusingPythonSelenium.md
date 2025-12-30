Before starting the project, start Google Chrome and the demo web application inside the project environment. To do so, open a new terminal using the “+” button available on the terminal side of the file editor and run the following command:

cd /usercode/automated-testing && bash script.sh
Note: From this point onwards, complete all tasks and navigations exclusively within the browser running in the project environment.

Once Google Chrome is launched, navigate to the following URL:
http://localhost:8081/

Add and Remove Elements
Navigate to the following URL:
http://localhost:8081/
Run the test script using the following command and verify that it passes without any failures:
cd /usercode/automated-testing && pytest --capture=no tests/functional/test_add_remove_elements.py

Drag and Drop
cd /usercode/automated-testing && pytest --capture=no tests/functional/test_drag_and_drop.py

Test the Forgot Password Functionality
cd /usercode/automated-testing && pytest --capture=no tests/functional/test_forgot_password.py

Test the JavaScript Alerts Functionality
cd /usercode/automated-testing && pytest --capture=no tests/functional/test_javascript_alerts.py

Test the Multiple Windows Functionality
cd /usercode/automated-testing && pytest --capture=no tests/functional/test_multiple_windows.py

Test the Performance of Dynamic Controls
cd /usercode/automated-testing && pytest --capture=no tests/performance/test_dynamic_controls.py

Regression Test the File Download Functionality
cd /usercode/automated-testing && pytest --capture=no tests/regression/test_file_download.py
Run the following command inside the terminal to manually check if the file has been downloaded:
ls /root/Downloads/
Additionally, after the test script execution, delete the downloaded files using the following command:
rm -r /root/Downloads/*

Regression Test the File Upload Functionality
cd /usercode/automated-testing && pytest --capture=no tests/regression/test_file_upload.py

Test the Security of Form Authentication
cd /usercode/automated-testing && pytest --capture=no tests/security/test_form_authentication.py

Test the UI for Broken Images
cd /usercode/automated-testing && pytest --capture=no tests/ui/test_broken_images.py

Test the UI for the Horizontal Slider
cd /usercode/automated-testing && pytest --capture=no tests/ui/test_horizontal_slider.py

Test the UI for the Hover Functionality
cd /usercode/automated-testing && pytest --capture=no tests/ui/test_hovers.py

Test the UI for the Infinite Scroll Functionality
cd /usercode/automated-testing && pytest --capture=no tests/ui/test_infinite_scroll.py
