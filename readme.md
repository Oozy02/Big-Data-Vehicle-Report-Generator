# Vehicle-Report-Generator

## Introduction

Hello there!

I hope this message finds you well. This README provides details about the basic implementation of the vehicle reporter. The v1.0.0 has been implemented in a serial manner. However, it is worth noting that significant improvements can be achieved by implementing CPU-heavy tasks in parallel. Unfortunately, due to time constraints, the current implementation remains serial. But still, a bunch of internal functions are made parallel using Dask.

## Setup Instructions

To set up and run the application, please follow these steps:

1. Open the terminal on your machine.

2. Create a virtual environment for best practices using the following command:

   ```
   python -m venv env
   ```

3. Activate the virtual environment using the appropriate command for your operating system:

   - Windows:
     ```
     env\Scripts\activate.bat
     ```
   - macOS and Linux:
     ```
     source env/bin/activate
     ```

4. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

5. Run the application using the following command:

   ```
   python app.py
   ```

## Using the API

To utilize the API, you can use any API testing platform, such as POSTMAN. Follow these steps:

1. Make a new GET request with the following URL: http://127.0.0.1:5000/asset_report

2. Provide epoch time in the Query params as start_time & end_time to get the desired report.

Please note that the task may take a few minutes (approximately 2-3 minutes) to process 3-4 months of data due to its long-running nature.

## Further Improvements

As mentioned earlier, the current implementation follows a basic request-response approach. For more efficient handling of CPU-heavy tasks, an asynchronous approach using Celery can be implemented. However, for this initial version, we opted for a simpler approach within the given time constraints.

Thank you for your understanding, and if you have any further questions or need any assistance, feel free to reach out.

