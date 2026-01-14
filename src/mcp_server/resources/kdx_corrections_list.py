import logging
from typing import List
from mcp.types import TextContent
from mcp_server.utils.kdbx import get_kdb_connection
from mcp_server.utils.format_utils import format_data_for_display
from mcp_server.utils.embeddings_helpers import get_embedding_config
from pandas import read_csv

logger = logging.getLogger(__name__)


async def kdbx_get_corrections_impl(table: str) -> List[TextContent]:
    try:
        final_output = read_csv() 
        corrections = read_csv("/home/matthew/kdb-x-mcp-server/corrections.csv")
        return [TextContent(type="text", text=corrections.to_string())]
    except Exception as error:
        logger.error(f"Failed to get correction list '{table}': {error}")
        error_output = f"\n CORRECTION FETCH FAILED: {table}\n{'=' *60}\nError: {error}"
        return [TextContent(type="text", text=error_output)]


def register_resources(mcp_server):
    @mcp_server.resource("kdbx://corrections")
    async def kdbx_get_corrections() -> List[TextContent]:
        """
        Generate all user corrections. The AI should consider this when making queries, it should aim not to repeat known "BAD" querys
        Returns:
            List[TextContent]: The list of bad queries and good queries, along with the user request that corresponds to both.
        """
        return await kdbx_get_corrections_impl()

    return ['kdbx://corrections']

