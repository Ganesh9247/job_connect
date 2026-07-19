import React, { useContext, useEffect, useState } from 'react';
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
