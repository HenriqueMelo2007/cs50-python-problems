def main():
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }
    user_input = input("File name: ").strip().lower()
    
    for key, value in media_types.items():
      if user_input.endswith(key):
        print(value)
        return
      
    print("application/octet-stream")


if __name__ == "__main__":
    main()
