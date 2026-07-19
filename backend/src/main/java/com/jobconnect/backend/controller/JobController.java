package com.jobconnect.backend.controller;

import com.jobconnect.backend.entity.Job;
import com.jobconnect.backend.repository.JobRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/jobs")
public class JobController {
    
    @Autowired
    private JobRepository jobRepository;

    @GetMapping("/public")
    public ResponseEntity<List<Job>> getAllJobs() {
        return ResponseEntity.ok(jobRepository.findAll());
    }
    
    @GetMapping("/public/{id}")
    public ResponseEntity<Job> getJobById(@PathVariable Long id) {
        return jobRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/public/search")
    public ResponseEntity<List<Job>> searchJobs(
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) String location,
            @RequestParam(required = false) String jobType,
            @RequestParam(required = false) String workMode) {
        
        // Handle empty strings as null for the query
        keyword = (keyword != null && keyword.trim().isEmpty()) ? null : keyword;
        location = (location != null && location.trim().isEmpty()) ? null : location;
        jobType = (jobType != null && jobType.trim().isEmpty()) ? null : jobType;
        workMode = (workMode != null && workMode.trim().isEmpty()) ? null : workMode;

        return ResponseEntity.ok(jobRepository.searchJobs(keyword, location, jobType, workMode));
    }
}
