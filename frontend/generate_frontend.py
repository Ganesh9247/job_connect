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
    "context/AuthContext.jsx": """import React, { createContext, useState, useEffect } from 'react';
import api from '../services/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const storedUser = localStorage.getItem('user');
        const token = localStorage.getItem('token');
        if (storedUser && token) {
            setUser(JSON.parse(storedUser));
        }
        setLoading(false);
    }, []);

    const login = async (email, password) => {
        const response = await api.post('/auth/login', { email, password });
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            const userData = {
                id: response.data.id,
                email: response.data.email,
                role: response.data.role
            };
            localStorage.setItem('user', JSON.stringify(userData));
            setUser(userData);
        }
        return response.data;
    };

    const logout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout, loading }}>
            {children}
        </AuthContext.Provider>
    );
};
""",
    "App.jsx": """import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
""",
    "main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
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
            <div className="navbar-brand">
                <Link to="/">JobConnect</Link>
            </div>
            <div className="navbar-links">
                <Link to="/">Home</Link>
                <Link to="/jobs">Jobs</Link>
                {!user ? (
                    <>
                        <Link to="/login" className="btn-login">Login</Link>
                        <Link to="/register" className="btn-register">Register</Link>
                    </>
                ) : (
                    <>
                        {user.role === 'ROLE_JOB_SEEKER' && <Link to="/dashboard">Dashboard</Link>}
                        {user.role === 'ROLE_RECRUITER' && <Link to="/recruiter">Dashboard</Link>}
                        {user.role === 'ROLE_ADMIN' && <Link to="/admin">Admin</Link>}
                        <button onClick={handleLogout} className="btn-logout">Logout</button>
                    </>
                )}
            </div>
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
    padding: 1rem 2rem;
    background-color: #1a1a1a;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.navbar-brand a {
    font-size: 1.5rem;
    font-weight: bold;
    color: #4CAF50;
    text-decoration: none;
}

.navbar-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.navbar-links a {
    color: white;
    text-decoration: none;
    font-size: 1rem;
    transition: color 0.3s;
}

.navbar-links a:hover {
    color: #4CAF50;
}

.btn-login, .btn-register, .btn-logout {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    font-weight: bold;
    text-decoration: none;
}

.btn-login {
    background: transparent;
    border: 1px solid #4CAF50;
    color: #4CAF50 !important;
}

.btn-register {
    background: #4CAF50;
    color: white !important;
}

.btn-logout {
    background: #f44336;
    color: white;
}
""",
    "pages/Home.jsx": """import React from 'react';
import './Home.css';

const Home = () => {
    return (
        <div className="home">
            <div className="hero">
                <h1>Find Your Dream Job Today</h1>
                <p>Join thousands of professionals discovering their next big opportunity.</p>
                <div className="search-bar">
                    <input type="text" placeholder="Job title, keyword or company" />
                    <input type="text" placeholder="Location" />
                    <button>Search Jobs</button>
                </div>
            </div>
            <div className="stats">
                <div className="stat-box">
                    <h3>10k+</h3>
                    <p>Jobs Available</p>
                </div>
                <div className="stat-box">
                    <h3>5k+</h3>
                    <p>Companies Hiring</p>
                </div>
                <div className="stat-box">
                    <h3>50k+</h3>
                    <p>Registered Candidates</p>
                </div>
            </div>
        </div>
    );
};

export default Home;
""",
    "pages/Home.css": """
.home {
    min-height: calc(100vh - 70px);
    display: flex;
    flex-direction: column;
}

.hero {
    background: linear-gradient(135deg, #1a1a1a 0%, #2c3e50 100%);
    color: white;
    padding: 6rem 2rem;
    text-align: center;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.hero h1 {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    background: linear-gradient(to right, #4CAF50, #81C784);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: #aaa;
}

.search-bar {
    display: flex;
    gap: 1rem;
    width: 100%;
    max-width: 800px;
    background: white;
    padding: 0.5rem;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.search-bar input {
    flex: 1;
    padding: 1rem;
    border: none;
    outline: none;
    font-size: 1rem;
    border-right: 1px solid #eee;
}

.search-bar button {
    padding: 1rem 2rem;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s;
}

.search-bar button:hover {
    background: #45a049;
}

.stats {
    display: flex;
    justify-content: space-around;
    padding: 4rem 2rem;
    background: white;
}

.stat-box {
    text-align: center;
}

.stat-box h3 {
    font-size: 2.5rem;
    color: #1a1a1a;
    margin-bottom: 0.5rem;
}

.stat-box p {
    color: #666;
    font-size: 1.1rem;
}
""",
    "pages/Login.jsx": """import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import './Auth.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await login(email, password);
            if (data.role === 'ROLE_JOB_SEEKER') navigate('/dashboard');
            else if (data.role === 'ROLE_RECRUITER') navigate('/recruiter');
            else navigate('/admin');
        } catch (err) {
            setError(err.response?.data?.message || 'Login failed. Please try again.');
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h2>Welcome Back</h2>
                <p>Login to your account to continue</p>
                {error && <div className="error-message">{error}</div>}
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Email</label>
                        <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
                    </div>
                    <button type="submit" className="btn-submit">Login</button>
                </form>
            </div>
        </div>
    );
};

export default Login;
""",
    "pages/Register.jsx": """import React, { useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';
import './Auth.css';

const Register = () => {
    const [formData, setFormData] = useState({
        fullName: '',
        email: '',
        password: '',
        confirmPassword: '',
        phone: '',
        role: 'ROLE_JOB_SEEKER'
    });
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (formData.password !== formData.confirmPassword) {
            setError('Passwords do not match');
            return;
        }
        try {
            await api.post('/auth/register', formData);
            navigate('/login');
        } catch (err) {
            setError(err.response?.data?.message || 'Registration failed');
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h2>Create an Account</h2>
                <p>Join JobConnect today</p>
                {error && <div className="error-message">{error}</div>}
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Full Name</label>
                        <input type="text" name="fullName" value={formData.fullName} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Email</label>
                        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Phone</label>
                        <input type="text" name="phone" value={formData.phone} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>Confirm Password</label>
                        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
                    </div>
                    <div className="form-group">
                        <label>I am a</label>
                        <select name="role" value={formData.role} onChange={handleChange}>
                            <option value="ROLE_JOB_SEEKER">Job Seeker</option>
                            <option value="ROLE_RECRUITER">Recruiter</option>
                        </select>
                    </div>
                    <button type="submit" className="btn-submit">Register</button>
                </form>
            </div>
        </div>
    );
};

export default Register;
""",
    "pages/Auth.css": """
.auth-container {
    min-height: calc(100vh - 70px);
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f4f7f6;
    padding: 2rem;
}

.auth-card {
    background: white;
    padding: 3rem;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 450px;
}

.auth-card h2 {
    color: #1a1a1a;
    margin-bottom: 0.5rem;
    text-align: center;
}

.auth-card p {
    color: #666;
    text-align: center;
    margin-bottom: 2rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #333;
    font-weight: 500;
}

.form-group input, .form-group select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    box-sizing: border-box;
}

.form-group input:focus, .form-group select:focus {
    outline: none;
    border-color: #4CAF50;
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
}

.btn-submit {
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

.btn-submit:hover {
    background: #45a049;
}

.error-message {
    background: #ffebee;
    color: #c62828;
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1.5rem;
    text-align: center;
}
""",
    "index.css": """
:root {
  --primary-color: #4CAF50;
  --secondary-color: #2c3e50;
  --background-color: #f4f7f6;
  --text-color: #333;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background-color: var(--background-color);
  color: var(--text-color);
  line-height: 1.6;
}
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Frontend files generated successfully.")
