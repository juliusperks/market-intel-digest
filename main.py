from parse.parser import parse_file
from db.insert import insert_all

if __name__ == "__main__":
    entries = parse_file("data/raw/sample.txt")
    print(f"Parsed {len(entries)} entries.")
    
    insert_all(entries)
    print("All entries inserted into database.")
