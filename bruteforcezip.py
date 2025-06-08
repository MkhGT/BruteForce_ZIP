import zipfile

def brute_force_zip(zip_file_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_file_path)
    except FileNotFoundError:
        print("File ZIP tidak ditemukan.")
        return

    with open(wordlist_path, 'r', encoding='utf-8') as f:
        passwords = f.read().splitlines()

    print("Please Wait...")
    for password in passwords:
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"Password: {password}")
            return
        except:
            continue

    print("Tidak ada password yang cocok.")

# Contoh pemakaian
zip_file = "Z-Image.zip"
wordlist = "wordlist.txt"
brute_force_zip(zip_file, wordlist)
