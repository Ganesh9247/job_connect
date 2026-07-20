import React, { useState, useEffect, useContext } from 'react';
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
                const res = await api.get(`/jobs/public/${id}`);
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
