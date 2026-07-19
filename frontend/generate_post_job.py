import os

base_dir = "d:/Job Application/jobconnect/frontend/src"

files = {
    "pages/PostJob.jsx": """import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import './PostJob.css';

const PostJob = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        title: '',
        location: '',
        description: '',
        responsibilities: '',
        requirements: '',
        minExperience: '',
        maxExperience: '',
        minSalary: '',
        maxSalary: '',
        jobType: 'Full Time',
        workMode: 'On-site',
        openings: 1,
        deadline: ''
    });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
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
        <div className="post-job-container">
            <h2>Post a New Job</h2>
            {error && <div className="error-message">{error}</div>}
            
            <form className="post-job-form" onSubmit={handleSubmit}>
                <div className="form-row">
                    <div className="form-group">
                        <label>Job Title *</label>
                        <input type="text" name="title" value={formData.title} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Location *</label>
                        <input type="text" name="location" value={formData.location} onChange={handleChange} required />
                    </div>
                </div>

                <div className="form-group">
                    <label>Description *</label>
                    <textarea name="description" rows="3" value={formData.description} onChange={handleChange} required></textarea>
                </div>

                <div className="form-group">
                    <label>Responsibilities *</label>
                    <textarea name="responsibilities" rows="3" value={formData.responsibilities} onChange={handleChange} required></textarea>
                </div>

                <div className="form-group">
                    <label>Requirements *</label>
                    <textarea name="requirements" rows="3" value={formData.requirements} onChange={handleChange} required></textarea>
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label>Min Experience (Yrs) *</label>
                        <input type="number" step="0.1" name="minExperience" value={formData.minExperience} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Max Experience (Yrs) *</label>
                        <input type="number" step="0.1" name="maxExperience" value={formData.maxExperience} onChange={handleChange} required />
                    </div>
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label>Min Salary *</label>
                        <input type="number" name="minSalary" value={formData.minSalary} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Max Salary *</label>
                        <input type="number" name="maxSalary" value={formData.maxSalary} onChange={handleChange} required />
                    </div>
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label>Job Type *</label>
                        <select name="jobType" value={formData.jobType} onChange={handleChange}>
                            <option value="Full Time">Full Time</option>
                            <option value="Part Time">Part Time</option>
                            <option value="Contract">Contract</option>
                            <option value="Internship">Internship</option>
                        </select>
                    </div>
                    <div className="form-group">
                        <label>Work Mode *</label>
                        <select name="workMode" value={formData.workMode} onChange={handleChange}>
                            <option value="On-site">On-site</option>
                            <option value="Remote">Remote</option>
                            <option value="Hybrid">Hybrid</option>
                        </select>
                    </div>
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label>Openings *</label>
                        <input type="number" name="openings" value={formData.openings} onChange={handleChange} required min="1" />
                    </div>
                    <div className="form-group">
                        <label>Application Deadline *</label>
                        <input type="date" name="deadline" value={formData.deadline} onChange={handleChange} required />
                    </div>
                </div>

                <div className="form-actions">
                    <button type="button" className="btn-cancel" onClick={() => navigate('/recruiter')}>Cancel</button>
                    <button type="submit" className="btn-submit" disabled={loading}>
                        {loading ? 'Posting...' : 'Post Job'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default PostJob;
""",
    "pages/PostJob.css": """
.post-job-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.post-job-container h2 {
    margin-bottom: 2rem;
    color: #333;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 1rem;
}

.post-job-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-row {
    display: flex;
    gap: 1.5rem;
}

.form-row .form-group {
    flex: 1;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #555;
}

.form-group input, 
.form-group select, 
.form-group textarea {
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
    font-size: 1rem;
}

.form-group input:focus, 
.form-group select:focus, 
.form-group textarea:focus {
    outline: none;
    border-color: #4CAF50;
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
    margin-top: 1rem;
}

.btn-cancel {
    padding: 0.75rem 1.5rem;
    background: #f4f4f4;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
}

.btn-cancel:hover {
    background: #e0e0e0;
}

.btn-submit {
    padding: 0.75rem 2rem;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
}

.btn-submit:hover:not(:disabled) {
    background: #45a049;
}

.btn-submit:disabled {
    background: #a5d6a7;
    cursor: not-allowed;
}
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("PostJob files generated successfully.")
