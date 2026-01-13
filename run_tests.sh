# Get the directory where the script itself is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change into that directory
cd "$SCRIPT_DIR" || exit 1
export PYTHONPATH="$SCRIPT_DIR":$PYTHONPATH
. ~/mcp-venv/bin/activate
. .env
PYTHONPATH=/home/username/Documents:$PYTHONPATH
python -m unittest discover -s tests
