from magika import Magika


def main():
    # Initialize Magika
    magika = Magika()

    # Example file paths
    file_paths = ["downloads/image_5.jpg", "task6.py", "OSS.png"]

    # Process each file
    for file_path in file_paths:
        # Read file content as bytes
        with open(file_path, "rb") as file:
            file_content = file.read()

        # Identify the file type
        result = magika.identify_bytes(file_content)

        # Print the result
        print(f"File: {file_path}")
        print(f"Content Type Label: {result.output.ct_label}")
        print(f"Score: {result.output.score}")
        print(f"Group: {result.output.group}")
        print(f"MIME Type: {result.output.mime_type}")
        print(f"Magic: {result.output.magic}")
        print(f"Description: {result.output.description}\n")


if __name__ == "__main__":
    main()
