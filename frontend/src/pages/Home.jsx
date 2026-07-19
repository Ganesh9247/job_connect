import React from 'react';
import { Link } from 'react-router-dom';
import { Search, Briefcase, Users, TrendingUp, ArrowRight } from 'lucide-react';

const Home = () => {
    return (
        <div className="min-h-screen bg-gray-50 flex flex-col">
            {/* Hero Section */}
            <div className="relative overflow-hidden bg-white">
                <div className="absolute inset-0 bg-gradient-to-br from-brand-50 to-white z-0"></div>
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pt-20 pb-24 sm:pt-32 sm:pb-40">
                    <div className="text-center max-w-3xl mx-auto">
                        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-slate-900 tracking-tight mb-6">
                            Find your next dream job with <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-indigo-600">JobConnect</span>
                        </h1>
                        <p className="text-lg sm:text-xl text-slate-600 mb-10">
                            Discover thousands of job opportunities or find the perfect candidate. Your professional future starts here.
                        </p>
                        <div className="flex flex-col sm:flex-row justify-center gap-4">
                            <Link to="/jobs" className="flex items-center justify-center gap-2 bg-brand-600 text-white px-8 py-3.5 rounded-xl font-semibold text-lg hover:bg-brand-700 hover:shadow-lg transition-all">
                                <Search size={20} /> Browse Jobs
                            </Link>
                            <Link to="/register" className="flex items-center justify-center gap-2 bg-white text-brand-600 border border-brand-200 px-8 py-3.5 rounded-xl font-semibold text-lg hover:bg-brand-50 transition-all">
                                <Briefcase size={20} /> Post a Job
                            </Link>
                        </div>
                    </div>
                </div>
            </div>

            {/* Features Section */}
            <div className="py-20 bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-brand-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <Briefcase className="text-brand-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Thousands of Jobs</h3>
                            <p className="text-slate-600 leading-relaxed">Access a massive pool of opportunities from top companies worldwide, updated daily.</p>
                        </div>
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-indigo-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <Users className="text-indigo-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Top Talent</h3>
                            <p className="text-slate-600 leading-relaxed">Employers can easily filter and connect with verified, highly-skilled professionals.</p>
                        </div>
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-blue-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <TrendingUp className="text-blue-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Career Growth</h3>
                            <p className="text-slate-600 leading-relaxed">Advance your career with smart matching and personalized job recommendations.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            {/* Call to action footer */}
            <div className="bg-slate-900 py-16 mt-auto">
                <div className="max-w-4xl mx-auto px-4 text-center">
                    <h2 className="text-3xl font-bold text-white mb-6">Ready to take the next step?</h2>
                    <Link to="/register" className="inline-flex items-center gap-2 bg-brand-500 text-white px-8 py-3 rounded-xl font-semibold hover:bg-brand-400 transition-colors">
                        Create an Account <ArrowRight size={20} />
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default Home;
