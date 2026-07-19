import os

base_dir = "src"

files = {
    "components/FilterSidebar.jsx": """import React from 'react';
import './FilterSidebar.css';

const FilterSidebar = ({ filters, setFilters, onApply }) => {
    const handleChange = (e) => {
        setFilters({ ...filters, [e.target.name]: e.target.value });
    };

    return (
        <div className="filter-sidebar">
            <h3>Filters</h3>
            <div className="filter-group">
                <label>Keyword</label>
                <input type="text" name="keyword" value={filters.keyword || ''} onChange={handleChange} placeholder="Java, React..." />
            </div>
            <div className="filter-group">
                <label>Location</label>
                <input type="text" name="location" value={filters.location || ''} onChange={handleChange} placeholder="City, State" />
            </div>
            <div className="filter-group">
                <label>Job Type</label>
                <select name="jobType" value={filters.jobType || ''} onChange={handleChange}>
                    <option value="">Any</option>
                    <option value="Full Time">Full Time</option>
                    <option value="Part Time">Part Time</option>
                    <option value="Contract">Contract</option>
                    <option value="Internship">Internship</option>
                </select>
            </div>
            <div className="filter-group">
                <label>Work Mode</label>
                <select name="workMode" value={filters.workMode || ''} onChange={handleChange}>
                    <option value="">Any</option>
                    <option value="On-site">On-site</option>
                    <option value="Remote">Remote</option>
                    <option value="Hybrid">Hybrid</option>
                </select>
            </div>
            <button className="btn-apply-filters" onClick={onApply}>Apply Filters</button>
        </div>
    );
};

export default FilterSidebar;
""",
    "components/FilterSidebar.css": """
.filter-sidebar {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #eee;
}

.filter-sidebar h3 {
    margin-bottom: 1.5rem;
    color: #2c3e50;
    border-bottom: 2px solid #eee;
    padding-bottom: 0.5rem;
}

.filter-group {
    margin-bottom: 1rem;
}

.filter-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #444;
}

.filter-group input, .filter-group select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    outline: none;
}

.filter-group input:focus, .filter-group select:focus {
    border-color: #4CAF50;
}

.btn-apply-filters {
    width: 100%;
    padding: 0.75rem;
    background: #2196F3;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
    margin-top: 1rem;
}

.btn-apply-filters:hover {
    background: #1976D2;
}
""",
    "pages/Jobs.jsx": """import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Link } from 'react-router-dom';
import FilterSidebar from '../components/FilterSidebar';
import './Jobs.css';

const Jobs = () => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [filters, setFilters] = useState({});

    const fetchJobs = async () => {
        setLoading(true);
        try {
            const params = new URLSearchParams();
            if (filters.keyword) params.append('keyword', filters.keyword);
            if (filters.location) params.append('location', filters.location);
            if (filters.jobType) params.append('jobType', filters.jobType);
            if (filters.workMode) params.append('workMode', filters.workMode);
            
            const response = await api.get(`/jobs/public/search?${params.toString()}`);
            setJobs(response.data);
        } catch (error) {
            console.error("Error fetching jobs", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchJobs();
    }, []);

    return (
        <div className="jobs-page-wrapper">
            <aside className="jobs-sidebar">
                <FilterSidebar filters={filters} setFilters={setFilters} onApply={fetchJobs} />
            </aside>
            <main className="jobs-main-content">
                <h2>Available Jobs</h2>
                {loading ? (
                    <div className="loader">Loading jobs...</div>
                ) : (
                    <div className="job-list">
                        {jobs.length === 0 ? <p>No jobs found matching your criteria.</p> : null}
                        {jobs.map(job => (
                            <div className="job-card" key={job.id}>
                                <div className="job-header">
                                    <h3>{job.title}</h3>
                                    <span className="job-type">{job.jobType}</span>
                                </div>
                                <div className="job-details">
                                    <p><strong>Location:</strong> {job.location} ({job.workMode})</p>
                                    <p><strong>Experience:</strong> {job.minExperience} - {job.maxExperience} years</p>
                                    <p><strong>Salary:</strong> ${job.minSalary} - ${job.maxSalary}</p>
                                </div>
                                <Link to={`/jobs/${job.id}`} className="btn-view-details">View Details</Link>
                            </div>
                        ))}
                    </div>
                )}
            </main>
        </div>
    );
};

export default Jobs;
""",
    "pages/Jobs.css": """
.jobs-page-wrapper {
    display: flex;
    gap: 2rem;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.jobs-sidebar {
    flex: 1;
    min-width: 250px;
    max-width: 300px;
}

.jobs-main-content {
    flex: 3;
}

.jobs-main-content h2 {
    margin-bottom: 2rem;
    color: #1a1a1a;
}

.job-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.job-card {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #eee;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
}

.job-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0,0,0,0.1);
}

.job-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
}

.job-header h3 {
    font-size: 1.25rem;
    color: #2c3e50;
    margin: 0;
}

.job-type {
    background: #e8f5e9;
    color: #4CAF50;
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 500;
}

.job-details {
    flex-grow: 1;
    margin-bottom: 1.5rem;
}

.job-details p {
    margin-bottom: 0.5rem;
    color: #555;
    font-size: 0.95rem;
}

.btn-view-details {
    display: block;
    text-align: center;
    padding: 0.75rem;
    background: #4CAF50;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: bold;
    transition: background 0.3s;
}

.btn-view-details:hover {
    background: #45a049;
}

.loader {
    text-align: center;
    padding: 3rem;
    font-size: 1.2rem;
    color: #666;
}
""",
    "pages/Dashboard.jsx": """import React, { useContext, useEffect, useState, useRef } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import './Dashboard.css';

const Dashboard = () => {
    const { user } = useContext(AuthContext);
    const [applications, setApplications] = useState([]);
    const [uploadStatus, setUploadStatus] = useState('');
    const fileInputRef = useRef(null);
    
    useEffect(() => {
        const fetchApplications = async () => {
            try {
                const res = await api.get('/applications/my');
                setApplications(res.data);
            } catch (err) {
                console.error("Error fetching applications", err);
            }
        };
        fetchApplications();
    }, []);

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        if (file.type !== 'application/pdf') {
            setUploadStatus('Please select a PDF file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            setUploadStatus('Uploading...');
            await api.post('/profile/resume', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            setUploadStatus('Resume uploaded successfully!');
        } catch (err) {
            setUploadStatus(err.response?.data?.message || 'Failed to upload resume.');
        }
    };

    return (
        <div className="dashboard-container">
            <h2>Job Seeker Dashboard</h2>
            <div className="welcome-card">
                <h3>Welcome back, {user?.email}</h3>
                <p>Manage your profile and applications here.</p>
                <div className="resume-upload">
                    <input type="file" accept=".pdf" ref={fileInputRef} onChange={handleFileUpload} style={{display: 'none'}} />
                    <button className="btn-upload" onClick={() => fileInputRef.current.click()}>Upload Resume (PDF)</button>
                    {uploadStatus && <span className="upload-status">{uploadStatus}</span>}
                </div>
            </div>
            
            <div className="applications-section">
                <h3>My Applications</h3>
                {applications.length === 0 ? (
                    <p>You haven't applied to any jobs yet.</p>
                ) : (
                    <table className="apps-table">
                        <thead>
                            <tr>
                                <th>Job Title</th>
                                <th>Status</th>
                                <th>Applied Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {applications.map(app => (
                                <tr key={app.id}>
                                    <td>{app.job?.title || 'Unknown Job'}</td>
                                    <td><span className={`status ${app.status.toLowerCase()}`}>{app.status}</span></td>
                                    <td>{new Date(app.appliedDate).toLocaleDateString()}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
};

export default Dashboard;
""",
    "pages/AdminDashboard.jsx": """import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import './Dashboard.css';

const AdminDashboard = () => {
    const { user } = useContext(AuthContext);
    const [users, setUsers] = useState([]);
    const [jobs, setJobs] = useState([]);
    const [activeTab, setActiveTab] = useState('users');
    
    useEffect(() => {
        fetchUsers();
        fetchJobs();
    }, []);

    const fetchUsers = async () => {
        try {
            const res = await api.get('/admin/users');
            setUsers(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    const fetchJobs = async () => {
        try {
            const res = await api.get('/admin/jobs');
            setJobs(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    const deleteUser = async (id) => {
        if (window.confirm("Are you sure you want to delete this user?")) {
            await api.delete(`/admin/users/${id}`);
            fetchUsers();
        }
    };

    const deleteJob = async (id) => {
        if (window.confirm("Are you sure you want to delete this job?")) {
            await api.delete(`/admin/jobs/${id}`);
            fetchJobs();
        }
    };

    return (
        <div className="dashboard-container">
            <h2>Admin Dashboard</h2>
            <div className="welcome-card admin-theme">
                <h3>Administrator: {user?.email}</h3>
                <p>Manage the platform users and job listings.</p>
            </div>
            
            <div className="tabs">
                <button className={`tab-btn ${activeTab === 'users' ? 'active' : ''}`} onClick={() => setActiveTab('users')}>Users</button>
                <button className={`tab-btn ${activeTab === 'jobs' ? 'active' : ''}`} onClick={() => setActiveTab('jobs')}>Jobs</button>
            </div>

            <div className="applications-section">
                {activeTab === 'users' && (
                    <>
                        <h3>All Users</h3>
                        <table className="apps-table">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Role</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {users.map(u => (
                                    <tr key={u.id}>
                                        <td>{u.id}</td>
                                        <td>{u.fullName}</td>
                                        <td>{u.email}</td>
                                        <td>{u.role}</td>
                                        <td><button className="btn-sm danger" onClick={() => deleteUser(u.id)}>Delete</button></td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </>
                )}

                {activeTab === 'jobs' && (
                    <>
                        <h3>All Jobs</h3>
                        <table className="apps-table">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Title</th>
                                    <th>Location</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {jobs.map(j => (
                                    <tr key={j.id}>
                                        <td>{j.id}</td>
                                        <td>{j.title}</td>
                                        <td>{j.location}</td>
                                        <td>{j.status}</td>
                                        <td><button className="btn-sm danger" onClick={() => deleteJob(j.id)}>Delete</button></td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </>
                )}
            </div>
        </div>
    );
};

export default AdminDashboard;
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Phase 2 frontend files generated successfully.")
