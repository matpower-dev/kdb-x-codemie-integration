import logging
import pykx as kx
import json
from typing import Dict, Any
from mcp_server.utils.kdbx import get_kdb_connection

logger = logging.getLogger(__name__)
MAX_ROWS_RETURNED = 1000

async def run_correction_impl(sqlSelectQuery: str) -> Dict[str, Any]:
    try:
        conn = get_kdb_connection()
        
        # below query gets kdbx table data back as json for correct conversion of different datatypes
        result = conn('{r:.s.e x;`rowCount`data!(count r;.j.j y sublist r)}', kx.CharVector(sqlSelectQuery), MAX_ROWS_RETURNED)
        total = int(result['rowCount'])
        if 0==total:
            return {"status": "success", "data": [], "message": "No rows returned"}
        # parse json result
        rows = json.loads(result['data'].py().decode('utf-8'))
        return {
            "status": "success",
            "data": "No data returned",
            "message": f"Testing",
        }

        logger.info(f"Query returned {total} rows.")
        return {"status": "success", "data": rows}

    except Exception as e:
        logger.error(f"Query failed: {e}")
        if ".s.e" in str(e):
            logger.error(f"It looks like the SQL interface is not loaded. You can load it manually by running .s.init[]:")
            return {
                "status": "error",
                "error_type": "sql_interface_not_loaded",
                "message": "It looks like the SQL interface is not loaded in the KDB-X database. Please initialize it by running `.s.init[]` in your KDB-X session, or contact your system administrator.",
                "technical_details": str(e)
            }
        return {"status": "error", "message": str(e)}


def register_tools(mcp_server):
    @mcp_server.tool()
    async def kdbx_correction_query(query: str) -> Dict[str, Any]:
        return await run_correction_impl(sqlSelectQuery=query)

    return ['kdbx_run_sql_query']