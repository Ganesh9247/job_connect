import os

base_dir = "src"

files = {
    "pages/Jobs.jsx": """import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Link } from 'react-router-dom';
import './Jobs.css';

const Jobs = () => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchJobs = async () => {
            try {
                const response = await api.get('/jobs/public');
                setJobs(response.data);
            } catch (error) {
                console.error("Error fetching jobs", error);
            } finally {
                setLoading(false);
            }
        };
        fetchJobs();
    }, []);

    if (loading) return <div className="loader">Loading jobs...</div>;

    return (
        <div className="jobs-container">
            <h2>Available Jobs</h2>
            <div className="job-list">
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
        </div>
    );
};

export default Jobs;
""",
    "pages/Jobs.css": """
.jobs-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.jobs-container h2 {
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
    "pages/JobDetails.jsx": """import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';
import { AuthContext } from '../context/AuthContext';
import './JobDetails.css';

const JobDetails = () => {
    const { id } = useParams();
    const [job, setJob] = useState(null);
    const [loading, setLoading] = useState(true);
    const { user } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchJob = async () => {
            try {
                const response = await api.get(`/jobs/public/${id}`);
                setJob(response.data);
            } catch (error) {
                console.error("Error fetching job details", error);
            } finally {
                setLoading(false);
            }
        };
        fetchJob();
    }, [id]);

    const handleApply = async () => {
        if (!user) {
            alert('Please login to apply');
            navigate('/login');
            return;
        }
        if (user.role !== 'ROLE_JOB_SEEKER') {
            alert('Only Job Seekers can apply');
            return;
        }
        
        try {
            await api.post(`/applications/apply/${id}`);
            alert('Applied successfully!');
        } catch (err) {
            alert(err.response?.data?.message || 'Failed to apply. You may have already applied.');
        }
    };

    if (loading) return <div className="loader">Loading job details...</div>;
    if (!job) return <div className="loader">Job not found.</div>;

    return (
        <div className="job-details-container">
            <div className="job-details-header">
                <h2>{job.title}</h2>
                <div className="job-tags">
                    <span>{job.jobType}</span>
                    <span>{job.workMode}</span>
                </div>
            </div>
            
            <div className="job-details-body">
                <div className="main-content">
                    <section>
                        <h3>Job Description</h3>
                        <p>{job.description}</p>
                    </section>
                    <section>
                        <h3>Responsibilities</h3>
                        <p>{job.responsibilities}</p>
                    </section>
                    <section>
                        <h3>Requirements</h3>
                        <p>{job.requirements}</p>
                    </section>
                </div>
                
                <div className="sidebar">
                    <div className="summary-card">
                        <h3>Summary</h3>
                        <ul>
                            <li><strong>Location:</strong> {job.location}</li>
                            <li><strong>Experience:</strong> {job.minExperience} - {job.maxExperience} years</li>
                            <li><strong>Salary:</strong> ${job.minSalary} - ${job.maxSalary}</li>
                            <li><strong>Openings:</strong> {job.openings}</li>
                            <li><strong>Deadline:</strong> {job.deadline}</li>
                        </ul>
                        <button className="btn-apply" onClick={handleApply}>Apply Now</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default JobDetails;
""",
    "pages/JobDetails.css": """
.job-details-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.job-details-header {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}

.job-details-header h2 {
    font-size: 2rem;
    color: #1a1a1a;
    margin-bottom: 1rem;
}

.job-tags span {
    background: #e8f5e9;
    color: #4CAF50;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
    margin-right: 1rem;
}

.job-details-body {
    display: flex;
    gap: 2rem;
}

.main-content {
    flex: 2;
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.main-content section {
    margin-bottom: 2rem;
}

.main-content h3 {
    color: #2c3e50;
    border-bottom: 2px solid #eee;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.main-content p {
    color: #444;
    white-space: pre-wrap;
    line-height: 1.6;
}

.sidebar {
    flex: 1;
}

.summary-card {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.summary-card h3 {
    margin-bottom: 1rem;
    color: #1a1a1a;
}

.summary-card ul {
    list-style: none;
    margin-bottom: 2rem;
}

.summary-card li {
    margin-bottom: 1rem;
    color: #555;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #f0f0f0;
}

.btn-apply {
    width: 100%;
    padding: 1rem;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s;
}

.btn-apply:hover {
    background: #45a049;
}
""",
    "pages/Dashboard.jsx": """import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import './Dashboard.css';

const Dashboard = () => {
    const { user } = useContext(AuthContext);
    const [applications, setApplications] = useState([]);
    
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

    return (
        <div className="dashboard-container">
            <h2>Job Seeker Dashboard</h2>
            <div className="welcome-card">
                <h3>Welcome back, {user?.email}</h3>
                <p>Manage your profile and applications here.</p>
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
    "pages/RecruiterDashboard.jsx": """import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';
import './Dashboard.css';

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
        <div className="dashboard-container">
            <h2>Recruiter Dashboard</h2>
            <div className="welcome-card">
                <h3>Welcome back, {user?.email}</h3>
                <p>Manage your job postings and applicants.</p>
                <button className="btn-post-job">Post New Job</button>
            </div>
            
            <div className="applications-section">
                <h3>My Posted Jobs</h3>
                {jobs.length === 0 ? (
                    <p>You haven't posted any jobs yet.</p>
                ) : (
                    <table className="apps-table">
                        <thead>
                            <tr>
                                <th>Job Title</th>
                                <th>Location</th>
                                <th>Status</th>
                                <th>Openings</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {jobs.map(job => (
                                <tr key={job.id}>
                                    <td>{job.title}</td>
                                    <td>{job.location}</td>
                                    <td><span className={`status ${job.status.toLowerCase()}`}>{job.status}</span></td>
                                    <td>{job.openings}</td>
                                    <td>
                                        <button className="btn-sm">View Applicants</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
};

export default RecruiterDashboard;
""",
    "pages/Dashboard.css": """
.dashboard-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.dashboard-container h2 {
    margin-bottom: 2rem;
    color: #1a1a1a;
}

.welcome-card {
    background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
    color: white;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 2rem;
}

.welcome-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.btn-post-job {
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
    background: white;
    color: #4CAF50;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
}

.applications-section {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.applications-section h3 {
    margin-bottom: 1.5rem;
    color: #2c3e50;
    border-bottom: 2px solid #eee;
    padding-bottom: 0.5rem;
}

.apps-table {
    width: 100%;
    border-collapse: collapse;
}

.apps-table th, .apps-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #eee;
}

.apps-table th {
    font-weight: 600;
    color: #666;
    background-color: #f9f9f9;
}

.status {
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.85rem;
    font-weight: bold;
}

.status.applied { background: #e3f2fd; color: #1976d2; }
.status.active { background: #e8f5e9; color: #4CAF50; }
.status.closed { background: #ffebee; color: #d32f2f; }

.btn-sm {
    padding: 0.5rem 1rem;
    background: #2196F3;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Frontend pages generated successfully.")
