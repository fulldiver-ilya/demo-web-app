import argparse

from app import app

def main():
    parser = argparse.ArgumentParser(description="Boostrap Lands Workshop application.")
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Run in Debug mode",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5050,
        help="Port to run the application on",
    )

    args = parser.parse_args()

    app.run(debug=args.debug, host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()
