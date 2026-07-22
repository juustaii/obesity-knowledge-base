import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface CrawlerStatus {
  active: boolean;
  last_run: string;
  update_frequency_days: number;
  recent_activity: any[];
}

interface CrawlerConfig {
  keywords?: string[];
  sources_enabled?: Record<string, boolean>;
  min_relevance_score?: number;
  update_frequency_days?: number;
}

export default function Dashboard() {
  const [crawlerStatus, setCrawlerStatus] = useState<CrawlerStatus | null>(null);
  const [config, setConfig] = useState<CrawlerConfig | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  useEffect(() => {
    fetchStatus();
    fetchConfig();
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_BASE}/api/v1/crawler/status`);
      setCrawlerStatus(response.data);
    } catch (err) {
      setError('Failed to fetch crawler status');
    } finally {
      setLoading(false);
    }
  };

  const fetchConfig = async () => {
    try {
      const response = await axios.get(`${API_BASE}/api/v1/crawler/config`);
      setConfig(response.data);
    } catch (err) {
      setError('Failed to fetch configuration');
    }
  };

  const handleRunCrawler = async () => {
    try {
      setLoading(true);
      await axios.post(`${API_BASE}/api/v1/crawler/run`);
      setSuccessMessage('Crawler job started successfully!');
      setTimeout(() => {
        fetchStatus();
        setSuccessMessage(null);
      }, 2000);
    } catch (err) {
      setError('Failed to start crawler');
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateConfig = async (newConfig: CrawlerConfig) => {
    try {
      setLoading(true);
      await axios.post(`${API_BASE}/api/v1/crawler/config`, newConfig);
      setSuccessMessage('Configuration updated successfully!');
      setTimeout(() => {
        fetchConfig();
        setSuccessMessage(null);
      }, 2000);
    } catch (err) {
      setError('Failed to update configuration');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Obesity Knowledge Base</h1>
          <p className="text-gray-600">Admin Dashboard - Crawler & Q&A Agent Management</p>
        </div>

        {/* Alert Messages */}
        {error && (
          <div className="mb-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}
        {successMessage && (
          <div className="mb-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded">
            {successMessage}
          </div>
        )}

        {/* Status Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          {/* Crawler Status */}
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Crawler Status</h2>
            {crawlerStatus ? (
              <>
                <div className="mb-3">
                  <span className="text-sm text-gray-600">Status: </span>
                  <span className={`font-semibold ${
                    crawlerStatus.active ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {crawlerStatus.active ? '🟢 Active' : '🔴 Inactive'}
                  </span>
                </div>
                <div className="mb-3">
                  <span className="text-sm text-gray-600">Last Run: </span>
                  <span className="font-mono text-sm">
                    {crawlerStatus.last_run ? new Date(crawlerStatus.last_run).toLocaleString() : 'Never'}
                  </span>
                </div>
                <div>
                  <span className="text-sm text-gray-600">Update Frequency: </span>
                  <span className="font-semibold">{crawlerStatus.update_frequency_days} days</span>
                </div>
              </>
            ) : (
              <p className="text-gray-500">Loading...</p>
            )}
          </div>

          {/* Recent Activity */}
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Activity</h2>
            {crawlerStatus?.recent_activity.length ? (
              <ul className="text-sm space-y-2">
                {crawlerStatus.recent_activity.slice(0, 3).map((activity, idx) => (
                  <li key={idx} className="text-gray-600">
                    <span className="font-mono text-xs bg-gray-100 px-2 py-1 rounded">
                      {new Date(activity.timestamp).toLocaleDateString()}
                    </span>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-500">No recent activity</p>
            )}
          </div>

          {/* Quick Actions */}
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
            <button
              onClick={handleRunCrawler}
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-2 px-4 rounded transition"
            >
              {loading ? 'Running...' : '▶️ Run Crawler Now'}
            </button>
          </div>
        </div>

        {/* Configuration Section */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-semibold text-gray-900 mb-6">Crawler Configuration</h2>
          
          <div className="space-y-4">
            {/* Search Keywords */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Search Keywords
              </label>
              <textarea
                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                rows={4}
                defaultValue="obesity treatment, weight loss, bariatric surgery, GLP-1, metabolic syndrome"
                placeholder="Enter keywords separated by commas"
              />
            </div>

            {/* Update Frequency */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Update Frequency (days)
              </label>
              <input
                type="number"
                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                defaultValue={7}
                min={1}
              />
            </div>

            {/* Data Sources */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Data Sources
              </label>
              <div className="space-y-2">
                {['PubMed', 'ClinicalTrials.gov', 'WHO Guidelines'].map((source) => (
                  <label key={source} className="flex items-center">
                    <input
                      type="checkbox"
                      defaultChecked
                      className="w-4 h-4 text-blue-600 rounded focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="ml-2 text-sm text-gray-700">{source}</span>
                  </label>
                ))}
              </div>
            </div>

            {/* Relevance Threshold */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Minimum Relevance Score
              </label>
              <input
                type="number"
                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                defaultValue={0.7}
                min={0}
                max={1}
                step={0.1}
              />
            </div>
          </div>

          <button
            onClick={() => handleUpdateConfig({})}
            disabled={loading}
            className="mt-6 bg-green-600 hover:bg-green-700 disabled:bg-gray-400 text-white font-semibold py-2 px-6 rounded transition"
          >
            {loading ? 'Saving...' : '✅ Save Configuration'}
          </button>
        </div>
      </div>
    </div>
  );
}
