import os
import glob

base_dir = "d:/Job Application/jobconnect/frontend"
src_dir = os.path.join(base_dir, "src")

# 1. Update tailwind.config.js
tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },
        slate: {
          850: '#151e2e',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      boxShadow: {
        'glass': '0 4px 30px rgba(0, 0, 0, 0.1)',
      }
    },
  },
  plugins: [],
}
"""
with open(os.path.join(base_dir, "tailwind.config.js"), "w") as f:
    f.write(tailwind_config)

# PostCSS config
postcss_config = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""
with open(os.path.join(base_dir, "postcss.config.js"), "w") as f:
    f.write(postcss_config)

# 2. Update index.html
index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>JobConnect | Modern Job Portal</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body class="bg-gray-50 text-slate-800 antialiased font-sans">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""
with open(os.path.join(base_dir, "index.html"), "w") as f:
    f.write(index_html)

# 3. Update index.css
index_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer utilities {
  .glass {
    @apply bg-white/70 backdrop-blur-md border border-white/20 shadow-glass;
  }
}
"""
with open(os.path.join(src_dir, "index.css"), "w") as f:
    f.write(index_css)

# 4. React Components
components = {
    "components/Navbar.jsx": """import React, { useContext, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { Briefcase, Menu, X, User, LogOut } from 'lucide-react';

const Navbar = () => {
    const { user, logout } = useContext(AuthContext);
    const navigate = useNavigate();
    const [isOpen, setIsOpen] = useState(false);

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    const toggleMenu = () => setIsOpen(!isOpen);

    const NavLinks = () => (
        <>
            <Link to="/jobs" className="text-slate-600 hover:text-brand-600 font-medium transition-colors py-2 md:py-0">Find Jobs</Link>
            {!user ? (
                <div className="flex flex-col md:flex-row items-center gap-4 mt-4 md:mt-0">
                    <Link to="/login" className="text-brand-600 font-medium hover:text-brand-700 w-full text-center md:w-auto">Log in</Link>
                    <Link to="/register" className="bg-brand-600 text-white px-5 py-2 rounded-lg font-medium hover:bg-brand-700 transition-colors shadow-sm w-full text-center md:w-auto">Sign up</Link>
                </div>
            ) : (
                <div className="flex flex-col md:flex-row items-center gap-4 mt-4 md:mt-0">
                    {user.role === 'ROLE_JOB_SEEKER' && <Link to="/dashboard" className="text-slate-600 hover:text-brand-600 font-medium py-2 md:py-0">Dashboard</Link>}
                    {user.role === 'ROLE_RECRUITER' && <Link to="/recruiter" className="text-slate-600 hover:text-brand-600 font-medium py-2 md:py-0">Dashboard</Link>}
                    {user.role === 'ROLE_ADMIN' && <Link to="/admin" className="text-slate-600 hover:text-brand-600 font-medium py-2 md:py-0">Admin</Link>}
                    <button onClick={handleLogout} className="flex items-center gap-2 text-red-500 hover:text-red-700 font-medium py-2 md:py-0 transition-colors">
                        <LogOut size={18} /> Logout
                    </button>
                </div>
            )}
        </>
    );

    return (
        <nav className="bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">
                    <div className="flex items-center gap-2">
                        <Briefcase className="text-brand-600" size={28} />
                        <Link to="/" className="text-2xl font-bold text-slate-800 tracking-tight">
                            Job<span className="text-brand-600">Connect</span>
                        </Link>
                    </div>
                    
                    {/* Desktop Menu */}
                    <div className="hidden md:flex items-center gap-8">
                        <NavLinks />
                    </div>

                    {/* Mobile Menu Button */}
                    <div className="md:hidden flex items-center">
                        <button onClick={toggleMenu} className="text-slate-600 hover:text-brand-600 focus:outline-none">
                            {isOpen ? <X size={28} /> : <Menu size={28} />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {isOpen && (
                <div className="md:hidden bg-white border-t border-gray-100 px-4 pt-2 pb-6 flex flex-col space-y-2 shadow-lg">
                    <NavLinks />
                </div>
            )}
        </nav>
    );
};

export default Navbar;
""",
    "pages/Home.jsx": """import React from 'react';
import { Link } from 'react-router-dom';
import { Search, Briefcase, Users, TrendingUp, ArrowRight } from 'lucide-react';

const Home = () => {
    return (
        <div className="min-h-screen bg-gray-50 flex flex-col">
            {/* Hero Section */}
            <div className="relative overflow-hidden bg-white">
                <div className="absolute inset-0 bg-gradient-to-br from-brand-50 to-white z-0"></div>
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pt-20 pb-24 sm:pt-32 sm:pb-40">
                    <div className="text-center max-w-3xl mx-auto">
                        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-slate-900 tracking-tight mb-6">
                            Find your next dream job with <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-indigo-600">JobConnect</span>
                        </h1>
                        <p className="text-lg sm:text-xl text-slate-600 mb-10">
                            Discover thousands of job opportunities or find the perfect candidate. Your professional future starts here.
                        </p>
                        <div className="flex flex-col sm:flex-row justify-center gap-4">
                            <Link to="/jobs" className="flex items-center justify-center gap-2 bg-brand-600 text-white px-8 py-3.5 rounded-xl font-semibold text-lg hover:bg-brand-700 hover:shadow-lg transition-all">
                                <Search size={20} /> Browse Jobs
                            </Link>
                            <Link to="/register" className="flex items-center justify-center gap-2 bg-white text-brand-600 border border-brand-200 px-8 py-3.5 rounded-xl font-semibold text-lg hover:bg-brand-50 transition-all">
                                <Briefcase size={20} /> Post a Job
                            </Link>
                        </div>
                    </div>
                </div>
            </div>

            {/* Features Section */}
            <div className="py-20 bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-brand-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <Briefcase className="text-brand-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Thousands of Jobs</h3>
                            <p className="text-slate-600 leading-relaxed">Access a massive pool of opportunities from top companies worldwide, updated daily.</p>
                        </div>
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-indigo-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <Users className="text-indigo-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Top Talent</h3>
                            <p className="text-slate-600 leading-relaxed">Employers can easily filter and connect with verified, highly-skilled professionals.</p>
                        </div>
                        <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                            <div className="bg-blue-100 w-14 h-14 rounded-xl flex items-center justify-center mb-6">
                                <TrendingUp className="text-blue-600" size={28} />
                            </div>
                            <h3 className="text-xl font-bold text-slate-800 mb-3">Career Growth</h3>
                            <p className="text-slate-600 leading-relaxed">Advance your career with smart matching and personalized job recommendations.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            {/* Call to action footer */}
            <div className="bg-slate-900 py-16 mt-auto">
                <div className="max-w-4xl mx-auto px-4 text-center">
                    <h2 className="text-3xl font-bold text-white mb-6">Ready to take the next step?</h2>
                    <Link to="/register" className="inline-flex items-center gap-2 bg-brand-500 text-white px-8 py-3 rounded-xl font-semibold hover:bg-brand-400 transition-colors">
                        Create an Account <ArrowRight size={20} />
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default Home;
""",
    "pages/Login.jsx": """import React, { useState, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { Mail, Lock, ArrowRight } from 'lucide-react';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            await login(email, password);
            navigate('/');
        } catch (err) {
            setError(err.response?.data?.message || 'Invalid credentials');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-md w-full space-y-8 bg-white p-10 rounded-2xl shadow-xl border border-gray-100">
                <div>
                    <h2 className="mt-2 text-center text-3xl font-extrabold text-slate-900">Welcome back</h2>
                    <p className="mt-2 text-center text-sm text-slate-600">
                        Don't have an account?{' '}
                        <Link to="/register" className="font-medium text-brand-600 hover:text-brand-500 transition-colors">Sign up</Link>
                    </p>
                </div>
                
                {error && (
                    <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
                        <p className="text-sm text-red-700">{error}</p>
                    </div>
                )}
                
                <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-slate-700 mb-1">Email address</label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <Mail className="h-5 w-5 text-gray-400" />
                                </div>
                                <input type="email" required value={email} onChange={(e) => setEmail(e.target.value)}
                                    className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm transition-all"
                                    placeholder="you@example.com" />
                            </div>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-slate-700 mb-1">Password</label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <Lock className="h-5 w-5 text-gray-400" />
                                </div>
                                <input type="password" required value={password} onChange={(e) => setPassword(e.target.value)}
                                    className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm transition-all"
                                    placeholder="••••••••" />
                            </div>
                        </div>
                    </div>

                    <button type="submit" disabled={loading}
                        className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-brand-600 hover:bg-brand-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-500 transition-all disabled:opacity-70 shadow-md hover:shadow-lg">
                        {loading ? 'Signing in...' : 'Sign in'}
                        {!loading && <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;
""",
    "pages/Register.jsx": """import React, { useState, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { User, Mail, Lock, Briefcase, ArrowRight } from 'lucide-react';

const Register = () => {
    const [formData, setFormData] = useState({ fullName: '', email: '', password: '', role: 'ROLE_JOB_SEEKER' });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { register } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true); setError('');
        try {
            await register(formData.fullName, formData.email, formData.password, formData.role);
            navigate('/login');
        } catch (err) {
            setError(err.response?.data?.message || 'Registration failed');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-md w-full space-y-8 bg-white p-10 rounded-2xl shadow-xl border border-gray-100">
                <div>
                    <h2 className="mt-2 text-center text-3xl font-extrabold text-slate-900">Create an account</h2>
                    <p className="mt-2 text-center text-sm text-slate-600">
                        Already have an account?{' '}
                        <Link to="/login" className="font-medium text-brand-600 hover:text-brand-500 transition-colors">Log in</Link>
                    </p>
                </div>
                
                {error && (
                    <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
                        <p className="text-sm text-red-700">{error}</p>
                    </div>
                )}
                
                <form className="mt-8 space-y-5" onSubmit={handleSubmit}>
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">Full Name</label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <User className="h-5 w-5 text-gray-400" />
                            </div>
                            <input type="text" required value={formData.fullName} onChange={(e) => setFormData({...formData, fullName: e.target.value})}
                                className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm"
                                placeholder="John Doe" />
                        </div>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">Email address</label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <Mail className="h-5 w-5 text-gray-400" />
                            </div>
                            <input type="email" required value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})}
                                className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm"
                                placeholder="you@example.com" />
                        </div>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">Password</label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <Lock className="h-5 w-5 text-gray-400" />
                            </div>
                            <input type="password" required value={formData.password} onChange={(e) => setFormData({...formData, password: e.target.value})}
                                className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm"
                                placeholder="••••••••" />
                        </div>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">I am a...</label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <Briefcase className="h-5 w-5 text-gray-400" />
                            </div>
                            <select value={formData.role} onChange={(e) => setFormData({...formData, role: e.target.value})}
                                className="appearance-none block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:border-brand-500 sm:text-sm bg-white">
                                <option value="ROLE_JOB_SEEKER">Job Seeker</option>
                                <option value="ROLE_RECRUITER">Recruiter / Employer</option>
                            </select>
                        </div>
                    </div>

                    <button type="submit" disabled={loading}
                        className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-brand-600 hover:bg-brand-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-500 shadow-md hover:shadow-lg transition-all mt-6">
                        {loading ? 'Creating account...' : 'Create Account'}
                        {!loading && <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Register;
""",
    "pages/RecruiterDashboard.jsx": """import React, { useContext, useEffect, useState } from 'react';
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
"""
}

for filepath, content in components.items():
    full_path = os.path.join(src_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

# Remove old CSS files
for css_file in ["Navbar.css", "Home.css", "Login.css", "Dashboard.css", "PostJob.css", "Jobs.css", "JobDetails.css", "FilterSidebar.css"]:
    for root, _, files in os.walk(src_dir):
        if css_file in files:
            try:
                os.remove(os.path.join(root, css_file))
            except:
                pass

print("Modern UI Phase 1 applied successfully.")
