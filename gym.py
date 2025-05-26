


import time
import os
import csv

class GymManager:
    def __init__(self):
        self.members = []  # List to store member information (dictionaries)
        self.filename = "gym_members.csv"  # Default filename for CSV data
        self.load_data()
    def clear_screen(self):
        """Clears the screen."""
        if os.name == "nt":  # Windows
            os.system("cls")
        else:  # Linux or Mac
            os.system("clear")
    def add_member(self):
        """Adds a new member to the system and saves to CSV."""
        self.clear_screen()
        time.sleep(1)
        name = input("Enter the name of the member: ")
        membership_number = input("Enter the ID: ")
        membership_status = input("Enter membership status (active or unactive): ")
        if membership_status.lower() not in ("active", "unactive"):
            print("Invalid membership status. Please enter 'active' or 'unactive'.")
            return
        new_member = {"name": name, "membership_number": membership_number, "status": membership_status}
        self.members.append(new_member)
        self.save_data()  # Save the updated data
        print(f"Member {name} added successfully!")
    def search_member(self):
        self.clear_screen()
        time.sleep(1)
        search_type = input("Enter search type (name, ID, or status): ")
        search_value = input("Enter search value: ")
        found_members = []
        for member in self.members:
            if search_type.lower() == "name":
                if search_value.lower() in member["name"].lower():  # Search by name
                    found_members.append(member)
            elif search_type.lower() == "id":
                if member["membership_number"] == search_value:  # Search by ID
                    found_members.append(member)
            elif search_type.lower() == "status":
                if member["status"].lower() == search_value.lower():  # Search by status
                    found_members.append(member)
            else:
                print("Invalid search type. Please enter 'name', 'ID', or 'status'.")
        if found_members:
            for member in found_members:
                print(f"Name: {member['name']}")
                print(f"Membership ID: {member['membership_number']}")
                print(f"Status: {member['status']}")
                print("----------------------")
        else:
            print("No members found.")
    def show_all_members(self):
        """Displays information for all members."""
        self.clear_screen()
        time.sleep(1)
        if not self.members:
            print("No members found.")
            return
        for member in self.members:
            print(f"Name: {member['name']}")
            print(f"Membership ID: {member['membership_number']}")
            print(f"Status: {member['status']}")
            print("----------------------")

    def save_data(self):
        with open(self.filename, "w", newline="") as csvfile:
            fieldnames = ["name", "membership_number", "status"]  # CSV header row
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header row
            for member in self.members:
                writer.writerow(member)  # Write each member as a row
    def load_data(self):
        try:
            with open(self.filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.members.append(row)  # Add each row to the members list
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist

    def edit_member(self):
      """Edits information for an existing member."""
      self.clear_screen()
      time.sleep(1)
      search_value = input("Enter member ID to edit: ")
      found_member = None
      for member in self.members:
          if member["membership_number"] == search_value:
              found_member = member
              break
      if found_member:
          print(f"Editing member: {found_member['name']}")
          new_name = input("Enter new name (press Enter to keep current): ")
          if new_name:
              found_member["name"] = new_name
          new_status = input("Enter new status (active or unactive) (press Enter to keep current): ")
          if new_status:
              found_member["status"] = new_status
          self.save_data()  # Save the updated data
          print("Member information updated successfully!")
      else:
          print("Member not found.")
    def delete_member(self):
        """Deletes a member from the system."""
        self.clear_screen()
        time.sleep(1)
        search_value = input("Enter member ID to delete: ")
        found_member = None
        for member in self.members:
            if member["membership_number"] == search_value:
                found_member = member
                break
        if found_member:
            self.members.remove(found_member)
            self.save_data()  # Save the updated data
            print("Member deleted successfully!")
        else:
            print("Member not found.")
def main():
    manager = GymManager()
    while True:
        print("\n    ----->Gym **REMO** Member Management System<-----\n")
        print("1. Add Member")
        print("2. Search Member")
        print("3. Show All Members")
        print("4. Edit Member")
        print("5. Delete Member")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_member()
        elif choice == "2":
            manager.search_member()
        elif choice == "3":
            manager.show_all_members()
        elif choice == "4":
            manager.edit_member()
        elif choice == "5":
            manager.delete_member()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




      
