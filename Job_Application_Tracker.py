import datetime
job_applications = []
while True:
    dict1 = {}
    print("=" * 10, "JOB APPLICATION TRACKER", "=" * 10)
    print("1. Add new application")
    print("2. View applications")
    print("3. Update application status")
    print("4. Search applications")
    print("5. Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        company = input("enter company name:")
        role = input("enter the role:")
        ctc = f"{int(input('enter the ctc in lakhs:'))} CTC"
        location = input("enter the location of this job:")
        work_mode = input("enter the mode of the work:")
        date_applied1 = input("enter the date on which you applied for this role in this format yyyy-mm-dd1:")
        date_applied = datetime.datetime.strptime(date_applied1, "%Y-%m-%d") 
        application_source = input("enter the source of this job application:")
        job_link = input("enter the job link:")
        resume_submitted = input("paste the name of the resume you submitted for this role:")
        status = input("enter current status of this role:")
        notes = input("enter if you want to save any important infomation:")
        dict1["company"] = company
        dict1["role"] = role
        dict1["ctc"] = ctc
        dict1["location"] = location
        dict1["work_mode"] = work_mode
        dict1["date_applied"] = date_applied
        dict1["application_source"] = application_source
        dict1["job_link"] = job_link
        dict1["resume_submitted"] = resume_submitted
        dict1["status"] = status
        dict1["notes"] = notes
        job_applications.append(dict1)
    elif choice == 2:
        print("View application selected")
        count = 1
        for dict1 in job_applications:
                print(f"{count}. {dict1["company"]} - {dict1["role"]} - {dict1["status"]}")
                count += 1
    elif choice == 3:
        print("Update application selected")
        update_status = input("enter the value to be updated:")
        update_company_name = input("enetr the company name you want to change the status of:")
        for dict1 in job_applications:
            if update_company_name == dict1["company"]:
                dict1["status"] = update_status
    elif choice == 4:
        print("Search application")
        #search by any field that you want
        search_by = int(input())
        if search_by == 1:
            search_company = input("enter the name of the company you want to search")
        elif search_by == 2:
            search_role = input("enter the name of the role you want to search")
        elif search_by == 3:
            search_status = input("enter the status you want to search ")
        elif search_by == 4:
            search_loc = input("enter the status you want to search by")
        for job in job_applications:
            if search_by == 1:
                if search_company == job["company"]:
                    print(f"{job["company"]} - {job["role"]} - {job["status"]}")
            elif search_by == 2:
                if search_role == job["role"]:
                    print(f"{job["company"]} - {job["role"]} - {job["status"]}")
            elif search_by == 3:
                if search_status == job["status"]:
                    print(f"{job["company"]} - {job["role"]} - {job["status"]}")
            elif search_by == 4:
                if search_loc == job["location"]:
                    print(f"{job["company"]} - {job["role"]} - {job["status"]}")            
    elif choice == 5:
        print("exit")
        break
        

