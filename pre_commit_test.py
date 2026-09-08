import subprocess
import sys


def _run(cmd: list[str]) -> int:
    result = subprocess.run(cmd, check=False)  # noqa: S603
    return result.returncode


def main() -> None:
    print("Installing dependencies...")
    if _run(["uv", "sync"]) != 0:
        print("Failed to install dependencies")
        sys.exit(1)

    print("Running tests...")
    for module in ("calculator", "logger", "notifier"):
        cmd = ["uv", "run", "python", "-m", "nose2", "-v", "-s", f"src/{module}/test/"]
        if _run(cmd) != 0:
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
