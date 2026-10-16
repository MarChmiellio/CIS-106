FILE_NAME = "dogs.txt"
def load_dogs():
  dogs = []
  try:
      with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 4 and parts[0] != "Name":
              try:
                  dog = {
                      "name": parts[0],
                      "breed": parts[1],
                      "age": int(parts[2]),
                      "weight": float(parts[3])
                  }
                  dogs.append(dog)
              except ValueError:
                  print("Skipping an invalid record in the file.")    
  except FileNotFoundError:
      pass
  return dogs
def save_dogs(dogs):
    """Save all current dogs to a text file, one dog per line."""
    with open(FILE_NAME, "w") as file:
      file.write("Name|Breed|Age|Weight\n")
      for dog in dogs:
          file.write(dog["name"] + "|" + dog["breed"] + "|" +                            
                     str(dog["age"]) + "|" + str(dog["weight"]) + "\n")
def menu():
    """Display the choices and get the user's selection."""
    print("\nDog Rescue")
    print("----------")
    print("1. Add a Dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Delete Dog")
    print("5. Quit")
    return input("Select a choice: ").strip()
def add_dog(dogs):
  """Ask for dog information and add a new dog to the list."""
  name = input("Dog Name: ").strip()
  if name == "" or "|" in name:
    print("Please enter a valid dog name.")
    return
  for dog in dogs:
      if dog["name"].lower() == name.lower():
          print("A dog with that name already exists.")
          return
  breed = input("Dog Breed: ").strip()
  if breed == "" or "|" in breed:
      print("Please enter a valid breed.")
      return
  while True:
      try:
          age = int(input("Age (years): "))
          if age >= 0:
              break
          print("Age cannot be negative.")
      except ValueError:
          print("Please enter a whole number for age.")
  while True:
    try:
        weight = float(input("Weight (lbs): "))
        if weight > 0:
          break
        print("Weight must be greater than zero.")
    except ValueError:
        print("Please enter a number for weight.")
  new_dog = {"name": name, "breed": breed, "age": age, "weight": weight}
  dogs.append(new_dog)
  print(name + " was added successfully!")  
def view_dogs(dogs):
    """Display all dogs in an easy-to-read table."""
    if len(dogs) == 0:
      print("\nThere are no dogs in the rescue.")
      return
    print("\nRescue Dogs")
    print("-" * 69)
    print("{:<18} {:<27} {:>7} {:>11}".format(
        "Name", "Breed", "Age", "Weight (lbs)"))
    print("-" * 69)
    for dog in dogs:
        print("{:<18} {:<27} {:>7} {:>11}".format(
            dog["name"], dog["breed"], dog["age"], dog["weight"]))
def find_dog(dogs):
    """Search for a dog by name and display its information."""
    name = input("Enter dog name to search: ").strip()
    for dog in dogs:
        if dog["name"].lower() == name.lower():
          print("\nFound " + dog["name"])
          print("Breed: " + dog["breed"])
          print("Age: " + str(dog["age"]))
          print("Weight: " + str(dog["weight"]) + " lbs")
          return
    print("Sorry, unable to find " + name)
def delete_dog(dogs):
    """Find a dog by name and remove it from the list."""
    name = input("Enter dog name to delete: "). strip()
    for dog in dogs:
        if dog["name"].lower() == name.lower():
            dogs.remove(dog)
            print(dog["name"] + " was deleted successfully!")
            return
    print("Sorry, unable to find " + name)
def main():
    """Start the application and keep the menu running until Quit."""
    dogs = load_dogs()
    while True:
        choice = menu()
        if choice == "1":
            add_dog(dogs)
            save_dogs(dogs)
        elif choice == "2":
          view_dogs(dogs)
        elif choice == "3":
            find_dog(dogs)
        elif choice == "4":
            delete_dog(dogs)
            save_dogs(dogs)
        elif choice == "5":
            save_dogs(dogs)
            print("Dog records saved to " + FILE_NAME)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 through 5.")
if __name__ == "__main__":
    main()
          
        
