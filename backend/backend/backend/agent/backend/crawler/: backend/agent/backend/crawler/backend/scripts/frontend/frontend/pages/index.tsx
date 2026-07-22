import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="max-w-6xl mx-auto px-4 py-16">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            Obesity Knowledge Base
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            AI-powered clinical decision support for obesity management
          </p>
          <div className="flex gap-4 justify-center">
            <Link href="/dashboard">
              <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition">
                Admin Dashboard
              </button>
            </Link>
            <Link href="/chat">
              <button className="bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition">
                Ask a Question
              </button>
            </Link>
          </div>
        </div>

        {/* Features */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="text-3xl mb-3">🤖</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Q&A Agent</h3>
            <p className="text-gray-600">
              Ask clinical questions and get answers backed by authoritative obesity research and guidelines.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="text-3xl mb-3">🔍</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Web Crawler</h3>
            <p className="text-gray-600">
              Automatically discovers and indexes new obesity resources from PubMed, ClinicalTrials.gov, and more.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="text-3xl mb-3">⚙️</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Settings</h3>
            <p className="text-gray-600">
              Configure crawler search criteria, relevance thresholds, and data sources from the admin dashboard.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
