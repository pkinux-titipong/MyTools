import subprocess

def main():
    while True:
        print("\n########################################")
        print("#                                      #")
        print ("# WEBSITE TEST TOOLS (type Q to leave) #")
        print("#                                      #")
        print("#             Dev by Pank pkinux       #")
        print("########################################")
        print("\nPlease select module that you like:")
        print("1. Website Status Check")
        print("2. Site Map Check")
        print("q. Quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            subprocess.run(["python", "webcheck.py"])
        elif choice == '2':
            subprocess.run(["python", "treemap.py"])
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

