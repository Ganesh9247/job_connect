import React, { useState } from 'react';
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
