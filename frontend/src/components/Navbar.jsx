import React, { useContext, useState } from 'react';
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
