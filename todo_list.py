class toDoList():
    def __init__(self):
        self.jobs = []  
    
    def add_job(self):
        job = input("Please enter a job: ")
        self.jobs.append(job) 

    def remove_job(self):
        self.show_jobs() 
        job_index = int(input("Please enter the number of the job you want to remove (starting from 1): ")) - 1
        if 0 <= job_index < len(self.jobs):
            removed_job = self.jobs.pop(job_index)
            print(f"Removed job: {removed_job}")
        else:
            print("Invalid job number!")

    def show_jobs(self):
        if not self.jobs:
            print("No jobs in the list.")
        else:
            print("Your jobs:")
            for i, job in enumerate(self.jobs, 1):
                print(f"{i}. {job}")


list = toDoList()

while True:
    action = input("What would you like to do? (add, remove, show, quit): ").strip().lower()
    if action == 'add':
        list.add_job()
    elif action == 'remove':
        list.remove_job()
    elif action == 'show':
        list.show_jobs()
    elif action == 'quit':
        print("Goodbye!")
        break
    else:
        print("Unknown action, please try again!")
