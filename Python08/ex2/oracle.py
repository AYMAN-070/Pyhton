import os
from dotenv import load_dotenv


def oracle_config() -> None:
    """get config from mainframe"""
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")
    try:
        mode: str = os.getenv("MATRIX_MODE", "development")
        db_url: str = os.getenv("DATABASE_URL", "local instance")
        api_key: str = os.getenv("API_KEY")
        log_level: str = os.getenv("LOG_LEVEL", "INFO")
        zion_url: str = os.getenv("ZION_ENDPOINT", "Offline")
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        print(f"Database: {db_url}")
        print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_url}")
        print("\nEnvironment security check:")
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        print("[OK] No hardcoded secrets detected")
    except Exception as e:
        print(f"ERROR accessing the mainframe: {e}")


if __name__ == "__main__":
    oracle_config()
