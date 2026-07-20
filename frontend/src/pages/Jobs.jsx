import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import FilterSidebar from '../components/FilterSidebar';
import { Search, MapPin, Briefcase, DollarSign, Clock } from 'lucide-react';

const Jobs = () => {
    const [jobs, setJobs] = useState([]);
    const [filteredJobs, setFilteredJobs] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchJobs = async () => {
            try {
                const res = await api.get('/jobs/public');
                setJobs(res.data);
                setFilteredJobs(res.data);
            } catch (err) {
                console.error("Error fetching jobs", err);
            } finally {
                setLoading(false);
            }
        };
        fetchJobs();
    }, []);

    const handleSearch = (e) => {
        const term = e.target.value.toLowerCase();
        setSearchTerm(term);
        const filtered = jobs.filter(job => 
            job.title.toLowerCase().includes(term) || 
            job.location.toLowerCase().includes(term) ||
            job.description.toLowerCase().includes(term)
        );
        setFilteredJobs(filtered);
    };

    const handleFilterChange = (filters) => {
        let result = jobs;
        
        if (searchTerm) {
            result = result.filter(job => 
                job.title.toLowerCase().includes(searchTerm) || 
                job.location.toLowerCase().includes(searchTerm)
            );
        }

        if (filters.jobType) {
            result = result.filter(job => job.jobType === filters.jobType);
        }
        
        if (filters.workMode) {
            result = result.filter(job => job.workMode === filters.workMode);
        }

        setFilteredJobs(result);
    };

    const formatDate = (dateString) => {
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    };

    return (
        <div className="min-h-screen bg-gray-50 pt-8 pb-16">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                
                {/* Search Header */}
                <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 mb-8 flex flex-col sm:flex-row gap-4 items-center">
                    <div className="relative flex-grow w-full">
                        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <Search className="h-5 w-5 text-gray-400" />
                        </div>
                        <input 
                            type="text" 
                            placeholder="Search by job title, keyword or location..." 
                            value={searchTerm}
                            onChange={handleSearch}
                            className="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-lg transition-all"
                        />
                    </div>
                    <button className="bg-brand-600 text-white px-8 py-3 rounded-xl font-semibold hover:bg-brand-700 transition-colors w-full sm:w-auto shadow-sm">
                        Find Jobs
                    </button>
                </div>

                <div className="flex flex-col lg:flex-row gap-8">
                    {/* Sidebar */}
                    <div className="w-full lg:w-1/4">
                        <FilterSidebar onFilterChange={handleFilterChange} />
                    </div>

                    {/* Job Listings */}
                    <div className="w-full lg:w-3/4">
                        <div className="mb-4 flex justify-between items-center">
                            <h2 className="text-xl font-bold text-slate-800">Showing {filteredJobs.length} Jobs</h2>
                            <select className="border border-gray-300 rounded-lg px-3 py-2 text-sm bg-white focus:ring-brand-500 focus:border-brand-500">
                                <option>Most Relevant</option>
                                <option>Newest</option>
                            </select>
                        </div>
                        
                        {loading ? (
                            <div className="flex justify-center items-center py-20">
                                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-brand-600"></div>
                            </div>
                        ) : filteredJobs.length === 0 ? (
                            <div className="bg-white rounded-2xl p-12 text-center border border-gray-100 shadow-sm">
                                <Search className="mx-auto h-12 w-12 text-gray-300 mb-4" />
                                <h3 className="text-lg font-medium text-slate-900 mb-1">No jobs found</h3>
                                <p className="text-slate-500">Try adjusting your search or filters to find what you're looking for.</p>
                            </div>
                        ) : (
                            <div className="space-y-4">
                                {filteredJobs.map(job => (
                                    <div key={job.id} className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow group">
                                        <div className="flex flex-col sm:flex-row justify-between items-start gap-4">
                                            <div>
                                                <Link to={`/jobs/${job.id}`} className="text-xl font-bold text-brand-600 hover:text-brand-800 transition-colors group-hover:underline">
                                                    {job.title}
                                                </Link>
                                                
                                                <div className="flex flex-wrap items-center gap-4 mt-3 text-sm text-slate-600">
                                                    <span className="flex items-center gap-1.5"><MapPin size={16} className="text-gray-400" /> {job.location}</span>
                                                    <span className="flex items-center gap-1.5"><Briefcase size={16} className="text-gray-400" /> {job.jobType}</span>
                                                    {job.minSalary && (
                                                        <span className="flex items-center gap-1.5"><DollarSign size={16} className="text-gray-400" /> ${job.minSalary.toLocaleString()} - ${job.maxSalary.toLocaleString()}</span>
                                                    )}
                                                </div>
                                                
                                                <p className="mt-4 text-slate-600 line-clamp-2">
                                                    {job.description}
                                                </p>
                                            </div>
                                            
                                            <div className="flex flex-col items-end justify-between h-full min-w-[120px]">
                                                <span className={`px-3 py-1 text-xs font-semibold rounded-full ${
                                                    job.workMode === 'Remote' ? 'bg-green-100 text-green-800' :
                                                    job.workMode === 'Hybrid' ? 'bg-blue-100 text-blue-800' :
                                                    'bg-purple-100 text-purple-800'
                                                }`}>
                                                    {job.workMode}
                                                </span>
                                                
                                                <span className="flex items-center gap-1.5 text-xs text-slate-400 mt-4 sm:mt-auto">
                                                    <Clock size={14} /> {formatDate(job.postedDate)}
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Jobs;
