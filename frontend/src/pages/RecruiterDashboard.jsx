import React, { useContext, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import { Briefcase, Plus, Users, MapPin, Building } from 'lucide-react';

const RecruiterDashboard = () => {
    const { user } = useContext(AuthContext);
    const [jobs, setJobs] = useState([]);
    
    useEffect(() => {
        const fetchJobs = async () => {
            try {
                const res = await api.get('/recruiter/jobs');
                setJobs(res.data);
            } catch (err) {
                console.error("Error fetching posted jobs", err);
            }
        };
        fetchJobs();
    }, []);

    return (
        <div className="min-h-screen bg-gray-50 p-4 sm:p-8">
            <div className="max-w-7xl mx-auto">
                <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900">Recruiter Dashboard</h1>
                        <p className="text-slate-600 mt-1">Welcome back, {user?.email}</p>
                    </div>
                    <Link to="/recruiter/post-job" className="flex items-center gap-2 bg-brand-600 text-white px-6 py-2.5 rounded-lg font-medium hover:bg-brand-700 transition-colors shadow-sm">
                        <Plus size={20} /> Post New Job
                    </Link>
                </div>
                
                <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                    <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-slate-50/50">
                        <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
                            <Briefcase size={20} className="text-brand-500" /> My Posted Jobs
                        </h2>
                        <span className="bg-brand-100 text-brand-700 text-sm font-bold px-3 py-1 rounded-full">{jobs.length} total</span>
                    </div>
                    
                    {jobs.length === 0 ? (
                        <div className="p-12 text-center flex flex-col items-center">
                            <div className="bg-gray-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                                <Briefcase className="text-gray-400" size={32} />
                            </div>
                            <p className="text-lg text-slate-600 mb-4">You haven't posted any jobs yet.</p>
                            <Link to="/recruiter/post-job" className="text-brand-600 font-medium hover:underline">Create your first job posting</Link>
                        </div>
                    ) : (
                        <div className="overflow-x-auto">
                            <table className="w-full text-left border-collapse">
                                <thead>
                                    <tr className="bg-gray-50 border-b border-gray-100">
                                        <th className="p-4 font-semibold text-slate-600 text-sm uppercase tracking-wider">Job Title</th>
                                        <th className="p-4 font-semibold text-slate-600 text-sm uppercase tracking-wider">Location</th>
                                        <th className="p-4 font-semibold text-slate-600 text-sm uppercase tracking-wider">Status</th>
                                        <th className="p-4 font-semibold text-slate-600 text-sm uppercase tracking-wider">Openings</th>
                                        <th className="p-4 font-semibold text-slate-600 text-sm uppercase tracking-wider">Actions</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-100">
                                    {jobs.map(job => (
                                        <tr key={job.id} className="hover:bg-slate-50/50 transition-colors">
                                            <td className="p-4">
                                                <div className="font-semibold text-slate-900">{job.title}</div>
                                                <div className="text-sm text-slate-500 mt-1">{job.jobType}</div>
                                            </td>
                                            <td className="p-4">
                                                <div className="flex items-center gap-1 text-slate-600">
                                                    <MapPin size={16} /> {job.location}
                                                </div>
                                            </td>
                                            <td className="p-4">
                                                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${job.status === 'ACTIVE' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                                                    {job.status}
                                                </span>
                                            </td>
                                            <td className="p-4 text-slate-600 font-medium">{job.openings}</td>
                                            <td className="p-4">
                                                <button className="flex items-center gap-1 text-brand-600 hover:text-brand-800 font-medium bg-brand-50 hover:bg-brand-100 px-3 py-1.5 rounded-md transition-colors">
                                                    <Users size={16} /> Applicants
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default RecruiterDashboard;
