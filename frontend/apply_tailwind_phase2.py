import os

base_dir = "d:/Job Application/jobconnect/frontend/src"

components = {
    "pages/Jobs.jsx": """import React, { useState, useEffect } from 'react';
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
                const res = await api.get('/jobs');
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
""",
    "components/FilterSidebar.jsx": """import React, { useState } from 'react';
import { Filter } from 'lucide-react';

const FilterSidebar = ({ onFilterChange }) => {
    const [jobType, setJobType] = useState('');
    const [workMode, setWorkMode] = useState('');

    const handleApply = () => {
        onFilterChange({ jobType, workMode });
    };

    const handleClear = () => {
        setJobType('');
        setWorkMode('');
        onFilterChange({ jobType: '', workMode: '' });
    };

    return (
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 sticky top-24">
            <div className="flex items-center gap-2 mb-6 border-b border-gray-100 pb-4">
                <Filter size={20} className="text-brand-600" />
                <h3 className="text-lg font-bold text-slate-800">Filters</h3>
            </div>
            
            <div className="space-y-6">
                <div>
                    <h4 className="font-semibold text-slate-700 mb-3">Job Type</h4>
                    <select 
                        value={jobType} 
                        onChange={(e) => setJobType(e.target.value)}
                        className="w-full border border-gray-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-brand-500 focus:border-brand-500 bg-white"
                    >
                        <option value="">All Types</option>
                        <option value="Full Time">Full Time</option>
                        <option value="Part Time">Part Time</option>
                        <option value="Contract">Contract</option>
                        <option value="Internship">Internship</option>
                    </select>
                </div>

                <div>
                    <h4 className="font-semibold text-slate-700 mb-3">Work Mode</h4>
                    <select 
                        value={workMode} 
                        onChange={(e) => setWorkMode(e.target.value)}
                        className="w-full border border-gray-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-brand-500 focus:border-brand-500 bg-white"
                    >
                        <option value="">All Modes</option>
                        <option value="On-site">On-site</option>
                        <option value="Remote">Remote</option>
                        <option value="Hybrid">Hybrid</option>
                    </select>
                </div>

                <div className="pt-4 flex flex-col gap-3">
                    <button onClick={handleApply} className="w-full bg-brand-600 text-white py-2.5 rounded-lg font-medium hover:bg-brand-700 transition-colors shadow-sm">
                        Apply Filters
                    </button>
                    <button onClick={handleClear} className="w-full bg-gray-100 text-slate-700 py-2.5 rounded-lg font-medium hover:bg-gray-200 transition-colors">
                        Clear All
                    </button>
                </div>
            </div>
        </div>
    );
};

export default FilterSidebar;
""",
    "pages/JobDetails.jsx": """import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';
import { AuthContext } from '../context/AuthContext';
import { MapPin, Briefcase, DollarSign, Clock, Building, ArrowLeft, BookmarkPlus, Send } from 'lucide-react';

const JobDetails = () => {
    const { id } = useParams();
    const [job, setJob] = useState(null);
    const [loading, setLoading] = useState(true);
    const { user } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchJob = async () => {
            try {
                const res = await api.get(`/jobs/${id}`);
                setJob(res.data);
            } catch (err) {
                console.error("Error fetching job details", err);
            } finally {
                setLoading(false);
            }
        };
        fetchJob();
    }, [id]);

    const handleApply = async () => {
        if (!user) {
            navigate('/login');
            return;
        }
        
        try {
            await api.post('/applications', {
                jobId: job.id,
                expectedSalary: job.minSalary,
                noticePeriod: 30
            });
            alert("Application submitted successfully!");
        } catch (err) {
            alert(err.response?.data?.message || "Failed to submit application");
        }
    };

    if (loading) return <div className="min-h-screen flex justify-center items-center"><div className="animate-spin rounded-full h-12 w-12 border-b-2 border-brand-600"></div></div>;
    if (!job) return <div className="min-h-screen flex justify-center items-center text-xl text-slate-500">Job not found.</div>;

    return (
        <div className="min-h-screen bg-gray-50 pt-8 pb-16">
            <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <button onClick={() => navigate(-1)} className="flex items-center gap-2 text-slate-500 hover:text-brand-600 font-medium mb-6 transition-colors">
                    <ArrowLeft size={20} /> Back to jobs
                </button>

                <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                    {/* Header Banner */}
                    <div className="bg-gradient-to-r from-slate-900 to-slate-800 p-8 text-white relative">
                        <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-6">
                            <div>
                                <h1 className="text-3xl font-extrabold mb-2">{job.title}</h1>
                                <div className="flex items-center gap-2 text-slate-300 mb-4 text-lg">
                                    <Building size={20} /> TechNova Solutions (Demo)
                                </div>
                                <div className="flex flex-wrap items-center gap-x-6 gap-y-3 text-sm font-medium">
                                    <span className="flex items-center gap-1.5"><MapPin size={16} className="text-brand-400" /> {job.location}</span>
                                    <span className="flex items-center gap-1.5"><Briefcase size={16} className="text-brand-400" /> {job.jobType}</span>
                                    {job.minSalary && (
                                        <span className="flex items-center gap-1.5"><DollarSign size={16} className="text-brand-400" /> ${job.minSalary.toLocaleString()} - ${job.maxSalary.toLocaleString()}</span>
                                    )}
                                </div>
                            </div>
                            <div className="flex gap-3 w-full md:w-auto">
                                <button onClick={handleApply} className="flex-1 md:flex-none flex items-center justify-center gap-2 bg-brand-500 text-white px-8 py-3 rounded-xl font-bold hover:bg-brand-400 transition-colors shadow-lg">
                                    <Send size={18} /> Apply Now
                                </button>
                                <button className="flex items-center justify-center p-3 rounded-xl bg-white/10 text-white hover:bg-white/20 transition-colors border border-white/20">
                                    <BookmarkPlus size={24} />
                                </button>
                            </div>
                        </div>
                    </div>

                    {/* Content */}
                    <div className="p-8">
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                            <div className="md:col-span-2 space-y-8">
                                <section>
                                    <h2 className="text-xl font-bold text-slate-900 mb-4 border-b border-gray-100 pb-2">Job Description</h2>
                                    <p className="text-slate-700 whitespace-pre-line leading-relaxed">{job.description}</p>
                                </section>

                                <section>
                                    <h2 className="text-xl font-bold text-slate-900 mb-4 border-b border-gray-100 pb-2">Responsibilities</h2>
                                    <p className="text-slate-700 whitespace-pre-line leading-relaxed">{job.responsibilities}</p>
                                </section>

                                <section>
                                    <h2 className="text-xl font-bold text-slate-900 mb-4 border-b border-gray-100 pb-2">Requirements</h2>
                                    <p className="text-slate-700 whitespace-pre-line leading-relaxed">{job.requirements}</p>
                                </section>
                            </div>

                            {/* Sidebar Info */}
                            <div className="md:col-span-1">
                                <div className="bg-slate-50 p-6 rounded-xl border border-slate-100">
                                    <h3 className="font-bold text-slate-900 mb-4">Job Overview</h3>
                                    
                                    <div className="space-y-4">
                                        <div>
                                            <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold mb-1">Posted Date</p>
                                            <p className="text-slate-800 font-medium flex items-center gap-2"><Clock size={16} className="text-brand-500"/> {new Date(job.postedDate).toLocaleDateString()}</p>
                                        </div>
                                        <div>
                                            <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold mb-1">Work Mode</p>
                                            <p className="text-slate-800 font-medium">{job.workMode}</p>
                                        </div>
                                        <div>
                                            <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold mb-1">Experience Required</p>
                                            <p className="text-slate-800 font-medium">{job.minExperience} - {job.maxExperience} years</p>
                                        </div>
                                        <div>
                                            <p className="text-xs text-slate-500 uppercase tracking-wider font-semibold mb-1">Openings</p>
                                            <p className="text-slate-800 font-medium">{job.openings} Positions</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default JobDetails;
""",
    "pages/Dashboard.jsx": """import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import { FileText, Briefcase, Bookmark, Clock, Upload } from 'lucide-react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    const { user } = useContext(AuthContext);
    const [applications, setApplications] = useState([]);
    const [resumeFile, setResumeFile] = useState(null);
    const [uploading, setUploading] = useState(false);

    useEffect(() => {
        const fetchApplications = async () => {
            try {
                const res = await api.get('/applications/my-applications');
                setApplications(res.data);
            } catch (err) {
                console.error("Error fetching applications", err);
            }
        };
        fetchApplications();
    }, []);

    const handleFileChange = (e) => {
        setResumeFile(e.target.files[0]);
    };

    const handleUpload = async (e) => {
        e.preventDefault();
        if (!resumeFile) return;

        setUploading(true);
        const formData = new FormData();
        formData.append('file', resumeFile);

        try {
            await api.post('/profile/resume/upload', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            alert('Resume uploaded successfully!');
            setResumeFile(null);
        } catch (err) {
            alert('Failed to upload resume.');
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 p-4 sm:p-8">
            <div className="max-w-7xl mx-auto">
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900">Job Seeker Dashboard</h1>
                    <p className="text-slate-600 mt-1">Welcome back, {user?.email}</p>
                </div>
                
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    
                    {/* Left Column - Main Content */}
                    <div className="lg:col-span-2 space-y-8">
                        <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                            <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-slate-50/50">
                                <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
                                    <Briefcase size={20} className="text-brand-500" /> My Applications
                                </h2>
                                <span className="bg-brand-100 text-brand-700 text-sm font-bold px-3 py-1 rounded-full">{applications.length} total</span>
                            </div>
                            
                            {applications.length === 0 ? (
                                <div className="p-12 text-center">
                                    <FileText className="mx-auto h-12 w-12 text-gray-300 mb-4" />
                                    <p className="text-slate-600 mb-4">You haven't applied to any jobs yet.</p>
                                    <Link to="/jobs" className="text-brand-600 font-medium hover:underline">Browse open positions</Link>
                                </div>
                            ) : (
                                <div className="divide-y divide-gray-100">
                                    {applications.map(app => (
                                        <div key={app.id} className="p-6 hover:bg-slate-50/50 transition-colors">
                                            <div className="flex justify-between items-start mb-2">
                                                <h3 className="font-bold text-lg text-brand-700 hover:underline cursor-pointer">{app.job.title}</h3>
                                                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                                                    app.status === 'APPLIED' ? 'bg-blue-100 text-blue-800' :
                                                    app.status === 'REJECTED' ? 'bg-red-100 text-red-800' :
                                                    'bg-green-100 text-green-800'
                                                }`}>
                                                    {app.status}
                                                </span>
                                            </div>
                                            <div className="flex items-center gap-4 text-sm text-slate-500">
                                                <span className="flex items-center gap-1"><Clock size={14}/> Applied: {new Date(app.appliedDate).toLocaleDateString()}</span>
                                                <span>Exp Salary: ${app.expectedSalary}</span>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>

                    {/* Right Column - Sidebar */}
                    <div className="lg:col-span-1 space-y-8">
                        
                        {/* Resume Upload Card */}
                        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                            <h2 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2">
                                <FileText size={20} className="text-brand-500" /> Manage Resume
                            </h2>
                            <p className="text-sm text-slate-600 mb-4">Upload your latest resume to make applying faster.</p>
                            
                            <form onSubmit={handleUpload} className="space-y-4">
                                <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-brand-400 transition-colors cursor-pointer relative">
                                    <input 
                                        type="file" 
                                        accept=".pdf" 
                                        onChange={handleFileChange}
                                        className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                                    />
                                    <Upload className="mx-auto h-8 w-8 text-gray-400 mb-2" />
                                    <p className="text-sm text-slate-600 font-medium">
                                        {resumeFile ? resumeFile.name : 'Click or drag PDF to upload'}
                                    </p>
                                </div>
                                
                                <button 
                                    type="submit" 
                                    disabled={!resumeFile || uploading}
                                    className="w-full bg-brand-600 text-white py-2.5 rounded-lg font-medium hover:bg-brand-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                    {uploading ? 'Uploading...' : 'Upload Resume'}
                                </button>
                            </form>
                        </div>
                        
                        {/* Saved Jobs Card */}
                        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                            <h2 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2">
                                <Bookmark size={20} className="text-brand-500" /> Saved Jobs
                            </h2>
                            <div className="text-center p-6 bg-slate-50 rounded-lg border border-slate-100">
                                <p className="text-slate-500 text-sm">You have no saved jobs.</p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
""",
    "pages/PostJob.jsx": """import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import { ArrowLeft, Save, Briefcase } from 'lucide-react';

const PostJob = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        title: '', location: '', description: '', responsibilities: '', requirements: '',
        minExperience: '', maxExperience: '', minSalary: '', maxSalary: '',
        jobType: 'Full Time', workMode: 'On-site', openings: 1, deadline: ''
    });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true); setError('');
        try {
            await api.post('/recruiter/jobs', formData);
            alert("Job posted successfully!");
            navigate('/recruiter');
        } catch (err) {
            setError(err.response?.data?.message || 'Failed to post job. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
            <div className="max-w-4xl mx-auto">
                <button onClick={() => navigate(-1)} className="flex items-center gap-2 text-slate-500 hover:text-brand-600 font-medium mb-6 transition-colors">
                    <ArrowLeft size={20} /> Back to Dashboard
                </button>

                <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                    <div className="p-6 md:p-8 border-b border-gray-100 bg-slate-50/50">
                        <h2 className="text-2xl font-bold text-slate-900 flex items-center gap-2">
                            <Briefcase className="text-brand-500" /> Post a New Job
                        </h2>
                        <p className="text-slate-600 mt-2">Fill in the details below to create a new job posting.</p>
                    </div>

                    <form onSubmit={handleSubmit} className="p-6 md:p-8 space-y-8">
                        {error && <div className="bg-red-50 border-l-4 border-red-500 p-4 text-red-700 rounded-md">{error}</div>}
                        
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Job Title *</label>
                                <input type="text" name="title" value={formData.title} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none transition-all" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Location *</label>
                                <input type="text" name="location" value={formData.location} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none transition-all" />
                            </div>
                        </div>

                        <div>
                            <label className="block text-sm font-semibold text-slate-700 mb-2">Description *</label>
                            <textarea name="description" rows="4" value={formData.description} onChange={handleChange} required 
                                className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none transition-all"></textarea>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Responsibilities *</label>
                                <textarea name="responsibilities" rows="4" value={formData.responsibilities} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none transition-all"></textarea>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Requirements *</label>
                                <textarea name="requirements" rows="4" value={formData.requirements} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none transition-all"></textarea>
                            </div>
                        </div>

                        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Min Exp (Yrs)</label>
                                <input type="number" step="0.1" name="minExperience" value={formData.minExperience} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Max Exp (Yrs)</label>
                                <input type="number" step="0.1" name="maxExperience" value={formData.maxExperience} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Min Salary</label>
                                <input type="number" name="minSalary" value={formData.minSalary} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Max Salary</label>
                                <input type="number" name="maxSalary" value={formData.maxSalary} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 focus:border-brand-500 outline-none" />
                            </div>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                            <div className="md:col-span-1">
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Job Type</label>
                                <select name="jobType" value={formData.jobType} onChange={handleChange} className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 outline-none bg-white">
                                    <option>Full Time</option><option>Part Time</option><option>Contract</option><option>Internship</option>
                                </select>
                            </div>
                            <div className="md:col-span-1">
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Work Mode</label>
                                <select name="workMode" value={formData.workMode} onChange={handleChange} className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 outline-none bg-white">
                                    <option>On-site</option><option>Remote</option><option>Hybrid</option>
                                </select>
                            </div>
                            <div className="md:col-span-1">
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Openings</label>
                                <input type="number" name="openings" value={formData.openings} onChange={handleChange} required min="1" 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 outline-none" />
                            </div>
                            <div className="md:col-span-1">
                                <label className="block text-sm font-semibold text-slate-700 mb-2">Deadline</label>
                                <input type="date" name="deadline" value={formData.deadline} onChange={handleChange} required 
                                    className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-500 outline-none" />
                            </div>
                        </div>

                        <div className="pt-6 border-t border-gray-100 flex justify-end gap-4">
                            <button type="button" onClick={() => navigate(-1)} className="px-6 py-3 font-semibold rounded-lg text-slate-600 bg-slate-100 hover:bg-slate-200 transition-colors">
                                Cancel
                            </button>
                            <button type="submit" disabled={loading} className="px-8 py-3 font-semibold rounded-lg text-white bg-brand-600 hover:bg-brand-700 disabled:opacity-70 shadow-md flex items-center gap-2 transition-colors">
                                <Save size={18} /> {loading ? 'Posting...' : 'Post Job'}
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default PostJob;
"""
}

for filepath, content in components.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Modern UI Phase 2 applied successfully.")
