import json
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import requests
from bs4 import BeautifulSoup
import feedparser

class CrawlerManager:
    """
    Manages web crawler for discovering and indexing obesity resources
    """
    
    def __init__(self):
        self.config_path = Path("../../crawler-config")
        self.config = self._load_config()
        self.active = self.config.get("crawler_settings", {}).get("active", True)
        self.last_run = None
        self.activity_log = []
    
    def _load_config(self) -> Dict[str, Any]:
        """Load crawler configuration from JSON files"""
        config = {}
        
        # Load search criteria
        search_criteria_path = self.config_path / "search-criteria.json"
        if search_criteria_path.exists():
            with open(search_criteria_path, 'r') as f:
                config.update(json.load(f))
        
        # Load relevance rules
        relevance_rules_path = self.config_path / "relevance-rules.json"
        if relevance_rules_path.exists():
            with open(relevance_rules_path, 'r') as f:
                config.update(json.load(f))
        
        return config
    
    def update_config(self, new_settings: Dict[str, Any]):
        """
        Update crawler configuration
        """
        for key, value in new_settings.items():
            if key == "crawler_settings":
                self.config["crawler_settings"].update(value)
            elif key == "search_sources":
                self.config["search_sources"] = value
            elif key == "relevance_scoring":
                self.config["relevance_scoring"] = value
            else:
                self.config[key] = value
        
        self._save_config()
    
    def _save_config(self):
        """Save configuration back to JSON files"""
        # In production, would save to both search-criteria.json and relevance-rules.json
        pass
    
    async def run_crawl(self) -> str:
        """
        Execute crawler to discover new obesity resources
        """
        job_id = f"job_{datetime.now().isoformat()}"
        self.last_run = datetime.now()
        
        try:
            results = await self._execute_crawl()
            self._log_activity({
                "job_id": job_id,
                "timestamp": self.last_run.isoformat(),
                "status": "completed",
                "results_count": len(results),
                "results": results
            })
            return job_id
        except Exception as e:
            self._log_activity({
                "job_id": job_id,
                "timestamp": self.last_run.isoformat(),
                "status": "failed",
                "error": str(e)
            })
            raise
    
    async def _execute_crawl(self) -> List[Dict[str, Any]]:
        """
        Execute crawling across configured sources
        """
        results = []
        
        # Crawl each configured source
        for source in self.config.get("search_sources", []):
            if not source.get("enabled", False):
                continue
            
            source_name = source.get("name")
            
            if source_name == "PubMed":
                results.extend(await self._crawl_pubmed(source))
            elif source_name == "ClinicalTrials.gov":
                results.extend(await self._crawl_clinical_trials(source))
            elif source_name == "WHO Guidelines":
                results.extend(await self._crawl_who(source))
        
        return results
    
    async def _crawl_pubmed(self, source: Dict) -> List[Dict]:
        """
        Crawl PubMed for obesity research articles
        """
        # In production, would use:
        # - NCBI E-utilities API (Entrez)
        # - Search keywords from config
        # - Filter by date, publication type, etc.
        # - Extract: title, authors, abstract, DOI, journal, year
        # - Check relevance against criteria
        # - Return high-confidence results
        
        return []
    
    async def _crawl_clinical_trials(self, source: Dict) -> List[Dict]:
        """
        Crawl ClinicalTrials.gov for obesity trials
        """
        # In production, would use:
        # - ClinicalTrials.gov API
        # - Search keywords and trial phases from config
        # - Filter by status (Recruiting, Active)
        # - Extract: trial ID, title, status, enrollment, outcomes
        # - Check against inclusion criteria
        # - Return matching trials
        
        return []
    
    async def _crawl_who(self, source: Dict) -> List[Dict]:
        """
        Crawl WHO for obesity guidelines
        """
        # In production, would:
        # - Fetch WHO publications page
        # - Filter for obesity-related guidelines
        # - Extract publication details
        # - Download and parse guidelines
        # - Index and store
        
        return []
    
    def _log_activity(self, activity: Dict[str, Any]):
        """
        Log crawler activity
        """
        self.activity_log.append(activity)
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current crawler status
        """
        return {
            "active": self.active,
            "last_run": self.last_run.isoformat() if self.last_run else None,
            "update_frequency_days": self.config.get("crawler_settings", {}).get("update_frequency_days", 7),
            "recent_activity": self.activity_log[-5:] if self.activity_log else []
        }
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get current crawler configuration
        """
        return self.config
    
    def is_active(self) -> bool:
        """
        Check if crawler is active
        """
        return self.active
