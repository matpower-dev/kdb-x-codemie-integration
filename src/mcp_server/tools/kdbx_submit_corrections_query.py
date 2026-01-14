import logging
import pykx as kx
import json
from typing import Dict, Any
from mcp_server.utils.kdbx import get_kdb_connection

logger = logging.getLogger(__name__)
MAX_ROWS_RETURNED = 1000

async def kdbx_run_submit_corrections_query_impl(query: str, badquery: str, goodquery:str) -> Dict[str, Any]:
    try:
        conn = get_kdb_connection()
        to_run = f"INSERT INTO corrections (QUERY, BAD, GOOD) VALUES ('{query}', '{badquery}', '{goodquery}')"
        conn('{r:.s.e x}', kx.CharVector(to_run))
        return {
           "status": "success",
           "data": to_run,
           "message": "corrections table updated",
        }
    except Exception as e:
        logger.error(f"Query failed: {e}")
        return {
                "status": "error",
                "error_type": "update_error",
                "message": "Error on updating the corrections table",
                "technical_details": str(e)
            }
        return {"status": "error", "message": str(e)}


def register_tools(mcp_server):
    @mcp_server.tool()
    async def kdbx_submit_corrections_query(query: str, badquery: str, goodquery: str) -> Dict[str, Any]:
        """
        Execute a SQL query and return structured results only to be used on kdb and not on kdbai.

        This function processes SQL SELECT statements to retrieve data from the underlying
        database. It parses the query, executes it against the data source, and returns
        the results in a structured format suitable for further analysis or display.

        Use the kdbx_sql_query_guidance resource when creating queries


        Supported query types:
            - SELECT statements with column specifications
            - WHERE clauses for filtering
            - ORDER BY for result sorting
            - LIMIT for result pagination
            - Basic aggregation functions (COUNT, SUM, AVG, etc.)

        For query syntax and examples, see: file://guidance/kdbx-sql-queries

        Args:
            query (str): SQL SELECT query string to execute. Must be a valid SQL statement
                        following standard SQL syntax conventions.

        Returns:
            Dict[str, Any]: Query execution results.
        """
        return await kdbx_run_submit_corrections_query_impl(query=query, badquery=badquery, goodquery=goodquery)

    return ['kdbx_run_submit_corrections_query']
