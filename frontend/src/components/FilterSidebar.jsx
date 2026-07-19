import React, { useState } from 'react';
import { Filter } from 'lucide-react';

const FilterSidebar = ({ onFilterChange }) => {
    const [jobType, setJobType] = useState('');
    const [workMode, setWorkMode] = useState('');

    const handleApply = () => {
        onFilterChange({ jobType, workMode });
    };

    const handleClear = () => {
        setJobType('');
        setWorkMode('');
        onFilterChange({ jobType: '', workMode: '' });
    };

    return (
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 sticky top-24">
            <div className="flex items-center gap-2 mb-6 border-b border-gray-100 pb-4">
                <Filter size={20} className="text-brand-600" />
                <h3 className="text-lg font-bold text-slate-800">Filters</h3>
            </div>
            
            <div className="space-y-6">
                <div>
                    <h4 className="font-semibold text-slate-700 mb-3">Job Type</h4>
                    <select 
                        value={jobType} 
                        onChange={(e) => setJobType(e.target.value)}
                        className="w-full border border-gray-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-brand-500 focus:border-brand-500 bg-white"
                    >
                        <option value="">All Types</option>
                        <option value="Full Time">Full Time</option>
                        <option value="Part Time">Part Time</option>
                        <option value="Contract">Contract</option>
                        <option value="Internship">Internship</option>
                    </select>
                </div>

                <div>
                    <h4 className="font-semibold text-slate-700 mb-3">Work Mode</h4>
                    <select 
                        value={workMode} 
                        onChange={(e) => setWorkMode(e.target.value)}
                        className="w-full border border-gray-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-brand-500 focus:border-brand-500 bg-white"
                    >
                        <option value="">All Modes</option>
                        <option value="On-site">On-site</option>
                        <option value="Remote">Remote</option>
                        <option value="Hybrid">Hybrid</option>
                    </select>
                </div>

                <div className="pt-4 flex flex-col gap-3">
                    <button onClick={handleApply} className="w-full bg-brand-600 text-white py-2.5 rounded-lg font-medium hover:bg-brand-700 transition-colors shadow-sm">
                        Apply Filters
                    </button>
                    <button onClick={handleClear} className="w-full bg-gray-100 text-slate-700 py-2.5 rounded-lg font-medium hover:bg-gray-200 transition-colors">
                        Clear All
                    </button>
                </div>
            </div>
        </div>
    );
};

export default FilterSidebar;
