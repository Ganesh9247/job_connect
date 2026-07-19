import React, { useContext, useEffect, useState } from 'react';
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
            await api.post('/profile/resume', formData, {
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
