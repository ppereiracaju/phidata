import os
import sys
import logging
from dotenv import load_dotenv

class EnvironmentSetup:
    def __init__(self):
        # Initialize paths
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.dirname(self.current_dir)
        self.grandparent_dir = os.path.dirname(self.parent_dir)
        self.env_file_path = None

    def locate_env_file(self):
        # Determine the correct .env file path
        if os.path.isfile(f"{self.current_dir}/.env"):
            self.env_file_path = self.current_dir
        elif os.path.isfile(f"{self.parent_dir}/.env"):
            self.env_file_path = self.parent_dir
        elif os.path.isfile(f"{self.grandparent_dir}/.env"):
            self.env_file_path = self.grandparent_dir
        else:
            raise Exception("Missing .env file")
        
        # Log the determined path
        logging.info(f".env file found at: {self.env_file_path}")

    def setup_path(self):
        # Insert the directory path into sys.path
        sys.path.insert(0, self.env_file_path)
        logging.info(f"Added to sys.path: {self.env_file_path}")

    def load_env_variables(self):
        # Load the .env file
        if load_dotenv(os.path.join(self.env_file_path, ".env"), override=True):
            logging.info(".env file loaded successfully")
        else:
            logging.error("Failed to load .env file")

    def setup_environment(self):
        # Run the setup process
        self.locate_env_file()
        self.setup_path()
        self.load_env_variables()

        # Optional: log directory information
        logging.info("Setup complete with the following paths:")
        logging.info(f"Current Directory: {self.current_dir}")
        logging.info(f"Parent Directory: {self.parent_dir}")
        logging.info(f"Grandparent Directory: {self.grandparent_dir}")

    def get_env_variable(self, key):
        """Retrieve the value of an environment variable."""
        value = os.getenv(key)
        if value is None:
            logging.warning(f"Environment variable '{key}' not found.")
        return value

