#!/usr/bin/env python3
"""
Standalone crawler execution script for scheduled GitHub Actions runs
"""

import asyncio
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from crawler.crawler import CrawlerManager

async def main():
    """
    Execute crawler job
    """
    print("[CRAWLER] Starting obesity resource discovery...")
    
    crawler = CrawlerManager()
    
    if not crawler.is_active():
        print("[CRAWLER] Crawler is disabled in configuration")
        return
    
    try:
        job_id = await crawler.run_crawl()
        print(f"[CRAWLER] Job {job_id} completed successfully")
        status = crawler.get_status()
        print(f"[CRAWLER] Status: {status}")
    except Exception as e:
        print(f"[CRAWLER] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
