import os

base_dir = "src"

files = {
    "services/api.js": """import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8080/api',
});

api.interceptors.request.use(config => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api;
""",
    "services/authService.js": """import api from './api';

const login = async (email, password) => {
    const response = await api.post('/auth/login', { email, password });
    if (response.data.token) {
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

const register = async (fullName, email, password, role) => {
    return await api.post('/auth/register', { fullName, email, password, role });
};

const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
};

const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem('user'));
};

const authService = {
    login,
    register,
    logout,
    getCurrentUser,
};

export default authService;
""",
    "context/AuthContext.jsx": """import React, { createContext, useState, useEffect } from 'react';
import authService from '../services/authService';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const currentUser = authService.getCurrentUser();
        if (currentUser) {
            setUser(currentUser);
        }
    }, []);

    const login = async (email, password) => {
        const data = await authService.login(email, password);
        setUser(data);
    };

    const register = async (fullName, email, password, role) => {
        await authService.register(fullName, email, password, role);
    };

    const logout = () => {
        authService.logout();
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
""",
    "components/Navbar.jsx": """import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import './Navbar.css';

const Navbar = () => {
    const { user, logout } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">JobConnect</Link>
            </div>
            <ul className="navbar-links">
                <li><Link to="/jobs">Find Jobs</Link></li>
                {!user && (
                    <>
                        <li><Link to="/login" className="btn-login">Login</Link></li>
                        <li><Link to="/register" className="btn-register">Register</Link></li>
                    </>
                )}
                {user && user.role === 'ROLE_JOB_SEEKER' && (
                    <li><Link to="/dashboard">Dashboard</Link></li>
                )}
                {user && user.role === 'ROLE_RECRUITER' && (
                    <li><Link to="/recruiter">Dashboard</Link></li>
                )}
                {user && user.role === 'ROLE_ADMIN' && (
                    <li><Link to="/admin">Admin</Link></li>
                )}
                {user && (
                    <li><button onClick={handleLogout} className="btn-logout">Logout</button></li>
                )}
            </ul>
        </nav>
    );
};

export default Navbar;
""",
    "components/Navbar.css": """
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    padding: 1rem 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.navbar-logo a {
    font-size: 1.5rem;
    font-weight: bold;
    color: #4CAF50;
    text-decoration: none;
}

.navbar-links {
    list-style: none;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin: 0;
}

.navbar-links a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
}

.navbar-links a:hover {
    color: #4CAF50;
}

.btn-login, .btn-register {
    padding: 0.5rem 1rem;
    border-radius: 4px;
}

.btn-login {
    border: 1px solid #4CAF50;
    color: #4CAF50 !important;
}

.btn-register {
    background-color: #4CAF50;
    color: white !important;
}

.btn-logout {
    background: none;
    border: none;
    color: #d32f2f;
    font-weight: bold;
    cursor: pointer;
    font-size: 1rem;
}
""",
    "pages/Home.jsx": """import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
    return (
        <div className="home-container">
            <header className="hero-section">
                <h1>Welcome to JobConnect</h1>
                <p>Find your dream job or hire the best talent with ease.</p>
                <div className="cta-buttons">
                    <Link to="/jobs" className="btn-primary">Browse Jobs</Link>
                    <Link to="/register" className="btn-secondary">Post a Job</Link>
                </div>
            </header>
        </div>
    );
};

export default Home;
""",
    "pages/Home.css": """
.home-container {
    text-align: center;
    padding: 4rem 2rem;
}

.hero-section h1 {
    font-size: 3rem;
    color: #1a1a1a;
    margin-bottom: 1rem;
}

.hero-section p {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 2rem;
}

.cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.btn-primary, .btn-secondary {
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.1rem;
}

.btn-primary {
    background-color: #4CAF50;
    color: white;
}

.btn-secondary {
    border: 2px solid #4CAF50;
    color: #4CAF50;
}
""",
    "pages/Login.jsx": """import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import './Login.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login(email, password);
            navigate('/'); // Redirect to home or dashboard
        } catch (err) {
            setError(err.response?.data?.message || 'Invalid credentials');
        }
    };

    return (
        <div className="auth-container">
            <form className="auth-form" onSubmit={handleSubmit}>
                <h2>Login</h2>
                {error && <div className="error-message">{error}</div>}
                
                <div className="form-group">
                    <label>Email</label>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                </div>
                
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>
                
                <button type="submit" className="btn-submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
""",
    "pages/Login.css": """
.auth-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
}

.auth-form {
    background: white;
    padding: 2.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 400px;
}

.auth-form h2 {
    margin-bottom: 1.5rem;
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 1.25rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #555;
}

.form-group input, .form-group select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.btn-submit {
    width: 100%;
    padding: 0.75rem;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
}

.error-message {
    background: #ffebee;
    color: #c62828;
    padding: 0.75rem;
    border-radius: 4px;
    margin-bottom: 1rem;
    text-align: center;
}
""",
    "pages/Register.jsx": """import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import './Login.css'; // Reuse login styles

const Register = () => {
    const [fullName, setFullName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('ROLE_JOB_SEEKER');
    const [error, setError] = useState('');
    const { register } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await register(fullName, email, password, role);
            alert("Registration successful. Please login.");
            navigate('/login');
        } catch (err) {
            setError(err.response?.data?.message || 'Registration failed');
        }
    };

    return (
        <div className="auth-container">
            <form className="auth-form" onSubmit={handleSubmit}>
                <h2>Register</h2>
                {error && <div className="error-message">{error}</div>}
                
                <div className="form-group">
                    <label>Full Name</label>
                    <input type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                </div>
                
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>

                <div className="form-group">
                    <label>I am a...</label>
                    <select value={role} onChange={(e) => setRole(e.target.value)}>
                        <option value="ROLE_JOB_SEEKER">Job Seeker</option>
                        <option value="ROLE_RECRUITER">Recruiter</option>
                    </select>
                </div>
                
                <button type="submit" className="btn-submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Base frontend files generated successfully.")
