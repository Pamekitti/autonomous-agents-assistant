from typing import Dict, Any
from duckduckgo_search import DDGS
import logging
import os

def web_search(query: str, num_results: int = 3) -> Dict[str, Any]:
    """Execute web search using DuckDuckGo API"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=num_results))
        return {
            "success": True,
            "results": [
                {
                    'title': r['title'],
                    'link': r['link'],
                    'snippet': r['body']
                } for r in results
            ],
            "query": query
        }
    except Exception as e:
        logging.error(f"Web search error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "query": query
        } 