import requests
import sys

# Check if the script is being passed an employee ID
if len(sys.argv) < 2:
    print("Please provide an employee ID as an argument")
    sys.exit(1)

# Get the employee ID from the command line argument
employee_id = sys.argv[1]

# Make a request to the API to get the employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

# Check if the response was successful
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    sys.exit(1)

# Parse the JSON response
todo_list = response.json()

# Count the number of completed tasks
completed_tasks = [task for task in todo_list if task['completed']]
num_completed_tasks = len(completed_tasks)

# Format and print the output
employee_name = todo_list[0]['name']
total_num_tasks = len(todo_list)
print(f"Employee {employee_name} is done with {num_completed_tasks}/{total_num_tasks} tasks:")

for task in completed_tasks:
    print(f"\t{task['title']}")
