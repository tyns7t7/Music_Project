import data_handler
import library_ops
import analytics

def main():
    data_handler.create_initial_dataset()
    library = data_handler.load_library()

    while True:
        print("\n=== MUSIC KEYWORD LIBRARY SEARCHER ===")
        print("1. Display All Songs")
        print("2. Search Songs by Keyword")
        print("3. Add a New Song")
        print("4. Update an Existing Song")
        print("5. Delete a Song")
        print("6. Generate Summary Report")
        print("7. Run NumPy & Pandas Data Analysis")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            library_ops.display_all_songs(library)
        elif choice == "2":
            library_ops.search_songs(library)
        elif choice == "3":
            library = library_ops.add_song(library)
            data_handler.save_library(library)
        elif choice == "4":
            library = library_ops.update_song(library)
            data_handler.save_library(library)
        elif choice == "5":
            library = library_ops.delete_song(library)
            data_handler.save_library(library)
        elif choice == "6":
            library_ops.show_data_structure_summary(library)
        elif choice == "7":
            analytics.run_data_analysis(data_handler.FILE_NAME)
        elif choice == "8":
            print("Exiting Music Library Searcher. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

main()