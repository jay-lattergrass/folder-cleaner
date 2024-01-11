# File Organization Utility

A Python script for moving and organizing files from a root directory to a new targeted directory and subdirectories based on file extensions.

## Files

- `main.py`: Main script to run the file organization utility.
- `settings.py`: Python script containing customizable settings such as `ROOT_DIR`, `TARGET_DIR`, subdirectories, and file extensions.
- `transfer.py`: Python script containing the file transfer and organization logic.
- `tests/test_directory_perms.py`: Test script for testing directory permissions.

## Configuration

1. Open `settings.py` to customize the following parameters:
   - `ROOT_DIR`: The root directory from which files will be organized.
   - `TARGET_DIR`: The targeted directory where organized files will be moved.
   - Customize subdirectories and file extensions based on your preferences.

## Usage

1. Ensure you have Python installed on your machine.
2. Navigate to the project directory:

   ```bash
   cd /path/to/your/project
   ```

3. Run the file organization utility using the following command:

   ```bash
   python main.py
   ```

4. The utility will move and organize files based on the configured settings.

## Example

```bash
python main.py
```

## Testing

Run the directory permissions test using:

```bash
python -m unittest tests.test_directory_perms
```

## Contributing

Feel free to contribute or report issues. Pull requests are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
