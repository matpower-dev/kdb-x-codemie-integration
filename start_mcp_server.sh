# Get the directory where the script itself is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ARG=${1:-5896}
# Change into that directory
cd "$SCRIPT_DIR" || exit 1
export PYTHONPATH="$SCRIPT_DIR":$PYTHONPATH
. ~/myenv/bin/activate
. .env
mcp-server --db.port=$ARG
